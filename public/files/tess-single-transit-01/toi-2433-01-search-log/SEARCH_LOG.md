# Search log: toi-2433-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 50 (22 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000405763009-0152-s_lc.fits` | 17765 | 13909 | 2.50 | 11 | 11 |
| `tess2019198215352-s0014-0000000405763009-0150-s_lc.fits` | 19337 | 18423 | 3.00 | 6 | 6 |
| `tess2019226182529-s0015-0000000405763009-0151-s_lc.fits` | 18757 | 13201 | 2.50 | 20 | 20 |
| `tess2021204101404-s0041-0000000405763009-0212-s_lc.fits` | 19149 | 18320 | 3.00 | 13 | 13 |
| `tess2022190063128-s0054-0000000405763009-0227-s_lc.fits` | 18890 | 17898 | 3.00 | 0 | 0 |
| `tess2022217014003-s0055-0000000405763009-0242-s_lc.fits` | 19562 | 12293 | 4.50 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
