<!-- cygnus:generated-draft -->
# Search log: toi-275-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 0.9195617, 't0_bjd': 2460041.96466, 'veto_phase': 0.0784, 'depth_ppm': 9180.0, 'duration_h': 1.153, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 91), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:11Z (rowupdate 2023-08-10 16:02:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 8 (4 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 19385 | 18854 | 2.50 | 336 | 0 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 20076 | 18276 | 4.50 | 224 | 0 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 19692 | 12905 | 5.00 | 72 | 0 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 18684 | 14739 | 3.00 | 314 | 8 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 18944 | 16998 | 3.50 | 393 | 0 |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 15678 | 14541 | 12.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
