<!-- cygnus:generated-draft -->
# Search log: toi-4012-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1.82544, 't0_bjd': 2459883.126997, 'veto_phase': 0.0597, 'depth_ppm': 21650.0, 'duration_h': 1.744, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 74), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:07Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 25 (7 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 19962 | 19280 | 2.50 | 204 | 13 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 17602 | 16749 | 2.50 | 67 | 6 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 19029 | 15596 | 3.00 | 128 | 6 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 19132 | 8839 | 3.00 | 66 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
