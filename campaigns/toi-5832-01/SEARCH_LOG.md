<!-- cygnus:generated-draft -->
# Search log: toi-5832-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.1357505, 't0_bjd': 2459795.478353, 'veto_phase': 0.0426, 'depth_ppm': 11560.0, 'duration_h': 3.504, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 98), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:44Z (rowupdate 2025-09-03 12:05:55)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 19174 | 15122 | 3.00 | 19 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
