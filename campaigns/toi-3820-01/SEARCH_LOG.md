<!-- cygnus:generated-draft -->
# Search log: toi-3820-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 5.4290781, 't0_bjd': 2459503.092356, 'veto_phase': 0.0357, 'depth_ppm': 7391.6084773, 'duration_h': 3.1018506, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 5), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:03Z (rowupdate 2024-11-15 16:02:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 75 (27 distinct events, 5 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 17466 | 15681 | 2.50 | 97 | 2 |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 18089 | 15554 | 3.00 | 20 | 4 |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 19542 | 16725 | 4.00 | 3 | 0 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 19544 | 16599 | 2.50 | 102 | 19 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 18677 | 14520 | 2.50 | 132 | 35 |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 18292 | 14724 | 2.50 | 56 | 15 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
