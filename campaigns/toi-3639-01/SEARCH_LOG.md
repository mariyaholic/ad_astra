<!-- cygnus:generated-draft -->
# Search log: toi-3639-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.7208592, 't0_bjd': 2459851.117615, 'veto_phase': 0.0331, 'depth_ppm': 15720.0, 'duration_h': 3.034, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 26), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:32Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 44 (19 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 20079 | 19612 | 2.50 | 57 | 8 |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 20712 | 17991 | 2.50 | 39 | 12 |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 19502 | 19025 | 3.00 | 8 | 0 |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 20209 | 12874 | 2.50 | 20 | 4 |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 17967 | 17329 | 2.50 | 21 | 6 |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 18545 | 16718 | 2.50 | 38 | 14 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
