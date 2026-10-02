<!-- cygnus:generated-draft -->
# Search log: toi-6916-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.9155539, 't0_bjd': 2459222.28434, 'veto_phase': 0.0594, 'depth_ppm': 12003.0, 'duration_h': 3.72, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 39), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:21Z (rowupdate 2025-02-02 12:03:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 19370 | 14127 | 3.00 | 27 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
