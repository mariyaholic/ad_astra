<!-- cygnus:generated-draft -->
# Search log: toi-3315-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.2330803, 't0_bjd': 2459386.216984, 'veto_phase': 0.0551, 'depth_ppm': 6900.0, 'duration_h': 4.617, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 33), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:03Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 3 (3 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 20707 | 11841 | 3.50 | 38 | 0 |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 18862 | 15228 | 3.50 | 6 | 0 |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 19064 | 14940 | 3.50 | 32 | 0 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 17790 | 15379 | 2.50 | 242 | 1 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 18969 | 15117 | 2.50 | 270 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
