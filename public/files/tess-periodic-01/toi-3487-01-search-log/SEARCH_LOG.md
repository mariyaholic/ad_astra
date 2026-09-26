<!-- [private Drive store] -->
# Search log: toi-3487-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 404 (149 distinct events, 29 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 20119 | 13822 | 2.50 | 45 | 45 |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 20707 | 14603 | 2.50 | 89 | 89 |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 18862 | 15598 | 3.00 | 48 | 48 |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 19064 | 16540 | 3.00 | 41 | 41 |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 18814 | 16133 | 3.00 | 78 | 78 |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 17790 | 15360 | 2.50 | 103 | 103 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
