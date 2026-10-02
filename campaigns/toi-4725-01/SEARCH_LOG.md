<!-- cygnus:generated-draft -->
# Search log: toi-4725-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.0763072, 't0_bjd': 2459546.99513, 'veto_phase': 0.0368, 'depth_ppm': 16220.0, 'duration_h': 1.223, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 15), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:38Z (rowupdate 2025-02-05 12:03:06)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 95 (58 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 18677 | 14339 | 2.50 | 256 | 35 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 18292 | 14320 | 2.50 | 198 | 60 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
