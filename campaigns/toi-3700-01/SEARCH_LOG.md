<!-- cygnus:generated-draft -->
# Search log: toi-3700-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.4184429, 't0_bjd': 2460286.353547, 'veto_phase': 0.0459, 'depth_ppm': 12333.3914621, 'duration_h': 3.2423132, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 84), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:49Z (rowupdate 2024-09-10 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 42 (23 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 19337 | 12053 | 3.50 | 9 | 2 |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 19029 | 16050 | 3.00 | 23 | 0 |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 19132 | 8639 | 2.50 | 88 | 40 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
