<!-- cygnus:generated-draft -->
# Search log: toi-3868-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 18.565813, 't0_bjd': 2459660.902382, 'veto_phase': 0.02, 'depth_ppm': 9420.0, 'duration_h': 3.82, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 49), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:49Z (rowupdate 2025-04-12 12:03:09)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 32 (12 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022057073128-s0049-0000000310994622-0221-s_lc.fits` | 19331 | 10050 | 2.50 | 78 | 0 |
| `tess2022027120115-s0048-0000000310994622-0219-s_lc.fits` | 20202 | 15818 | 3.00 | 0 | 0 |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 19947 | 13740 | 2.50 | 157 | 32 |
| `tess2024058030222-s0076-0000000310994622-0271-s_lc.fits` | 19502 | 14851 | 3.50 | 17 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
