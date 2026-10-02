<!-- cygnus:generated-draft -->
# Search log: toi-5571-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 731.4778512, 't0_bjd': 2458854.228883, 'veto_phase': 0.02, 'depth_ppm': 5900.0, 'duration_h': 3.41, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 54), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:03Z (rowupdate 2026-03-26 12:03:43)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 109 (57 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000088565745-0218-s_lc.fits` | 19544 | 15982 | 2.50 | 49 | 0 |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 18494 | 12447 | 2.50 | 14 | 14 |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 19337 | 12159 | 2.50 | 97 | 95 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
