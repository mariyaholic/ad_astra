<!-- cygnus:generated-draft -->
# Search log: toi-3958-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 12.0031646, 't0_bjd': 2459864.071397, 'veto_phase': 0.0272, 'depth_ppm': 5497.3001958, 'duration_h': 5.2145528, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 80), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:33Z (rowupdate 2026-09-22 12:04:07)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 171 (69 distinct events, 14 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 20712 | 17990 | 2.50 | 54 | 40 |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 19962 | 19475 | 3.00 | 7 | 3 |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 20209 | 12874 | 2.50 | 33 | 33 |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 13003 | 12675 | 2.50 | 23 | 21 |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 18545 | 16717 | 2.50 | 10 | 10 |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 18357 | 17731 | 2.50 | 64 | 64 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
