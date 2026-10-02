<!-- cygnus:generated-draft -->
# Search log: toi-3849-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1.2220437, 't0_bjd': 2459938.035061, 'veto_phase': 0.0957, 'depth_ppm': 20110.0, 'duration_h': 1.871, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 78), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:24Z (rowupdate 2026-07-17 12:03:25)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 11 (3 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 18494 | 12704 | 3.00 | 134 | 0 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 19544 | 16461 | 2.50 | 421 | 11 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 19232 | 12178 | 3.00 | 146 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
