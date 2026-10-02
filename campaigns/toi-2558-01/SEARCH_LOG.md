<!-- cygnus:generated-draft -->
# Search log: toi-2558-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 17.7859152, 't0_bjd': 2459233.127609, 'veto_phase': 0.02, 'depth_ppm': 6535.8664276, 'duration_h': 4.2520718, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 56), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:08Z (rowupdate 2025-07-09 16:00:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 40 (16 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 18231 | 16815 | 2.50 | 76 | 20 |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 17997 | 13629 | 2.50 | 18 | 18 |
| `tess2023018032328-s0061-0000000283307274-0250-s_lc.fits` | 18312 | 15580 | 3.00 | 16 | 1 |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | 20000 | 15294 | 3.50 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
