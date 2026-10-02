<!-- cygnus:generated-draft -->
# Search log: toi-2584-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.6965638, 't0_bjd': 2459245.2948, 'veto_phase': 0.0407, 'depth_ppm': 12380.0, 'duration_h': 3.056, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 64), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:27Z (rowupdate 2024-01-23 12:02:45)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 3 (2 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 18312 | 15773 | 3.50 | 6 | 0 |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 18677 | 14793 | 4.00 | 2 | 2 |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 18292 | 14474 | 3.50 | 6 | 0 |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 20000 | 17281 | 3.00 | 28 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
