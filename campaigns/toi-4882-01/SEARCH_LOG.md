<!-- cygnus:generated-draft -->
# Search log: toi-4882-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.4360402, 't0_bjd': 2459329.594358, 'veto_phase': 0.0343, 'depth_ppm': 7040.0, 'duration_h': 2.438, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 69), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:43Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 206 (83 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 19107 | 18358 | 3.50 | 35 | 35 |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 19385 | 18834 | 2.50 | 213 | 171 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
