<!-- cygnus:generated-draft -->
# Search log: toi-2957-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1.5314941, 't0_bjd': 2460014.569549, 'veto_phase': 0.1013, 'depth_ppm': 19629.0085308, 'duration_h': 2.4818244, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 79), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:28Z (rowupdate 2024-09-10 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 156 (92 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 19107 | 18357 | 2.50 | 39 | 0 |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 19385 | 18853 | 2.50 | 45 | 37 |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 20105 | 19274 | 3.00 | 8 | 1 |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 19922 | 13656 | 2.50 | 145 | 118 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
