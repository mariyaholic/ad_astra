# Search log: toi-7399-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 287 (119 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019279210107-s0017-0000000233194447-0161-s_lc.fits` | 18012 | 12603 | 2.50 | 88 | 85 |
| `tess2019198215352-s0014-0000000233194447-0150-s_lc.fits` | 19337 | 18420 | 2.50 | 68 | 68 |
| `tess2019226182529-s0015-0000000233194447-0151-s_lc.fits` | 18757 | 16339 | 3.50 | 14 | 14 |
| `tess2019306063752-s0018-0000000233194447-0162-s_lc.fits` | 17554 | 14019 | 3.00 | 3 | 3 |
| `tess2019357164649-s0020-0000000233194447-0165-s_lc.fits` | 18954 | 17619 | 3.00 | 59 | 59 |
| `tess2020020091053-s0021-0000000233194447-0167-s_lc.fits` | 19694 | 18544 | 3.00 | 58 | 58 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
