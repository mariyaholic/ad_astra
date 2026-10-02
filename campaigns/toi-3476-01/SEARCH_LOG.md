<!-- cygnus:generated-draft -->
# Search log: toi-3476-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.3205081, 't0_bjd': 2459385.89681, 'veto_phase': 0.0363, 'depth_ppm': 13290.0, 'duration_h': 2.51, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 66), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:32Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 92 (35 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 20085 | 18025 | 2.50 | 106 | 19 |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 17790 | 16117 | 2.50 | 117 | 64 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 18969 | 15838 | 3.00 | 79 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
