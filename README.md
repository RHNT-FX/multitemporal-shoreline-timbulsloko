# Multitemporal Shoreline Change — Desa Timbulsloko, Demak (2016–2026)

**Analisis Perubahan Garis Pantai dan Estimasi Kehilangan Daratan Menggunakan Citra Satelit Multitemporal Landsat dan Sentinel-2 di Desa Timbulsloko, Demak (2016–2026)**

Tugas Besar Pengolahan Citra Digital, Semester Gasal 2026/2027, Program Studi Informatika, Institut Teknologi Kalimantan.

> **Status:** skeleton only. Module functions raise `NotImplementedError` until their owner implements them. The plan documents (`00_PLAN_OVERVIEW.md` through `05_STEP_BY_STEP.md`) sit next to this folder; copy them into `docs/` when this moves to GitHub. `05_STEP_BY_STEP.md` is the day-by-day runbook.

## Questions this project answers
1. How many metres (and m/yr) has the Timbulsloko shoreline retreated between 2016 and 2026?
2. How many hectares of land were lost (and gained), and where?
3. Which water index and segmentation method extracts the shoreline most accurately on this muddy, tambak-dominated coast?
4. How consistent are Landsat 8/9 (30 m) and Sentinel-2 (10 m)?

## Area of interest
`data/aoi/aoi_timbulsloko.geojson` is a box of lon 110.45–110.55 °E, lat −6.95 to −6.84 °N, about 11 × 12 km. Processing uses **EPSG:32749** (UTM 49S). The box was fitted around the OpenStreetMap coastline and the Timbulsloko village node, and still needs a check on imagery.

## Coding rules
Before writing code, by hand or with an AI assistant, read [`AGENTS.md`](AGENTS.md). In short: full-word names with units, one step per line, plain loops instead of tricks, no unexplained "magic". Readable beats short. `CLAUDE.md` points Claude Code to the same rules.

## Repository layout
```
AGENTS.md               coding rules (read first)
config/params.yaml      all tunable parameters
data/aoi/               AOI GeoJSON (required by the brief)
data/vectors/           sea seed, village point, OSM reference coastline, transect baseline (TODO)
data/baseline/          labelled points, reference shorelines, training polygons, BASELINE_PROTOCOL.md
data/raw|interim/       git-ignored, lives on Google Drive
metadata/               scenes.csv (brief's scene table), candidates.csv, tides.csv
src/shoreline/          the pipeline as importable functions
notebooks/              01–06 working notebooks + Tubes_PCD_Timbulsloko.ipynb (submission)
outputs/                figures (PNG with attribution), tables (CSV), vectors (GeoJSON)
reports/                laporan and slides (PDF)
```

## How to run
**Colab**
1. Mount Drive: the raw data lives in `MyDrive/pcd_timbulsloko/`. Link: _TODO_.
2. `!git clone <repo-url> && cd multitemporal-shoreline-timbulsloko && pip install -r requirements.txt`
3. `import os; os.environ["DATA_ROOT"] = "/content/drive/MyDrive/pcd_timbulsloko"`
4. Open `notebooks/Tubes_PCD_Timbulsloko.ipynb` → Runtime → Run all.

**Local**
```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Data sources
| Data | Source | Notes |
|---|---|---|
| Landsat 8/9 C2 L2 SR | USGS EarthExplorer / GEE | WRS-2 path/row 120/065 (verify) |
| Sentinel-2 L2A (L1C for 2016) | Copernicus Data Space Ecosystem / GEE | MGRS tile T49MDN (verify) |
| Tide prediction | BIG / pyTMD (EOT20) | stored in `metadata/tides.csv` |
| Reference coastline, village point | OpenStreetMap | © OpenStreetMap contributors, ODbL 1.0 (reference only) |

GEE is used **only** to search for scenes and export AOI clips. All processing is our own Python, as the brief requires.

## Team
| Role | Name | NIM | Owns |
|---|---|---|---|
| M1 Data lead | | | acquisition, `io.py`, `radiometry.py`, `geometry.py` |
| M2 Segmentation lead | | | `enhance.py`, `indices.py`, `segment.py` |
| M3 Representation & change lead | | | `contour.py`, `descriptors.py`, `change.py` |
| M4 Evaluation & report lead | | | `evaluate.py`, baseline, report, slides |

## Attribution
Every figure carries the attribution for the data it shows:
- "Contains modified Copernicus Sentinel data 2026"
- "Landsat imagery courtesy of the U.S. Geological Survey"
