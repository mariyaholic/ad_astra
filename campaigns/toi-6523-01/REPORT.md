<!-- cygnus:generated-draft -->
# Known-object test, TOI-6523.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6523-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4866, calibrate_screen #4840, event_census #4850, fetch_independent #4854, fetch_products #4833, known_signal_recovery #4844, moving_objects #4852, period_aliases #4851, prior_art #4868, residual_screen #4848, stellar_context #4845, variability_guard #4867
- Runner finished (UTC): 2026-09-30T22:32:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6523.01 (BJD 2460908.2292: gap (catalogue 11239 ppm); BJD 2460916.0386: recovered, depth 10221 ± 471 ppm (catalogue 11239 ppm); BJD 2460923.8481: recovered, depth 9600 ± 489 ppm (catalogue 11239 ppm); BJD 2460931.6576: recovered, depth 10852 ± 486 ppm (catalogue 11239 ppm); BJD 2460666.1358: not recovered, depth 7191 ± 912 ppm (catalogue 11239 ppm); BJD 2460673.9453: recovered, depth 10464 ± 419 ppm (catalogue 11239 ppm); BJD 2460681.7548: recovered, depth 9632 ± 441 ppm (catalogue 11239 ppm); BJD 2460689.5642: not recovered, depth 4427 ± 573 ppm (catalogue 11239 ppm); BJD 2460697.3737: not recovered, depth 8503 ± 455 ppm (catalogue 11239 ppm); BJD 2460705.1831: gap (catalogue 11239 ppm); BJD 2460712.9926: recovered, depth 9693 ± 474 ppm (catalogue 11239 ppm); BJD 2460752.0399: recovered, depth 9801 ± 476 ppm (catalogue 11239 ppm); BJD 2460759.8494: gap (catalogue 11239 ppm); BJD 2460767.6589: recovered, depth 11146 ± 470 ppm (catalogue 11239 ppm); BJD 2460830.1346: gap (catalogue 11239 ppm); BJD 2460837.9440: partial, depth 10064 ± 462 ppm (catalogue 11239 ppm); BJD 2460845.7535: partial, depth 9577 ± 431 ppm (catalogue 11239 ppm); BJD 2460853.5629: recovered, depth 11213 ± 443 ppm (catalogue 11239 ppm); BJD 2460861.3724: partial, depth 9058 ± 427 ppm (catalogue 11239 ppm); BJD 2460869.1819: gap (catalogue 11239 ppm); BJD 2460876.9913: recovered, depth 10349 ± 434 ppm (catalogue 11239 ppm)).
Outside the catalogued epoch the screen left 10 threshold entries forming **4 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6523.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 167720788 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 103.402787 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -64.437403 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460908.229186 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 7.809463 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11239.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.133 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8603 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-23 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | lightcurve | 96 | True | `7f35ea6ce0138cbc` | True |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | lightcurve | 87 | False | `872b63e6f84f5ace` | True |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | lightcurve | 88 | False | `b2acf91177ce2929` | True |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | lightcurve | 90 | False | `4c4cd020f8850f97` | True |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | lightcurve | 93 | False | `aae98e2e41085e25` | True |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | lightcurve | 94 | False | `b06ba3d196b740a2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460908.22919 | gap | 0 | — | 11239 | — |
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460916.03865 | recovered | 124 | 10221 ± 471 | 11239 | 0.03 |
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460923.84811 | recovered | 124 | 9600 ± 489 | 11239 | 0.67 |
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460931.65757 | recovered | 124 | 10852 ± 486 | 11239 | -0.00 |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 2460666.13583 | not_recovered | 39 | 7191 ± 912 | 11239 | — |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 2460673.94530 | recovered | 124 | 10464 ± 419 | 11239 | -0.19 |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 2460681.75476 | recovered | 123 | 9632 ± 441 | 11239 | -0.46 |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 2460689.56422 | not_recovered | 103 | 4427 ± 573 | 11239 | — |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | 2460697.37368 | not_recovered | 124 | 8503 ± 455 | 11239 | — |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | 2460705.18315 | gap | 0 | — | 11239 | — |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | 2460712.99261 | recovered | 124 | 9693 ± 474 | 11239 | 0.43 |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 2460752.03993 | recovered | 124 | 9801 ± 476 | 11239 | 0.60 |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 2460759.84939 | gap | 0 | — | 11239 | — |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 2460767.65885 | recovered | 124 | 11146 ± 470 | 11239 | -0.79 |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 2460830.13456 | gap | 0 | — | 11239 | — |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 2460837.94402 | partial | 124 | 10064 ± 462 | 11239 | 0.12 |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 2460845.75348 | partial | 124 | 9577 ± 431 | 11239 | -0.68 |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 2460853.56294 | recovered | 124 | 11213 ± 443 | 11239 | -0.04 |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 2460861.37241 | partial | 124 | 9058 ± 427 | 11239 | -0.20 |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 2460869.18187 | gap | 0 | — | 11239 | — |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 2460876.99133 | recovered | 124 | 10349 ± 434 | 11239 | -0.29 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2024353092137-s0087-0000000167720788-0284-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025014115807-s0088-0000000167720788-0285-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025154050500-s0093-0000000167720788-0290-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460927.05115 | -0.01805 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000167720788-0287-s_lc.fits` | 2460768.14264 | -0.01801 | 2 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000167720788-0291-s_lc.fits` | 2460874.84722 | -0.01713 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000167720788-0293-s_lc.fits` | 2460925.93448 | -0.01467 | 2 | PDCSAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6523.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:32:08Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:32:11Z: TOI-6523.01 (TIC 167720788, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:32:15Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:32:18Z: UCAC4 128-009756 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460908.2292: gap (catalogue 11239 ppm); BJD 2460916.0386: recovered, depth 10221 ± 471 ppm (catalogue 11239 ppm); BJD 2460923.8481: recovered, depth 9600 ± 489 ppm (catalogue 11239 ppm); BJD 2460931.6576: recovered, depth 10852 ± 486 ppm (catalogue 11239 ppm); BJD 2460666.1358: not recovered, depth 7191 ± 912 ppm (catalogue 11239 ppm); BJD 2460673.9453: recovered, depth 10464 ± 419 ppm (catalogue 11239 ppm); BJD 2460681.7548: recovered, depth 9632 ± 441 ppm (catalogue 11239 ppm); BJD 2460689.5642: not recovered, depth 4427 ± 573 ppm (catalogue 11239 ppm); BJD 2460697.3737: not recovered, depth 8503 ± 455 ppm (catalogue 11239 ppm); BJD 2460705.1831: gap (catalogue 11239 ppm); BJD 2460712.9926: recovered, depth 9693 ± 474 ppm (catalogue 11239 ppm); BJD 2460752.0399: recovered, depth 9801 ± 476 ppm (catalogue 11239 ppm); BJD 2460759.8494: gap (catalogue 11239 ppm); BJD 2460767.6589: recovered, depth 11146 ± 470 ppm (catalogue 11239 ppm); BJD 2460830.1346: gap (catalogue 11239 ppm); BJD 2460837.9440: partial, depth 10064 ± 462 ppm (catalogue 11239 ppm); BJD 2460845.7535: partial, depth 9577 ± 431 ppm (catalogue 11239 ppm); BJD 2460853.5629: recovered, depth 11213 ± 443 ppm (catalogue 11239 ppm); BJD 2460861.3724: partial, depth 9058 ± 427 ppm (catalogue 11239 ppm); BJD 2460869.1819: gap (catalogue 11239 ppm); BJD 2460876.9913: recovered, depth 10349 ± 434 ppm (catalogue 11239 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3, 3, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6523.01: Gaia DR3 5285469153407649664 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6523.01: Teff 5802 K, R* 1.20 ± 0.10, M* 1.16 ± 0.12, ρ* 0.67 ± 0.18 ρ☉ (dwarf sequence, M_G 3.98, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6523.01: 11 Gaia neighbour(s) within 52.5", contamination 26.32%; depth 10221 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 5285469084688173952, 31.5", ΔG 1.86); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6523.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6523.01: UCAC4 128-009756 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6523-01.yaml
python -m cygnus.multi report campaigns/toi-6523-01.yaml
```
