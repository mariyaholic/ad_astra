# Search log: toi-4585-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 124 (52 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020049080258-s0022-0000000233529335-0174-s_lc.fits` | 19579 | 16918 | 3.00 | 7 | 3 |
| `tess2019198215352-s0014-0000000233529335-0150-s_lc.fits` | 19337 | 15136 | 3.50 | 0 | 0 |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 18757 | 11925 | 2.50 | 11 | 11 |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 17765 | 15145 | 3.00 | 19 | 19 |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 18012 | 14184 | 2.50 | 80 | 80 |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 18052 | 16520 | 3.50 | 11 | 11 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
