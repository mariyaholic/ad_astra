<!-- cygnus:generated-draft -->
# Search log: toi-2644-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 9.7439744, 't0_bjd': 2459300.317115, 'veto_phase': 0.02, 'depth_ppm': 6711.0590566, 'duration_h': 1.9764395, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 58), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:13Z (rowupdate 2021-10-29 12:59:15)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 59 (30 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 18066 | 15495 | 3.00 | 112 | 46 |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 19107 | 16596 | 3.00 | 29 | 13 |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | 20105 | 17662 | 3.50 | 48 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
