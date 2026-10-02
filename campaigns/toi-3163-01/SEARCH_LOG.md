<!-- cygnus:generated-draft -->
# Search log: toi-3163-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 3.0749168, 't0_bjd': 2459357.894877, 'veto_phase': 0.0543, 'depth_ppm': 8540.0, 'duration_h': 2.67, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 97), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:32:38Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 19 (8 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 19385 | 18854 | 3.00 | 229 | 4 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 19922 | 13906 | 3.00 | 215 | 0 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 19064 | 16844 | 3.00 | 135 | 1 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 18814 | 15847 | 2.50 | 343 | 14 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
