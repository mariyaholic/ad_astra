<!-- [private Drive store] -->
# Search log: toi-3098-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 281 (50 distinct events, 34 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 19107 | 16943 | 3.00 | 51 | 51 |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 19385 | 18572 | 3.00 | 67 | 67 |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 20105 | 17705 | 3.00 | 56 | 56 |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 19922 | 14076 | 2.50 | 48 | 48 |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 19064 | 16023 | 2.50 | 59 | 59 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
