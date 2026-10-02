<!-- cygnus:generated-draft -->
# Search log: toi-6326-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.3556749, 't0_bjd': 2459907.561815, 'veto_phase': 0.0889, 'depth_ppm': 9377.0, 'duration_h': 3.351, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 13), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:26Z (rowupdate 2025-09-19 12:04:41)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 18357 | 10251 | 3.00 | 137 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
