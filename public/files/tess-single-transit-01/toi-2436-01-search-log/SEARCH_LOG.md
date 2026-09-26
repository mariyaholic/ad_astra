# Search log: toi-2436-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 100 (41 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019226182529-s0015-0000000154568734-0151-s_lc.fits` | 18757 | 17513 | 3.50 | 3 | 3 |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 19337 | 18419 | 2.50 | 79 | 79 |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 19694 | 18746 | 3.50 | 18 | 18 |
| `tess2021175071901-s0040-0000000154568734-0211-s_lc.fits` | 20309 | 19605 | 3.00 | 0 | 0 |
| `tess2021204101404-s0041-0000000154568734-0212-s_lc.fits` | 19149 | 18320 | 4.50 | 0 | 0 |
| `tess2021364111932-s0047-0000000154568734-0218-s_lc.fits` | 19544 | 17443 | 3.50 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
