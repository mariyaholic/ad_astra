<!-- cygnus:generated-draft -->
# Search log: toi-3246-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.319754, 't0_bjd': 2459351.899577, 'veto_phase': 0.0402, 'depth_ppm': 10910.0, 'duration_h': 2.78, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 11), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:19Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 17790 | 15427 | 3.50 | 14 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
