# Search log: toi-2098-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 225 (98 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000356700488-0152-s_lc.fits` | 17765 | 15696 | 2.50 | 59 | 59 |
| `tess2019198215352-s0014-0000000356700488-0150-s_lc.fits` | 19337 | 18416 | 2.50 | 94 | 94 |
| `tess2019279210107-s0017-0000000356700488-0161-s_lc.fits` | 18012 | 12606 | 2.50 | 54 | 54 |
| `tess2019306063752-s0018-0000000356700488-0162-s_lc.fits` | 17554 | 14020 | 3.00 | 11 | 11 |
| `tess2019331140908-s0019-0000000356700488-0164-s_lc.fits` | 18052 | 16288 | 4.00 | 0 | 0 |
| `tess2019357164649-s0020-0000000356700488-0165-s_lc.fits` | 18954 | 17627 | 3.50 | 7 | 7 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
