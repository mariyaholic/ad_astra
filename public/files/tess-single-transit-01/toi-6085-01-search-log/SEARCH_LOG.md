# Search log: toi-6085-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 188 (74 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000160223936-0150-s_lc.fits` | 19337 | 18423 | 3.00 | 17 | 14 |
| `tess2019331140908-s0019-0000000160223936-0164-s_lc.fits` | 18052 | 16693 | 3.00 | 6 | 6 |
| `tess2019357164649-s0020-0000000160223936-0165-s_lc.fits` | 18954 | 17626 | 3.00 | 40 | 40 |
| `tess2020133194932-s0025-0000000160223936-0182-s_lc.fits` | 18489 | 17238 | 3.00 | 33 | 33 |
| `tess2020160202036-s0026-0000000160223936-0188-s_lc.fits` | 17909 | 16937 | 2.50 | 82 | 82 |
| `tess2021175071901-s0040-0000000160223936-0211-s_lc.fits` | 20309 | 19611 | 3.00 | 13 | 13 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
