# tess-mono-01 lead vetting log

Started 2026-09-25 with the new `python -m cygnus.campaign vet campaigns/<slug>.yaml [--events BJD,…]`
(`src/cygnus/campaign/vet.py`). The tool writes `campaigns/<slug>/vetting/` (`vetting.json`,
`VETTING.md`, one figure per event) and a ledger run `cygnus.campaign:<id>:lead_vetting`.
**Paused by the user on 2026-09-25** after the targets below. Nothing here changes a record's outcome
or evidence level; each report's reviewer section still has to be updated by hand.

## Checks the tool adds per event

| Check | What it tests |
|---|---|
| Sibling TOI ephemerides | a periodic TOI on the same TIC (NASA Exoplanet Archive `toi` table) predicted at the event |
| Box fit finds a dip / shape matches reference | box depth and duration (quadratic baseline) vs the catalogued transit re-measured the same way |
| Detrending alternatives | depth under polynomial (orders 1–3) and running median (0.5, 1, 2 d, event masked) detrendings |
| Red-noise significance | box statistic vs 300 random epochs of the same light curve |
| Background / centroid / pointing | SAP_BKG, MOM_CENTR1/2, POS_CORR1/2 shifts at the event vs random epochs |
| Quality flags and coverage | flags within ±0.5 d, nearest momentum dump, usable in-transit cadences |
| Gaia neighbours | Gaia DR3 (G < 17) within 52″ bright enough to produce the depth if fully eclipsed |
| Common mode | up to 5 SPOC 120-s light curves on the same camera/CCD in the same sector |
| Difference image | SPOC target pixel file: out-of-transit − in-transit centroid vs the out-of-transit centroid (bootstrap σ) |
| Stellar density / secondary eclipse | data-allowed aliases P = ΔT/n: circular central-transit duration limit; phase-0.5 dip with red-noise errors |

## Results so far (tool states; reviewer reading in brackets)

| Target | Event | Tool result | Reading |
|---|---|---|---|
| TOI-2666.01 | S99, BJD 2461049.164 | all checks pass; difference image on target (0.4″, 0.7σ); depth ratio 1.02 ± 0.02, same 1.16-h duration; no secondary at 26 of 52 aliases (1σ 77 ppm) | **Strongest lead: survives every test run.** V-shaped (index 1.47) on both events, consistent with the ExoFOP note "v-shaped; possible EB": a grazing planet or an eclipsing binary. |
| TOI-3500.02 | E1 S90, BJD 2460757.320 | passes shape, detrending, red noise, engineering, common mode, difference image (0.3″) | **Lead survives.** Unresolved Gaia neighbour 3.7″ away, ΔG 2.7, could host the signal; TESS pixels cannot separate them. |
| TOI-3500.02 | E2 S101, BJD 2461107.641 | depth matches, but pointing/centroid excursions (POS_CORR2 +29σ), detrending spread 1.6–7.8 ppt, momentum dump 8.8 h away | [suspect event; timing still notable, see below] |
| TOI-3500.02 | timing | reference → E1 = 700.62 d, E1 → E2 = 350.32 d | the three events are consistent with P = 350.3/n d; the joint alias list needs the rerun with final code |
| TOI-5812.02 | S82, BJD 2460549.461 | sibling check **failed**: TOI-5812.01 (WASP-134 b, KP, P 10.1466 d) predicted −0.01 ± 0.02 h | **Rejected:** a transit of the known planet WASP-134 b. |
| TOI-2318.01 | S52, BJD 2459743.03 | box fit finds no dip (−382 ± 110 ppm); POS_CORR1 +8σ; 172/274 usable cadences | **Rejected:** systematics. |
| TOI-6674.01 | S18, BJD 2458801.12 | background +130σ, scattered-light flags, event at the edge of a data gap; depth 0.36× reference | **Rejected:** scattered light. |
| TOI-2065.01 | S23, BJD 2458930.40 | no dip in box fit; background +257σ; scattered-light and manual-exclude flags | **Rejected:** scattered light. |
| TOI-6666.01 | S18, BJD 2458790.94 | pointing/centroid ~570σ; Earth-point and momentum-dump flags; 4 of 5 same-CCD neighbours dip; difference image 20″ off | **Rejected:** spacecraft pointing systematic (common mode). |

| TOI-6650.04 | six hand-given events, S57–S84 | sibling check **failed** on all six: each within −0.52 to +0.22 h (±0.01 h) of a predicted TOI-6650.01 transit (PC, P 20.3292 d, 10524 ppm) | **Resolved:** the ~20.33-d event train is the known TOI-6650.01, not a new signal. |

Catalogue context (ExoFOP TOI table, downloaded 2026-09-25): TOI-7857.01 is noted on ExoFOP as a possible
circumbinary-planet transit (so the host may be an eclipsing binary). TOI-6695.01 has an ExoFOP note of a
possible additional transit at TBJD 1525.648.

## Not yet vetted (resume here)

- TOI-6695.01, TOI-225.01, TOI-1835.02, TOI-6667.01, TOI-7857.01, TOI-7399.01:
  `python -m cygnus.campaign vet campaigns/<slug>.yaml`.
- The reviewer flags, with their events given by hand:
  - TOI-790.03: `--events 2458552.06`;
  - TOI-2534.01: `--events 2461174.36`;
  - TOI-3724.01: `--events 2459928.32,2460294.69`.
- Rerun TOI-2666.01, TOI-3500.02, TOI-5812.02, TOI-2318.01 and TOI-6674.01 with the final code (the
  red-noise secondary errors, the joint periods and the no-dip gate were added mid-batch). Their products
  are cached, so each rerun is quick.
- Then write each report's Reviewer notes from `vetting/VETTING.md` and decide which leads get dossiers.
  TOI-2666.01 and TOI-3500.02 are the current front-runners.

## Erratum 2026-09-26: difference-image rule

Until 2026-09-26 `cygnus.campaign vet` marked the difference-image centroid check `passed` whenever the offset was not significant, however large it was. The rule is now: `passed` only for an offset below 0.25 TESS pixel; a larger offset that is not significant is `inconclusive` (the image cannot place the dip). Two readings above used the old rule: TOI-2065.01 E1 (offset 27.7″, 1.0σ) and TOI-2318.01 E1 (20.5″, 2.4σ) were recorded `passed` and would now be `inconclusive`. Both leads were rejected on other tests (scattered light; systematics), so neither conclusion changes. Their generated `vetting/VETTING.md` files are left as produced; a rerun with the current code regenerates them. See `docs/SUITE_EXPANSION.md` §7.1, item 12.

## 2026-09-26: suite-expansion checks on the leads

All 76 known-object campaigns were re-run with the new record checks (`docs/SUITE_EXPANSION.md` §7.3). Earlier
science outputs are unchanged (leaf-by-leaf comparison). For the leads:

- **TOI-2065.01 (already rejected, scattered light):** the VSX guard **failed**. VSX lists KELT KC08C10921, type EA
  (Algol-type eclipsing binary), P = 71.9649 d, 0.9″ from the target, and SIMBAD classifies the host HD 111605 as SB*
  (spectroscopic binary, 0.2″). This independently points to a binary; the rejection stands.
- **All 13 leads:** the per-event census is `failed`. At least one persistent event of each carries an in-event quality
  flag or a pointing shift. For TOI-2666.01 the lead event E1 (BJD_TDB 2461049.1644) is only *caution* (Argabrightening
  within ±0.25 d), and the other two events are suspect. Read `event_census.json` per event before using the summary state.
- **Moving objects** (TESS-centred SkyBoT, corrected 2026-09-26): no known object bright and close enough at any
  queried lead epoch. Several are `inconclusive` because SkyBoT did not answer some epochs.
- **Independent repetition / ZTF:** `not_tested` everywhere. No light curve from another instrument was fetched;
  adding Kepler/K2/HLSP or ZTF products to `fetch_products` is the next discriminating test.

## Reconciliation 2026-09-26: records and reports brought in line with the verdicts

All seven vetted campaigns were re-run with the final code (cached products; fresh `vetting/VETTING.md` and ledger runs); the regenerated tool states confirm the earlier readings. The five rejected leads (TOI-5812.02, TOI-2318.01, TOI-6674.01, TOI-2065.01, TOI-6666.01) had their sky records reconciled: `outcome` lead -> `pipeline_check`, evidence level cleared (the TOI-6650.04 precedent), and the repeat-candidate sentence dropped from the record summary; each REPORT.md carries the verdict with its tool evidence. The two surviving leads (TOI-2666.01, TOI-3500.02) keep their records unchanged and gained the rerun reading in REPORT.md; both are the dossier front-runners. The per-target failure entries under `FAILED:field:*` in the explorer provenance are unrelated to vetting (Gaia cone fetches).
