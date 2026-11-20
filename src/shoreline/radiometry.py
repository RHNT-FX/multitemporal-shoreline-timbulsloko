"""Convert raw satellite numbers (DN) to reflectance, and build cloud masks. Owner: M1.

Sources:
    - USGS Landsat 8-9 Collection 2 Level-2 Science Product Guide (scale 0.0000275, offset -0.2).
    - ESA Sentinel-2 product specification: from processing baseline 04.00 (25 Jan 2022) the
      products carry an offset of -1000 (BOA_ADD_OFFSET / RADIO_ADD_OFFSET).
"""
import numpy as np


# Landsat Collection 2 Level-2: reflectance = DN * LANDSAT_SCALE + LANDSAT_OFFSET
LANDSAT_SCALE = 0.0000275
LANDSAT_OFFSET = -0.2

# Sentinel-2: reflectance = (DN + offset) / S2_QUANTIFICATION_VALUE
S2_QUANTIFICATION_VALUE = 10000
S2_OFFSET_DN = -1000


def landsat_to_reflectance(digital_numbers: np.ndarray, scale: float = LANDSAT_SCALE,
                           offset: float = LANDSAT_OFFSET) -> np.ndarray:
    """Landsat surface reflectance from the stored integers (DN).

    Inputs:
        digital_numbers: a Landsat SR_B* band as stored in the file.

    Returns:
        float32 reflectance between 0 and 1. Fill pixels (DN = 0) and DNs outside the valid
        range 7273-43636 become NaN, not -0.2.

    Formula: reflectance = DN * scale + offset.
    Check: DN 10000 -> 0.075, DN 43636 -> about 1.0, DN 0 -> NaN.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def s2_offset_for_baseline(processing_baseline: str, offset_dn: int = S2_OFFSET_DN,
                           first_baseline_with_offset: str = "04.00") -> int:
    """Which DN offset a Sentinel-2 product needs.

    Inputs:
        processing_baseline: from the product name or metadata, e.g. "05.09" or "N0509".

    Returns:
        offset_dn (-1000) if the baseline is 04.00 or newer, otherwise 0.

    Steps:
        1. Remove a leading "N" and turn "0509" or "05.09" into two numbers: (5, 9).
        2. Compare those numbers with (4, 0). Do NOT compare the text, because text comparison
           of "4.00" and "04.00" gives the wrong answer.
    Check: "02.07" -> 0; "04.00", "N0509", "05.11" -> -1000.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def s2_to_reflectance(digital_numbers: np.ndarray, offset_dn: int = 0,
                      quantification_value: int = S2_QUANTIFICATION_VALUE) -> np.ndarray:
    """Sentinel-2 reflectance: (DN + offset_dn) / quantification_value. DN 0 becomes NaN.

    For GEE "*_HARMONIZED" exports the offset is already removed, so use offset_dn = 0.
    A CDSE export may already be float reflectance: check the values before converting.
    Clip to 0..1 and print how many pixels were clipped.
    Check: DN 2000 with offset_dn -1000 -> 0.1.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def landsat_qa_mask(qa_pixel_band: np.ndarray, bits_to_mask: tuple = (0, 1, 2, 3, 4)) -> np.ndarray:
    """True where a Landsat pixel is not usable, using the QA_PIXEL band.

    Bits of QA_PIXEL that mark a bad pixel: 0 fill, 1 dilated cloud, 2 cirrus, 3 cloud,
    4 cloud shadow. A bit is "set" when (qa_value AND 2**bit) is not 0.

    Returns:
        True/False mask with the same shape as qa_pixel_band.
    Check: 21824 (clear land) and 21952 (clear water) -> False; 22280 (cloud) and 1 (fill) -> True.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def s2_scl_mask(scl_band: np.ndarray, invalid_classes: tuple = (0, 1, 3, 8, 9, 10)) -> np.ndarray:
    """True where a Sentinel-2 pixel is not usable, using the Scene Classification Layer (SCL).

    SCL classes treated as bad: 0 no data, 1 saturated/defective, 3 cloud shadow,
    8 cloud medium probability, 9 cloud high probability, 10 thin cirrus.
    Check: 6 (water) -> False; 9 and 0 -> True.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def dilate_mask(mask: np.ndarray, grow_by_px: int = 1) -> np.ndarray:
    """Grow a bad-pixel mask by grow_by_px pixels, to also catch the soft edges of clouds.

    Uses binary dilation with a round structuring element (skimage.morphology.disk).
    """
    raise NotImplementedError("Not written yet - owner: M1")
