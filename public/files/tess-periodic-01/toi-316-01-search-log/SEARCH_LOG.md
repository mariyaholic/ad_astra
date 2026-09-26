<!-- [private Drive store] -->
# Search log: toi-316-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 73 (14 distinct events, 9 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 18864 | 14805 | 2.50 | 24 | 24 |
| `tess2021232031932-s0042-0000000008988289-0213-s_lc.fits` | 18342 | 11465 | 3.00 | 0 | 0 |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | 18339 | 14116 | 2.50 | 8 | 8 |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 19207 | 15160 | 4.00 | 41 | 41 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
