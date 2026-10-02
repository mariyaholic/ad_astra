<!-- cygnus:generated-draft -->
# Search log: toi-2255-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 11.9526103, 't0_bjd': 2459727.117395, 'veto_phase': 0.02, 'depth_ppm': 9860.0, 'duration_h': 2.74, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 34), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:06Z (rowupdate 2024-12-20 12:02:56)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 86 (57 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022138205153-s0052-0000000265146266-0224-s_lc.fits` | 17602 | 14672 | 3.50 | 17 | 0 |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 19074 | 15751 | 2.50 | 47 | 5 |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 18489 | 17234 | 5.00 | 83 | 81 |
| `tess2020160202036-s0026-0000000265146266-0188-s_lc.fits` | 17909 | 16940 | 3.00 | 5 | 0 |
| `tess2022273165103-s0057-0000000265146266-0245-s_lc.fits` | 20712 | 17990 | 3.00 | 27 | 0 |
| `tess2022330142927-s0059-0000000265146266-0248-s_lc.fits` | 19029 | 16039 | 3.00 | 6 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
