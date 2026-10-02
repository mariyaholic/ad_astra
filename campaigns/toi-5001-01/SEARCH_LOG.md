<!-- cygnus:generated-draft -->
# Search log: toi-5001-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.069043, 't0_bjd': 2459379.729414, 'veto_phase': 0.0516, 'depth_ppm': 8170.0, 'duration_h': 4.185, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 59), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:16Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 124 (67 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 20085 | 18100 | 2.50 | 279 | 69 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 18969 | 15663 | 2.50 | 150 | 55 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
