"""Read config/params.yaml and build file paths. Shared by everyone.

Two kinds of paths:
    - Small project files (AOI, CSV tables, outputs) are inside the repository folder.
    - Big raster data (raw / interim / processed) can live somewhere else, for example on
      Google Drive in Colab. Set the environment variable DATA_ROOT to that folder, and
      data_dir() will use it. Without DATA_ROOT, data_dir() uses <repository>/data.
"""
import os
from pathlib import Path

import yaml


# Where is the repository folder?
# __file__ is a variable that Python fills in automatically: it is the path of THIS file,
# for example ".../multitemporal-shoreline-timbulsloko/src/shoreline/config.py".
# Going up three folders from this file gives the repository folder:
#     config.py  ->  shoreline/  ->  src/  ->  repository folder
THIS_FILE = Path(__file__).resolve()
SHORELINE_FOLDER = THIS_FILE.parent
SRC_FOLDER = SHORELINE_FOLDER.parent
REPO_ROOT = SRC_FOLDER.parent

PARAMS_FILE = REPO_ROOT / "config" / "params.yaml"

# The three data stages, in pipeline order
DATA_STAGES = ["raw", "interim", "processed"]


def load_params(params_file: Path | None = None) -> dict:
    """Read the parameter file and return it as a dictionary.

    Inputs:
        params_file: path to a YAML file. If None, config/params.yaml is used.

    Returns:
        A dictionary, for example params["segmentation"]["sea_erosion_radius"] -> 2.

    The file is read again on every call. That is a little slower, but it means every call
    gives a fresh dictionary, so changing it in one notebook cell cannot affect another call.
    """
    if params_file is None:
        params_file = PARAMS_FILE

    with open(params_file, encoding="utf-8") as yaml_file:
        params = yaml.safe_load(yaml_file)

    return params


def repo_path(key: str) -> Path:
    """Full path of a file listed under `paths:` in params.yaml.

    Example: repo_path("aoi") -> <repository>/data/aoi/aoi_timbulsloko.geojson
    """
    params = load_params()
    relative_path = params["paths"][key]
    full_path = REPO_ROOT / relative_path
    return full_path


def data_root() -> Path:
    """Folder that holds raw/, interim/ and processed/.

    Returns the DATA_ROOT environment variable if it is set (Colab: the Google Drive folder),
    otherwise <repository>/data.
    """
    data_root_from_environment = os.environ.get("DATA_ROOT")

    if data_root_from_environment is not None and data_root_from_environment != "":
        return Path(data_root_from_environment).expanduser()

    params = load_params()
    return REPO_ROOT / params["paths"]["data_root"]


def data_dir(stage: str, sub_path: str = "", create_folder: bool = False) -> Path:
    """Path inside one data stage.

    Inputs:
        stage: "raw", "interim" or "processed".
        sub_path: folders and/or file name inside that stage, written with "/",
            for example "landsat/L8_2016_08_15" or "S2_2026_07_20_refl.tif".
        create_folder: if True, create the folder so a file can be saved there.
            When sub_path ends in a file name (it has a ".something" ending), the folder
            that will contain the file is created.

    Returns:
        The full path. Example: data_dir("raw", "landsat/L8_2016_08_15")
        -> <data root>/raw/landsat/L8_2016_08_15
    """
    if stage not in DATA_STAGES:
        raise ValueError(f"stage must be one of {DATA_STAGES}, but got '{stage}'")

    full_path = data_root() / stage / sub_path

    if create_folder:
        looks_like_a_file = full_path.suffix != ""
        if looks_like_a_file:
            folder_to_create = full_path.parent
        else:
            folder_to_create = full_path
        folder_to_create.mkdir(parents=True, exist_ok=True)

    return full_path


def output_dir(kind: str, create_folder: bool = True) -> Path:
    """Folder outputs/<kind>, where kind is "figures", "tables" or "vectors"."""
    output_folder = repo_path("outputs") / kind

    if create_folder:
        output_folder.mkdir(parents=True, exist_ok=True)

    return output_folder
