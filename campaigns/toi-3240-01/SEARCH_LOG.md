<!-- cygnus:generated-draft -->
# Search log: toi-3240-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.8600722, 't0_bjd': 2459357.914411, 'veto_phase': 0.0312, 'depth_ppm': 16960.0, 'duration_h': 1.93, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 24), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:23Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 72 (32 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 19385 | 18854 | 3.00 | 37 | 0 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 20085 | 17246 | 2.50 | 210 | 54 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 18814 | 15993 | 3.50 | 22 | 0 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 17790 | 15659 | 2.50 | 206 | 18 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
