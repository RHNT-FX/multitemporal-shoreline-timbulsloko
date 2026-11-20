# Baseline Protocol

The brief requires 100–200 labelled points or polygons from visual interpretation or manual digitisation, with a description of the method and its limitations. Owner: **M4**.

## 1. Files in this folder
| File | Content | Used for |
|---|---|---|
| `points_2026.geojson`, `points_2016.geojson` | 200 labelled points per epoch | Segmentation accuracy (confusion matrix) |
| `ref_shoreline_2026.geojson`, `ref_shoreline_2016.geojson` | Hand-digitised sea–land boundary | Shoreline position error (RMSE) |
| `train_polygons_{year}.geojson` | 10–20 small polygons per class | Feature selection (E1) and the optional classifier. **Never** used for evaluation |

All are in EPSG:4326 and were made in QGIS.

## 2. Point fields
| Field | Values |
|---|---|
| `id` | int |
| `year` | 2016 / 2026 / … |
| `label` | `water` / `land` |
| `subclass` | `open_sea`, `tambak`, `mangrove`, `mudflat`, `built`, `other` |
| `confidence` | 1 = unsure / mixed pixel, 2 = likely, 3 = certain |
| `source` | e.g. `S2 L2A 2026-07-20 false colour`, `Google Earth Pro 2026-06` |
| `source_date` | YYYY-MM-DD |
| `annotator` | M1–M4 |

## 3. Sampling design
- 200 points per epoch, with **160 in the coastal zone** (a ±1.5 km buffer around the shoreline envelope) and **40 elsewhere** in the AOI.
- Stratified by a draft water mask, about 50/50 water and land. Use QGIS *Random points inside polygons* with a minimum distance of 30 m and seed 2026.
- **Blind labelling:** hide the algorithm's mask while labelling.
- Two annotators independently label the same 50 points, and we report Cohen's kappa.

## 4. Reference shorelines
Digitise at about 1:5 000 on the same-date Sentinel-2 image (false colour, stretched). Cover at least the Timbulsloko segment, and check against near-date high-res imagery where available.

## 5. Limitations (copy into the report)
- Visual interpretation is subjective; the inter-annotator kappa quantifies it.
- High-res imagery dates and tide states differ from the satellite scene.
- Mixed pixels at 10 m and 30 m.
- 2016 high-res coverage may be sparse.
- There is no field survey, so the baseline is an interpretation, not ground truth.

## 6. Log
| Date | Annotator | File | Points / features | Notes |
|---|---|---|---|---|
| | | | | |
