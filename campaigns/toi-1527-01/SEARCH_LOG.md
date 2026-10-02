<!-- cygnus:generated-draft -->
# Search log: toi-1527-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.0625809, 't0_bjd': 2460600.889284, 'veto_phase': 0.0456, 'depth_ppm': 2884.0, 'duration_h': 3.69, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 3), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:26:56Z (rowupdate 2025-05-02 16:23:22)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 30 (16 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 18545 | 16464 | 4.00 | 39 | 0 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 20712 | 17989 | 2.50 | 518 | 30 |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 18357 | 11161 | 3.00 | 181 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
