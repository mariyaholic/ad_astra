<!-- cygnus:generated-draft -->
# Search log: toi-3242-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.0001627, 't0_bjd': 2459356.230477, 'veto_phase': 0.0602, 'depth_ppm': 10600.0, 'duration_h': 2.892, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 88), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:00Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 56 (18 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 20085 | 17612 | 3.00 | 180 | 3 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 19922 | 14078 | 3.00 | 58 | 0 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 19064 | 17245 | 3.00 | 139 | 1 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 18814 | 16257 | 2.50 | 266 | 39 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 17790 | 15697 | 2.50 | 344 | 13 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
