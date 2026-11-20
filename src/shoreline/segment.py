"""Thresholding, morphology and sea extraction. Owner: M2.

Course topics: Sub-CPMK 6 (morphology) and Sub-CPMK 7 (segmentation).

Order of use:
    index image -> threshold() -> clean_mask() -> extract_sea() -> sea mask and land mask
"""
import numpy as np


def otsu(values: np.ndarray, number_of_bins: int = 256) -> float:
    """Our own Otsu threshold (Otsu 1979).

    Inputs:
        values: the index values to split into two groups. NaN values are ignored.
        number_of_bins: number of histogram bins.

    Returns:
        The threshold. Values ABOVE it are the "bright" group (water for MNDWI).

    Steps:
        1. Histogram of the values; p = counts / total; keep the centre of every bin.
        2. omega(k) = cumulative sum of p            (share of pixels at or below bin k)
           mu(k)    = cumulative sum of p * centre   (their mean, times omega)
           mu_total = the last value of mu
        3. between_class_variance(k) = (mu_total * omega(k) - mu(k))^2 / (omega(k) * (1 - omega(k)))
           Skip bins where omega is exactly 0 or 1.
        4. The threshold is the bin centre where between_class_variance is largest.
    Check: within one bin width of skimage.filters.threshold_otsu.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def threshold(index_image: np.ndarray, method: str = "otsu_buffer",
              valid_mask: np.ndarray | None = None, buffer_mask: np.ndarray | None = None,
              fixed_value: float = 0.0, number_of_classes: int = 3,
              hysteresis_low: float | None = None,
              hysteresis_high: float | None = None) -> tuple[np.ndarray, list[float]]:
    """Make a water mask from an index image (experiment E3).

    Inputs:
        index_image: e.g. the MNDWI image.
        method: which rule to use:
            "fixed"        water = index > fixed_value
            "otsu"         Otsu on all valid pixels
            "otsu_buffer"  Otsu only on pixels inside buffer_mask (a band about 1.5 km
                           around the coast), so the histogram has two clear peaks
            "multi_otsu"   Otsu with number_of_classes classes; water = the highest class
            "hysteresis"   strong water above hysteresis_high, plus connected weaker water
                           above hysteresis_low
        valid_mask: True where the pixel is usable. None = all pixels.
        buffer_mask: needed for "otsu_buffer".

    Returns:
        water_mask: True = water.
        thresholds_used: list of the threshold value(s), to report per scene (table T3).
    """
    raise NotImplementedError("Not written yet - owner: M2")


def clean_mask(mask: np.ndarray, opening_radius: int = 1, closing_radius: int = 1,
               min_object_px: int = 10) -> np.ndarray:
    """Remove small noise from a water mask.

    Steps:
        1. Opening (erosion, then dilation) with a disk of opening_radius removes lone water pixels.
        2. Closing (dilation, then erosion) with a disk of closing_radius fills 1-pixel gaps.
        3. Remove water groups and land holes smaller than min_object_px
           (params: 10 px for Sentinel-2, 3 px for Landsat).
    Returns a new mask; the input is not changed.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def extract_sea(water_mask: np.ndarray, seed_row: int, seed_col: int,
                erosion_radius: int = 2) -> np.ndarray:
    """Keep only the open sea, not the fish ponds (tambak) next to it (experiment E4).

    Inputs:
        water_mask: True = water (sea and ponds together).
        seed_row, seed_col: pixel of the sea seed point, which is open sea in every year.
        erosion_radius: radius of the disk, in pixels.

    Steps:
        1. eroded_mask = erosion of water_mask with a disk of erosion_radius.
           This cuts thin water connections (narrower than about 2 * erosion_radius + 1 pixels)
           between the sea and the ponds.
        2. Label the connected groups of eroded_mask (8 neighbours) and keep only the group
           that contains the seed pixel.
        3. sea_mask = dilation of that group with the same disk, AND water_mask.
           The dilation gives back the sea's own edge without re-flooding the cut-off ponds.
    Note: "morphological reconstruction" would re-flood the ponds, so we do not use it here.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def region_grow(index_image: np.ndarray, seed_row: int, seed_col: int, minimum_value: float,
                max_neighbour_difference: float) -> np.ndarray:
    """Our own region growing from the sea seed: an alternative to extract_sea for E4.

    Steps (breadth-first search with a list used as a queue):
        1. Start with the seed pixel in the queue and in the region.
        2. Take a pixel from the queue. Look at its 8 neighbours.
        3. Add a neighbour to the region (and the queue) when its index value is above
           minimum_value AND differs from the current pixel by less than max_neighbour_difference.
        4. Repeat until the queue is empty.
    """
    raise NotImplementedError("Not written yet - owner: M2")
