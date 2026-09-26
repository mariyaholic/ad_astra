<!-- [private Drive store] -->
# Search log: toi-671-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 387 (166 distinct events, 24 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 19107 | 18256 | 2.50 | 173 | 173 |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 18187 | 15866 | 2.50 | 54 | 54 |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | 20105 | 19274 | 3.00 | 15 | 15 |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 19922 | 14076 | 2.50 | 109 | 109 |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 19064 | 16531 | 3.00 | 36 | 36 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
