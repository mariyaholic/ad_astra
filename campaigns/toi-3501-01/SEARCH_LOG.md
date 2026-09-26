<!-- cygnus:generated-draft -->
# Search log: toi-3501-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 125 (44 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 18249 | 14858 | 2.50 | 35 | 23 |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 19107 | 16698 | 2.50 | 48 | 48 |
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | 20105 | 18217 | 3.00 | 12 | 12 |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 18814 | 15181 | 3.00 | 42 | 42 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
