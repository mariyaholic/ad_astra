# Search log: toi-2277-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 505 (194 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020133194932-s0025-0000000288516853-0182-s_lc.fits` | 18489 | 17239 | 3.00 | 42 | 39 |
| `tess2019198215352-s0014-0000000288516853-0150-s_lc.fits` | 19337 | 18407 | 3.50 | 9 | 9 |
| `tess2019331140908-s0019-0000000288516853-0164-s_lc.fits` | 18052 | 16683 | 3.50 | 7 | 7 |
| `tess2019357164649-s0020-0000000288516853-0165-s_lc.fits` | 18954 | 17624 | 2.50 | 132 | 132 |
| `tess2020020091053-s0021-0000000288516853-0167-s_lc.fits` | 19694 | 18400 | 2.50 | 202 | 202 |
| `tess2020106103520-s0024-0000000288516853-0180-s_lc.fits` | 19074 | 18190 | 2.50 | 116 | 116 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
