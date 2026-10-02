<!-- cygnus:generated-draft -->
# Search log: toi-2192-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 6.2643442, 't0_bjd': 2459039.462278, 'veto_phase': 0.0381, 'depth_ppm': 10552.2490654, 'duration_h': 3.8202596, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 7), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:09Z (rowupdate 2024-12-05 16:02:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 52 (14 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 17546 | 16781 | 2.50 | 166 | 6 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 18182 | 15236 | 2.50 | 127 | 17 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 19987 | 14543 | 3.00 | 72 | 0 |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 19824 | 15092 | 2.50 | 60 | 28 |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 18620 | 15265 | 3.00 | 19 | 1 |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 18167 | 14817 | 3.00 | 49 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
