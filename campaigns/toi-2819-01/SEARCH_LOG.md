<!-- cygnus:generated-draft -->
# Search log: toi-2819-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.3905983, 't0_bjd': 2460236.732778, 'veto_phase': 0.0339, 'depth_ppm': 8720.9304105, 'duration_h': 2.3792658, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 53), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:00Z (rowupdate 2025-04-17 16:00:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 133 (60 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 18677 | 14357 | 2.50 | 197 | 33 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 18292 | 14147 | 2.50 | 145 | 9 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 19370 | 14228 | 2.50 | 228 | 91 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
