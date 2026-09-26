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

## 2026-09-26: meticulous vetting of the two dossier front-runners

Beyond the `vet` tool (whose states are in each campaign's `vetting/VETTING.md`), the SPOC DV products,
parity tests, raw-data dips and ZTF were checked by hand. Products live in scratch
`lead_vetting_2026-09-26/` (scripts + JSONs); the readings below cite them.

### TOI-2666.01 (TIC 170889511, HD 80133): lead retained; period unresolved; EB reading at P 36.53 d refuted

SPOC DV products exist for three sector combinations (fetched to scratch `campaign_toi-2666-01/`):

- **S35 DV:** TCE fitted P = 13.92639 ± 0.00045 d, T0 = 2459259.1591 (the catalogued transit), depth 18,377 ppm.
  Its 2nd modelled transit (2459273.0855) falls **inside S35 data and is absent**: box fit −180 ± 96 ppm.
  Two observed events (S35 only) cannot fix a period; the fit is a two-event artifact.
- **S35+S61 DV (file named `...s0065...dvt.fits`):** TCE 1 P = 34.36669 ± 0.00003 d (NTRANS 2), TCE 2
  P = 720.93 d, depth 579 ± 100 ppm, MES 10.1. The S61 sector **contains no transit at all** — the deepest
  3σ-grouped dips are 1-5 ppt spot crossings, and the box fits at the TCE 1 model's S61 epoch (2459980.860,
  −254 ± 87 ppm), at the 13.93-d model's S61 epoch (2459966.459: −223 ± 65 ppm) and at the 7.50-d model's
  S61 epoch (2459987.750: −766 ± 460 ppm) are all nulls. Both SPOC periods are refuted by their own
  predicted transits landing on covered, dipless data.
- **S99 DV:** TCE P = 7.50451 ± 0.0017 d, T0 = 2461049.1611 (the lead event E1), depth 286 ± 83 ppm,
  TSNR 4.28, NTRANS 3, bootstrap odd/even **not computed** (value 0.0, significance −1.0). The period is the
  E1-to-2461064.170 interval halved; the k=2 dip at 2461064.170 is measured here at 251 ± 80 ppm (3.1σ within
  its window, χ²ν 1.04) and k=3 (2461071.675) is a null (−336 ± 105 ppm, 13 cadences). Another two-event artifact.

Parity test on the P 36.53 d secondary-eclipse alias (the vet's only ≥4σ phase-0.5 dip, 316 ± 62 ppm over 3
epochs): 36.53 d = ΔT(ref→E1)/49, and 49 is **odd**, so the two measured deep events would alternate primary and
secondary if P = 36.53 d were the period of an EB — both are measured ~12-15 ppt deep (depth ratio 1.02 ± 0.02),
which refutes an EB with a 316-ppm secondary at that alias. The 316-ppm phase-0.5 dip is therefore not the
companion's secondary; the host's strong spot variability (1-3.4 ppt dips lasting 2-61 h in every sector,
local robust σ 500-680 ppm — also the reason the box-fit χ²ν reads 21.8) is the more plausible source.

Independent epochs: Kepler/K2 has no coverage at the target position (MAST discovery: 0 products — recorded);
ZTF has one OID at 3″ whose VOTable carries **no points** (host G 7.5, saturated); Gaia DR3 has **no** radial
velocity for the host (G 7.54, above the RVS bright limit) and no NSS solution (earlier NSS campaign);
ESO TAP timed out (known 2026-09-26 outage) so archival-RV bounds are **not tested** today.

**Reading: the lead survives as a real, on-target, deep (12-15 ppt) grazing eclipse pair on HD 80133 whose
period is unresolved.** All short-period interpretations (13.93, 34.37, 7.50 d — SPOC's own fits — and the
vet's excluded aliases) are refuted by absent predicted transits; what remains are the 52 data-allowed aliases,
all P ≥ 12.79 d by the density limit, most with phase-0.5 windows landing in the 683-d and 58-d seasonal gaps
(so a grazing EB's secondary can hide there). Equal depths (1.02 ± 0.02), equal durations (1.00), the
difference images on target for both events and no capable Gaia neighbour within 52.5″ (ΔG limit 4.53 for the
12.5 ppt depth; G<17 census) leave a grazing planet (R_p ≈ 1.1-1.4 R_Jup for b near 1 at these depths) or an
equal-depth grazing EB. Both surviving interpretations need RV: a stellar companion gives K ~ km/s at every
surviving alias; a planet gives ≲ 100 m/s. Next test: archival or new RV (not_tested today: ESO outage, Gaia
RVS absent), ground photometry at the predicted phases of the shortest surviving aliases (12.79-40 d), and
future TESS sectors against the alias ephemerides.

### TOI-3500.02 (TIC 443666343): E2 rejected as an off-target/pointing artifact; E1 fully clean; period P = 700.62/n unresolved

- **E2 (S101) is rejected.** Its difference-image centroid is **6.74″ from the out-of-transit centroid at
  11.5σ** (E1: 0.35″ at 0.7σ), i.e. the deficit does not sit on the stamp's flux core; the event carries
  POS_CORR2 +28.9σ and MOM_CENTR2 +19.2σ excursions (aperture-loss signature), its depth is detrending-unstable
  (1,614-7,796 ppm) and its duration ratio is 0.80. A pointing excursion during the event makes a transit-shaped
  false dip; no Gaia source capable of the depth exists at the deficit's ~7″ offset (the capable list has
  nothing between 4″ and 43″). **E2 does not support any period.**
- **The E1 "secondary-eclipse" failure was E2 contamination.** The phase-0.5 windows of the aliases
  P = 700.62/n (odd multiples of 350.31 d) all land on t_ref + 1050.94 d = E2's epoch, so those rows measure
  E2's dip (7,491 ± 186 ppm). With E2 excluded, the remaining covered aliases are clean: P 35.03 (−80 ± 186),
  50.04 (313 ± 167), 58.39 (24 ± 167), 87.58 (208 ± 167), 18.44 (206 ± 74 over 7 epochs) — no ≥4σ secondary
  anywhere. Planet-consistent for the short aliases; EB secondaries could still hide in the seasonal gaps for
  the long ones (140-700 d).
- **E1 (S90) passes every check** (weighted fit χ²ν 1.19, shape ratio 1.08 ± 0.06, duration ratio 1.00,
  detrending stable 7,480-7,885 ppm, red noise 36σ, 237/237 cadences, common mode clean, density limit
  16 of 17 aliases compatible, shortest 35.03 d; 18.44 d excluded).
- **The capable blends are excluded as the E1 dip source.** The 3.71″ neighbour (G 14.07, **same Gaia parallax
  as the host, 5.21 mas** — a co-moving companion) maps through the S90 TPF WCS to 0.182 px from the placed host
  in the direction **opposite** the measured deficit centroid; the deficit (0.35″, 0.7σ) sits at the stamp's
  flux centroid, which a 12.5:1 host/blend ratio pins within ~0.3-0.4″ of the host. The 43.2″ neighbour (ΔG 3.88)
  is a different pixel region and shows no deep ZTF dips (154 usable points, range ±0.05 mag).
- **ZTF (IRSA, 2026-09-26):** host G 11.35: 70 catflags-0 zg points (mag 11.812-11.923), 0-1 points within ±2 h
  of any joint-alias predicted phase — no coverage to test; the 3.71″ neighbour: **no ZTF light curve exists**
  (0 rows — not_tested, not a pass).
- The alias family after E2's rejection widens from the 9 "joint" periods back to the 17 data-allowed aliases
  of ΔT(ref→E1) = 700.6242 d (P = 700.62, 350.31, 233.54, …, 35.03 d compatible). The 2:1 spacing structure
  (ref→E1 = 2 × 350.31) makes P = 350.31 d the most economical single reading, but two events cannot fix a period.

**Reading: lead retained (Unverified lead), now resting on two clean on-target events.** Next test: RV on the
host (G 11.35, measurable), ground photometry at the predicted phases of the compatible aliases, and the
P = 350.31 ephemeris against future TESS sectors (next predicted transit 2027-08, sector coverage permitting).

| toi-1835-02 | E1 (S23) | Sibling ephemerides failed: the known sibling TOI-1835.01 (P 5.6420 d, 544 ppm) predicted -0.27 +/- 0.06 h at the event | **Rejected: a transit of the sibling planet TOI-1835.01.** |
| toi-225.01 | E1 (S96) | Box fit finds no dip (799 +/- 331 ppm); scattered-light flags on 502 cadences, SAP_BKG +42.6 sigma | **Rejected: systematics.** |
| toi-6667.01 | E1 (S104) | Difference image 108.7 arcsec from the OOT centroid (34 sigma) - the deficit is not on the target; detrending depth 2,914-9,410 ppm | **Rejected: the deficit is elsewhere.** |

| toi-6695.01 | E1 (S61), E2 (S88) | E1 passes every check (diff image 0.8 arcsec on target, no secondary at 14 covered aliases); E2 rejected (diff image 12.0 arcsec off at 14.7 sigma, pointing excursions) | **Survives via E1 (Unverified lead): 26 data-allowed aliases of DeltaT 723.995 d; next tests ZTF/ground photometry at alias phases, future sectors, RV.** |
| toi-7399.01 | E1 (S20) | Shape mismatch (depth ratio 0.49 +/- 0.15, duration 0.65); red noise 4.4 sigma; MOM_CENTR2 +14.7 sigma / POS_CORR2 +10.2 sigma; 39% of deficit in aperture | **Rejected: shape mismatch + pointing systematics.** |
| toi-7857.01 | E1 (S55) | Shape mismatch: depth ratio 5.15 +/- 0.58, duration ratio 3.00 (23.9 ppt, 3.8 h vs the 4.6 ppt, 1.27 h reference) | **Rejected: not the same signal** (consistent with an EB eclipse on a possible circumbinary host, not the TOI's transit). |

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
