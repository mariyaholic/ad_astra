<!-- cygnus:generated-draft -->
# Known-object test, TOI-3639.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3639-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4324, calibrate_screen #4299, event_census #4311, fetch_independent #4314, fetch_products #4288, known_signal_recovery #4303, moving_objects #4313, period_aliases #4312, prior_art #4326, residual_screen #4310, stellar_context #4304, variability_guard #4325
- Runner finished (UTC): 2026-09-30T21:48:12Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3639.01 (BJD 2459828.2342: recovered, depth 15090 ± 1049 ppm (catalogue 15720 ppm); BJD 2459833.9550: recovered, depth 14938 ± 1159 ppm (catalogue 15720 ppm); BJD 2459839.6759: not recovered, depth 16656 ± 1002 ppm (catalogue 15720 ppm); BJD 2459845.3968: recovered, depth 11712 ± 1053 ppm (catalogue 15720 ppm); BJD 2459851.1176: recovered, depth 17689 ± 1133 ppm (catalogue 15720 ppm); BJD 2459856.8385: not recovered, depth 12254 ± 1016 ppm (catalogue 15720 ppm); BJD 2459862.5593: recovered, depth 13013 ± 1028 ppm (catalogue 15720 ppm); BJD 2459868.2802: recovered, depth 14641 ± 1070 ppm (catalogue 15720 ppm); BJD 2459874.0011: partial, depth 10781 ± 1064 ppm (catalogue 15720 ppm); BJD 2459879.7219: recovered, depth 14449 ± 1019 ppm (catalogue 15720 ppm); BJD 2460371.7158: not recovered, depth 14425 ± 1171 ppm (catalogue 15720 ppm); BJD 2460377.4367: recovered, depth 11084 ± 1085 ppm (catalogue 15720 ppm); BJD 2460383.1575: not recovered, depth 13909 ± 1021 ppm (catalogue 15720 ppm); BJD 2460388.8784: not recovered, depth 9261 ± 1129 ppm (catalogue 15720 ppm); BJD 2460394.5992: not recovered, depth 5675 ± 1075 ppm (catalogue 15720 ppm); BJD 2460400.3201: recovered, depth 14482 ± 1034 ppm (catalogue 15720 ppm); BJD 2460406.0410: recovered, depth 11262 ± 977 ppm (catalogue 15720 ppm); BJD 2460411.7618: gap (catalogue 15720 ppm); BJD 2460417.4827: not recovered, depth 12699 ± 1058 ppm (catalogue 15720 ppm); BJD 2460423.2035: partial, depth 9219 ± 970 ppm (catalogue 15720 ppm); BJD 2460560.5042: recovered, depth 13445 ± 1142 ppm (catalogue 15720 ppm); BJD 2460566.2250: recovered, depth 17045 ± 1122 ppm (catalogue 15720 ppm); BJD 2460571.9459: not recovered, depth 10023 ± 1438 ppm (catalogue 15720 ppm); BJD 2460577.6667: recovered, depth 13899 ± 1068 ppm (catalogue 15720 ppm); BJD 2460583.3876: partial, depth 12451 ± 1112 ppm (catalogue 15720 ppm); BJD 2460589.1085: recovered, depth 14006 ± 977 ppm (catalogue 15720 ppm); BJD 2460594.8293: recovered, depth 11832 ± 1009 ppm (catalogue 15720 ppm); BJD 2460600.5502: partial, depth 14007 ± 1035 ppm (catalogue 15720 ppm); BJD 2460606.2710: recovered, depth 13725 ± 945 ppm (catalogue 15720 ppm)).
Outside the catalogued epoch the screen left 44 threshold entries forming **19 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459866.5496 matches the catalogued transit's depth (8040 vs 15090 ppm), 38.268 d later; 0 of 38 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3639.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 365447203 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 327.74025 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 58.840391 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459851.117615 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.7208592 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15720.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.034 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.201 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | lightcurve | 56 | True | `a96e41e0c1915806` | True |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | lightcurve | 57 | False | `a16a071329a069c4` | True |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | lightcurve | 76 | False | `3abc22c3fb411885` | True |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | lightcurve | 77 | False | `04238a359c3385f5` | True |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | lightcurve | 83 | False | `8f47c6834e88af30` | True |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | lightcurve | 84 | False | `10a644201f48d97f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459828.23418 | recovered | 91 | 15090 ± 1049 | 15720 | 1.13 |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459833.95504 | recovered | 91 | 14938 ± 1159 | 15720 | 0.33 |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459839.67590 | not_recovered | 91 | 16656 ± 1002 | 15720 | — |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459845.39676 | recovered | 91 | 11712 ± 1053 | 15720 | -0.36 |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459851.11761 | recovered | 91 | 17689 ± 1133 | 15720 | 0.20 |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459856.83847 | not_recovered | 91 | 12254 ± 1016 | 15720 | — |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459862.55933 | recovered | 91 | 13013 ± 1028 | 15720 | 0.03 |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459868.28019 | recovered | 92 | 14641 ± 1070 | 15720 | 0.27 |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459874.00105 | partial | 91 | 10781 ± 1064 | 15720 | 0.73 |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459879.72191 | recovered | 91 | 14449 ± 1019 | 15720 | 0.05 |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 2460371.71580 | not_recovered | 91 | 14425 ± 1171 | 15720 | — |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 2460377.43666 | recovered | 91 | 11084 ± 1085 | 15720 | 0.89 |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 2460383.15752 | not_recovered | 91 | 13909 ± 1021 | 15720 | — |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 2460388.87838 | not_recovered | 91 | 9261 ± 1129 | 15720 | — |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 2460394.59924 | not_recovered | 91 | 5675 ± 1075 | 15720 | — |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460400.32010 | recovered | 91 | 14482 ± 1034 | 15720 | -0.15 |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460406.04096 | recovered | 91 | 11262 ± 977 | 15720 | -0.75 |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460411.76182 | gap | 0 | — | 15720 | — |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460417.48268 | not_recovered | 91 | 12699 ± 1058 | 15720 | — |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460423.20353 | partial | 91 | 9219 ± 970 | 15720 | -0.28 |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460560.50416 | recovered | 91 | 13445 ± 1142 | 15720 | 0.83 |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460566.22501 | recovered | 91 | 17045 ± 1122 | 15720 | -1.43 |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460571.94587 | not_recovered | 60 | 10023 ± 1438 | 15720 | — |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460577.66673 | recovered | 91 | 13899 ± 1068 | 15720 | 0.90 |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460583.38759 | partial | 91 | 12451 ± 1112 | 15720 | 0.37 |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460589.10845 | recovered | 91 | 14006 ± 977 | 15720 | -0.31 |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460594.82931 | recovered | 91 | 11832 ± 1009 | 15720 | -0.66 |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460600.55017 | partial | 91 | 14007 ± 1035 | 15720 | 0.53 |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460606.27103 | recovered | 91 | 13725 ± 945 | 15720 | 0.42 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024058030222-s0076-0000000365447203-0271-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: — |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460565.15012 | -0.03234 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459866.56215 | -0.03224 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459866.54965 | -0.02939 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460604.59183 | -0.02731 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459825.33407 | -0.03325 | 2 | PDCSAP | 3 | no |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460586.00029 | -0.02918 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459825.76603 | -0.02911 | 2 | PDCSAP+SAP | 3 | no |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459825.34935 | -0.02877 | 2 | PDCSAP | 3 | no |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459825.32852 | -0.02844 | 2 | PDCSAP | 3 | no |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460586.01140 | -0.02602 | 2 | PDCSAP | 3 | no |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460420.48840 | -0.02580 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460602.18075 | -0.02532 | 2 | PDCSAP | 1 | no |
| `tess2024274222008-s0084-0000000365447203-0281-s_lc.fits` | 2460609.67092 | -0.01715 | 2 | SAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000365447203-0243-s_lc.fits` | 2459832.57310 | -0.01663 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459866.48020 | -0.01647 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459878.13978 | -0.01520 | 2 | SAP | 1 | no |
| `tess2022273165103-s0057-0000000365447203-0245-s_lc.fits` | 2459866.53437 | -0.01520 | 2 | SAP | 3 | no |
| `tess2024085201119-s0077-0000000365447203-0272-s_lc.fits` | 2460399.59568 | -0.01498 | 2 | SAP | 1 | no |
| `tess2024249191853-s0083-0000000365447203-0280-s_lc.fits` | 2460559.60975 | -0.01347 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459866.54965 | 8040 | 15090 | 38.2683 | 0 / 38 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3639.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:48:05Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:48:08Z: TOI-3639.01 (TIC 365447203, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:48:10Z: Gaia DR3 2202400341106857216 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:48:11Z: TOI-3639 (*); TOI-3639.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459828.2342: recovered, depth 15090 ± 1049 ppm (catalogue 15720 ppm); BJD 2459833.9550: recovered, depth 14938 ± 1159 ppm (catalogue 15720 ppm); BJD 2459839.6759: not recovered, depth 16656 ± 1002 ppm (catalogue 15720 ppm); BJD 2459845.3968: recovered, depth 11712 ± 1053 ppm (catalogue 15720 ppm); BJD 2459851.1176: recovered, depth 17689 ± 1133 ppm (catalogue 15720 ppm); BJD 2459856.8385: not recovered, depth 12254 ± 1016 ppm (catalogue 15720 ppm); BJD 2459862.5593: recovered, depth 13013 ± 1028 ppm (catalogue 15720 ppm); BJD 2459868.2802: recovered, depth 14641 ± 1070 ppm (catalogue 15720 ppm); BJD 2459874.0011: partial, depth 10781 ± 1064 ppm (catalogue 15720 ppm); BJD 2459879.7219: recovered, depth 14449 ± 1019 ppm (catalogue 15720 ppm); BJD 2460371.7158: not recovered, depth 14425 ± 1171 ppm (catalogue 15720 ppm); BJD 2460377.4367: recovered, depth 11084 ± 1085 ppm (catalogue 15720 ppm); BJD 2460383.1575: not recovered, depth 13909 ± 1021 ppm (catalogue 15720 ppm); BJD 2460388.8784: not recovered, depth 9261 ± 1129 ppm (catalogue 15720 ppm); BJD 2460394.5992: not recovered, depth 5675 ± 1075 ppm (catalogue 15720 ppm); BJD 2460400.3201: recovered, depth 14482 ± 1034 ppm (catalogue 15720 ppm); BJD 2460406.0410: recovered, depth 11262 ± 977 ppm (catalogue 15720 ppm); BJD 2460411.7618: gap (catalogue 15720 ppm); BJD 2460417.4827: not recovered, depth 12699 ± 1058 ppm (catalogue 15720 ppm); BJD 2460423.2035: partial, depth 9219 ± 970 ppm (catalogue 15720 ppm); BJD 2460560.5042: recovered, depth 13445 ± 1142 ppm (catalogue 15720 ppm); BJD 2460566.2250: recovered, depth 17045 ± 1122 ppm (catalogue 15720 ppm); BJD 2460571.9459: not recovered, depth 10023 ± 1438 ppm (catalogue 15720 ppm); BJD 2460577.6667: recovered, depth 13899 ± 1068 ppm (catalogue 15720 ppm); BJD 2460583.3876: partial, depth 12451 ± 1112 ppm (catalogue 15720 ppm); BJD 2460589.1085: recovered, depth 14006 ± 977 ppm (catalogue 15720 ppm); BJD 2460594.8293: recovered, depth 11832 ± 1009 ppm (catalogue 15720 ppm); BJD 2460600.5502: partial, depth 14007 ± 1035 ppm (catalogue 15720 ppm); BJD 2460606.2710: recovered, depth 13725 ± 945 ppm (catalogue 15720 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459866.5496, ΔT = 38.268 d, 0 of 38 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3639.01: Gaia DR3 2202400341106857216 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3639.01: Teff 5117 K, R* 0.95 ± 0.08, M* 0.97 ± 0.10, ρ* 1.13 ± 0.29 ρ☉ (dwarf sequence, M_G 4.90, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3639.01: 100 Gaia neighbour(s) within 52.5", contamination 71.43%; depth 15090 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 2202400272387385472, 43.6", ΔG 0.42); a centroid test is needed |
| Pointing and quality census per event | failed | 4 persistent event(s), 1 clean; BJD 2459866.5496 suspect: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR1 z=+9.7, MOM_CENTR2 z=-16.6, POS_CORR1 z=+10.5, POS_CORR2 z=-17.9, SAP_BKG z=+34.4; BJD 2459866.5621 suspect: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR1 z=+9.2, MOM_CENTR2 z=-16.1, POS_CORR1 z=+9.2, POS_CORR2 z=-16.4, SAP_BKG z=+34.1; BJD 2460565.1501 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3639.01: Gaia DR3 2202400341106857216   ROT                            P=None at 0.5" |
| Object-class guard (SIMBAD) | passed | TOI-3639.01: TOI-3639 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3639-01.yaml
python -m cygnus.multi report campaigns/toi-3639-01.yaml
```
