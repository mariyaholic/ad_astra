<!-- cygnus:generated-draft -->
# Search log: toi-2721-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.162733, 't0_bjd': 2459222.321706, 'veto_phase': 0.0498, 'depth_ppm': 12870.0, 'duration_h': 3.319, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 16), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:46Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 41332 | 29385 | 3.00 | 132 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
