<!-- cygnus:generated-draft -->
# Known-object test, TOI-5207.02

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5207-02.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4196, calibrate_screen #4172, event_census #4182, fetch_independent #4192, fetch_products #4169, known_signal_recovery #4174, moving_objects #4184, period_aliases #4183, prior_art #4198, residual_screen #4181, stellar_context #4175, variability_guard #4197
- Runner finished (UTC): 2026-09-30T21:42:09Z

## Bottom line

Positive control **inconclusive**: BJD 2459951.0420: gap (catalogue 16245 ppm).
Outside the catalogued epoch the screen left 19 threshold entries forming **5 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5207.02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 147892178 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 142.729233 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 71.740257 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459679.677932 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 67.8410209 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16244.5390069 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.0940127 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.2754 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-08-07 12:04:27 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | lightcurve | 60 | False | `c151b682340bf4bb` | True |
| `tess2024003055635-s0074-0000000147892178-0269-s_lc.fits` | lightcurve | 74 | False | `bdf113cde5cd7db0` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459951.04202 | gap | 0 | — | 16245 | — |
| `tess2024003055635-s0074-0000000147892178-0269-s_lc.fits` | — | epoch not in this light curve | — | — | 16245 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024003055635-s0074-0000000147892178-0269-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459956.51305 | -0.02765 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459956.47972 | -0.02651 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459942.21706 | -0.02280 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459956.55055 | -0.02524 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000147892178-0249-s_lc.fits` | 2459955.53666 | -0.02319 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5207.02**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:42:02Z
- TESS_TOI (done, 2026-09-30): 2 match(es) in TESS_TOI within 30" as of 2026-09-30T21:42:03Z: TOI-5207.01 (TIC 147892178, disposition PC); TOI-5207.02 (TIC 147892178, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:42:06Z: Gaia DR3 1119626991143916288 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:42:07Z: TOI-5207 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2459951.0420: gap (catalogue 16245 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5207.02: Gaia DR3 1119626991143916288 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5207.02: Teff 3809 K, R* 0.57 ± 0.05, M* 0.56 ± 0.06, ρ* 2.97 ± 0.77 ρ☉ (dwarf sequence, M_G 8.26, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5207.02: 4 Gaia neighbour(s) within 52.5", contamination 20.13%; depth 16245 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 1119626922424922624, 29.3", ΔG 1.69); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 1 clean; BJD 2459956.4797 suspect: momentum dump (in event), manual exclude (within ±0.25 d); BJD 2459956.5131 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5207.02: Gaia DR3 1119626991143916288   ROT                            P=None at 0.6" |
| Object-class guard (SIMBAD) | passed | TOI-5207.02: TOI-5207 otype * (star_or_other) at 0.5" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5207-02.yaml
python -m cygnus.multi report campaigns/toi-5207-02.yaml
```
