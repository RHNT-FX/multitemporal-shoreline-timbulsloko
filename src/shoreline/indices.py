"""Water and vegetation indices, and how well a feature separates water from land. Owner: M2.

Course topic: Sub-CPMK 8 (feature extraction and selection).

Which band is which colour:
    colour   Landsat 8/9   Sentinel-2
    blue     B2            B2
    green    B3            B3
    red      B4            B4
    NIR      B5            B8
    SWIR1    B6            B11
    SWIR2    B7            B12

All inputs are reflectance (0..1) arrays of the same shape.

References: McFeeters (1996) NDWI; Xu (2006) MNDWI; Feyisa et al. (2014) AWEI;
Kaufman & Remer (1994) separability index M.
"""
import numpy as np


def normalized_difference(first_band: np.ndarray, second_band: np.ndarray) -> np.ndarray:
    """(first_band - second_band) / (first_band + second_band).

    The result is NaN where the sum is 0 or where an input is NaN.
    NDWI, MNDWI and NDVI all use this function.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """NDWI (Normalized Difference Water Index, McFeeters 1996) = (Green - NIR) / (Green + NIR).

    Not the same as Gao's (1996) NDWI, which uses NIR and SWIR and measures plant water.
    Check: green 0.1, nir 0.3 -> -0.5.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def mndwi(green: np.ndarray, swir1: np.ndarray) -> np.ndarray:
    """MNDWI (Modified NDWI, Xu 2006) = (Green - SWIR1) / (Green + SWIR1).

    SWIR1 must already be on the same pixel grid as green (Sentinel-2: 20 m -> 10 m first).
    """
    raise NotImplementedError("Not written yet - owner: M2")


def awei_nsh(green: np.ndarray, nir: np.ndarray, swir1: np.ndarray, swir2: np.ndarray) -> np.ndarray:
    """AWEI_nsh (Automated Water Extraction Index, "no shadow", Feyisa et al. 2014).

    AWEI_nsh = 4 * (Green - SWIR1) - (0.25 * NIR + 2.75 * SWIR2)
    Check: green 0.1, nir 0.05, swir1 0.02, swir2 0.01 -> 0.28.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def awei_sh(blue: np.ndarray, green: np.ndarray, nir: np.ndarray, swir1: np.ndarray,
            swir2: np.ndarray) -> np.ndarray:
    """AWEI_sh (the "shadow" version, Feyisa et al. 2014).

    AWEI_sh = Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 * SWIR2
    """
    raise NotImplementedError("Not written yet - owner: M2")


def ndvi(red: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """NDVI (Normalized Difference Vegetation Index) = (NIR - Red) / (NIR + Red).

    Only used as extra information (mangrove and vegetation), not for the water mask.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def separability_m(water_values: np.ndarray, land_values: np.ndarray) -> float:
    """Separability index M (Kaufman & Remer 1994), for experiment E1.

    M = |mean_water - mean_land| / (std_water + std_land)
    M above 1 means the feature separates water and land well.
    Inputs are the feature values inside the water and the land training polygons.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def fisher_ratio(water_values: np.ndarray, land_values: np.ndarray) -> float:
    """Fisher ratio, for experiment E1.

    Fisher ratio = (mean_water - mean_land)^2 / (std_water^2 + std_land^2)
    """
    raise NotImplementedError("Not written yet - owner: M2")
