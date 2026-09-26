# Search log: toi-6980-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 4 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 211 (90 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021232031932-s0042-0000000422912527-0213-s_lc.fits` | 18342 | 12976 | 3.00 | 0 | 0 |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 18684 | 14849 | 3.00 | 13 | 13 |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | 17804 | 14744 | 3.00 | 4 | 4 |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 18677 | 15355 | 2.50 | 194 | 194 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.
