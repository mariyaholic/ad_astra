<!-- cygnus:generated-draft -->
# Search log: toi-6249-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1092.002299, 't0_bjd': 2458853.470005, 'veto_phase': 0.02, 'depth_ppm': 1689.5997267, 'duration_h': 5.604929, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 52), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:57Z (rowupdate 2023-06-05 12:03:22)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 103 (25 distinct events, 19 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019357164649-s0020-0000000456260074-0165-s_lc.fits` | 18954 | 17630 | 5.00 | 0 | 0 |
| `tess2022357055054-s0060-0000000456260074-0249-s_lc.fits` | 18494 | 12718 | 5.00 | 0 | 0 |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 19337 | 12138 | 2.50 | 103 | 103 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
