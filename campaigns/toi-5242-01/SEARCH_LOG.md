<!-- cygnus:generated-draft -->
# Search log: toi-5242-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.4038486, 't0_bjd': 2459445.351035, 'veto_phase': 0.0486, 'depth_ppm': 16500.0, 'duration_h': 1.87, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 38), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:19Z (rowupdate 2025-09-19 12:04:41)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 88 (37 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 19232 | 15925 | 3.00 | 37 | 28 |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 19047 | 17152 | 3.00 | 52 | 52 |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 19174 | 17256 | 3.00 | 14 | 8 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
