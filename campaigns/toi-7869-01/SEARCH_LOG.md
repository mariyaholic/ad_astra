<!-- cygnus:generated-draft -->
# Search log: toi-7869-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 43.4488182, 't0_bjd': 2460200.335931, 'veto_phase': 0.02, 'depth_ppm': 5134.3277128, 'duration_h': 6.2736347, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 41), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:27Z (rowupdate 2026-07-25 12:04:08)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 100 (50 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000188620407-0264-s_lc.fits` | 18569 | 14943 | 2.50 | 48 | 2 |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 18864 | 14882 | 3.00 | 9 | 9 |
| `tess2021232031932-s0042-0000000188620407-0213-s_lc.fits` | 18342 | 9350 | 2.50 | 3 | 0 |
| `tess2023263165758-s0070-0000000188620407-0265-s_lc.fits` | 18339 | 13754 | 3.50 | 0 | 0 |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 18487 | 14651 | 3.00 | 89 | 89 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
