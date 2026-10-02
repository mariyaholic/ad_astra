<!-- cygnus:generated-draft -->
# Search log: toi-5884-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.8311038, 't0_bjd': 2459822.29685, 'veto_phase': 0.0352, 'depth_ppm': 4240.0, 'duration_h': 3.283, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 77), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:20Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 27 (16 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 18619 | 18138 | 2.50 | 282 | 27 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
