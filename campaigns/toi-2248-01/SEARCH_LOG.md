<!-- cygnus:generated-draft -->
# Search log: toi-2248-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 62.1624516, 't0_bjd': 2460077.706461, 'veto_phase': 0.02, 'depth_ppm': 3710.0, 'duration_h': 4.319, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 47), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:44Z (rowupdate 2024-04-25 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 231 (110 distinct events, 14 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 20085 | 19381 | 2.50 | 154 | 57 |
| `tess2023018032328-s0061-0000000179580045-0250-s_lc.fits` | 18312 | 15351 | 3.50 | 0 | 0 |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 18517 | 15598 | 2.50 | 74 | 74 |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 19107 | 17436 | 2.50 | 92 | 92 |
| `tess2023096110322-s0064-0000000179580045-0257-s_lc.fits` | 19385 | 18854 | 3.00 | 0 | 0 |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | 20707 | 16552 | 3.00 | 8 | 8 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
