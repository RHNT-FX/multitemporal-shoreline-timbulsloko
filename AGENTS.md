# AGENTS.md — How to write code in this repository

Read this file before writing or changing any code here. It applies to **every AI coding assistant** (Claude Code, Codex, Copilot, Cursor, Gemini, ChatGPT, …) **and to every team member**.

---

## Who reads this code

The readers are 5th-semester informatics students. They know basic Python (variables, `if`, `for`, functions, lists and dictionaries) and basic NumPy.

Every team member must be able to explain **any line** of this code, live, during the presentation Q&A, which is a large part of the individual grade. Code that the team cannot explain loses marks, even if it works.

## The one rule

> **Readable beats short. Readable beats fast. Readable beats clever.**

Write code that a classmate can follow from top to bottom on the first reading, without searching the internet.

- If you have to choose between five clear lines and one dense line, write the five lines.
- If a slower version is easier to understand, use the slower version. The AOI is only about 1110 × 1224 pixels, so nearly everything runs fast enough anyway.
- NumPy operations that read like the formula are fine and preferred. For example, `ndwi_image = (green - nir) / (green + nir)` is both short and readable.
- The rule is against **tricks**, not against NumPy.

---

## Rule 1 — Names say what the thing is

- Use full words: `water_mask`, `green_band`, `threshold_value`, `pixel_size_m`.
- Do not use single letters or private abbreviations: no `W`, `g`, `t`, `rc`, `cm`, `tmp`, `res`, `arr`, `val`, `df2`.
- Put the **unit at the end** of the name: `_m`, `_ha`, `_px`, `_pct`, `_deg`, `_m_per_year`.
- A boolean array ends in `_mask`, for example `sea_mask`. A single True/False value starts with `is_` or `has_`, for example `is_cloudy`.
- Write time as `_before` / `_after` or `_2016` / `_2026`, never `0` / `1`.
- Loop variables get real names too: `for scene_key in scene_keys:`, not `for s in ss:`.

```python
# Bad
W = idx > t
S = es(W, sr, sc, 2)

# Good
water_mask = mndwi_image > threshold_value
sea_mask = extract_sea(water_mask, seed_row, seed_col, erosion_radius=2)
```

**Short names everyone already knows** (these are allowed):

| Name | Meaning |
|---|---|
| `np`, `pd`, `plt`, `gpd` | numpy, pandas, matplotlib.pyplot, geopandas |
| `fig`, `ax` | a matplotlib figure and one of its plot areas (axes) |
| `row`, `col` | pixel position in an image (row goes down, col goes right) |
| `x`, `y` | map coordinates in metres (EPSG:32749) |
| `lon`, `lat` | longitude and latitude in degrees (EPSG:4326) |

**Technical abbreviations from the plan** may be used in names, as long as the docstring spells them out once:
- AOI, CRS, DN
- QA, SCL
- NDWI, MNDWI, AWEI, NDVI
- NSM, EPR, LRR, SCE
- EDT, FD

Examples: `mndwi_image`, `nsm_m`, `epr_m_per_year`.

---

## Rule 2 — One step per line, and give each step a name

```python
# Bad: what are b[1] and b[3]? why 1e-9?
ndwi = (b[1] - b[3]) / (b[1] + b[3] + 1e-9)

# Good
green_band = reflectance_stack[1]       # band order: blue, green, red, nir, swir1, swir2
nir_band = reflectance_stack[3]
numerator = green_band - nir_band
denominator = green_band + nir_band
ndwi_image = numerator / denominator    # NDWI = (Green - NIR) / (Green + NIR), McFeeters (1996)
```

Do not chain more than two calls together. Split long chains into named steps:

```python
# Bad
length_m = gpd.read_file(path).to_crs(32749).geometry.iloc[0].simplify(5).length

# Good
shoreline_table = gpd.read_file(shoreline_path)
shoreline_table_utm = shoreline_table.to_crs(32749)          # metres instead of degrees
shoreline_line = shoreline_table_utm.geometry.iloc[0]        # the first (and only) line
simple_line = shoreline_line.simplify(5)                     # Douglas-Peucker, 5 m tolerance
length_m = simple_line.length
```

---

## Rule 3 — Plain `for` loops and `if` blocks instead of compact tricks

Do not use the things in the left column. Write the right column instead.

| Avoid | Write instead |
|---|---|
| `lambda` | A normal `def` with a name |
| A comprehension with more than one `for`, or with an `if` inside | A `for` loop that appends to a list |
| Ternary `a if condition else b` | A full `if … else` block |
| `map`, `filter`, `functools.reduce`, `itertools` | A `for` loop |
| Walrus `:=` | A separate assignment line |
| `*args`, `**kwargs`, `*parts` | Named parameters |
| `zip(*rows)` or other star unpacking | An explicit loop or indexing |
| `dict.fromkeys(...)` to remove duplicates | A loop with `if item not in result_list:` |
| `value = x or default` | `if x is None:` followed by `x = default` |
| Functions defined inside functions, closures | Separate top-level functions |
| Decorators (`@lru_cache`, `@property`, custom ones) | Plain functions |
| Classes, inheritance, dataclasses | Functions and dictionaries |
| `try: … except: pass`, or a bare `except:` | Let the error show, or catch **one named error** and print a helpful message |
| Several statements on one line (`a = 1; b = 2`) | One statement per line |

A simple comprehension with one `for` and no `if` is allowed:

```python
squared_values = [value * value for value in values]
```

```python
# Bad
keys = [s for s in scenes if s.startswith("S2") and s not in done] or default_keys

# Good
keys = []
for scene_key in scenes:
    is_sentinel2 = scene_key.startswith("S2")
    is_already_done = scene_key in done
    if is_sentinel2 and not is_already_done:
        keys.append(scene_key)

if len(keys) == 0:
    keys = default_keys
```

---

## Rule 4 — No "magic": explain anything that seems to come from nowhere

Some Python names look like they come from nowhere, because Python creates them automatically, for example `__name__`, `__main__` and `__file__`. Readers then ask "where does this come from?". Avoid them, or explain them in a comment right where they are used.

**No `if __name__ == "__main__":` in `src/`.**
- The files in `src/shoreline/` are toolboxes of functions. Notebooks call them, and nothing in `src/` runs by itself.
- If a script truly must run from the terminal (rare), put it in `scripts/` and write the explanation right above the block:

```python
# Python fills in __name__ automatically.
# If you run this file directly (python scripts/make_figures.py), __name__ is "__main__",
# so the line below runs. If another file imports this file, __name__ is "make_figures"
# instead, and the line below is skipped.
if __name__ == "__main__":
    make_all_figures()
```

**`__file__`** must also be explained where it is used. `src/shoreline/config.py` shows how.

**No hidden global variables.**
- A function uses only its parameters, plus CONSTANTS written in CAPITALS at the top of the same file.
- Each constant has a comment saying where its value comes from.
- A function never reads a variable that was defined in some notebook cell.

**Show which library a function comes from.** Import the module, then call the function through it:

```python
# Bad: the reader sees label(...) and cannot tell which library it is from
from scipy.ndimage import label
labelled_image, count = label(eroded_mask)

# Good
from scipy import ndimage

# ndimage.label gives every connected group of True pixels its own number: 1, 2, 3, ...
labelled_image, number_of_groups = ndimage.label(eroded_mask)
```

The first time a library function appears in a file, add a one-line comment on what it does, unless its name already says it.

**NumPy tricks get either a comment or a plain loop.** This covers `np.newaxis` / `None` indexing, broadcasting, fancy indexing, `axis=`, `np.unravel_index`, `np.einsum` and `np.lib.stride_tricks`. Write array shapes in comments, for example `# shape: (6, rows, cols)`.

```python
# Bad: what do argmax and unravel_index return?
peak = np.unravel_index(np.argmax(c), c.shape)

# Good: the slow but obvious way
largest_value = -np.inf
peak_row = 0
peak_col = 0
number_of_rows = correlation_image.shape[0]
number_of_cols = correlation_image.shape[1]
for row in range(number_of_rows):
    for col in range(number_of_cols):
        if correlation_image[row, col] > largest_value:
            largest_value = correlation_image[row, col]
            peak_row = row
            peak_col = col

# Also fine: the short version, with a comment that explains it
flat_position = np.argmax(correlation_image)       # position of the largest value, counted as if the image were one long row
peak_row, peak_col = np.unravel_index(flat_position, correlation_image.shape)   # turn that position back into (row, col)
```

---

## Rule 5 — Imports

- Put all imports at the **top of the file**. Never import inside a function.
- One import per line: `import os` and then `import sys` on the next line, not `import os, sys`.
- Use three groups, in this order, with an empty line between them:
  1. Python's built-in modules (`os`, `math`, `pathlib`)
  2. installed libraries (`numpy`, `rasterio`, `skimage`)
  3. our own modules (`from shoreline import segment`)
- Our own modules are imported by full name: `from shoreline import segment`, and then called as `segment.otsu(...)`. Do not use relative imports such as `from . import segment`.
- Do not use `from __future__ import ...`, `if TYPE_CHECKING:` blocks, or `from x import *`.

---

## Rule 6 — Functions

- **One function does one job.** Aim for fewer than about 40 lines. If a function has three stages, write three small functions and call them in order.
- **Every value comes in as a parameter.** Low-level functions do not read `params.yaml` themselves. The notebook loads the parameters and passes the values in. `config.py` is the only exception. This makes every function testable and easy to follow.
- **Parameter names are full words with units.** Default values equal the values in `params.yaml`.
- **Return one value, or a pair.** If a function returns more than two things, return a **dictionary with named keys**, so callers write `result["loss_ha"]` instead of `result[3]`.
- **Never change an input array.** Do not use `+=` on a parameter or `out=`. Use `.copy()` first if you need to modify it.
- **Simple type hints are welcome:** `def ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:`.
  - Use only basic types: `np.ndarray`, `float`, `int`, `str`, `bool`, `list`, `dict`, `tuple`, `Path`, `pd.DataFrame`, `LineString`.
  - Use `X | None` when a value is optional.
  - Do not use `TypeVar`, `Protocol`, `Callable`, `Literal`, `Iterable`, or type hints written as strings.

---

## Rule 7 — Docstrings and comments

Every function gets a docstring in this format:

```python
def clean_mask(mask: np.ndarray, opening_radius: int = 1, closing_radius: int = 1,
               min_object_px: int = 10) -> np.ndarray:
    """Remove small noise from a water mask.

    Inputs:
        mask: True = water. Shape (rows, cols).
        opening_radius: radius of the round structuring element for opening, in pixels.
        closing_radius: radius for closing, in pixels.
        min_object_px: water groups (and land holes) smaller than this are removed.

    Returns:
        A new True/False mask with the same shape. The input is not changed.

    Steps:
        1. Opening (erosion, then dilation) removes isolated water pixels.
        2. Closing (dilation, then erosion) fills gaps one pixel wide.
        3. Remove water groups and land holes smaller than min_object_px.

    Reference: Gonzalez & Woods (2018), chapter 9. Plan: 02_PIPELINE_METHODS.md, Stage 3.2.
    """
```

- Comments explain **why**, and point to the plan step they implement, for example `# see 02_PIPELINE_METHODS.md, Stage 3.3`.
- Write formulas the way the paper writes them, and say which variable holds each symbol.
- **Language:** code, names, comments and docstrings are in English. Markdown cells in notebooks are in Bahasa Indonesia, because that is the report language.

---

## Rule 8 — Numbers and parameters

- **No magic numbers.** Every value that can be tuned lives in `config/params.yaml`.
- A fixed physical constant becomes a CONSTANT at the top of the module, with its source in a comment:

```python
# USGS Landsat 8-9 Collection 2 Level-2 Science Product Guide:
# reflectance = DN * LANDSAT_SCALE + LANDSAT_OFFSET
LANDSAT_SCALE = 0.0000275
LANDSAT_OFFSET = -0.2
```

- Anything random uses the seed `params["project"]["seed"]`, which is 2026.

---

## Rule 9 — Write the algorithm ourselves, then check it against the library

The course grades understanding. For the algorithms named in the plan, write our own step-by-step version following the formula in the docstring:
- Otsu
- histogram equalisation
- FFT low-pass
- phase correlation
- region growing
- chain code
- Fourier descriptors
- transects
- accuracy metrics

Then **compare** our version with the library version in a test. Do not replace our version with a library one-liner.

---

## Rule 10 — Errors and checks

- **Check inputs early, with a clear message** that says what to fix:

```python
if water_mask.dtype != bool:
    raise ValueError(f"water_mask must contain True/False values, but its type is {water_mask.dtype}")
```

- **f-strings are fine.** Keep the formatting inside them simple, for example `{value:.2f}`.
- **`assert` belongs only in `tests/`.**
- **In notebooks, print what happened:** array shapes, minimum and maximum values, pixel counts and thresholds.

---

## Rule 11 — Notebooks

- One step per cell.
  - Before the cell: a Markdown cell (in Bahasa Indonesia) saying **what** this step does and **why**.
  - After it: an **Analisis** cell with the actual numbers.
- Notebooks call functions from `src/shoreline/`. Only a small helper (a few lines) may be defined inside a notebook.
- Variables in notebooks follow the same naming rules as `src/`. The parameter dictionary is called `params`.
- **Runtime → Restart and run all** must work from top to bottom.

---

## Rule 12 — Tests

- Tests go in `tests/test_<module>.py` and run with `pytest -q`.
- Each test checks one behaviour.
- Use tiny inputs written out by hand, so a reader can work out the answer in their head:

```python
import numpy as np

from shoreline import indices


def test_ndwi_with_simple_numbers():
    green = np.array([0.1])
    nir = np.array([0.3])
    result = indices.ndwi(green, nir)
    expected = -0.5                      # (0.1 - 0.3) / (0.1 + 0.3)
    assert abs(result[0] - expected) < 1e-9
```

---

## Project rules that every agent must also follow

1. **The course brief.**
   - Google Earth Engine is used **only** to search for scenes and export AOI clips. All core processing is our own Python.
   - Analysis runs on reflectance GeoTIFFs, never on PNG or JPG.
   - Every figure goes through `viz` helpers that add the attribution text.
   - Never commit raster files.
2. **Ownership.**
   - Each module has an owner (M1–M4, listed in `src/shoreline/__init__.py`), and every member's contribution history is graded.
   - Change only the module or modules you were asked about.
   - Leave `raise NotImplementedError("Not written yet - owner: Mx")` in functions you were not asked to write.
3. **Stable names.** Do not rename functions, because the plan documents in `docs/` refer to them. A parameter may be renamed only together with every place that uses it, in code and in the docs.
4. **Git.** Do not commit or push unless you are asked to.
5. **When you finish,** explain in plain words what you changed, why, and how to check it.

---

## Self-check before you finish

- [ ] Could a classmate explain every line without searching the internet?
- [ ] Is every name a full word, with its unit where it has one?
- [ ] Is there nothing from the "Avoid" table in Rule 3?
- [ ] Is every "magic" name (`__file__`, `__name__`, NumPy tricks) explained, or gone?
- [ ] Does every number come from `params.yaml` or from a CONSTANT with a source comment?
- [ ] Does every function have a docstring with Inputs, Returns and Steps?
- [ ] Does every figure carry the attribution text?
- [ ] Do the tests pass with `pytest -q`?
