<!-- cygnus:generated-draft -->
# Search log: toi-6117-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 9.866312, 't0_bjd': 2459850.257269, 'veto_phase': 0.0335, 'depth_ppm': 5737.0, 'duration_h': 5.285, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 17), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:50Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 36 (10 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 17967 | 17330 | 2.50 | 150 | 36 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
