<!-- cygnus:generated-draft -->
# Search log: toi-3673-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 2.2390796, 't0_bjd': 2459909.495737, 'veto_phase': 0.0776, 'depth_ppm': 17069.0, 'duration_h': 2.781, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 4), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:27:01Z (rowupdate 2024-09-10 10:08:02)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 8 (3 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 19962 | 17885 | 2.50 | 120 | 8 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 20712 | 17989 | 3.00 | 40 | 0 |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 18545 | 16716 | 3.00 | 11 | 0 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 18357 | 11074 | 2.50 | 146 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
