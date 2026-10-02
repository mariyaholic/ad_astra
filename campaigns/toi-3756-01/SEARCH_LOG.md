<!-- cygnus:generated-draft -->
# Search log: toi-3756-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.4236732, 't0_bjd': 2459912.449974, 'veto_phase': 0.0208, 'depth_ppm': 10682.1531772, 'duration_h': 1.4711492, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 9), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:14Z (rowupdate 2024-09-08 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 279 (139 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 19029 | 16649 | 2.50 | 133 | 22 |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 19337 | 11933 | 2.50 | 186 | 124 |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 19132 | 11802 | 2.50 | 174 | 133 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
