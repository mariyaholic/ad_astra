<!-- cygnus:generated-draft -->
# Known-object test, TOI-3673.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3673-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4070, calibrate_screen #4046, event_census #4055, fetch_independent #4058, fetch_products #4036, known_signal_recovery #4048, moving_objects #4057, period_aliases #4056, prior_art #4075, residual_screen #4054, stellar_context #4050, variability_guard #4072
- Runner finished (UTC): 2026-09-30T21:36:08Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3673.01 (BJD 2459882.6268: gap (catalogue 17069 ppm); BJD 2459884.8659: recovered, depth 15417 ± 1203 ppm (catalogue 17069 ppm); BJD 2459887.1049: not recovered, depth 15210 ± 1247 ppm (catalogue 17069 ppm); BJD 2459889.3440: recovered, depth 16654 ± 1205 ppm (catalogue 17069 ppm); BJD 2459891.5831: recovered, depth 16243 ± 1155 ppm (catalogue 17069 ppm); BJD 2459893.8222: partial, depth 14658 ± 1187 ppm (catalogue 17069 ppm); BJD 2459896.0613: recovered, depth 16321 ± 1922 ppm (catalogue 17069 ppm); BJD 2459898.3003: recovered, depth 19089 ± 1284 ppm (catalogue 17069 ppm); BJD 2459900.5394: partial, depth 18420 ± 1128 ppm (catalogue 17069 ppm); BJD 2459902.7785: recovered, depth 20579 ± 1163 ppm (catalogue 17069 ppm); BJD 2459905.0176: recovered, depth 16140 ± 1200 ppm (catalogue 17069 ppm); BJD 2459907.2567: recovered, depth 17112 ± 1240 ppm (catalogue 17069 ppm); BJD 2459909.4957: recovered, depth 17347 ± 1268 ppm (catalogue 17069 ppm); BJD 2459853.5187: not recovered, depth 2507 ± 1079 ppm (catalogue 17069 ppm); BJD 2459855.7578: recovered, depth 15062 ± 930 ppm (catalogue 17069 ppm); BJD 2459857.9969: not recovered, depth 13631 ± 1002 ppm (catalogue 17069 ppm); BJD 2459860.2360: partial, depth 13476 ± 960 ppm (catalogue 17069 ppm); BJD 2459862.4751: recovered, depth 11417 ± 964 ppm (catalogue 17069 ppm); BJD 2459864.7141: gap (catalogue 17069 ppm); BJD 2459866.9532: partial, depth 17321 ± 967 ppm (catalogue 17069 ppm); BJD 2459869.1923: recovered, depth 17712 ± 1022 ppm (catalogue 17069 ppm); BJD 2459871.4314: recovered, depth 15242 ± 1019 ppm (catalogue 17069 ppm); BJD 2459873.6705: not recovered, depth 15185 ± 959 ppm (catalogue 17069 ppm); BJD 2459875.9095: not recovered, depth 14964 ± 1006 ppm (catalogue 17069 ppm); BJD 2459878.1486: not recovered, depth 14479 ± 917 ppm (catalogue 17069 ppm); BJD 2459880.3877: recovered, depth 14739 ± 967 ppm (catalogue 17069 ppm); BJD 2460585.6978: not recovered, depth 11289 ± 1185 ppm (catalogue 17069 ppm); BJD 2460587.9369: not recovered, depth 17530 ± 1039 ppm (catalogue 17069 ppm); BJD 2460590.1759: not recovered, depth 15934 ± 1049 ppm (catalogue 17069 ppm); BJD 2460592.4150: recovered, depth 15542 ± 1057 ppm (catalogue 17069 ppm); BJD 2460594.6541: not recovered, depth 14310 ± 1060 ppm (catalogue 17069 ppm); BJD 2460596.8932: gap (catalogue 17069 ppm); BJD 2460599.1323: recovered, depth 13762 ± 1193 ppm (catalogue 17069 ppm); BJD 2460601.3713: not recovered, depth 13489 ± 1109 ppm (catalogue 17069 ppm); BJD 2460603.6104: not recovered, depth 17298 ± 1083 ppm (catalogue 17069 ppm); BJD 2460605.8495: not recovered, depth 18533 ± 1086 ppm (catalogue 17069 ppm); BJD 2460608.0886: not recovered, depth 16452 ± 1059 ppm (catalogue 17069 ppm); BJD 2460610.3277: not recovered, depth 6767 ± 1305 ppm (catalogue 17069 ppm); BJD 2460612.5667: gap (catalogue 17069 ppm); BJD 2460614.8058: recovered, depth 20751 ± 1101 ppm (catalogue 17069 ppm); BJD 2460617.0449: gap (catalogue 17069 ppm); BJD 2460619.2840: recovered, depth 17048 ± 985 ppm (catalogue 17069 ppm); BJD 2460621.5230: recovered, depth 16066 ± 1009 ppm (catalogue 17069 ppm); BJD 2460623.7621: recovered, depth 18774 ± 1101 ppm (catalogue 17069 ppm); BJD 2460626.0012: gap (catalogue 17069 ppm); BJD 2460628.2403: gap (catalogue 17069 ppm); BJD 2460630.4794: recovered, depth 17347 ± 1057 ppm (catalogue 17069 ppm); BJD 2460632.7184: recovered, depth 18911 ± 1014 ppm (catalogue 17069 ppm); BJD 2460634.9575: recovered, depth 17026 ± 1002 ppm (catalogue 17069 ppm)).
Outside the catalogued epoch the screen left 8 threshold entries forming **3 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459897.7940 matches the catalogued transit's depth (8554 vs 15417 ppm), 12.918 d later; 0 of 12 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3673.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 452964680 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 8.722569 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 54.743514 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459909.495737 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.2390796 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17069.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.781 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.2514 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | lightcurve | 58 | True | `344fbb8b791afab2` | True |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | lightcurve | 57 | False | `580ff4601b9e1e67` | True |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | lightcurve | 84 | False | `63eba1ac83e30961` | True |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | lightcurve | 85 | False | `27300324a1cefc19` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459882.62678 | gap | 0 | — | 17069 | — |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459884.86586 | recovered | 83 | 15417 ± 1203 | 17069 | 0.25 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459887.10494 | not_recovered | 83 | 15210 ± 1247 | 17069 | — |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459889.34402 | recovered | 84 | 16654 ± 1205 | 17069 | 0.50 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459891.58310 | recovered | 84 | 16243 ± 1155 | 17069 | 0.63 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459893.82218 | partial | 83 | 14658 ± 1187 | 17069 | -0.64 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459896.06126 | recovered | 40 | 16321 ± 1922 | 17069 | -0.56 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459898.30034 | recovered | 83 | 19089 ± 1284 | 17069 | 0.75 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459900.53942 | partial | 83 | 18420 ± 1128 | 17069 | -0.01 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459902.77850 | recovered | 84 | 20579 ± 1163 | 17069 | 0.24 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459905.01758 | recovered | 84 | 16140 ± 1200 | 17069 | -0.40 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459907.25666 | recovered | 83 | 17112 ± 1240 | 17069 | -0.24 |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459909.49574 | recovered | 83 | 17347 ± 1268 | 17069 | 0.78 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459853.51875 | not_recovered | 84 | 2507 ± 1079 | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459855.75783 | recovered | 84 | 15062 ± 930 | 17069 | 0.13 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459857.99691 | not_recovered | 84 | 13631 ± 1002 | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459860.23599 | partial | 83 | 13476 ± 960 | 17069 | 0.42 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459862.47507 | recovered | 83 | 11417 ± 964 | 17069 | -0.08 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459864.71415 | gap | 0 | — | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459866.95322 | partial | 83 | 17321 ± 967 | 17069 | -0.10 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459869.19230 | recovered | 83 | 17712 ± 1022 | 17069 | 1.01 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459871.43138 | recovered | 84 | 15242 ± 1019 | 17069 | 0.59 |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459873.67046 | not_recovered | 84 | 15185 ± 959 | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459875.90954 | not_recovered | 84 | 14964 ± 1006 | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459878.14862 | not_recovered | 84 | 14479 ± 917 | 17069 | — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 2459880.38770 | recovered | 83 | 14739 ± 967 | 17069 | 0.42 |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460585.69778 | not_recovered | 83 | 11289 ± 1185 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460587.93686 | not_recovered | 83 | 17530 ± 1039 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460590.17594 | not_recovered | 83 | 15934 ± 1049 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460592.41501 | recovered | 83 | 15542 ± 1057 | 17069 | -0.02 |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460594.65409 | not_recovered | 84 | 14310 ± 1060 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460596.89317 | gap | 0 | — | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460599.13225 | recovered | 84 | 13762 ± 1193 | 17069 | 0.10 |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460601.37133 | not_recovered | 84 | 13489 ± 1109 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460603.61041 | not_recovered | 83 | 17298 ± 1083 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460605.84949 | not_recovered | 83 | 18533 ± 1086 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460608.08857 | not_recovered | 83 | 16452 ± 1059 | 17069 | — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 2460610.32765 | not_recovered | 54 | 6767 ± 1305 | 17069 | — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460612.56673 | gap | 0 | — | 17069 | — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460614.80581 | recovered | 84 | 20751 ± 1101 | 17069 | 0.23 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460617.04489 | gap | 0 | — | 17069 | — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460619.28397 | recovered | 83 | 17048 ± 985 | 17069 | 0.52 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460621.52305 | recovered | 83 | 16066 ± 1009 | 17069 | 0.22 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460623.76213 | recovered | 83 | 18774 ± 1101 | 17069 | -0.15 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460626.00121 | gap | 0 | — | 17069 | — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460628.24029 | gap | 0 | — | 17069 | — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460630.47937 | recovered | 84 | 17347 ± 1057 | 17069 | -0.34 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460632.71845 | recovered | 83 | 18911 ± 1014 | 17069 | -0.33 |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2460634.95753 | recovered | 83 | 17026 ± 1002 | 17069 | 0.09 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2022273165103-s0057-0000000452964680-0245-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024274222008-s0084-0000000452964680-0281-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024300212641-s0085-0000000452964680-0282-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459897.79400 | -0.03581 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459897.82038 | -0.03164 | 2 | PDCSAP | 2 | no |
| `tess2022302161335-s0058-0000000452964680-0247-s_lc.fits` | 2459883.57751 | -0.02390 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459897.79400 | 8554 | 15417 | 12.9179 | 0 / 12 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3673.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:36:02Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:36:04Z: TOI-3673.01 (TIC 452964680, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:36:06Z: Gaia DR3 418155340182780672 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:36:07Z: TOI-3673 (*); TOI-3673.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459882.6268: gap (catalogue 17069 ppm); BJD 2459884.8659: recovered, depth 15417 ± 1203 ppm (catalogue 17069 ppm); BJD 2459887.1049: not recovered, depth 15210 ± 1247 ppm (catalogue 17069 ppm); BJD 2459889.3440: recovered, depth 16654 ± 1205 ppm (catalogue 17069 ppm); BJD 2459891.5831: recovered, depth 16243 ± 1155 ppm (catalogue 17069 ppm); BJD 2459893.8222: partial, depth 14658 ± 1187 ppm (catalogue 17069 ppm); BJD 2459896.0613: recovered, depth 16321 ± 1922 ppm (catalogue 17069 ppm); BJD 2459898.3003: recovered, depth 19089 ± 1284 ppm (catalogue 17069 ppm); BJD 2459900.5394: partial, depth 18420 ± 1128 ppm (catalogue 17069 ppm); BJD 2459902.7785: recovered, depth 20579 ± 1163 ppm (catalogue 17069 ppm); BJD 2459905.0176: recovered, depth 16140 ± 1200 ppm (catalogue 17069 ppm); BJD 2459907.2567: recovered, depth 17112 ± 1240 ppm (catalogue 17069 ppm); BJD 2459909.4957: recovered, depth 17347 ± 1268 ppm (catalogue 17069 ppm); BJD 2459853.5187: not recovered, depth 2507 ± 1079 ppm (catalogue 17069 ppm); BJD 2459855.7578: recovered, depth 15062 ± 930 ppm (catalogue 17069 ppm); BJD 2459857.9969: not recovered, depth 13631 ± 1002 ppm (catalogue 17069 ppm); BJD 2459860.2360: partial, depth 13476 ± 960 ppm (catalogue 17069 ppm); BJD 2459862.4751: recovered, depth 11417 ± 964 ppm (catalogue 17069 ppm); BJD 2459864.7141: gap (catalogue 17069 ppm); BJD 2459866.9532: partial, depth 17321 ± 967 ppm (catalogue 17069 ppm); BJD 2459869.1923: recovered, depth 17712 ± 1022 ppm (catalogue 17069 ppm); BJD 2459871.4314: recovered, depth 15242 ± 1019 ppm (catalogue 17069 ppm); BJD 2459873.6705: not recovered, depth 15185 ± 959 ppm (catalogue 17069 ppm); BJD 2459875.9095: not recovered, depth 14964 ± 1006 ppm (catalogue 17069 ppm); BJD 2459878.1486: not recovered, depth 14479 ± 917 ppm (catalogue 17069 ppm); BJD 2459880.3877: recovered, depth 14739 ± 967 ppm (catalogue 17069 ppm); BJD 2460585.6978: not recovered, depth 11289 ± 1185 ppm (catalogue 17069 ppm); BJD 2460587.9369: not recovered, depth 17530 ± 1039 ppm (catalogue 17069 ppm); BJD 2460590.1759: not recovered, depth 15934 ± 1049 ppm (catalogue 17069 ppm); BJD 2460592.4150: recovered, depth 15542 ± 1057 ppm (catalogue 17069 ppm); BJD 2460594.6541: not recovered, depth 14310 ± 1060 ppm (catalogue 17069 ppm); BJD 2460596.8932: gap (catalogue 17069 ppm); BJD 2460599.1323: recovered, depth 13762 ± 1193 ppm (catalogue 17069 ppm); BJD 2460601.3713: not recovered, depth 13489 ± 1109 ppm (catalogue 17069 ppm); BJD 2460603.6104: not recovered, depth 17298 ± 1083 ppm (catalogue 17069 ppm); BJD 2460605.8495: not recovered, depth 18533 ± 1086 ppm (catalogue 17069 ppm); BJD 2460608.0886: not recovered, depth 16452 ± 1059 ppm (catalogue 17069 ppm); BJD 2460610.3277: not recovered, depth 6767 ± 1305 ppm (catalogue 17069 ppm); BJD 2460612.5667: gap (catalogue 17069 ppm); BJD 2460614.8058: recovered, depth 20751 ± 1101 ppm (catalogue 17069 ppm); BJD 2460617.0449: gap (catalogue 17069 ppm); BJD 2460619.2840: recovered, depth 17048 ± 985 ppm (catalogue 17069 ppm); BJD 2460621.5230: recovered, depth 16066 ± 1009 ppm (catalogue 17069 ppm); BJD 2460623.7621: recovered, depth 18774 ± 1101 ppm (catalogue 17069 ppm); BJD 2460626.0012: gap (catalogue 17069 ppm); BJD 2460628.2403: gap (catalogue 17069 ppm); BJD 2460630.4794: recovered, depth 17347 ± 1057 ppm (catalogue 17069 ppm); BJD 2460632.7184: recovered, depth 18911 ± 1014 ppm (catalogue 17069 ppm); BJD 2460634.9575: recovered, depth 17026 ± 1002 ppm (catalogue 17069 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459897.7940, ΔT = 12.918 d, 0 of 12 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3673.01: Gaia DR3 418155340182780672 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3673.01: dwarf priors not applied — 1.22 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3673.01: 26 Gaia neighbour(s) within 52.5", contamination 26.96%; depth 15417 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 418155271463307648, 40.4", ΔG 2.78); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2459897.7940 suspect: POS_CORR1 z=+6.6, POS_CORR2 z=+7.6, SAP_BKG z=+75.7 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3673.01: Gaia DR3 418155340182780672    ROT                            P=None at 0.1" |
| Object-class guard (SIMBAD) | passed | TOI-3673.01: TOI-3673 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-3673.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3673-01.yaml
python -m cygnus.multi report campaigns/toi-3673-01.yaml
```
