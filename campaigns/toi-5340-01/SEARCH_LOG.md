<!-- cygnus:generated-draft -->
# Search log: toi-5340-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.9393117, 't0_bjd': 2459519.940368, 'veto_phase': 0.0594, 'depth_ppm': 6420.0, 'duration_h': 4.696, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 8), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:11Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 2 (1 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 18677 | 15281 | 3.00 | 40 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
