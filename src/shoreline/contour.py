"""Find the sea-land boundary and turn it into map lines. Owner: M3.

Course topics: Sub-CPMK 7 (edge detection) and Sub-CPMK 9 (representation).
"""
import numpy as np
from rasterio.transform import Affine
from shapely.geometry import LineString


def pixel_boundary(sea_mask: np.ndarray) -> list[np.ndarray]:
    """Boundary pixels of the sea mask, in order along the boundary.

    Uses cv2.findContours(..., cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE).
    Careful: OpenCV gives points as (x, y) = (col, row). Swap them to (row, col).

    Returns:
        A list of arrays, one per boundary piece, each with shape (number_of_points, 2)
        holding (row, col). This is also the input for the Freeman chain code.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def subpixel_shoreline(index_image: np.ndarray, threshold_value: float, sea_mask: np.ndarray,
                       band_width_px: int = 2, valid_mask: np.ndarray | None = None) -> list[np.ndarray]:
    """Shoreline with sub-pixel precision (marching squares).

    Steps:
        1. skimage.measure.find_contours(index_image, threshold_value) gives lines of
           (row, col) points where the index crosses the threshold.
        2. Keep only points within band_width_px of the sea-mask boundary. This drops the
           edges of inland ponds.
        3. Drop pieces that touch the image edge or invalid (cloud) pixels.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def canny_boundary(index_image: np.ndarray, sigma: float, sea_mask: np.ndarray,
                   band_width_px: int = 2) -> np.ndarray:
    """Canny edges of the index image, kept only near the sea boundary (experiment E5).

    Uses skimage.feature.canny(index_image, sigma=sigma). Canny also finds pond walls,
    which is why only edges within band_width_px of the sea boundary are kept.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def to_linestring(row_col_points: np.ndarray, transform: Affine) -> LineString:
    """Turn (row, col) pixel points into a line in map coordinates (EPSG:32749, metres).

    Use rasterio.transform.xy(transform, rows, cols, offset="center").
    offset="center" matters: a pixel's centre is half a pixel away from its corner. Using the
    corner shifts the whole line by 5 m (Sentinel-2) or 15 m (Landsat).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def simplify(line: LineString, tolerance_m: float) -> LineString:
    """Douglas-Peucker simplification: line.simplify(tolerance_m, preserve_topology=False).

    tolerance_m is in metres: 0.5 pixel = 5 m for Sentinel-2, 15 m for Landsat.
    """
    raise NotImplementedError("Not written yet - owner: M3")
