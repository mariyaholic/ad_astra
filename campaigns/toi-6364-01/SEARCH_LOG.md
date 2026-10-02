<!-- cygnus:generated-draft -->
# Search log: toi-6364-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 25.8866192, 't0_bjd': 2459899.625001, 'veto_phase': 0.02, 'depth_ppm': 13915.0, 'duration_h': 3.737, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 70), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:49Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 46 (26 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 19337 | 10973 | 3.00 | 35 | 35 |
| `tess2024114025118-s0078-0000000407517154-0273-s_lc.fits` | 13003 | 12677 | 3.00 | 6 | 0 |
| `tess2024142205832-s0079-0000000407517154-0274-s_lc.fits` | 19542 | 19071 | 3.00 | 11 | 0 |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 18357 | 14009 | 2.50 | 11 | 11 |
| `tess2024326142117-s0086-0000000407517154-0283-s_lc.fits` | 19132 | 10456 | 3.50 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
