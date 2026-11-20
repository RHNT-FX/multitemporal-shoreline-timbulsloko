"""Shoreline change pipeline for Desa Timbulsloko, Demak (2016-2026).

Why does this file exist?
    A folder with a file called __init__.py is a "package" in Python. Because this file is
    here, notebooks can write `from shoreline import segment`. The file itself does nothing else.

The modules follow the order of the pipeline (see docs/02_PIPELINE_METHODS.md).
Owner = the team member who writes and explains that module.

    module       what it does                                    owner
    ----------   ---------------------------------------------   ------
    config       read params.yaml, build file paths              shared
    io           read/write rasters, clip to AOI, scene table    M1
    radiometry   DN -> reflectance, cloud masks (QA / SCL)       M1
    geometry     grids, resampling, co-registration              M1
    enhance      stretch, histogram equalisation, denoising      M2
    indices      NDWI / MNDWI / AWEI / NDVI, separability        M2
    segment      Otsu, thresholds, morphology, sea extraction    M2
    contour      boundaries, sub-pixel contour, lines            M3
    descriptors  chain code, Fourier descriptors, shape          M3
    change       transects, NSM / EPR / LRR, distances, area     M3
    evaluate     confusion matrix, errors, uncertainty           M4
    viz          figures and the required attribution text       shared

Coding rules for everyone (people and AI assistants): see AGENTS.md in the repository root.
"""
