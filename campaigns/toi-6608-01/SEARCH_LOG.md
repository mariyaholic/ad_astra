<!-- cygnus:generated-draft -->
# Search log: toi-6608-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 7.3144752, 't0_bjd': 2460093.589256, 'veto_phase': 0.02, 'depth_ppm': 19146.0, 'duration_h': 1.481, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 12), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:22Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 9 (4 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 17790 | 15719 | 2.50 | 40 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
