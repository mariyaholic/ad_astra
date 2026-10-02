<!-- cygnus:generated-draft -->
# Search log: toi-4028-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.9589142, 't0_bjd': 2459884.285896, 'veto_phase': 0.0382, 'depth_ppm': 16160.0, 'duration_h': 2.42, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 89), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:04Z (rowupdate 2026-09-09 12:03:38)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 26 (11 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 19962 | 19475 | 2.50 | 90 | 22 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 17602 | 16411 | 2.50 | 79 | 0 |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 13003 | 12676 | 2.50 | 38 | 4 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
