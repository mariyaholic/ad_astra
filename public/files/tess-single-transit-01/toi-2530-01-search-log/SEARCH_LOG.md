# Search log: toi-2530-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 46 (17 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000052059926-0262-s_lc.fits` | 19824 | 15257 | 2.50 | 36 | 36 |
| `tess2023237165326-s0069-0000000052059926-0264-s_lc.fits` | 18569 | 14755 | 2.50 | 7 | 7 |
| `tess2025206162959-s0095-0000000052059926-0292-s_lc.fits` | 18167 | 15251 | 3.00 | 3 | 3 |
| `tess2025232030459-s0096-0000000052059926-0293-s_lc.fits` | 18487 | 14657 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
