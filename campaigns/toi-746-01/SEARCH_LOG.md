<!-- cygnus:generated-draft -->
# Search log: toi-746-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 10.9803114, 't0_bjd': 2458599.298747, 'veto_phase': 0.02, 'depth_ppm': 8276.212333, 'duration_h': 2.0361453, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 29), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:50Z (rowupdate 2024-09-19 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 65 (27 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 19527 | 11701 | 2.50 | 37 | 16 |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 20119 | 14345 | 2.50 | 51 | 22 |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 20479 | 17223 | 2.50 | 52 | 25 |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 18182 | 12850 | 2.50 | 33 | 2 |
| `tess2020238165205-s0029-0000000167418903-0193-s_lc.fits` | 18864 | 14500 | 3.00 | 12 | 0 |
| `tess2020266004630-s0030-0000000167418903-0195-s_lc.fits` | 19687 | 15960 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
