<!-- cygnus:generated-draft -->
# Search log: toi-3706-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 4.3701795, 't0_bjd': 2460286.769995, 'veto_phase': 0.0541, 'depth_ppm': 15001.3632154, 'duration_h': 3.7808822, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 96), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:33Z (rowupdate 2024-09-10 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 28 (14 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 19337 | 11584 | 2.50 | 28 | 18 |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 19029 | 16386 | 2.50 | 47 | 10 |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 19132 | 9348 | 4.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
