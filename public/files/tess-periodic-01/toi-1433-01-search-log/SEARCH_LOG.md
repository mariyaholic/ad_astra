<!-- [private Drive store] -->
# Search log: toi-1433-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 71 (11 distinct events, 11 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000013684720-0150-s_lc.fits` | 19337 | 13792 | 5.00 | 6 | 0 |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | 18757 | 13116 | 6.00 | 15 | 15 |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | 19149 | 18320 | 5.00 | 12 | 12 |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | 19562 | 14749 | 5.50 | 18 | 18 |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | 19947 | 14650 | 8.00 | 14 | 14 |
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | 19174 | 13541 | 4.50 | 12 | 12 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
