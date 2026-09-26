# Search log: toi-2263-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 94 (38 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000159400561-0150-s_lc.fits` | 19337 | 18423 | 3.00 | 0 | 0 |
| `tess2019331140908-s0019-0000000159400561-0164-s_lc.fits` | 18052 | 16692 | 3.00 | 0 | 0 |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 18954 | 17630 | 3.00 | 14 | 14 |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 19694 | 18602 | 2.50 | 62 | 62 |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 18489 | 17245 | 3.00 | 9 | 9 |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 17909 | 16939 | 2.50 | 9 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
