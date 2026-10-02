<!-- cygnus:generated-draft -->
# Search log: toi-3510-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.8724894, 't0_bjd': 2459772.035438, 'veto_phase': 0.0603, 'depth_ppm': 13480.0, 'duration_h': 2.772, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 22), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:15Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 24 (6 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 18890 | 12705 | 2.50 | 61 | 21 |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 19562 | 18881 | 4.00 | 1 | 0 |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 19232 | 18238 | 3.00 | 9 | 3 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 19947 | 18961 | 3.00 | 43 | 0 |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 19174 | 13744 | 3.00 | 9 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
