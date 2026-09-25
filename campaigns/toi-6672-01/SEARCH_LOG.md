# Search log: toi-6672-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 66 (31 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000331644554-0152-s_lc.fits` | 17765 | 14389 | 2.50 | 164 | 29 |
| `tess2022244194134-s0056-0000000331644554-0243-s_lc.fits` | 20079 | 18678 | 2.50 | 19 | 19 |
| `tess2024058030222-s0076-0000000331644554-0271-s_lc.fits` | 19502 | 16132 | 3.00 | 11 | 11 |
| `tess2024249191853-s0083-0000000331644554-0280-s_lc.fits` | 17967 | 17330 | 2.50 | 7 | 7 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
