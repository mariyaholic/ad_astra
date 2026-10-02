<!-- cygnus:generated-draft -->
# Known-object test, TOI-5302.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5302-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4901, calibrate_screen #4885, event_census #4895, fetch_independent #4898, fetch_products #4874, known_signal_recovery #4887, moving_objects #4897, period_aliases #4896, prior_art #4904, residual_screen #4891, stellar_context #4888, variability_guard #4903
- Runner finished (UTC): 2026-09-30T22:36:46Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5302.01 (BJD 2460211.7350: recovered, depth 8789 ± 793 ppm (catalogue 18430 ppm); BJD 2460215.9768: recovered, depth 8840 ± 821 ppm (catalogue 18430 ppm); BJD 2460220.2185: gap (catalogue 18430 ppm); BJD 2460224.4603: recovered, depth 7013 ± 842 ppm (catalogue 18430 ppm); BJD 2460228.7021: recovered, depth 11540 ± 897 ppm (catalogue 18430 ppm); BJD 2460232.9438: recovered, depth 7399 ± 879 ppm (catalogue 18430 ppm); BJD 2460237.1856: not recovered, depth 8651 ± 932 ppm (catalogue 18430 ppm); BJD 2460241.4274: not recovered, depth 11737 ± 908 ppm (catalogue 18430 ppm); BJD 2460245.6691: not recovered, depth 4077 ± 1104 ppm (catalogue 18430 ppm); BJD 2460249.9109: not recovered, depth 10401 ± 969 ppm (catalogue 18430 ppm); BJD 2460254.1527: not recovered, depth 7534 ± 916 ppm (catalogue 18430 ppm); BJD 2460258.3944: not recovered, depth 8553 ± 956 ppm (catalogue 18430 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5302.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 337025682 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 32.249191 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 8.057199 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459490.634183 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.2417694 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 18430.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.832 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.0557 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | lightcurve | 70 | False | `6caf6678887c226d` | True |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | lightcurve | 71 | False | `31891ce5ae115b84` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460211.73498 | recovered | 55 | 8789 ± 793 | 18430 | -0.90 |
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460215.97675 | recovered | 55 | 8840 ± 821 | 18430 | -0.81 |
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460220.21852 | gap | 0 | — | 18430 | — |
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460224.46029 | recovered | 55 | 7013 ± 842 | 18430 | -0.92 |
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460228.70206 | recovered | 55 | 11540 ± 897 | 18430 | -0.84 |
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 2460232.94383 | recovered | 55 | 7399 ± 879 | 18430 | -0.96 |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460237.18560 | not_recovered | 55 | 8651 ± 932 | 18430 | — |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460241.42737 | not_recovered | 55 | 11737 ± 908 | 18430 | — |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460245.66914 | not_recovered | 55 | 4077 ± 1104 | 18430 | — |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460249.91091 | not_recovered | 54 | 10401 ± 969 | 18430 | — |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460254.15268 | not_recovered | 55 | 7534 ± 916 | 18430 | — |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 2460258.39444 | not_recovered | 55 | 8553 ± 956 | 18430 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023263165758-s0070-0000000337025682-0265-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023289093419-s0071-0000000337025682-0266-s_lc.fits` | 12 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-5302.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:36:27Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:36:32Z: TOI-5302.01 (TIC 337025682, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:36:37Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:36:42Z: UCAC4 491-003153 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460211.7350: recovered, depth 8789 ± 793 ppm (catalogue 18430 ppm); BJD 2460215.9768: recovered, depth 8840 ± 821 ppm (catalogue 18430 ppm); BJD 2460220.2185: gap (catalogue 18430 ppm); BJD 2460224.4603: recovered, depth 7013 ± 842 ppm (catalogue 18430 ppm); BJD 2460228.7021: recovered, depth 11540 ± 897 ppm (catalogue 18430 ppm); BJD 2460232.9438: recovered, depth 7399 ± 879 ppm (catalogue 18430 ppm); BJD 2460237.1856: not recovered, depth 8651 ± 932 ppm (catalogue 18430 ppm); BJD 2460241.4274: not recovered, depth 11737 ± 908 ppm (catalogue 18430 ppm); BJD 2460245.6691: not recovered, depth 4077 ± 1104 ppm (catalogue 18430 ppm); BJD 2460249.9109: not recovered, depth 10401 ± 969 ppm (catalogue 18430 ppm); BJD 2460254.1527: not recovered, depth 7534 ± 916 ppm (catalogue 18430 ppm); BJD 2460258.3944: not recovered, depth 8553 ± 956 ppm (catalogue 18430 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 12; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5302.01: Gaia DR3 2521437864823640320 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5302.01: Teff 4782 K, R* 0.76 ± 0.06, M* 0.78 ± 0.08, ρ* 1.81 ± 0.47 ρ☉ (dwarf sequence, M_G 6.19, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-5302.01: 1 Gaia neighbour(s) within 52.5", contamination 0.15%; depth 8789 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5302.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5302.01: UCAC4 491-003153 otype * (star_or_other) at 0.5" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5302-01.yaml
python -m cygnus.multi report campaigns/toi-5302-01.yaml
```
