<!-- cygnus:generated-draft -->
# Known-object test, TOI-2957.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2957-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4938, calibrate_screen #4920, event_census #4932, fetch_independent #4936, fetch_products #4905, known_signal_recovery #4926, moving_objects #4934, period_aliases #4933, prior_art #4940, residual_screen #4929, stellar_context #4928, variability_guard #4939
- Runner finished (UTC): 2026-09-30T22:42:08Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2957.01 (BJD 2460014.5695: recovered, depth 29916 ± 2098 ppm (catalogue 19629 ppm); BJD 2460016.1010: not recovered, depth 7249 ± 1894 ppm (catalogue 19629 ppm); BJD 2460017.6325: not recovered, depth 10433 ± 1850 ppm (catalogue 19629 ppm); BJD 2460019.1640: not recovered, depth 9449 ± 1892 ppm (catalogue 19629 ppm); BJD 2460020.6955: not recovered, depth 13440 ± 1899 ppm (catalogue 19629 ppm); BJD 2460022.2270: not recovered, depth 13289 ± 1930 ppm (catalogue 19629 ppm); BJD 2460023.7585: not recovered, depth 10418 ± 2035 ppm (catalogue 19629 ppm); BJD 2460025.2900: not recovered, depth 13538 ± 1984 ppm (catalogue 19629 ppm); BJD 2460026.8215: partial, depth 6706 ± 2011 ppm (catalogue 19629 ppm); BJD 2460028.3530: not recovered, depth 11363 ± 1937 ppm (catalogue 19629 ppm); BJD 2460029.8845: not recovered, depth 13650 ± 1878 ppm (catalogue 19629 ppm); BJD 2460031.4160: partial, depth 13247 ± 1807 ppm (catalogue 19629 ppm); BJD 2460032.9475: recovered, depth 14541 ± 2006 ppm (catalogue 19629 ppm); BJD 2460034.4790: not recovered, depth 9756 ± 2050 ppm (catalogue 19629 ppm); BJD 2460036.0105: recovered, depth 8385 ± 1948 ppm (catalogue 19629 ppm); BJD 2460037.5420: not recovered, depth 13680 ± 2000 ppm (catalogue 19629 ppm); BJD 2460039.0735: not recovered, depth 12272 ± 2008 ppm (catalogue 19629 ppm); BJD 2460040.6049: partial, depth 26762 ± 2809 ppm (catalogue 19629 ppm); BJD 2460042.1364: not recovered, depth 10530 ± 1985 ppm (catalogue 19629 ppm); BJD 2460043.6679: not recovered, depth 8631 ± 1854 ppm (catalogue 19629 ppm); BJD 2460045.1994: not recovered, depth 7078 ± 1831 ppm (catalogue 19629 ppm); BJD 2460046.7309: not recovered, depth 13144 ± 1881 ppm (catalogue 19629 ppm); BJD 2460048.2624: gap (catalogue 19629 ppm); BJD 2460049.7939: not recovered, depth 9026 ± 1977 ppm (catalogue 19629 ppm); BJD 2460051.3254: not recovered, depth 9358 ± 1915 ppm (catalogue 19629 ppm); BJD 2460052.8569: not recovered, depth 7397 ± 2005 ppm (catalogue 19629 ppm); BJD 2460054.3884: recovered, depth 12056 ± 1904 ppm (catalogue 19629 ppm); BJD 2460055.9199: not recovered, depth 11341 ± 1844 ppm (catalogue 19629 ppm); BJD 2460057.4514: not recovered, depth 14928 ± 1846 ppm (catalogue 19629 ppm); BJD 2460058.9829: not recovered, depth 13819 ± 1841 ppm (catalogue 19629 ppm); BJD 2460060.5144: not recovered, depth 7333 ± 1869 ppm (catalogue 19629 ppm); BJD 2460062.0459: partial, depth 3460 ± 1924 ppm (catalogue 19629 ppm); BJD 2460063.5774: not recovered, depth 11303 ± 1870 ppm (catalogue 19629 ppm); BJD 2460065.1089: partial, depth 15034 ± 2023 ppm (catalogue 19629 ppm); BJD 2460066.6403: not recovered, depth 12196 ± 2089 ppm (catalogue 19629 ppm); BJD 2460748.1552: not recovered, depth -1673 ± 1867 ppm (catalogue 19629 ppm); BJD 2460749.6867: partial, depth -1574 ± 1842 ppm (catalogue 19629 ppm); BJD 2460751.2182: not recovered, depth 2785 ± 1859 ppm (catalogue 19629 ppm); BJD 2460752.7497: not recovered, depth 2998 ± 1813 ppm (catalogue 19629 ppm); BJD 2460754.2812: not recovered, depth 7662 ± 1856 ppm (catalogue 19629 ppm); BJD 2460755.8127: not recovered, depth 2132 ± 1806 ppm (catalogue 19629 ppm); BJD 2460757.3442: not recovered, depth 2377 ± 1805 ppm (catalogue 19629 ppm); BJD 2460758.8757: not recovered, depth 1797 ± 1917 ppm (catalogue 19629 ppm); BJD 2460760.4072: gap (catalogue 19629 ppm); BJD 2460761.9387: not recovered, depth -4936 ± 1755 ppm (catalogue 19629 ppm); BJD 2460763.4702: partial, depth 1499 ± 1876 ppm (catalogue 19629 ppm); BJD 2460765.0017: not recovered, depth 3424 ± 1821 ppm (catalogue 19629 ppm); BJD 2460766.5332: not recovered, depth 247 ± 1801 ppm (catalogue 19629 ppm); BJD 2460768.0646: not recovered, depth 6491 ± 1909 ppm (catalogue 19629 ppm); BJD 2460769.5961: partial, depth 1988 ± 1816 ppm (catalogue 19629 ppm); BJD 2460771.1276: not recovered, depth 2645 ± 1811 ppm (catalogue 19629 ppm); BJD 2460772.6591: not recovered, depth 2706 ± 1843 ppm (catalogue 19629 ppm); BJD 2460774.1906: not recovered, depth -3358 ± 1906 ppm (catalogue 19629 ppm); BJD 2461046.7966: partial, depth 5847 ± 2528 ppm (catalogue 19629 ppm); BJD 2461048.3281: not recovered, depth -2148 ± 2111 ppm (catalogue 19629 ppm); BJD 2461049.8596: not recovered, depth -2792 ± 2176 ppm (catalogue 19629 ppm); BJD 2461051.3911: not recovered, depth 4886 ± 2131 ppm (catalogue 19629 ppm); BJD 2461052.9225: partial, depth 4690 ± 2149 ppm (catalogue 19629 ppm); BJD 2461054.4540: not recovered, depth -3834 ± 2250 ppm (catalogue 19629 ppm); BJD 2461055.9855: gap (catalogue 19629 ppm); BJD 2461057.5170: gap (catalogue 19629 ppm); BJD 2461059.0485: gap (catalogue 19629 ppm); BJD 2461060.5800: gap (catalogue 19629 ppm); BJD 2461062.1115: gap (catalogue 19629 ppm); BJD 2461063.6430: not recovered, depth 5225 ± 2236 ppm (catalogue 19629 ppm); BJD 2461065.1745: not recovered, depth 76 ± 2111 ppm (catalogue 19629 ppm); BJD 2461066.7060: not recovered, depth 3863 ± 2258 ppm (catalogue 19629 ppm); BJD 2461068.2375: partial, depth 2018 ± 2145 ppm (catalogue 19629 ppm); BJD 2461069.7690: not recovered, depth -2200 ± 2195 ppm (catalogue 19629 ppm); BJD 2461071.3005: not recovered, depth 732 ± 2303 ppm (catalogue 19629 ppm); BJD 2461072.8320: gap (catalogue 19629 ppm)).
Outside the catalogued epoch the screen left 156 threshold entries forming **92 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2957.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 463469906 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 153.779587 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -54.937282 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460014.569549 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1.5314941 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 19629.0085308 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.4818244 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.5248 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | lightcurve | 63 | True | `5522dbf5eee7169a` | True |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | lightcurve | 64 | False | `309bbfc454a7f36e` | True |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | lightcurve | 90 | False | `3c7fe6982c0b1b64` | True |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | lightcurve | 99 | False | `d16b0088076943d2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460014.56955 | recovered | 74 | 29916 ± 2098 | 19629 | 0.15 |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460016.10104 | not_recovered | 74 | 7249 ± 1894 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460017.63254 | not_recovered | 75 | 10433 ± 1850 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460019.16403 | not_recovered | 74 | 9449 ± 1892 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460020.69553 | not_recovered | 73 | 13440 ± 1899 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460022.22702 | not_recovered | 75 | 13289 ± 1930 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460023.75851 | not_recovered | 74 | 10418 ± 2035 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460025.29001 | not_recovered | 74 | 13538 ± 1984 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460026.82150 | partial | 75 | 6706 ± 2011 | 19629 | -0.01 |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460028.35300 | not_recovered | 74 | 11363 ± 1937 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460029.88449 | not_recovered | 74 | 13650 ± 1878 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460031.41598 | partial | 75 | 13247 ± 1807 | 19629 | -0.28 |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460032.94748 | recovered | 74 | 14541 ± 2006 | 19629 | -0.14 |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460034.47897 | not_recovered | 74 | 9756 ± 2050 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460036.01047 | recovered | 75 | 8385 ± 1948 | 19629 | -0.02 |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460037.54196 | not_recovered | 74 | 13680 ± 2000 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460039.07345 | not_recovered | 74 | 12272 ± 2008 | 19629 | — |
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2460040.60495 | partial | 33 | 26762 ± 2809 | 19629 | -0.15 |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460042.13644 | not_recovered | 74 | 10530 ± 1985 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460043.66794 | not_recovered | 74 | 8631 ± 1854 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460045.19943 | not_recovered | 75 | 7078 ± 1831 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460046.73093 | not_recovered | 74 | 13144 ± 1881 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460048.26242 | gap | 0 | — | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460049.79391 | not_recovered | 75 | 9026 ± 1977 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460051.32541 | not_recovered | 75 | 9358 ± 1915 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460052.85690 | not_recovered | 74 | 7397 ± 2005 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.38840 | recovered | 75 | 12056 ± 1904 | 19629 | -0.01 |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460055.91989 | not_recovered | 75 | 11341 ± 1844 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460057.45138 | not_recovered | 74 | 14928 ± 1846 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460058.98288 | not_recovered | 74 | 13819 ± 1841 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460060.51437 | not_recovered | 75 | 7333 ± 1869 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460062.04587 | partial | 74 | 3460 ± 1924 | 19629 | -0.24 |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460063.57736 | not_recovered | 74 | 11303 ± 1870 | 19629 | — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460065.10885 | partial | 75 | 15034 ± 2023 | 19629 | 0.68 |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460066.64035 | not_recovered | 75 | 12196 ± 2089 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460748.15522 | not_recovered | 75 | -1673 ± 1867 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460749.68672 | partial | 74 | -1574 ± 1842 | 19629 | 1.00 |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460751.21821 | not_recovered | 75 | 2785 ± 1859 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460752.74971 | not_recovered | 75 | 2998 ± 1813 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460754.28120 | not_recovered | 74 | 7662 ± 1856 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460755.81269 | not_recovered | 75 | 2132 ± 1806 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460757.34419 | not_recovered | 75 | 2377 ± 1805 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460758.87568 | not_recovered | 74 | 1797 ± 1917 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460760.40718 | gap | 0 | — | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460761.93867 | not_recovered | 75 | -4936 ± 1755 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460763.47016 | partial | 74 | 1499 ± 1876 | 19629 | 2.50 |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460765.00166 | not_recovered | 75 | 3424 ± 1821 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460766.53315 | not_recovered | 75 | 247 ± 1801 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460768.06465 | not_recovered | 74 | 6491 ± 1909 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460769.59614 | partial | 74 | 1988 ± 1816 | 19629 | 1.94 |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460771.12763 | not_recovered | 75 | 2645 ± 1811 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460772.65913 | not_recovered | 74 | 2706 ± 1843 | 19629 | — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460774.19062 | not_recovered | 73 | -3358 ± 1906 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461046.79657 | partial | 74 | 5847 ± 2528 | 19629 | 2.06 |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461048.32807 | not_recovered | 74 | -2148 ± 2111 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461049.85956 | not_recovered | 75 | -2792 ± 2176 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461051.39105 | not_recovered | 74 | 4886 ± 2131 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461052.92255 | partial | 75 | 4690 ± 2149 | 19629 | 2.43 |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461054.45404 | not_recovered | 74 | -3834 ± 2250 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461055.98554 | gap | 0 | — | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461057.51703 | gap | 0 | — | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461059.04853 | gap | 0 | — | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461060.58002 | gap | 0 | — | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461062.11151 | gap | 0 | — | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461063.64301 | not_recovered | 74 | 5225 ± 2236 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461065.17450 | not_recovered | 75 | 76 ± 2111 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461066.70600 | not_recovered | 74 | 3863 ± 2258 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461068.23749 | partial | 74 | 2018 ± 2145 | 19629 | -0.19 |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461069.76898 | not_recovered | 75 | -2200 ± 2195 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461071.30048 | not_recovered | 74 | 732 ± 2303 | 19629 | — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461072.83197 | gap | 0 | — | 19629 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000463469906-0255-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.42663 | -0.05695 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461072.16434 | -0.05677 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461046.18250 | -0.05738 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461046.27417 | -0.05600 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460055.50964 | -0.04787 | 2 | PDCSAP | 1 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.65719 | -0.02113 | 4 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.57247 | -0.02057 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.89331 | -0.02014 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.66344 | -0.01997 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.89748 | -0.01993 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.69469 | -0.01973 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.58219 | -0.01953 | 6 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.52871 | -0.01946 | 5 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.72108 | -0.01891 | 10 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.49677 | -0.01888 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.78359 | -0.01879 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.92248 | -0.01869 | 6 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.64469 | -0.01860 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.86243 | -0.01857 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.81521 | -0.01839 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.83984 | -0.01834 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.47107 | -0.01802 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.51413 | -0.01795 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.90165 | -0.01790 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.76692 | -0.01784 | 8 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461068.03221 | -0.01759 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.54052 | -0.01757 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.62872 | -0.01756 | 19 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.86206 | -0.01755 | 5 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.54955 | -0.01752 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.59955 | -0.01736 | 7 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.55858 | -0.01725 | 8 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.15925 | -0.01722 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.59191 | -0.01720 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.60997 | -0.01712 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.97874 | -0.01709 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.67386 | -0.01701 | 4 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.66830 | -0.01695 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.77664 | -0.01695 | 6 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.68567 | -0.01689 | 5 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.17384 | -0.01683 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.44816 | -0.01680 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.73914 | -0.01677 | 6 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.84470 | -0.01671 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.78984 | -0.01670 | 5 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.79817 | -0.01660 | 5 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.44260 | -0.01644 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.11898 | -0.01641 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.90582 | -0.01626 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.70303 | -0.01617 | 8 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.45718 | -0.01610 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.87077 | -0.01609 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.75373 | -0.01600 | 7 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.78049 | -0.01574 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.74609 | -0.01571 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.65164 | -0.01546 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.80688 | -0.01540 | 2 | SAP | 2 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.95165 | -0.01537 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.84438 | -0.01531 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.33426 | -0.01525 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.61244 | -0.01522 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.99610 | -0.01514 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.81276 | -0.01513 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.28982 | -0.01494 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.22870 | -0.01488 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.48010 | -0.01476 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.87109 | -0.01468 | 8 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460067.71076 | -0.01455 | 2 | SAP | 1, 2 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460062.84977 | -0.01450 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.18148 | -0.01443 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.22106 | -0.01430 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.20787 | -0.01415 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.88081 | -0.01413 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.31482 | -0.01412 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461068.02110 | -0.01406 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.29815 | -0.01406 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.96554 | -0.01405 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000463469906-0287-s_lc.fits` | 2460759.85900 | -0.01402 | 2 | SAP | 2 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.49191 | -0.01394 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.46204 | -0.01367 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.88845 | -0.01365 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461067.82526 | -0.01335 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000463469906-0300-s_lc.fits` | 2461053.11342 | -0.01319 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460062.75117 | -0.01303 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.82355 | -0.01275 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460067.48299 | -0.01271 | 2 | SAP | 1, 2 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.72910 | -0.01250 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.60827 | -0.01233 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460062.77200 | -0.01228 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460054.89577 | -0.01227 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460062.83589 | -0.01167 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000463469906-0257-s_lc.fits` | 2460061.38314 | -0.01161 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2957.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:41:53Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:41:58Z: TOI-2957.01 (TIC 463469906, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:42:02Z: Gaia DR3 5355301709572658048 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:42:05Z: TOI-2957.01 (Pl?); TOI-2957 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460014.5695: recovered, depth 29916 ± 2098 ppm (catalogue 19629 ppm); BJD 2460016.1010: not recovered, depth 7249 ± 1894 ppm (catalogue 19629 ppm); BJD 2460017.6325: not recovered, depth 10433 ± 1850 ppm (catalogue 19629 ppm); BJD 2460019.1640: not recovered, depth 9449 ± 1892 ppm (catalogue 19629 ppm); BJD 2460020.6955: not recovered, depth 13440 ± 1899 ppm (catalogue 19629 ppm); BJD 2460022.2270: not recovered, depth 13289 ± 1930 ppm (catalogue 19629 ppm); BJD 2460023.7585: not recovered, depth 10418 ± 2035 ppm (catalogue 19629 ppm); BJD 2460025.2900: not recovered, depth 13538 ± 1984 ppm (catalogue 19629 ppm); BJD 2460026.8215: partial, depth 6706 ± 2011 ppm (catalogue 19629 ppm); BJD 2460028.3530: not recovered, depth 11363 ± 1937 ppm (catalogue 19629 ppm); BJD 2460029.8845: not recovered, depth 13650 ± 1878 ppm (catalogue 19629 ppm); BJD 2460031.4160: partial, depth 13247 ± 1807 ppm (catalogue 19629 ppm); BJD 2460032.9475: recovered, depth 14541 ± 2006 ppm (catalogue 19629 ppm); BJD 2460034.4790: not recovered, depth 9756 ± 2050 ppm (catalogue 19629 ppm); BJD 2460036.0105: recovered, depth 8385 ± 1948 ppm (catalogue 19629 ppm); BJD 2460037.5420: not recovered, depth 13680 ± 2000 ppm (catalogue 19629 ppm); BJD 2460039.0735: not recovered, depth 12272 ± 2008 ppm (catalogue 19629 ppm); BJD 2460040.6049: partial, depth 26762 ± 2809 ppm (catalogue 19629 ppm); BJD 2460042.1364: not recovered, depth 10530 ± 1985 ppm (catalogue 19629 ppm); BJD 2460043.6679: not recovered, depth 8631 ± 1854 ppm (catalogue 19629 ppm); BJD 2460045.1994: not recovered, depth 7078 ± 1831 ppm (catalogue 19629 ppm); BJD 2460046.7309: not recovered, depth 13144 ± 1881 ppm (catalogue 19629 ppm); BJD 2460048.2624: gap (catalogue 19629 ppm); BJD 2460049.7939: not recovered, depth 9026 ± 1977 ppm (catalogue 19629 ppm); BJD 2460051.3254: not recovered, depth 9358 ± 1915 ppm (catalogue 19629 ppm); BJD 2460052.8569: not recovered, depth 7397 ± 2005 ppm (catalogue 19629 ppm); BJD 2460054.3884: recovered, depth 12056 ± 1904 ppm (catalogue 19629 ppm); BJD 2460055.9199: not recovered, depth 11341 ± 1844 ppm (catalogue 19629 ppm); BJD 2460057.4514: not recovered, depth 14928 ± 1846 ppm (catalogue 19629 ppm); BJD 2460058.9829: not recovered, depth 13819 ± 1841 ppm (catalogue 19629 ppm); BJD 2460060.5144: not recovered, depth 7333 ± 1869 ppm (catalogue 19629 ppm); BJD 2460062.0459: partial, depth 3460 ± 1924 ppm (catalogue 19629 ppm); BJD 2460063.5774: not recovered, depth 11303 ± 1870 ppm (catalogue 19629 ppm); BJD 2460065.1089: partial, depth 15034 ± 2023 ppm (catalogue 19629 ppm); BJD 2460066.6403: not recovered, depth 12196 ± 2089 ppm (catalogue 19629 ppm); BJD 2460748.1552: not recovered, depth -1673 ± 1867 ppm (catalogue 19629 ppm); BJD 2460749.6867: partial, depth -1574 ± 1842 ppm (catalogue 19629 ppm); BJD 2460751.2182: not recovered, depth 2785 ± 1859 ppm (catalogue 19629 ppm); BJD 2460752.7497: not recovered, depth 2998 ± 1813 ppm (catalogue 19629 ppm); BJD 2460754.2812: not recovered, depth 7662 ± 1856 ppm (catalogue 19629 ppm); BJD 2460755.8127: not recovered, depth 2132 ± 1806 ppm (catalogue 19629 ppm); BJD 2460757.3442: not recovered, depth 2377 ± 1805 ppm (catalogue 19629 ppm); BJD 2460758.8757: not recovered, depth 1797 ± 1917 ppm (catalogue 19629 ppm); BJD 2460760.4072: gap (catalogue 19629 ppm); BJD 2460761.9387: not recovered, depth -4936 ± 1755 ppm (catalogue 19629 ppm); BJD 2460763.4702: partial, depth 1499 ± 1876 ppm (catalogue 19629 ppm); BJD 2460765.0017: not recovered, depth 3424 ± 1821 ppm (catalogue 19629 ppm); BJD 2460766.5332: not recovered, depth 247 ± 1801 ppm (catalogue 19629 ppm); BJD 2460768.0646: not recovered, depth 6491 ± 1909 ppm (catalogue 19629 ppm); BJD 2460769.5961: partial, depth 1988 ± 1816 ppm (catalogue 19629 ppm); BJD 2460771.1276: not recovered, depth 2645 ± 1811 ppm (catalogue 19629 ppm); BJD 2460772.6591: not recovered, depth 2706 ± 1843 ppm (catalogue 19629 ppm); BJD 2460774.1906: not recovered, depth -3358 ± 1906 ppm (catalogue 19629 ppm); BJD 2461046.7966: partial, depth 5847 ± 2528 ppm (catalogue 19629 ppm); BJD 2461048.3281: not recovered, depth -2148 ± 2111 ppm (catalogue 19629 ppm); BJD 2461049.8596: not recovered, depth -2792 ± 2176 ppm (catalogue 19629 ppm); BJD 2461051.3911: not recovered, depth 4886 ± 2131 ppm (catalogue 19629 ppm); BJD 2461052.9225: partial, depth 4690 ± 2149 ppm (catalogue 19629 ppm); BJD 2461054.4540: not recovered, depth -3834 ± 2250 ppm (catalogue 19629 ppm); BJD 2461055.9855: gap (catalogue 19629 ppm); BJD 2461057.5170: gap (catalogue 19629 ppm); BJD 2461059.0485: gap (catalogue 19629 ppm); BJD 2461060.5800: gap (catalogue 19629 ppm); BJD 2461062.1115: gap (catalogue 19629 ppm); BJD 2461063.6430: not recovered, depth 5225 ± 2236 ppm (catalogue 19629 ppm); BJD 2461065.1745: not recovered, depth 76 ± 2111 ppm (catalogue 19629 ppm); BJD 2461066.7060: not recovered, depth 3863 ± 2258 ppm (catalogue 19629 ppm); BJD 2461068.2375: partial, depth 2018 ± 2145 ppm (catalogue 19629 ppm); BJD 2461069.7690: not recovered, depth -2200 ± 2195 ppm (catalogue 19629 ppm); BJD 2461071.3005: not recovered, depth 732 ± 2303 ppm (catalogue 19629 ppm); BJD 2461072.8320: gap (catalogue 19629 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2957.01: Gaia DR3 5355301713891172224 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2957.01: dwarf priors not applied — RUWE 2.5568936 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2957.01: 81 Gaia neighbour(s) within 52.5", contamination 86.99%; depth 29916 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 5355301713891171072, 24.2", ΔG -1.14); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2461067.4266 suspect: momentum dump (in event), manual exclude (within ±0.25 d); BJD 2461072.1643 suspect: SAP_BKG z=+10.2 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2957.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2957.01: TOI-2957.01 otype Pl? (star_or_other) at 0.0" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2957-01.yaml
python -m cygnus.multi report campaigns/toi-2957-01.yaml
```
