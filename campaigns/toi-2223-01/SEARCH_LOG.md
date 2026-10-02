<!-- cygnus:generated-draft -->
# Search log: toi-2223-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 6.9309657, 't0_bjd': 2459365.146877, 'veto_phase': 0.0477, 'depth_ppm': 6887.4200394, 'duration_h': 5.2921448, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 68), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:38Z (rowupdate 2024-09-01 12:02:56)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 34 (12 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 20126 | 19337 | 3.00 | 34 | 0 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 17546 | 16154 | 2.50 | 97 | 0 |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | 18182 | 15084 | 3.00 | 10 | 0 |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 20707 | 14609 | 3.00 | 48 | 0 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 19824 | 15239 | 2.50 | 180 | 34 |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 18862 | 15148 | 3.50 | 7 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
