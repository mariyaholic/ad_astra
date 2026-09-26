<!-- cygnus:generated-draft -->
# Search log: toi-340-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 433 (164 distinct events, 32 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 18864 | 14358 | 2.50 | 49 | 49 |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 18569 | 14665 | 3.00 | 159 | 159 |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 18487 | 15064 | 4.00 | 32 | 32 |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 19167 | 15509 | 3.50 | 169 | 169 |
| `tess2026164183000-s0105-0000000080439101-0307-s_lc.fits` | 19915 | 15433 | 7.00 | 0 | 0 |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 20484 | 12833 | 3.00 | 24 | 24 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
