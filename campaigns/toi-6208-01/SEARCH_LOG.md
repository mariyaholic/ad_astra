<!-- cygnus:generated-draft -->
# Search log: toi-6208-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.2266285, 't0_bjd': 2459872.105147, 'veto_phase': 0.0647, 'depth_ppm': 6662.0, 'duration_h': 5.412, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 45), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:38Z (rowupdate 2024-10-02 12:02:55)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 28 (15 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 19502 | 19024 | 3.50 | 0 | 0 |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 20209 | 11885 | 3.00 | 10 | 10 |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 17967 | 17330 | 2.50 | 56 | 14 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 18545 | 16718 | 2.50 | 62 | 4 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
