<!-- cygnus:generated-draft -->
# Search log: toi-5237-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.9889845, 't0_bjd': 2459444.873065, 'veto_phase': 0.0389, 'depth_ppm': 13920.0, 'duration_h': 1.858, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 82), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:42Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 434 (194 distinct events, 16 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 19232 | 18787 | 2.50 | 131 | 131 |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 19947 | 18961 | 2.50 | 262 | 262 |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 19174 | 14302 | 3.00 | 41 | 41 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
