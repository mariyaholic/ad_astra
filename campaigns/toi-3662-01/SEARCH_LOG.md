<!-- cygnus:generated-draft -->
# Search log: toi-3662-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 9.9908116, 't0_bjd': 2458813.713584, 'veto_phase': 0.0223, 'depth_ppm': 4620.0, 'duration_h': 3.566, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 20), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:28:00Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 64 (18 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 19132 | 11218 | 3.00 | 64 | 64 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
