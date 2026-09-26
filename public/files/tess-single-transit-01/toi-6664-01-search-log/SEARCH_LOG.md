# Search log: toi-6664-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 260 (134 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021175071901-s0040-0000000147561732-0211-s_lc.fits` | 20309 | 19608 | 2.50 | 117 | 50 |
| `tess2019198215352-s0014-0000000147561732-0150-s_lc.fits` | 19337 | 18419 | 3.50 | 3 | 3 |
| `tess2019357164649-s0020-0000000147561732-0165-s_lc.fits` | 18954 | 17626 | 3.00 | 24 | 24 |
| `tess2020020091053-s0021-0000000147561732-0167-s_lc.fits` | 19694 | 18281 | 2.50 | 177 | 177 |
| `tess2021204101404-s0041-0000000147561732-0212-s_lc.fits` | 19149 | 18318 | 3.00 | 0 | 0 |
| `tess2021364111932-s0047-0000000147561732-0218-s_lc.fits` | 19544 | 16479 | 3.00 | 6 | 6 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
