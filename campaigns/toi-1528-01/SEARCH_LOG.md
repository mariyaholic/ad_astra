<!-- cygnus:generated-draft -->
# Search log: toi-1528-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 110 (18 distinct events, 13 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 19962 | 18681 | 3.00 | 40 | 26 |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 13003 | 12676 | 4.00 | 26 | 26 |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 18357 | 12368 | 4.50 | 58 | 58 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
