<!-- cygnus:generated-draft -->
# Search log: toi-2876-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 6.2996307, 't0_bjd': 2459248.364238, 'veto_phase': 0.02, 'depth_ppm': 9530.0, 'duration_h': 1.918, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 100), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:53Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 20 (5 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 19370 | 15032 | 2.50 | 99 | 20 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
