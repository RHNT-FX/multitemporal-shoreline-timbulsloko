"""Put rasters on a fixed pixel grid, resample them, and check how well they line up. Owner: M1.

Course topics: Sub-CPMK 5 (registration, warping, zooming) and Sub-CPMK 3 (phase correlation,
which uses the Fourier shift theorem).
"""
import numpy as np


def reproject_to_grid(array: np.ndarray, source_profile: dict, grid: dict,
                      target_crs: str = "EPSG:32749",
                      resampling_method: str = "bilinear") -> tuple[np.ndarray, dict]:
    """Move a raster onto one of our fixed pixel grids.

    Every epoch of one sensor must sit on exactly the same pixels, otherwise comparing masks
    pixel by pixel shows fake change. (See 05_STEP_BY_STEP.md, step 1.1.)

    Inputs:
        array: shape (rows, cols) or (bands, rows, cols).
        source_profile: rasterio profile of the input (gives its crs and transform).
        grid: params["grid"]["s2_grid"] or params["grid"]["landsat_grid"], a dictionary with
            x0, y_top, res, width and height.
        target_crs: the CRS of the grid.
        resampling_method: "nearest" for masks and class bands (QA_PIXEL, SCL), "nearest" or
            "bilinear" for reflectance.

    Returns:
        new_array: the data on the grid.
        new_profile: the matching profile.

    Steps:
        1. Build the target transform from the grid: Affine(res, 0, x0, 0, -res, y_top).
        2. Call rasterio.warp.reproject() with that transform, width, height and CRS.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def resample(array: np.ndarray, zoom_factor: float, method: str = "bilinear") -> np.ndarray:
    """Make an image finer, e.g. 20 m -> 10 m with zoom_factor 2.0.

    method: "nearest", "bilinear" or "cubic". Experiment E6 compares the three for SWIR (B11/B12).
    Check: a sharp edge must stay at the same place (within 0.5 pixel) for all three methods.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def phase_correlation(reference_image: np.ndarray, moving_image: np.ndarray,
                      upsample_factor: int = 10) -> tuple[float, float, float]:
    """Our own phase correlation: how far is moving_image shifted compared to reference_image?

    Inputs:
        reference_image, moving_image: same shape, cut from a STABLE inland window (villages,
            roads), not the eroding coast. NaNs must be filled first.
        upsample_factor: how finely to measure below one pixel.

    Returns:
        shift_rows, shift_cols (in pixels) and peak_value (how sharp the match is).

    Steps (Fourier shift theorem):
        1. Multiply both images by a Hann window to soften the edges.
        2. F = FFT of reference_image, G = FFT of moving_image.
        3. R = F * conj(G) / |F * conj(G)|   (keep only the phase).
        4. r = inverse FFT of R. The position of its highest value is the shift.
        5. Refine below one pixel around that peak.
    Check against skimage.registration.phase_cross_correlation.
    """
    raise NotImplementedError("Not written yet - owner: M1")


def apply_shift(array: np.ndarray, shift_rows: float, shift_cols: float,
                interpolation_order: int = 1) -> np.ndarray:
    """Move an image by (shift_rows, shift_cols) pixels with scipy.ndimage.shift.

    interpolation_order: 1 for reflectance, 0 for True/False masks.
    """
    raise NotImplementedError("Not written yet - owner: M1")
