<!-- cygnus:generated-draft -->
# Search log: toi-6523-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 7.809463, 't0_bjd': 2460908.229186, 'veto_phase': 0.0331, 'depth_ppm': 11239.0, 'duration_h': 4.133, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 72), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:58Z (rowupdate 2026-07-23 16:00:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 10 (4 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 18487 | 14849 | 2.50 | 91 | 4 |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 19370 | 13805 | 3.00 | 27 | 0 |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | 20000 | 15439 | 3.00 | 6 | 0 |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 20105 | 17052 | 3.00 | 33 | 3 |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 18862 | 14768 | 3.50 | 11 | 0 |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 18620 | 14616 | 3.00 | 39 | 3 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
