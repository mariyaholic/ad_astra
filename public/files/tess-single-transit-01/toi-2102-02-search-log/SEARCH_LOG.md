# Search log: toi-2102-02

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 117 (41 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000289590465-0249-s_lc.fits` | 18494 | 12176 | 2.50 | 5 | 5 |
| `tess2019198215352-s0014-0000000289590465-0150-s_lc.fits` | 19337 | 17443 | 2.50 | 18 | 18 |
| `tess2019226182529-s0015-0000000289590465-0151-s_lc.fits` | 18757 | 15591 | 3.00 | 0 | 0 |
| `tess2019279210107-s0017-0000000289590465-0161-s_lc.fits` | 18012 | 11769 | 2.50 | 56 | 56 |
| `tess2019306063752-s0018-0000000289590465-0162-s_lc.fits` | 17554 | 13010 | 3.00 | 33 | 33 |
| `tess2019331140908-s0019-0000000289590465-0164-s_lc.fits` | 18052 | 15596 | 2.50 | 5 | 5 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
