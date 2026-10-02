<!-- cygnus:generated-draft -->
# Search log: toi-5207-02

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 2 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 67.8410209, 't0_bjd': 2459679.677932, 'veto_phase': 0.02, 'depth_ppm': 16244.5390069, 'duration_h': 3.0940127, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 14), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:31Z (rowupdate 2026-08-07 12:04:27)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 19 (5 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 18494 | 12717 | 2.50 | 19 | 19 |
| `tess2024003055635-s0074-0000000147892178-0269-s_lc.fits` | 19232 | 12086 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
