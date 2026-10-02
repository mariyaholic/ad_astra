<!-- cygnus:generated-draft -->
# Search log: toi-1891-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 15.3617729, 't0_bjd': 2460176.504188, 'veto_phase': 0.02, 'depth_ppm': 3321.0, 'duration_h': 1.745, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 93), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:20Z (rowupdate 2023-11-15 16:02:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 181 (82 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000139198430-0262-s_lc.fits` | 19824 | 15029 | 3.50 | 18 | 0 |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 20076 | 18275 | 3.00 | 22 | 10 |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 18182 | 14508 | 3.50 | 34 | 12 |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 18167 | 15375 | 3.00 | 102 | 54 |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 18487 | 15519 | 3.00 | 117 | 96 |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 19915 | 15418 | 3.00 | 28 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
