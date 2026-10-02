<!-- cygnus:generated-draft -->
# Search log: toi-1879-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 13.7045951, 't0_bjd': 2459703.289921, 'veto_phase': 0.0267, 'depth_ppm': 10116.0470111, 'duration_h': 5.8535412, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 61), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:20Z (rowupdate 2024-02-15 12:03:00)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 8 (2 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000243335710-0223-s_lc.fits` | 17707 | 11888 | 3.00 | 6 | 0 |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 19074 | 18212 | 2.50 | 34 | 8 |
| `tess2020133194932-s0025-0000000243335710-0182-s_lc.fits` | 18489 | 17244 | 2.50 | 14 | 0 |
| `tess2020160202036-s0026-0000000243335710-0188-s_lc.fits` | 17909 | 16942 | 3.00 | 0 | 0 |
| `tess2021175071901-s0040-0000000243335710-0211-s_lc.fits` | 20309 | 19608 | 3.00 | 0 | 0 |
| `tess2021204101404-s0041-0000000243335710-0212-s_lc.fits` | 19149 | 18321 | 3.00 | 11 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
