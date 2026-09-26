<!-- cygnus:generated-draft -->
# Search log: toi-1019-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 247 (45 distinct events, 36 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 18231 | 16931 | 3.00 | 64 | 52 |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 17997 | 13657 | 3.00 | 33 | 33 |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 18066 | 15448 | 3.50 | 61 | 61 |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 18312 | 15711 | 3.50 | 24 | 24 |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 18517 | 15800 | 3.00 | 37 | 37 |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 19107 | 18358 | 3.00 | 40 | 40 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
