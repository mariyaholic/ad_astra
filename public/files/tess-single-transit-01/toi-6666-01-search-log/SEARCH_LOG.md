# Search log: toi-6666-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 405 (147 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020106103520-s0024-0000000256429408-0180-s_lc.fits` | 19074 | 18212 | 2.50 | 226 | 130 |
| `tess2019253231442-s0016-0000000256429408-0152-s_lc.fits` | 17765 | 14945 | 3.00 | 8 | 8 |
| `tess2019279210107-s0017-0000000256429408-0161-s_lc.fits` | 18012 | 14085 | 3.00 | 48 | 48 |
| `tess2019306063752-s0018-0000000256429408-0162-s_lc.fits` | 17554 | 15296 | 2.50 | 157 | 157 |
| `tess2020133194932-s0025-0000000256429408-0182-s_lc.fits` | 18489 | 17241 | 3.00 | 53 | 53 |
| `tess2022273165103-s0057-0000000256429408-0245-s_lc.fits` | 20712 | 17982 | 3.00 | 9 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
