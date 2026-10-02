<!-- cygnus:generated-draft -->
# Search log: toi-4218-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.6269521, 't0_bjd': 2458514.633837, 'veto_phase': 0.0833, 'depth_ppm': 12010.0, 'duration_h': 3.503, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 42), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:30Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 2 (1 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 18312 | 15841 | 3.00 | 8 | 0 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 20000 | 19434 | 2.50 | 104 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
