<!-- cygnus:generated-draft -->
# Search log: toi-3445-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.9866836, 't0_bjd': 2459382.37766, 'veto_phase': 0.0561, 'depth_ppm': 14000.0, 'duration_h': 2.681, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 46), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:41Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 25 (14 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 20085 | 18135 | 2.50 | 320 | 9 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 18969 | 15647 | 3.00 | 142 | 16 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
