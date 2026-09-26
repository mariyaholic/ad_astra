<!-- cygnus:generated-draft -->
# Search log: toi-4422-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 1268 (293 distinct events, 100 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000263748033-0290-s_lc.fits` | 18862 | 16418 | 2.50 | 322 | 288 |
| `tess2023153011303-s0066-0000000263748033-0260-s_lc.fits` | 20707 | 16457 | 2.50 | 404 | 404 |
| `tess2025099153000-s0091-0000000263748033-0288-s_lc.fits` | 19780 | 13380 | 3.00 | 339 | 339 |
| `tess2025127075000-s0092-0000000263748033-0289-s_lc.fits` | 19207 | 16094 | 3.00 | 237 | 237 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
