"""Read and write rasters, clip to the AOI, and load the scene table. Owner: M1."""
from pathlib import Path

import numpy as np
import pandas as pd


def read_stack(raster_path: Path, band_numbers: list[int] | None = None) -> tuple[np.ndarray, dict]:
    """Read a GeoTIFF into an array, plus the information about where it is on the map.

    Inputs:
        raster_path: path of the GeoTIFF.
        band_numbers: which bands to read, counting from 1 (rasterio counts from 1).
            None means all bands.

    Returns:
        image_stack: float32 array with shape (bands, rows, cols). Nodata pixels become NaN.
        profile: rasterio's description of the file (crs, transform, width, height, ...).

    Steps:
        1. Open the file with rasterio.open().
        2. Read the bands and convert them to float32.
        3. Replace the nodata value with NaN.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def clip_to_aoi(input_raster_path: Path, aoi_geojson_path: Path, output_raster_path: Path) -> Path:
    """Cut a full satellite scene down to the AOI box and save the result.

    Steps:
        1. Read the AOI polygon and convert it to the raster's CRS.
        2. Cut with rasterio.mask.mask(..., crop=True).
        3. Save to output_raster_path and return that path.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def write_geotiff(output_path: Path, array: np.ndarray, profile: dict) -> Path:
    """Save a 2-D (rows, cols) or 3-D (bands, rows, cols) array as a GeoTIFF.

    Inputs:
        output_path: where to save.
        array: the data to save.
        profile: the profile of the raster the array came from (gives crs and transform).

    The function copies the profile and updates the band count, data type, nodata value
    (NaN for float data) and compression (deflate) to match the array. It returns output_path.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def load_scenes_table(csv_path: Path | None = None) -> pd.DataFrame:
    """Read metadata/scenes.csv into a table.

    Inputs:
        csv_path: path of the CSV. If None, use paths.scenes_table from params.yaml.

    Returns:
        The table, with date_utc read as a date and an extra column decimal_year
        (for example 2016-07-02 -> about 2016.50). Step 4.1 needs decimal_year for EPR and LRR.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def compute_aoi_cloud_pct(invalid_mask: np.ndarray, aoi_mask: np.ndarray) -> float:
    """Percentage of AOI pixels that are cloud, shadow, cirrus or nodata.

    Inputs:
        invalid_mask: True where the pixel is not usable
            (from radiometry.landsat_qa_mask or radiometry.s2_scl_mask).
        aoi_mask: True inside the AOI.

    Returns:
        A number from 0 to 100. It goes in the column cloud_aoi_pct of scenes.csv.

    Steps:
        1. Count the pixels that are inside the AOI.
        2. Count the pixels that are inside the AOI AND invalid.
        3. Percentage = 100 * (step 2) / (step 1).
    """
    raise NotImplementedError("Not written yet - owner: M1")
