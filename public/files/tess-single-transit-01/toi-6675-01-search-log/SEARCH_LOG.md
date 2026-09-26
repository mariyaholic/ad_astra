# Search log: toi-6675-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 64 (30 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 20309 | 16424 | 2.50 | 61 | 23 |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 18052 | 16730 | 2.50 | 12 | 12 |
| `tess2019357164649-s0020-0000000141522677-0165-s_lc.fits` | 18954 | 17632 | 3.00 | 3 | 3 |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 17909 | 16938 | 3.50 | 15 | 15 |
| `tess2021364111932-s0047-0000000141522677-0218-s_lc.fits` | 19544 | 17141 | 3.00 | 0 | 0 |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 19029 | 16706 | 2.50 | 11 | 11 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
