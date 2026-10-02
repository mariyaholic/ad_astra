<!-- cygnus:generated-draft -->
# Search log: toi-3559-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.5402287, 't0_bjd': 2459770.25382, 'veto_phase': 0.0571, 'depth_ppm': 8272.7904433, 'duration_h': 2.3204775, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 92), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:16Z (rowupdate 2024-09-07 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 27 (14 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 18890 | 17898 | 2.50 | 347 | 3 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 19149 | 18193 | 2.50 | 382 | 8 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 19562 | 18882 | 3.00 | 181 | 0 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 19947 | 17499 | 2.50 | 350 | 16 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 19174 | 18410 | 3.00 | 158 | 0 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 18619 | 18138 | 3.00 | 186 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
