<!-- cygnus:generated-draft -->
# Search log: toi-5851-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.5049415, 't0_bjd': 2459790.948702, 'veto_phase': 0.0329, 'depth_ppm': 14400.0, 'duration_h': 2.372, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 85), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:52Z (rowupdate 2026-07-30 12:03:44)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 92 (30 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 19174 | 16758 | 2.50 | 94 | 92 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
