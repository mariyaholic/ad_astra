<!-- cygnus:generated-draft -->
# Search log: toi-6562-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.0947485, 't0_bjd': 2460071.647261, 'veto_phase': 0.0792, 'depth_ppm': 5981.4894009, 'duration_h': 5.1910541, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 87), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:58Z (rowupdate 2023-07-21 12:03:15)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 28 (15 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 20085 | 14248 | 2.50 | 142 | 22 |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 17790 | 15719 | 3.00 | 39 | 6 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
