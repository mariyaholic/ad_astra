<!-- cygnus:generated-draft -->
# Search log: toi-4080-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.7519831, 't0_bjd': 2459764.98286, 'veto_phase': 0.0482, 'depth_ppm': 17240.0, 'duration_h': 2.891, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 40), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:24Z (rowupdate 2024-10-01 12:02:54)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 25 (8 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 17992 | 17305 | 2.50 | 98 | 0 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 20309 | 17319 | 3.00 | 12 | 0 |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 17602 | 16747 | 2.50 | 52 | 6 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 19029 | 16114 | 2.50 | 150 | 16 |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 18494 | 12264 | 3.00 | 21 | 3 |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 19337 | 11496 | 3.00 | 10 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
