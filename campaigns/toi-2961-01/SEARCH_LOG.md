<!-- cygnus:generated-draft -->
# Search log: toi-2961-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.6259138, 't0_bjd': 2459325.992412, 'veto_phase': 0.0393, 'depth_ppm': 10220.0, 'duration_h': 2.91, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 90), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:08Z (rowupdate 2025-02-03 12:03:45)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 24 (9 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 19107 | 18357 | 2.50 | 191 | 21 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 20105 | 19164 | 3.00 | 48 | 0 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 19922 | 13853 | 3.00 | 46 | 3 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
