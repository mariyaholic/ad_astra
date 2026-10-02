<!-- cygnus:generated-draft -->
# Search log: toi-4238-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1.2732245, 't0_bjd': 2459277.637194, 'veto_phase': 0.0802, 'depth_ppm': 23100.0, 'duration_h': 1.634, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 18), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:53Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 0 (0 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 19922 | 12741 | 2.50 | 251 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
