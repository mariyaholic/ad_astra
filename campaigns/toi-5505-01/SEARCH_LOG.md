<!-- cygnus:generated-draft -->
# Search log: toi-5505-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 11.1064221, 't0_bjd': 2459573.870053, 'veto_phase': 0.02, 'depth_ppm': 15290.0, 'duration_h': 2.12, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 75), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:12Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 71 (17 distinct events, 13 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 18292 | 13823 | 2.50 | 79 | 71 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
