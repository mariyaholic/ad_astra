<!-- cygnus:generated-draft -->
# Known-object test, TOI-3849.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3849-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4930, calibrate_screen #4914, event_census #4922, fetch_independent #4927, fetch_products #4902, known_signal_recovery #4917, moving_objects #4924, period_aliases #4923, prior_art #4935, residual_screen #4921, stellar_context #4919, variability_guard #4931
- Runner finished (UTC): 2026-09-30T22:41:15Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3849.01 (BJD 2459938.0351: gap (catalogue 20110 ppm); BJD 2459939.2571: not recovered, depth -2389 ± 1234 ppm (catalogue 20110 ppm); BJD 2459940.4791: not recovered, depth 15737 ± 1043 ppm (catalogue 20110 ppm); BJD 2459941.7012: recovered, depth 16156 ± 988 ppm (catalogue 20110 ppm); BJD 2459942.9232: recovered, depth 15931 ± 987 ppm (catalogue 20110 ppm); BJD 2459944.1453: not recovered, depth 11977 ± 960 ppm (catalogue 20110 ppm); BJD 2459945.3673: recovered, depth 14704 ± 923 ppm (catalogue 20110 ppm); BJD 2459946.5894: recovered, depth 17156 ± 904 ppm (catalogue 20110 ppm); BJD 2459947.8114: recovered, depth 15627 ± 959 ppm (catalogue 20110 ppm); BJD 2459949.0335: recovered, depth 13816 ± 991 ppm (catalogue 20110 ppm); BJD 2459950.2555: gap (catalogue 20110 ppm); BJD 2459951.4775: gap (catalogue 20110 ppm); BJD 2459952.6996: gap (catalogue 20110 ppm); BJD 2459953.9216: gap (catalogue 20110 ppm); BJD 2459955.1437: recovered, depth 21592 ± 1145 ppm (catalogue 20110 ppm); BJD 2459956.3657: gap (catalogue 20110 ppm); BJD 2459957.5878: not recovered, depth 15275 ± 984 ppm (catalogue 20110 ppm); BJD 2459958.8098: recovered, depth 14416 ± 971 ppm (catalogue 20110 ppm); BJD 2459960.0318: not recovered, depth 16958 ± 904 ppm (catalogue 20110 ppm); BJD 2459961.2539: recovered, depth 16026 ± 924 ppm (catalogue 20110 ppm); BJD 2459962.4759: recovered, depth 15781 ± 998 ppm (catalogue 20110 ppm); BJD 2459579.9763: gap (catalogue 20110 ppm); BJD 2459581.1983: recovered, depth 18965 ± 1089 ppm (catalogue 20110 ppm); BJD 2459582.4203: recovered, depth 15169 ± 1006 ppm (catalogue 20110 ppm); BJD 2459583.6424: recovered, depth 16043 ± 1021 ppm (catalogue 20110 ppm); BJD 2459584.8644: recovered, depth 16897 ± 1011 ppm (catalogue 20110 ppm); BJD 2459586.0865: recovered, depth 18000 ± 981 ppm (catalogue 20110 ppm); BJD 2459587.3085: recovered, depth 14281 ± 962 ppm (catalogue 20110 ppm); BJD 2459588.5306: recovered, depth 15456 ± 946 ppm (catalogue 20110 ppm); BJD 2459589.7526: recovered, depth 16740 ± 938 ppm (catalogue 20110 ppm); BJD 2459590.9747: recovered, depth 14598 ± 948 ppm (catalogue 20110 ppm); BJD 2459592.1967: recovered, depth 14139 ± 963 ppm (catalogue 20110 ppm); BJD 2459593.4187: gap (catalogue 20110 ppm); BJD 2459594.6408: gap (catalogue 20110 ppm); BJD 2459595.8628: gap (catalogue 20110 ppm); BJD 2459597.0849: recovered, depth 18523 ± 964 ppm (catalogue 20110 ppm); BJD 2459598.3069: recovered, depth 16107 ± 926 ppm (catalogue 20110 ppm); BJD 2459599.5290: recovered, depth 15138 ± 936 ppm (catalogue 20110 ppm); BJD 2459600.7510: recovered, depth 17785 ± 998 ppm (catalogue 20110 ppm); BJD 2459601.9730: recovered, depth 12020 ± 996 ppm (catalogue 20110 ppm); BJD 2459603.1951: recovered, depth 14500 ± 971 ppm (catalogue 20110 ppm); BJD 2459604.4171: recovered, depth 16567 ± 974 ppm (catalogue 20110 ppm); BJD 2459605.6392: recovered, depth 15239 ± 983 ppm (catalogue 20110 ppm); BJD 2459606.8612: recovered, depth 15382 ± 990 ppm (catalogue 20110 ppm); BJD 2460313.2025: recovered, depth 16614 ± 1269 ppm (catalogue 20110 ppm); BJD 2460314.4245: gap (catalogue 20110 ppm); BJD 2460315.6466: gap (catalogue 20110 ppm); BJD 2460316.8686: not recovered, depth -5402 ± 2203 ppm (catalogue 20110 ppm); BJD 2460318.0907: recovered, depth 15665 ± 1021 ppm (catalogue 20110 ppm); BJD 2460319.3127: gap (catalogue 20110 ppm); BJD 2460320.5347: recovered, depth 14104 ± 893 ppm (catalogue 20110 ppm); BJD 2460321.7568: recovered, depth 15889 ± 854 ppm (catalogue 20110 ppm); BJD 2460322.9788: recovered, depth 17225 ± 836 ppm (catalogue 20110 ppm); BJD 2460324.2009: recovered, depth 16728 ± 840 ppm (catalogue 20110 ppm); BJD 2460325.4229: recovered, depth 14671 ± 840 ppm (catalogue 20110 ppm); BJD 2460326.6450: recovered, depth 14732 ± 896 ppm (catalogue 20110 ppm); BJD 2460327.8670: gap (catalogue 20110 ppm); BJD 2460329.0890: gap (catalogue 20110 ppm); BJD 2460330.3111: gap (catalogue 20110 ppm); BJD 2460331.5331: gap (catalogue 20110 ppm); BJD 2460332.7552: gap (catalogue 20110 ppm); BJD 2460333.9772: recovered, depth 18167 ± 916 ppm (catalogue 20110 ppm); BJD 2460335.1993: recovered, depth 16117 ± 887 ppm (catalogue 20110 ppm); BJD 2460336.4213: recovered, depth 14321 ± 896 ppm (catalogue 20110 ppm); BJD 2460337.6434: partial, depth 15163 ± 899 ppm (catalogue 20110 ppm); BJD 2460338.8654: recovered, depth 15754 ± 921 ppm (catalogue 20110 ppm)).
Outside the catalogued epoch the screen left 11 threshold entries forming **3 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3849.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 147890655 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 142.086945 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 66.950156 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459938.035061 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1.2220437 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20110.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.871 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.2705 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-17 12:03:25 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | lightcurve | 60 | True | `a18018173c7327d5` | True |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | lightcurve | 47 | False | `ed3a9f2df996a6e5` | True |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | lightcurve | 74 | False | `138dbd188258f31f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459938.03506 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459939.25710 | not_recovered | 49 | -2389 ± 1234 | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459940.47915 | not_recovered | 57 | 15737 ± 1043 | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459941.70119 | recovered | 56 | 16156 ± 988 | 20110 | 0.02 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459942.92324 | recovered | 55 | 15931 ± 987 | 20110 | 0.11 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459944.14528 | not_recovered | 56 | 11977 ± 960 | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459945.36732 | recovered | 56 | 14704 ± 923 | 20110 | 0.47 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459946.58937 | recovered | 56 | 17156 ± 904 | 20110 | -0.28 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459947.81141 | recovered | 56 | 15627 ± 959 | 20110 | -0.22 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459949.03345 | recovered | 57 | 13816 ± 991 | 20110 | -0.07 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459950.25550 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459951.47754 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459952.69959 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459953.92163 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459955.14367 | recovered | 56 | 21592 ± 1145 | 20110 | 0.01 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459956.36572 | gap | 0 | — | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459957.58776 | not_recovered | 57 | 15275 ± 984 | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459958.80980 | recovered | 56 | 14416 ± 971 | 20110 | -0.51 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459960.03185 | not_recovered | 56 | 16958 ± 904 | 20110 | — |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459961.25389 | recovered | 56 | 16026 ± 924 | 20110 | 0.54 |
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 2459962.47593 | recovered | 56 | 15781 ± 998 | 20110 | -0.00 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459579.97626 | gap | 0 | — | 20110 | — |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459581.19830 | recovered | 56 | 18965 ± 1089 | 20110 | 0.03 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459582.42034 | recovered | 56 | 15169 ± 1006 | 20110 | -0.12 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459583.64239 | recovered | 56 | 16043 ± 1021 | 20110 | -0.26 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459584.86443 | recovered | 56 | 16897 ± 1011 | 20110 | -0.22 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459586.08648 | recovered | 57 | 18000 ± 981 | 20110 | 0.26 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459587.30852 | recovered | 56 | 14281 ± 962 | 20110 | -0.12 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459588.53056 | recovered | 56 | 15456 ± 946 | 20110 | 0.06 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459589.75261 | recovered | 56 | 16740 ± 938 | 20110 | -0.17 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459590.97465 | recovered | 56 | 14598 ± 948 | 20110 | -0.13 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459592.19669 | recovered | 56 | 14139 ± 963 | 20110 | -0.35 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459593.41874 | gap | 0 | — | 20110 | — |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459594.64078 | gap | 0 | — | 20110 | — |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459595.86282 | gap | 0 | — | 20110 | — |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459597.08487 | recovered | 56 | 18523 ± 964 | 20110 | -0.09 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459598.30691 | recovered | 56 | 16107 ± 926 | 20110 | 0.16 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459599.52896 | recovered | 56 | 15138 ± 936 | 20110 | 0.10 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459600.75100 | recovered | 56 | 17785 ± 998 | 20110 | -0.07 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459601.97304 | recovered | 56 | 12020 ± 996 | 20110 | -0.02 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459603.19509 | recovered | 56 | 14500 ± 971 | 20110 | -0.09 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459604.41713 | recovered | 56 | 16567 ± 974 | 20110 | 0.45 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459605.63917 | recovered | 57 | 15239 ± 983 | 20110 | -0.23 |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459606.86122 | recovered | 56 | 15382 ± 990 | 20110 | -0.09 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460313.20248 | recovered | 56 | 16614 ± 1269 | 20110 | 0.12 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460314.42452 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460315.64656 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460316.86861 | not_recovered | 15 | -5402 ± 2203 | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460318.09065 | recovered | 56 | 15665 ± 1021 | 20110 | 0.27 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460319.31270 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460320.53474 | recovered | 57 | 14104 ± 893 | 20110 | -0.02 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460321.75678 | recovered | 56 | 15889 ± 854 | 20110 | -0.58 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460322.97883 | recovered | 56 | 17225 ± 836 | 20110 | -0.11 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460324.20087 | recovered | 56 | 16728 ± 840 | 20110 | -0.20 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460325.42291 | recovered | 56 | 14671 ± 840 | 20110 | -0.37 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460326.64496 | recovered | 56 | 14732 ± 896 | 20110 | 0.14 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460327.86700 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460329.08904 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460330.31109 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460331.53313 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460332.75518 | gap | 0 | — | 20110 | — |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460333.97722 | recovered | 56 | 18167 ± 916 | 20110 | 0.18 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460335.19926 | recovered | 56 | 16117 ± 887 | 20110 | 0.17 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460336.42131 | recovered | 56 | 14321 ± 896 | 20110 | 0.47 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460337.64335 | partial | 56 | 15163 ± 899 | 20110 | -0.09 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 2460338.86539 | recovered | 56 | 15754 ± 921 | 20110 | 0.11 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147890655-0249-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024003055635-s0074-0000000147890655-0269-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459580.78423 | -0.02199 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459580.55228 | -0.02367 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021364111932-s0047-0000000147890655-0218-s_lc.fits` | 2459596.65106 | -0.02142 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3849.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:40:55Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:41:00Z: TOI-3849.01 (TIC 147890655, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:41:04Z: Gaia DR3 1068331097215848960 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:41:07Z: TOI-3849.01 (Pl?); TOI-3849 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459938.0351: gap (catalogue 20110 ppm); BJD 2459939.2571: not recovered, depth -2389 ± 1234 ppm (catalogue 20110 ppm); BJD 2459940.4791: not recovered, depth 15737 ± 1043 ppm (catalogue 20110 ppm); BJD 2459941.7012: recovered, depth 16156 ± 988 ppm (catalogue 20110 ppm); BJD 2459942.9232: recovered, depth 15931 ± 987 ppm (catalogue 20110 ppm); BJD 2459944.1453: not recovered, depth 11977 ± 960 ppm (catalogue 20110 ppm); BJD 2459945.3673: recovered, depth 14704 ± 923 ppm (catalogue 20110 ppm); BJD 2459946.5894: recovered, depth 17156 ± 904 ppm (catalogue 20110 ppm); BJD 2459947.8114: recovered, depth 15627 ± 959 ppm (catalogue 20110 ppm); BJD 2459949.0335: recovered, depth 13816 ± 991 ppm (catalogue 20110 ppm); BJD 2459950.2555: gap (catalogue 20110 ppm); BJD 2459951.4775: gap (catalogue 20110 ppm); BJD 2459952.6996: gap (catalogue 20110 ppm); BJD 2459953.9216: gap (catalogue 20110 ppm); BJD 2459955.1437: recovered, depth 21592 ± 1145 ppm (catalogue 20110 ppm); BJD 2459956.3657: gap (catalogue 20110 ppm); BJD 2459957.5878: not recovered, depth 15275 ± 984 ppm (catalogue 20110 ppm); BJD 2459958.8098: recovered, depth 14416 ± 971 ppm (catalogue 20110 ppm); BJD 2459960.0318: not recovered, depth 16958 ± 904 ppm (catalogue 20110 ppm); BJD 2459961.2539: recovered, depth 16026 ± 924 ppm (catalogue 20110 ppm); BJD 2459962.4759: recovered, depth 15781 ± 998 ppm (catalogue 20110 ppm); BJD 2459579.9763: gap (catalogue 20110 ppm); BJD 2459581.1983: recovered, depth 18965 ± 1089 ppm (catalogue 20110 ppm); BJD 2459582.4203: recovered, depth 15169 ± 1006 ppm (catalogue 20110 ppm); BJD 2459583.6424: recovered, depth 16043 ± 1021 ppm (catalogue 20110 ppm); BJD 2459584.8644: recovered, depth 16897 ± 1011 ppm (catalogue 20110 ppm); BJD 2459586.0865: recovered, depth 18000 ± 981 ppm (catalogue 20110 ppm); BJD 2459587.3085: recovered, depth 14281 ± 962 ppm (catalogue 20110 ppm); BJD 2459588.5306: recovered, depth 15456 ± 946 ppm (catalogue 20110 ppm); BJD 2459589.7526: recovered, depth 16740 ± 938 ppm (catalogue 20110 ppm); BJD 2459590.9747: recovered, depth 14598 ± 948 ppm (catalogue 20110 ppm); BJD 2459592.1967: recovered, depth 14139 ± 963 ppm (catalogue 20110 ppm); BJD 2459593.4187: gap (catalogue 20110 ppm); BJD 2459594.6408: gap (catalogue 20110 ppm); BJD 2459595.8628: gap (catalogue 20110 ppm); BJD 2459597.0849: recovered, depth 18523 ± 964 ppm (catalogue 20110 ppm); BJD 2459598.3069: recovered, depth 16107 ± 926 ppm (catalogue 20110 ppm); BJD 2459599.5290: recovered, depth 15138 ± 936 ppm (catalogue 20110 ppm); BJD 2459600.7510: recovered, depth 17785 ± 998 ppm (catalogue 20110 ppm); BJD 2459601.9730: recovered, depth 12020 ± 996 ppm (catalogue 20110 ppm); BJD 2459603.1951: recovered, depth 14500 ± 971 ppm (catalogue 20110 ppm); BJD 2459604.4171: recovered, depth 16567 ± 974 ppm (catalogue 20110 ppm); BJD 2459605.6392: recovered, depth 15239 ± 983 ppm (catalogue 20110 ppm); BJD 2459606.8612: recovered, depth 15382 ± 990 ppm (catalogue 20110 ppm); BJD 2460313.2025: recovered, depth 16614 ± 1269 ppm (catalogue 20110 ppm); BJD 2460314.4245: gap (catalogue 20110 ppm); BJD 2460315.6466: gap (catalogue 20110 ppm); BJD 2460316.8686: not recovered, depth -5402 ± 2203 ppm (catalogue 20110 ppm); BJD 2460318.0907: recovered, depth 15665 ± 1021 ppm (catalogue 20110 ppm); BJD 2460319.3127: gap (catalogue 20110 ppm); BJD 2460320.5347: recovered, depth 14104 ± 893 ppm (catalogue 20110 ppm); BJD 2460321.7568: recovered, depth 15889 ± 854 ppm (catalogue 20110 ppm); BJD 2460322.9788: recovered, depth 17225 ± 836 ppm (catalogue 20110 ppm); BJD 2460324.2009: recovered, depth 16728 ± 840 ppm (catalogue 20110 ppm); BJD 2460325.4229: recovered, depth 14671 ± 840 ppm (catalogue 20110 ppm); BJD 2460326.6450: recovered, depth 14732 ± 896 ppm (catalogue 20110 ppm); BJD 2460327.8670: gap (catalogue 20110 ppm); BJD 2460329.0890: gap (catalogue 20110 ppm); BJD 2460330.3111: gap (catalogue 20110 ppm); BJD 2460331.5331: gap (catalogue 20110 ppm); BJD 2460332.7552: gap (catalogue 20110 ppm); BJD 2460333.9772: recovered, depth 18167 ± 916 ppm (catalogue 20110 ppm); BJD 2460335.1993: recovered, depth 16117 ± 887 ppm (catalogue 20110 ppm); BJD 2460336.4213: recovered, depth 14321 ± 896 ppm (catalogue 20110 ppm); BJD 2460337.6434: partial, depth 15163 ± 899 ppm (catalogue 20110 ppm); BJD 2460338.8654: recovered, depth 15754 ± 921 ppm (catalogue 20110 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3849.01: Gaia DR3 1068331097215848960 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3849.01: Teff 5077 K, R* 0.85 ± 0.07, M* 0.90 ± 0.09, ρ* 1.48 ± 0.39 ρ☉ (dwarf sequence, M_G 5.38, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3849.01: 5 Gaia neighbour(s) within 52.5", contamination 12.76%; depth 16156 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 1068334052153348992, 34.9", ΔG 2.87); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2459580.7842 suspect: MOM_CENTR2 z=+5.9, POS_CORR2 z=+5.3, SAP_BKG z=+33.0 |
| Moving objects at screen-event epochs | not_tested | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3849.01: Gaia DR3 1068331097215848960   ROT                            P=None at 0.5" |
| Object-class guard (SIMBAD) | passed | TOI-3849.01: TOI-3849 otype * (star_or_other) at 0.4" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3849-01.yaml
python -m cygnus.multi report campaigns/toi-3849-01.yaml
```
