"""Contrast enhancement and noise removal. Owner: M2.

Course topics: Sub-CPMK 2 (spatial enhancement) and Sub-CPMK 3 (frequency-domain filtering).

Important: stretch, histogram equalisation and CLAHE are ONLY for pictures and for labelling.
Thresholds are always computed on the real reflectance or index values
(see 02_PIPELINE_METHODS.md, Stage 1, the note under the table).
"""
import numpy as np


def percentile_stretch(image: np.ndarray, low_percent: float = 2,
                       high_percent: float = 98) -> np.ndarray:
    """Linear contrast stretch for display. Output values are between 0 and 1.

    Steps:
        1. low_value = the low_percent percentile of the image, ignoring NaN (np.nanpercentile).
        2. high_value = the high_percent percentile.
        3. stretched = (image - low_value) / (high_value - low_value), then clip to 0..1.
    For a 3-band composite, stretch each band on its own.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def hist_equalize(image: np.ndarray, number_of_bins: int = 256) -> np.ndarray:
    """Our own histogram equalisation (Gonzalez & Woods 2018, section 3.3).

    Steps:
        1. Histogram of the valid (non-NaN) pixels.
        2. Cumulative sum of the histogram, divided by the total = the CDF (0..1).
        3. Every pixel gets the CDF value of its own bin.
    Check: compare with skimage.exposure.equalize_hist (correlation above 0.99).
    """
    raise NotImplementedError("Not written yet - owner: M2")


def clahe(image: np.ndarray, clip_limit: float = 2.0, tile_grid: tuple = (8, 8)) -> np.ndarray:
    """CLAHE (contrast-limited adaptive histogram equalisation) for display.

    Use OpenCV: cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid) on a uint8 copy
    of the image (0..255). The clip_limit 2.0 is OpenCV's scale. skimage's equalize_adapthist
    uses a different scale (0..1, usually 0.01), so do not pass 2.0 to skimage.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def denoise(image: np.ndarray, method: str = "median", gaussian_sigma: float = 1.0,
            median_size: int = 3, bilateral_diameter: int = 5) -> np.ndarray:
    """Smooth an index image before thresholding (experiment E2).

    Inputs:
        method: "none", "gaussian", "median", "bilateral" or "fft_lowpass".
        gaussian_sigma: used by "gaussian" and "fft_lowpass", in pixels.
        median_size: window size for "median", in pixels.
        bilateral_diameter: neighbourhood size for "bilateral", in pixels.

    NaN pixels: fill them with a nearby value first, filter, then put the NaN back.
    """
    raise NotImplementedError("Not written yet - owner: M2")


def fft_lowpass(image: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Gaussian low-pass filter done in the frequency domain.

    Steps:
        1. F = FFT of the image.
        2. H = Gaussian transfer function with the same sigma as the spatial Gaussian.
        3. smoothed = inverse FFT of (F * H), real part.
    With the same sigma, the result should equal the spatial Gaussian filter (convolution
    theorem). Show the difference image as proof.
    """
    raise NotImplementedError("Not written yet - owner: M2")
