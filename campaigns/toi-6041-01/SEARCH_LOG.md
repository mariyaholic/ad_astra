<!-- cygnus:generated-draft -->
# Search log: toi-6041-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1094.062167, 't0_bjd': 2459890.088192, 'veto_phase': 0.02, 'depth_ppm': 2352.0, 'duration_h': 3.534, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 1), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:26:46Z (rowupdate 2025-01-13 12:03:09)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 56 (14 distinct events, 9 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000192415680-0247-s_lc.fits` | 19962 | 19330 | 5.00 | 0 | 0 |
| `tess2019306063752-s0018-0000000192415680-0162-s_lc.fits` | 17554 | 14694 | 5.00 | 0 | 0 |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 18357 | 13167 | 3.00 | 56 | 56 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
