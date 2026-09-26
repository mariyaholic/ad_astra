# Search log: toi-4321-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 904 (406 distinct events, 20 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019169103026-s0013-0000000325081244-0146-s_lc.fits` | 20479 | 17213 | 2.50 | 199 | 181 |
| `tess2020186164531-s0027-0000000325081244-0189-s_lc.fits` | 17546 | 16777 | 2.50 | 26 | 26 |
| `tess2023181235917-s0067-0000000325081244-0261-s_lc.fits` | 19987 | 13469 | 3.50 | 11 | 11 |
| `tess2025180145000-s0094-0000000325081244-0291-s_lc.fits` | 18620 | 15378 | 2.50 | 142 | 142 |
| `tess2025206162959-s0095-0000000325081244-0292-s_lc.fits` | 18167 | 15372 | 2.50 | 316 | 316 |
| `tess2026060005000-s0101-0000000325081244-0303-s_lc.fits` | 18814 | 15336 | 2.50 | 228 | 228 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
