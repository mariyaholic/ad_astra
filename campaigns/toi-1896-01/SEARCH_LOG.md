# Search log: toi-1896-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 242 (108 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000174302697-0152-s_lc.fits` | 17765 | 13883 | 2.50 | 97 | 60 |
| `tess2019279210107-s0017-0000000174302697-0161-s_lc.fits` | 18012 | 13130 | 2.50 | 144 | 144 |
| `tess2022273165103-s0057-0000000174302697-0245-s_lc.fits` | 20712 | 17991 | 3.50 | 2 | 2 |
| `tess2024274222008-s0084-0000000174302697-0281-s_lc.fits` | 18545 | 16716 | 3.00 | 36 | 36 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
