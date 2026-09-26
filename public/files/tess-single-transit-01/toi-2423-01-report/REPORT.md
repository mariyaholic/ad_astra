# Known-object test, TOI-2423.01

> **Generated draft** (`python -m cygnus.campaign report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2423-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #561, fetch_products #560, known_signal_recovery #562, period_aliases #564, prior_art #565, residual_screen #563
- Runner finished (UTC): 2026-09-25T11:06:19Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 190 threshold entries forming **69 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-24)

**Evidence level: no candidate raised.** The positive control could not run: the catalogued epoch
(BJD 2459097.062) falls outside the six retrieved sectors (2, 4, 69, 96, 97). For each persistent
event I checked QUALITY flags, cadence gaps, SAP vs PDCSAP behaviour and flux-weighted centroids
(MOM_CENTR1/2) in `sector04/normalized_series.csv` and `sector04/screen.json`. The in/out centroid
baseline is small (2 out-of-event entries), so nominal sigmas are indicative only; difference-image
centroids are not built.

| Event (BJD) | What the on-disk outputs show | Verdict |
|---|---|---|
| 2458421.36820 | deepest entry -0.0437, up to 137 cadences (~4.6 h). Only 2 of 168 cadences in +/-2.8 h are non-zero QUALITY; gaps <= 4 min in +/-1.5 d. BUT centroid shifts -0.79 / -0.40 px (col/row) vs ~0.005 px out-of-event scatter: during the dip the light is not centered on the target | artifact-suspect (nearby/blended source or scattered light); not vetted |
| 2458421.46681 | -0.0030, 3 cadences; identical centroid behaviour (-0.78/-0.39 px) -> same complex as above | artifact-suspect; not vetted |
| 2458422.55915 | -0.0026, 2 cadences; 81 of 168 cadences in +/-2.8 h are non-zero QUALITY; centroid shift -0.29/-0.10 px vs ~0.005 px | systematic-suspect (stray-light-rich window); not vetted |
| 2458436.39-47 (six overlapping events) | shallow (-0.0024/-0.0027), <= 4 cadences each; non-zero-QUALITY cadences rise toward mid (16->74 of 168 each); centroid shifts ~-0.06/-0.05 px above ~0.005 px scatter | systematic-suspect; not vetted |

Two further deep excursions in sector 4 (-0.0827/-0.0799 at BJD 2458421.24/27, 8/12 min) are SAP only
(not persistent): most likely cosmic rays or scattered light. Not vetted.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2423.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 197807043 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 53.467245 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -57.621295 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459097.062 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 12640.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 4.208 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.5137 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2018234235059-s0002-0000000197807043-0121-s_lc.fits` | 2 | False | `6ff0e9a181e5e9b1` | False |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 4 | False | `b06db5e90cb33a67` | False |
| `tess2023237165326-s0069-0000000197807043-0264-s_lc.fits` | 69 | False | `0e64dfa86913905b` | False |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 96 | False | `b14510542814c6f6` | False |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 97 | False | `7d741c591899f2f5` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000197807043-0121-s_lc.fits` | — | epoch not in this light curve | — | — | 12640 | — |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | — | epoch not in this light curve | — | — | 12640 | — |
| `tess2023237165326-s0069-0000000197807043-0264-s_lc.fits` | — | epoch not in this light curve | — | — | 12640 | — |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 12640 | — |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | — | epoch not in this light curve | — | — | 12640 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018234235059-s0002-0000000197807043-0121-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 2000 |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2023237165326-s0069-0000000197807043-0264-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.36820 | -0.04370 | 137 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.46681 | -0.00295 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.47139 | -0.00272 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.41583 | -0.00265 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.43667 | -0.00257 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458422.55915 | -0.00256 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.39153 | -0.00252 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.39778 | -0.00243 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.23973 | -0.08274 | 36 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.26890 | -0.07993 | 4 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.39935 | -0.00687 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.48755 | -0.00634 | 3 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.53113 | -0.00588 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.37001 | -0.00584 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.24086 | -0.00569 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.39519 | -0.00541 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.40491 | -0.00527 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.47574 | -0.00488 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.38408 | -0.00483 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.70613 | -0.00479 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.35074 | -0.00456 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.40751 | -0.00445 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.61030 | -0.00423 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.08947 | -0.00411 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460987.63378 | -0.00406 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.55891 | -0.00404 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.34241 | -0.00403 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.15195 | -0.00399 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.19086 | -0.00398 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.62556 | -0.00393 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.73946 | -0.00386 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.45491 | -0.00380 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.57417 | -0.00377 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460967.36186 | -0.00370 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460987.45739 | -0.00369 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460981.30056 | -0.00362 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.22836 | -0.00346 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460980.56932 | -0.00339 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460925.90760 | -0.00326 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 2460987.92821 | -0.00323 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.50361 | -0.00297 | 8 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.54389 | -0.00294 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460927.13679 | -0.00270 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460926.88262 | -0.00260 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.16376 | -0.00258 | 3 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.48278 | -0.00258 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.49528 | -0.00258 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458422.52929 | -0.00254 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460925.95483 | -0.00253 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460927.03609 | -0.00250 | 3 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.17417 | -0.00246 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.14779 | -0.00238 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458415.06481 | -0.00237 | 2 | SAP | 1 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458422.49318 | -0.00235 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460925.74093 | -0.00234 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.49042 | -0.00233 | 3 | PDCSAP | 2 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458422.54248 | -0.00232 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.33736 | -0.00230 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460927.06943 | -0.00229 | 3 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.10334 | -0.00226 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.27556 | -0.00219 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460926.96734 | -0.00218 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458422.51610 | -0.00215 | 2 | PDCSAP | 1, 2 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460926.32566 | -0.00214 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458421.55083 | -0.00212 | 2 | PDCSAP | 2 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458436.47972 | -0.00210 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460918.61027 | -0.00205 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 2458415.30092 | -0.00203 | 2 | SAP | 1 | no |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 2460913.27268 | -0.00196 | 2 | PDCSAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2423.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T11:06:04Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T11:06:06Z: TOI-2423.01 (TIC 197807043, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T11:06:08Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T11:06:10Z: CD-58   719 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 4.5, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 80%, 90%, 0%, 100%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |


## Reviewer notes (2026-09-25, supersede pass)

**Superceded by the multi-archive runner:** re-run through `python -m cygnus.multi` on 2026-09-25, steps fetch_products, calibrate_screen, known_signal_recovery, residual_screen, period_aliases, prior_art (ledger fetch_products #1429, calibrate_screen #1430, known_signal_recovery #1431, residual_screen #1432, period_aliases #1433, prior_art #1434). Same retrieved products, same science outputs: entries, depths, k-star calibration and aliases match the production-runner results recorded here; the multi runner additionally records a screen-suitability census and a red-noise systematics model per light curve. The record is regenerated by the multi runner; nothing in the review changes.


## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2423-01.yaml
python -m cygnus.campaign report campaigns/toi-2423-01.yaml
```

## Addendum 2026-09-26: suite-expansion checks

Re-run on 2026-09-26 with the steps added by the suite expansion (`docs/SUITE_EXPANSION.md` §7.3) and the corrected moving-object check (TESS-centred SkyBoT positions, distance-aware). The earlier science outputs (screen, calibration, positive control, aliases, cross-match) were compared leaf by leaf and are unchanged apart from timestamps. States and notes below are copied from `sky_record.json`; the review above is not changed by them unless a note says so.

| Check | State | Note |
|---|---|---|
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2423.01: Gaia DR3 4729324799004633472 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2423.01: dwarf priors not applied — RUWE 3.3617349 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-2423.01: 4 Gaia neighbour(s) within 52.5", contamination 0.10%; depth 12640 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 8 persistent event(s), 0 clean; BJD 2458421.3682 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR1 z=-43.5, MOM_CENTR2 z=-51.7, POS_CORR1 z=-54.5, POS_CORR2 z=-54.2, SAP_BKG z=+25.9; BJD 2458421.4668 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR1 z=-1… |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Variable-catalogue collision (VSX) | passed | TOI-2423.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2423.01: CD-58   719 otype * (star_or_other) at 0.2" |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |

`failed` on the per-event census means at least one persistent screen event carries an in-event artifact flag or pointing shift (`event_census.json`); it is a statement about those events, not about the catalogued signal.
