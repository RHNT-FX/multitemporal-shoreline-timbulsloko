"""Figures. Shared by everyone.

Brief rule: EVERY figure must show the data attribution text. Every plotting function in this
file calls add_attribution(), so a figure made with these helpers always has it.
"""
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure


# Attribution text per data source, exactly as the brief asks.
ATTRIBUTION = {
    "S2": "Contains modified Copernicus Sentinel data 2026",
    "L8": "Landsat imagery courtesy of the U.S. Geological Survey",
    "L9": "Landsat imagery courtesy of the U.S. Geological Survey",
    "OSM": "© OpenStreetMap contributors (ODbL)",
}


def add_attribution(ax: Axes, sensors: list[str], font_size: float = 6) -> None:
    """Write the attribution text in the bottom-right corner of a plot.

    Inputs:
        ax: the matplotlib plot area (axes) to write on.
        sensors: which data the plot shows, using the keys of ATTRIBUTION,
            for example ["S2"] or ["L8", "L9", "OSM"].
        font_size: text size in points.

    Landsat 8 and Landsat 9 have the same text; it is written only once.
    """
    texts_to_write = []
    for sensor_name in sensors:
        text = ATTRIBUTION[sensor_name]
        if text not in texts_to_write:
            texts_to_write.append(text)

    if len(texts_to_write) == 0:
        return

    # One line per attribution text
    all_text = "\n".join(texts_to_write)

    # A dark, half-transparent box behind the text so it is readable on any image
    background_box = {
        "boxstyle": "round,pad=0.2",
        "facecolor": "black",
        "alpha": 0.45,
        "linewidth": 0,
    }

    # transform=ax.transAxes means x and y are measured from 0 to 1 across the plot area,
    # so (0.99, 0.01) is the bottom-right corner, whatever the image size is.
    ax.text(
        0.99,
        0.01,
        all_text,
        transform=ax.transAxes,
        horizontalalignment="right",
        verticalalignment="bottom",
        fontsize=font_size,
        color="white",
        bbox=background_box,
    )


def show_rgb(ax: Axes, rgb_image: np.ndarray, sensors: list[str], title: str = "") -> None:
    """Show a colour composite with its attribution.

    Inputs:
        ax: plot area to draw on.
        rgb_image: shape (rows, cols, 3), values already stretched to 0..1.
        sensors: data shown, for the attribution, e.g. ["S2"].
        title: plot title.
    """
    raise NotImplementedError("Not written yet - owner: shared")


def before_after(before_image: np.ndarray, after_image: np.ndarray, before_title: str,
                 after_title: str, sensors: list[str], colormap: str | None = None) -> Figure:
    """Side-by-side "before" and "after" images, each with its histogram underneath.

    The brief wants a before/after comparison for every technique.

    Returns:
        The matplotlib figure, so the notebook can save it with save_figure().
    """
    raise NotImplementedError("Not written yet - owner: shared")


def change_map(ax: Axes, loss_mask: np.ndarray, gain_mask: np.ndarray, land_mask: np.ndarray,
               sensors: list[str]) -> None:
    """Change map (figure F10): land loss in red, land gain in blue, stable land and sea in grey.

    The legend shows the hectares of loss and gain.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def transect_map(ax: Axes, transects: list, values: np.ndarray, sensors: list[str],
                 label: str = "EPR (m/yr)") -> None:
    """Transects coloured by a value such as EPR (figure F9).

    Use a red-white-blue colour scale with white at 0, so retreat and advance are easy to tell apart.
    """
    raise NotImplementedError("Not written yet - owner: M3")


def save_figure(fig: Figure, file_name: str, dpi: int = 200) -> None:
    """Save a figure as outputs/figures/<file_name>.png (PNG, as the brief recommends)."""
    raise NotImplementedError("Not written yet - owner: shared")
