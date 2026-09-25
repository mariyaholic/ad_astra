# Search log: toi-1893-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 229 (86 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019331140908-s0019-0000000264544388-0164-s_lc.fits` | 18052 | 16863 | 3.50 | 5 | 5 |
| `tess2019279210107-s0017-0000000264544388-0161-s_lc.fits` | 18012 | 14087 | 3.00 | 18 | 18 |
| `tess2019306063752-s0018-0000000264544388-0162-s_lc.fits` | 17554 | 14851 | 3.50 | 56 | 56 |
| `tess2020106103520-s0024-0000000264544388-0180-s_lc.fits` | 19074 | 18213 | 3.00 | 42 | 42 |
| `tess2020133194932-s0025-0000000264544388-0182-s_lc.fits` | 18489 | 17237 | 2.50 | 108 | 108 |
| `tess2020160202036-s0026-0000000264544388-0188-s_lc.fits` | 17909 | 16939 | 8.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
