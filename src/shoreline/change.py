"""Measure shoreline change: transects, rates, distances and area. Owner: M3.

Sign rule: distances are measured from a baseline on LAND towards the sea. So a negative
NSM, EPR or LRR means the shoreline moved landward (erosion).
Reference: Thieler et al. (2009), DSAS (Digital Shoreline Analysis System).
"""
import numpy as np
import pandas as pd
from shapely.geometry import LineString


def make_transects(baseline: LineString, spacing_m: float = 50, length_m: float = 4000,
                   seaward_side: str = "left") -> list[LineString]:
    """Lines at right angles to the baseline, every spacing_m metres, pointing to the sea.

    Inputs:
        baseline: the transect baseline in EPSG:32749 (drawn south-west to north-east,
            so the sea is on the left).
        spacing_m: distance between transects along the baseline.
        length_m: length of each transect.
        seaward_side: "left" or "right" of the baseline direction.

    Steps:
        1. For every distance 0, spacing_m, 2 * spacing_m, ... along the baseline,
           get the point with baseline.interpolate(distance).
        2. Direction of the baseline there: from the point 1 m before to the point 1 m after.
        3. Turn that direction 90 degrees to the seaward side.
        4. Transect = line from the point, length_m long, in that direction.
    Check: a baseline from (0, 0) to (1000, 0) gives 21 transects pointing to +y.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def intersect_transects(transects: list[LineString], shoreline: LineString,
                        which_crossing: str = "seaward") -> tuple[np.ndarray, np.ndarray]:
    """Distance from the baseline to the shoreline along every transect.

    Returns:
        distances_m: one distance per transect; NaN where the transect does not cross the shoreline.
        has_several_crossings: True where the transect crosses the shoreline more than once.
            In that case the most seaward crossing is used (which_crossing="seaward").
    """
    raise NotImplementedError("Not written yet - owner: M3")


def change_metrics(distances_m: np.ndarray, decimal_years: list[float]) -> pd.DataFrame:
    """Change numbers for every transect.

    Inputs:
        distances_m: shape (number_of_epochs, number_of_transects), from intersect_transects.
        decimal_years: date of each epoch, e.g. 2016.50 (column decimal_year of the scene table).

    Returns a table with one row per transect and these columns:
        NSM (m)       = distance in the last epoch - distance in the first epoch
        SCE (m)       = largest distance - smallest distance
        EPR (m/yr)    = NSM / years between the first and last epoch
        LRR (m/yr)    = slope of a straight-line fit of distance against year
                        (scipy.stats.linregress), with r_squared, standard_error and the
                        95% interval. Needs at least 3 epochs.
    Check: distances 1000 - 10 * (year - 2016) give EPR = LRR = -10 and r_squared = 1.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def edt_displacement(shoreline_before_mask: np.ndarray, shoreline_after_row_col: np.ndarray,
                     land_before_mask: np.ndarray, pixel_size_m: float) -> np.ndarray:
    """How far every point of the later shoreline is from the earlier shoreline (experiment E7).

    Steps:
        1. scipy.ndimage.distance_transform_edt on (NOT shoreline_before_mask) gives, for every
           pixel, the distance in pixels to the nearest earlier-shoreline pixel.
        2. Read that distance at every point of the later shoreline; multiply by pixel_size_m.
        3. Make it negative where the point lies on earlier land (the coast moved landward).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def hausdorff(first_points_xy: np.ndarray, second_points_xy: np.ndarray) -> float:
    """Hausdorff distance in metres: the worst-case distance between two shorelines.

    = the larger of scipy.spatial.distance.directed_hausdorff in both directions.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def area_change(land_before_mask: np.ndarray, sea_before_mask: np.ndarray,
                land_after_mask: np.ndarray, sea_after_mask: np.ndarray,
                valid_mask: np.ndarray, pixel_size_m: float) -> dict:
    """Land lost and gained between two dates, in hectares.

    Steps:
        1. loss_mask = land before AND sea after AND valid.
        2. gain_mask = sea before AND land after AND valid.
        3. hectares = number of pixels * pixel_size_m * pixel_size_m / 10000
           (one Sentinel-2 pixel = 0.01 ha, one Landsat pixel = 0.09 ha).

    Returns a dictionary with:
        loss_ha, gain_ha, net_ha, loss_mask, gain_mask, and transition_matrix
        (2 x 2 pixel counts: land/sea before x land/sea after).
    """
    raise NotImplementedError("Not written yet - owner: M3")
