# Search log: toi-4187-02

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 5 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 185 (82 distinct events, 2 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 39335 | 29437 | 3.50 | 36 | 36 |
| `tess2018292075959-s0004-0000000176780257-0124-s_lc.fits` | 18684 | 14757 | 4.00 | 0 | 0 |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 19687 | 16017 | 3.00 | 7 | 7 |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 18314 | 16634 | 2.50 | 62 | 62 |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 19915 | 14921 | 2.50 | 80 | 80 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
