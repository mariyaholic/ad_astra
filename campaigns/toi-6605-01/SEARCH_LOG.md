<!-- cygnus:generated-draft -->
# Search log: toi-6605-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 12.2981251, 't0_bjd': 2460087.153755, 'veto_phase': 0.0202, 'depth_ppm': 14968.0, 'duration_h': 3.98, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 73), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:03Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 18 (6 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | 19922 | 14078 | 3.00 | 0 | 0 |
| `tess2026033082000-s0100-0000000263207857-0302-s_lc.fits` | 19064 | 16089 | 3.00 | 6 | 0 |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 18814 | 16406 | 3.00 | 5 | 5 |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 17790 | 15767 | 2.50 | 17 | 13 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
