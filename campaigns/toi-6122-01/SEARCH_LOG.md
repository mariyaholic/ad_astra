<!-- cygnus:generated-draft -->
# Search log: toi-6122-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.6107024, 't0_bjd': 2459847.211624, 'veto_phase': 0.0763, 'depth_ppm': 5689.0, 'duration_h': 5.626, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 55), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:05Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 11 (9 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 19232 | 14653 | 2.50 | 87 | 2 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 19947 | 18084 | 2.50 | 199 | 9 |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 19502 | 16477 | 3.50 | 4 | 0 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 19174 | 14187 | 2.50 | 89 | 0 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 18619 | 18138 | 2.50 | 125 | 0 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 17967 | 17330 | 2.50 | 133 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
