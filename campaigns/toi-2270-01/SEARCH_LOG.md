# Search log: toi-2270-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 366 (154 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020106103520-s0024-0000000198178505-0180-s_lc.fits` | 19074 | 16224 | 2.50 | 114 | 106 |
| `tess2019198215352-s0014-0000000198178505-0150-s_lc.fits` | 19337 | 18416 | 4.50 | 13 | 13 |
| `tess2019226182529-s0015-0000000198178505-0151-s_lc.fits` | 18757 | 14993 | 3.00 | 98 | 98 |
| `tess2019253231442-s0016-0000000198178505-0152-s_lc.fits` | 17765 | 14977 | 2.50 | 68 | 68 |
| `tess2019279210107-s0017-0000000198178505-0161-s_lc.fits` | 18012 | 12608 | 3.00 | 42 | 42 |
| `tess2019306063752-s0018-0000000198178505-0162-s_lc.fits` | 17554 | 14022 | 2.50 | 39 | 39 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
