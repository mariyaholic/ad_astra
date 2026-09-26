<!-- [private Drive store] -->
# Search log: toi-3460-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 913 (308 distinct events, 24 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000039858507-0210-s_lc.fits` | 20126 | 18472 | 3.00 | 354 | 348 |
| `tess2023153011303-s0066-0000000039858507-0260-s_lc.fits` | 20707 | 15323 | 2.50 | 307 | 307 |
| `tess2025099153000-s0091-0000000039858507-0288-s_lc.fits` | 19780 | 13461 | 3.00 | 113 | 113 |
| `tess2025154050500-s0093-0000000039858507-0290-s_lc.fits` | 18862 | 16103 | 3.00 | 145 | 145 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
