# Search log: toi-2534-01

> Reviewed 2026-09-25; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 216 (71 distinct events, 28 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000219332978-0190-s_lc.fits` | 18182 | 13841 | 3.50 | 0 | 0 |
| `tess2023209231226-s0068-0000000219332978-0262-s_lc.fits` | 19824 | 14881 | 3.00 | 2 | 2 |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 18167 | 15147 | 3.00 | 41 | 41 |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 17790 | 15023 | 2.50 | 6 | 6 |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 18969 | 15025 | 2.50 | 164 | 164 |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | 19167 | 15591 | 3.00 | 3 | 3 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
