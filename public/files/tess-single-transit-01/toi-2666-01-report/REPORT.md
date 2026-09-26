# Known-object test, TOI-2666.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-24 (pilot of the
> known-object loop). Reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2666-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #74, fetch_products #73, known_signal_recovery #75, period_aliases #77, prior_art #78, residual_screen #76
- Runner finished (UTC): 2026-09-24T12:14:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2666.01 (BJD 2459259.1414: recovered, depth 12466 ± 43 ppm (catalogue 22040 ppm)).
Outside the catalogued epoch the screen left 59 threshold entries forming **32 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461049.1644 matches the catalogued transit's depth (14437 vs 12466 ppm), 1790.005 d later; 52 of 1790 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Reviewer notes (2026-09-24)

**Evidence level: Unverified lead** (a probable second transit of TOI-2666.01). The checks done by hand on the
sector 99 event, using the same SPOC PDCSAP/SAP light curves and 2-d running-median residuals:

| Test | Result | State |
|---|---|---|
| Quality flags and gaps | all cadences within ±0.2 d have QUALITY = 0; no gap > 10 min within ±1.5 d | passed |
| SAP vs PDCSAP | centre depth −18.9 ppt in both (20-min bins) | passed |
| Shape vs the catalogued transit (sector 35) | 20-min binned profiles −5.1/−14.8/−19.2/−14.6/−5.0 ppt (S35) vs −5.1/−15.0/−19.4/−15.1/−5.3 ppt (S99); width below −5 ppt 1.33 h in both | passed (consistent) |
| Flux-weighted centroid (MOM_CENTR1/2) in vs out of event | shifts 0.0009 and 0.0004 px against out-of-event scatter 0.0036 and 0.0091 px | passed (no shift seen at this precision) |
| Difference-image centroids / nearby-star blend | not done | not tested |
| Eclipsing-binary tests (odd/even, secondary eclipse, shape V vs U) | not done; only two events | not tested |
| TOI table / literature | TOI table (row updated 2022-04-19) lists no period; a web search (2026-09-24) found nothing on TOI-2666 or HD 80133; ADS and ExoFOP not searched | inconclusive |

What this supports: the same, repeatable ~1.9 % (centre), ~1.3 h dip on HD 80133 (TIC 170889511, Tmag 7.0) in
sectors 35 and 99, ΔT = 1790.005 d. What it does not: a period (52 aliases from 1790 d down to ~45 d remain
within the retrieved data), a planetary nature (a blended or grazing eclipsing binary is not excluded), or
novelty (ExoFOP and the TESS team may already hold this). Next test: ExoFOP TOI-2666 notes and SPOC DV for
sector 99; difference-image centroids for both events; predicted transits of the surviving aliases in other
TESS sectors or ground photometry.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2666.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 170889511 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 139.480865 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -3.387525 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459259.141383 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 22040.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 1.445 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 6.9887 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2022-04-19 12:02:07 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021039152502-s0035-0000000170889511-0205-s_lc.fits` | 35 | True | `37a2ecd845582f31` | False |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 61 | False | `c66e7a0a967d5e3e` | False |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 99 | False | `90366f3815e45208` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000170889511-0205-s_lc.fits` | 2459259.14138 | recovered | 43 | 12466 ± 43 | 22040 | 0.43 |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | — | epoch not in this light curve | — | — | 22040 | — |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 22040 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021039152502-s0035-0000000170889511-0205-s_lc.fits` | 10 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 5 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461049.16442 | -0.01420 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.77641 | -0.00272 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.62155 | -0.00233 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.49029 | -0.00268 | 2 | SAP | 1 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.78166 | -0.00258 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461073.06947 | -0.00255 | 2 | SAP | 1, 2 | no |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.57224 | -0.00254 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.60696 | -0.00239 | 2 | SAP | 1, 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.59277 | -0.00228 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.89030 | -0.00224 | 2 | SAP | 1, 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.63583 | -0.00221 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459982.18861 | -0.00200 | 15 | PDCSAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.73027 | -0.00187 | 3 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.73583 | -0.00184 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.48721 | -0.00168 | 2 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.82402 | -0.00162 | 3 | SAP | 2 | no |
| `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 2461072.50696 | -0.00161 | 2 | SAP | 1 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.33999 | -0.00151 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.79416 | -0.00150 | 4 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.88305 | -0.00147 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.94278 | -0.00145 | 3 | SAP | 1, 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.38166 | -0.00139 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459969.21473 | -0.00138 | 2 | SAP | 1, 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.68583 | -0.00137 | 4 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.92472 | -0.00135 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.64138 | -0.00133 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.47471 | -0.00132 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.89277 | -0.00129 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.40110 | -0.00129 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459981.90111 | -0.00125 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459982.17333 | -0.00121 | 2 | PDCSAP | 1 | no |
| `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 2459974.83155 | -0.00118 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461049.16442 | 14437 | 12466 | 1790.0053 | 52 / 1790 | 1790.01, 895.003, 596.668, 447.501, 358.001, 298.334, 255.715, 223.751, 198.889, 179, 162.728, 149.167, 137.693, 127.858, 119.334, 111.875, 105.294, 99.4447, 94.2108, 89.5003 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2666.01**

- NASA_Exoplanet_Archive (done, 2026-09-24): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-24T12:07:58Z
- TESS_TOI (done, 2026-09-24): 1 match(es) in TESS_TOI within 30" as of 2026-09-24T12:08:02Z: TOI-2666.01 (TIC 170889511, disposition APC)
- VSX (done, 2026-09-24): no match in VSX within 30" as of 2026-09-24T12:08:09Z
- SIMBAD (done, 2026-09-24): 2 match(es) in SIMBAD within 30" as of 2026-09-24T12:08:11Z: TOI-2666.01 (Pl?); HD  80133 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459259.1414: recovered, depth 12466 ± 43 ppm (catalogue 22040 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (10, 3.5, 5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 90%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2461049.1644, ΔT = 1790.005 d, 52 of 1790 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1790.01, 895.003, 596.668, 447.501, 358.001, 298.334, 255.715, 223.751, 198.889, 179, 162.728, 149.167 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |


## Reviewer notes (2026-09-25, supersede pass)

**Superceded by the multi-archive runner:** re-run through `python -m cygnus.multi` on 2026-09-25, steps fetch_products, calibrate_screen, known_signal_recovery, residual_screen, period_aliases, prior_art (ledger fetch_products #1495, calibrate_screen #1496, known_signal_recovery #1497, residual_screen #1498, period_aliases #1499, prior_art #1500). Same retrieved products, same science outputs: entries, depths, k-star calibration and aliases match the production-runner results recorded here; the multi runner additionally records a screen-suitability census and a red-noise systematics model per light curve. The record is regenerated by the multi runner; nothing in the review changes.


## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2666-01.yaml
python -m cygnus.campaign report campaigns/toi-2666-01.yaml
```

## Addendum 2026-09-26: suite-expansion checks

Re-run on 2026-09-26 with the steps added by the suite expansion (`docs/SUITE_EXPANSION.md` §7.3) and the corrected moving-object check (TESS-centred SkyBoT positions, distance-aware). The earlier science outputs (screen, calibration, positive control, aliases, cross-match) were compared leaf by leaf and are unchanged apart from timestamps. States and notes below are copied from `sky_record.json`; the review above is not changed by them unless a note says so.

| Check | State | Note |
|---|---|---|
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2666.01: Gaia DR3 3837451574150437120 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2666.01: dwarf priors not applied — RUWE 1.464014 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-2666.01: 3 Gaia neighbour(s) within 52.5", contamination 0.38%; depth 12466 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2461049.1644 caution: argabrightening (within ±0.25 d); BJD 2461072.6215 suspect: argabrightening (in event), manual exclude (in event), MOM_CENTR1 z=-5.0, POS_CORR1 z=-5.4; BJD 2461072.7764 suspect: argabrightening (in event), manual exclude (in event), MOM_CENTR1 z=-8.3, POS_CORR1 … |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Variable-catalogue collision (VSX) | passed | TOI-2666.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2666.01: HD  80133 otype PM* (star_or_other) at 1.1" |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |

`failed` on the per-event census means at least one persistent screen event carries an in-event artifact flag or pointing shift (`event_census.json`); it is a statement about those events, not about the catalogued signal.

## Reviewer notes (2026-09-26, vetting reconciliation)

Vetting rerun 2026-09-26 with the final code: the lead survives. Shape (ratio 1.02 +/- 0.02), detrending, red noise (158 sigma below the random-epoch null), background/pointing, common mode, Gaia neighbours, duration limit and difference image (0.4", 0.7 sigma) all pass. Open items: the error-weighted box fit is inconclusive (chi2_nu 21.8 - the pipeline errors do not describe the scatter; weighted depth unchanged), the event carries argabrightening flags within +/-0.5 d, and the secondary-eclipse search flags 1 of 26 covered aliases (P 36.53 d, 316 +/- 62 ppm) - a possible secondary that would fit the V-shaped eclipsing-binary reading. V-shaped index 1.47: grazing planet or EB. Dossier decision pending.

Source: `campaigns/toi-2666-01/vetting/VETTING.md` (regenerated 2026-09-26 with the final code) and `campaigns/tess-mono-01/LEAD_VETTING_LOG.md`.

## Reviewer notes (2026-09-26, meticulous DV + parity vetting)

**Evidence level unchanged: Unverified lead.** The ExoFOP/SPOC DV check (open decision 3) is now done, plus a
parity test and an independent-data census. Findings (full detail in the vetting log):

1. **SPOC's own DV periods are two-event artifacts, refuted by the data.** The S35 DV fitted P = 13.92639 d;
   its 2nd modelled transit (2459273.0855) is inside S35 data and absent (−180 ± 96 ppm). The S35+S61 DV fitted
   P = 34.36669 ± 0.00003 d; the S61 sector contains **no transit at all** (the model's S61 epoch 2459980.860
   measures −254 ± 87 ppm). The S99 DV fitted P = 7.50451 d at the lead event's epoch (depth 286 ± 83 ppm,
   TSNR 4.3); its k=3 predicted transit (2461071.675) is a null (−336 ± 105 ppm). Each fit is anchored on one
   or two observed events and refuted by its own absent predicted transits.
2. **The P 36.53 d "secondary" (316 ± 62 ppm) is parity-inconsistent.** 36.53 d = ΔT/49 with 49 odd, so the two
   measured deep events would alternate primary/secondary — both measure ~12-15 ppt. Not an EB secondary at
   that alias. The host's spot variability (1-3.4 ppt dips, 2-61 h, every sector) is the likelier source.
3. **Independent epochs are absent:** no Kepler/K2 coverage (0 products at the position, recorded); ZTF VOTable
   empty (host G 7.5, saturated); Gaia DR3 has no RVS velocity for the host; ESO TAP timed out (2026-09-26
   outage) so archival-RV bounds are **not tested** today.
4. **What remains:** the 52 data-allowed aliases (all P ≥ 12.79 d by the density limit), with most phase-0.5
   windows inside the seasonal gaps — a grazing EB's secondary can hide there. Equal depths (1.02 ± 0.02), equal
   durations, on-target difference images and no capable neighbour within 52.5″ leave a grazing planet
   (R_p ≈ 1.1-1.4 R_Jup at b near 1) or an equal-depth grazing EB.

**Verdict: the lead survives; the repeat event is real, but the period is unresolved and the EB-vs-planet
question needs RV.** A stellar companion gives K ~ km/s at every surviving alias (decisive); a planet gives
≲ 100 m/s. Recommended follow-up: archival or new RV (host V ~ 7 — easy), ground photometry at the predicted
phases of the shortest surviving aliases (12.79-40 d), and future TESS sectors against the alias ephemerides.
