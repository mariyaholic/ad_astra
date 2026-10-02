<!-- cygnus:generated-draft -->
# Search log: toi-3797-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 17.6229161, 't0_bjd': 2459586.242515, 'veto_phase': 0.02, 'depth_ppm': 8430.0, 'duration_h': 2.976, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 6), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:05Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 73 (38 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 19544 | 16557 | 2.50 | 153 | 30 |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 18494 | 12877 | 2.50 | 6 | 6 |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 19337 | 12564 | 2.50 | 126 | 37 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
