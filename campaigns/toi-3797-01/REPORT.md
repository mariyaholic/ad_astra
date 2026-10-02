<!-- cygnus:generated-draft -->
# Known-object test, TOI-3797.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3797-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4079, calibrate_screen #4060, event_census #4067, fetch_independent #4076, fetch_products #4059, known_signal_recovery #4061, moving_objects #4071, period_aliases #4068, prior_art #4081, residual_screen #4064, stellar_context #4062, variability_guard #4080
- Runner finished (UTC): 2026-09-30T21:36:51Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3797.01 (BJD 2459586.2425: recovered, depth 5827 ± 310 ppm (catalogue 8430 ppm); BJD 2459603.8654: recovered, depth 6871 ± 309 ppm (catalogue 8430 ppm); BJD 2459938.7008: gap (catalogue 8430 ppm); BJD 2459956.3238: gap (catalogue 8430 ppm); BJD 2460291.1592: recovered, depth 5974 ± 316 ppm (catalogue 8430 ppm); BJD 2460308.7821: recovered, depth 6273 ± 296 ppm (catalogue 8430 ppm)).
Outside the catalogued epoch the screen left 73 threshold entries forming **38 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460312.6118 matches the catalogued transit's depth (5380 vs 5827 ppm), 726.369 d later; 14 of 726 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3797.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 252912175 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 104.840901 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 48.30288 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459586.242515 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 17.6229161 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8430.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.976 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7983 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | lightcurve | 47 | True | `88dc133350e7ac99` | True |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | lightcurve | 60 | False | `6fe3c5bd98b215c5` | True |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | lightcurve | 73 | False | `d387399a3e0b9ce2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459586.24252 | recovered | 90 | 5827 ± 310 | 8430 | 0.00 |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459603.86543 | recovered | 89 | 6871 ± 309 | 8430 | 0.02 |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2459938.70084 | gap | 0 | — | 8430 | — |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2459956.32375 | gap | 0 | — | 8430 | — |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.15916 | recovered | 89 | 5974 ± 316 | 8430 | -0.01 |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460308.78208 | recovered | 89 | 6273 ± 296 | 8430 | -0.54 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.65916 | -0.01235 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.61176 | -0.01215 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460292.00314 | -0.01217 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.96772 | -0.01180 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.87675 | -0.01094 | 2 | SAP | 1, 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.63277 | -0.01059 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460292.06911 | -0.01059 | 3 | SAP | 1, 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.54805 | -0.01001 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2459943.07514 | -0.00978 | 3 | SAP | 1, 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.50083 | -0.00976 | 4 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.91842 | -0.00972 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.60065 | -0.00971 | 2 | PDCSAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.65499 | -0.00967 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.64232 | -0.00947 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.62704 | -0.00940 | 4 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460292.05314 | -0.00904 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.70638 | -0.00894 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2459942.91750 | -0.00868 | 2 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459597.23553 | -0.00866 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.95453 | -0.00860 | 2 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.71471 | -0.00857 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.82397 | -0.00857 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.47166 | -0.00846 | 4 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460288.73080 | -0.00845 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460292.02050 | -0.00839 | 3 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.53208 | -0.00819 | 3 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.48555 | -0.00817 | 4 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.64857 | -0.00816 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.52535 | -0.00816 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.55916 | -0.00813 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.76702 | -0.00812 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459597.01470 | -0.00806 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.45204 | -0.00805 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460291.74410 | -0.00788 | 3 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460312.54649 | -0.00780 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000252912175-0249-s_lc.fits` | 2459943.49945 | -0.00779 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000000252912175-0218-s_lc.fits` | 2459596.93554 | -0.00758 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000252912175-0268-s_lc.fits` | 2460288.82734 | -0.00727 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460312.61176 | 5380 | 5827 | 726.3691 | 14 / 726 | 726.369, 242.123, 145.274, 103.767, 80.7077, 66.0336, 55.8745, 48.4246, 42.7276, 38.23, 34.589, 31.5813, 29.0548, 26.9026 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3797.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:36:44Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:36:46Z: TOI-3797.01 (TIC 252912175, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:36:49Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:36:50Z: TOI-3797.01 (Pl?); TOI-3797 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459586.2425: recovered, depth 5827 ± 310 ppm (catalogue 8430 ppm); BJD 2459603.8654: recovered, depth 6871 ± 309 ppm (catalogue 8430 ppm); BJD 2459938.7008: gap (catalogue 8430 ppm); BJD 2459956.3238: gap (catalogue 8430 ppm); BJD 2460291.1592: recovered, depth 5974 ± 316 ppm (catalogue 8430 ppm); BJD 2460308.7821: recovered, depth 6273 ± 296 ppm (catalogue 8430 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460312.6118, ΔT = 726.369 d, 14 of 726 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (726.369, 242.123, 145.274, 103.767, 80.7077, 66.0336, 55.8745, 48.4246, 42.7276, 38.23, 34.589, 31.5813 … d); duration likelihood under Gaia priors (circular orbits) peaks at 26.9 d (weight 0.22) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3797.01: Gaia DR3 978647193617500288 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3797.01: Teff 5863 K, R* 1.14 ± 0.09, M* 1.08 ± 0.11, ρ* 0.73 ± 0.19 ρ☉ (dwarf sequence, M_G 4.20, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3797.01: 11 Gaia neighbour(s) within 52.5", contamination 16.59%; depth 5827 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 978647197914457088, 8.9", ΔG 2.56); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2459596.6592 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+8.9, MOM_CENTR2 z=-10.3, POS_CORR1 z=+9.5, POS_CORR2 z=-13.7, SAP_BKG z=+18.0; BJD 2460312.6118 suspect: MOM_CENTR1 z=+13.5, MOM_CENTR2 z=+11.1, POS_CORR1 z=+13.9, POS_CORR2 z=+10.3, SAP_BKG z=+6.2 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 4 light curve × candidate pair(s); aliases supported: none; excluded: none; 53 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-3797.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3797.01: TOI-3797 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3797-01.yaml
python -m cygnus.multi report campaigns/toi-3797-01.yaml
```
