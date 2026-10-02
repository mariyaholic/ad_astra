<!-- cygnus:generated-draft -->
# Search log: toi-2562-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.0483695, 't0_bjd': 2459770.738717, 'veto_phase': 0.0447, 'depth_ppm': 12060.0, 'duration_h': 2.896, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 50), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:52Z (rowupdate 2025-09-09 12:04:04)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 16 (5 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 18890 | 17898 | 2.50 | 98 | 2 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 20309 | 15453 | 2.50 | 157 | 0 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 19149 | 18320 | 2.50 | 165 | 4 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 19544 | 16396 | 2.50 | 293 | 3 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 18896 | 12862 | 2.50 | 108 | 6 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 17707 | 13652 | 3.00 | 37 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
