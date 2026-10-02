<!-- cygnus:generated-draft -->
# Search log: toi-3245-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.8977031, 't0_bjd': 2459354.766143, 'veto_phase': 0.0895, 'depth_ppm': 10130.0, 'duration_h': 4.148, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 83), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:46Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 9 (2 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 19780 | 10486 | 2.50 | 130 | 9 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
