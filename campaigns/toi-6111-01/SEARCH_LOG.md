<!-- cygnus:generated-draft -->
# Search log: toi-6111-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.8340292, 't0_bjd': 2459848.780642, 'veto_phase': 0.02, 'depth_ppm': 11944.0, 'duration_h': 1.289, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 43), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:33Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 75 (37 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 19502 | 18762 | 2.50 | 106 | 32 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 18619 | 18137 | 3.50 | 53 | 24 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 17967 | 17330 | 3.00 | 53 | 19 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
