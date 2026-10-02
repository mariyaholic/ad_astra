<!-- cygnus:generated-draft -->
# Search log: toi-6732-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 1.3003394, 't0_bjd': 2460121.49861, 'veto_phase': 0.0645, 'depth_ppm': 38320.0, 'duration_h': 1.341, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 32), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:29:01Z (rowupdate 2026-06-25 12:03:43)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 350 (158 distinct events, 13 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 18862 | 15737 | 2.50 | 163 | 135 |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 18969 | 15361 | 2.50 | 95 | 73 |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 19167 | 16072 | 2.50 | 154 | 142 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
