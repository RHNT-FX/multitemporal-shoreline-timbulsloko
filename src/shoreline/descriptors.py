"""Describe the shape of the shoreline with numbers. Owner: M3.

Course topics: Sub-CPMK 8 (feature extraction) and Sub-CPMK 9 (representation).
References: Freeman (1961) chain code; Zahn & Roskies (1972) Fourier descriptors;
Gonzalez & Woods (2018) chapter 11.
"""
import numpy as np


# Freeman 8-direction chain code: code -> (change in row, change in col).
# 0 = east, then counter-clockwise. Rows increase DOWNWARDS in an image,
# so "north" means the row number goes down by 1.
#
#     3  2  1
#     4  .  0
#     5  6  7
FREEMAN_DIRECTIONS = {
    0: (0, 1),     # east
    1: (-1, 1),    # north-east
    2: (-1, 0),    # north
    3: (-1, -1),   # north-west
    4: (0, -1),    # west
    5: (1, -1),    # south-west
    6: (1, 0),     # south
    7: (1, 1),     # south-east
}


def freeman_chain_code(boundary_row_col: np.ndarray) -> np.ndarray:
    """Our own Freeman chain code of an ordered boundary.

    Inputs:
        boundary_row_col: shape (number_of_points, 2), neighbouring boundary pixels in order
            (from contour.pixel_boundary).

    Steps:
        For every pair of consecutive points, compute (row change, col change) and look up
        which code in FREEMAN_DIRECTIONS has that change.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def chain_first_difference(chain_code: np.ndarray) -> np.ndarray:
    """First difference: (code[i] - code[i - 1]) mod 8.

    Turning the whole shape by 90 degrees does not change the first difference
    (rotation invariance).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def chain_min_rotation(chain_code: np.ndarray) -> np.ndarray:
    """Shape number: of all cyclic shifts of the code, the one that reads as the smallest number.

    Starting the code at another boundary point gives the same result (start-point invariance).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def chain_histogram(chain_code: np.ndarray) -> tuple[np.ndarray, float]:
    """How often each of the 8 directions occurs, and how mixed they are.

    Returns:
        direction_shares: 8 numbers that add up to 1.
        entropy_bits: Shannon entropy = -sum(share * log2(share)), between 0 and 3.
            A higher value means a more irregular coast.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def chain_length(chain_code: np.ndarray, pixel_size_m: float) -> float:
    """Boundary length in metres: even codes count 1 pixel, odd (diagonal) codes count sqrt(2) pixels."""
    raise NotImplementedError("Not written yet - owner: M3")


def resample_curve(points_xy: np.ndarray, number_of_points: int = 512) -> np.ndarray:
    """Put number_of_points points along a line, equally spaced by distance along the line.

    Steps:
        1. Distance from the start to every vertex (cumulative sum of segment lengths).
        2. number_of_points equally spaced distances from 0 to the total length.
        3. np.interp gives the x and the y at those distances.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def fourier_descriptors(points_xy: np.ndarray, number_of_points: int = 512,
                        close_by_mirroring: bool = True) -> np.ndarray:
    """Our own Fourier descriptors of a shoreline.

    Use the same stretch of coast (between the same two transects) for every year.

    Steps:
        1. Resample the line to number_of_points points (resample_curve).
        2. Write each point as a complex number z = x + i*y.
        3. A shoreline is an OPEN line, but the DFT treats the signal as repeating. Close it by
           adding the same points backwards (z, then z reversed), so there is no jump.
        4. coefficients = FFT(z) / len(z).
        5. Normalise: drop coefficient 0 (position), divide by |coefficient 1| (size),
           keep magnitudes (rotation and start point).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def reconstruct_fd(coefficients: np.ndarray, number_of_harmonics: int) -> np.ndarray:
    """Rebuild the line from only the lowest number_of_harmonics positive and negative harmonics.

    Used for figure F13 (K = 4, 8, 16, 32).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def fd_roughness(coefficients: np.ndarray, number_of_harmonics: int = 8) -> float:
    """Roughness = 1 - (energy in the lowest number_of_harmonics harmonics / total energy).

    Energy = sum of |coefficient|^2, without coefficient 0. A higher value means a rougher coast.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def shape_metrics(points_xy: np.ndarray) -> dict:
    """Simple numbers for one line.

    Returns a dictionary with:
        length_m, endpoint_distance_m, sinuosity (= length_m / endpoint_distance_m).
    """
    raise NotImplementedError("Not written yet - owner: M3")


def patch_props(mask: np.ndarray, pixel_size_m: float) -> list[dict]:
    """Numbers for every separate patch (8 neighbours) of a mask, e.g. the land-loss mask.

    Uses skimage.measure.regionprops. One dictionary per patch with:
        area_ha, perimeter_m, compactness (4 * pi * area / perimeter^2),
        eccentricity, orientation, major_axis_m.
    """
    raise NotImplementedError("Not written yet - owner: M3")
