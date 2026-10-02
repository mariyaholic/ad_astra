<!-- cygnus:generated-draft -->
# Known-object test, TOI-6347.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6347-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5199, calibrate_screen #5184, event_census #5192, fetch_independent #5196, fetch_products #5177, known_signal_recovery #5189, moving_objects #5194, period_aliases #5193, prior_art #5202, residual_screen #5191, stellar_context #5190, variability_guard #5200
- Runner finished (UTC): 2026-09-30T23:06:48Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6347.01 (BJD 2460639.4725: gap (catalogue 5042 ppm); BJD 2460643.4057: recovered, depth 2030 ± 210 ppm (catalogue 5042 ppm); BJD 2460647.3390: not recovered, depth 2300 ± 191 ppm (catalogue 5042 ppm); BJD 2460651.2723: gap (catalogue 5042 ppm); BJD 2460655.2055: gap (catalogue 5042 ppm); BJD 2460659.1388: not recovered, depth 1600 ± 191 ppm (catalogue 5042 ppm)).
Outside the catalogued epoch the screen left 13 threshold entries forming **4 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460641.1539 matches the catalogued transit's depth (3865 vs 2030 ppm), 2.313 d later; 0 of 2 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6347.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 467690903 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 61.169664 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 34.186114 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459935.419244 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.9332583 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5042.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.438 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.2367 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | lightcurve | 86 | False | `6bc084ad99736951` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460639.47248 | gap | 0 | — | 5042 | — |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460643.40574 | recovered | 133 | 2030 ± 210 | 5042 | 1.47 |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460647.33900 | not_recovered | 133 | 2300 ± 191 | 5042 | — |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460651.27225 | gap | 0 | — | 5042 | — |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460655.20551 | gap | 0 | — | 5042 | — |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460659.13877 | not_recovered | 133 | 1600 ± 191 | 5042 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460641.15390 | -0.01353 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460641.16987 | -0.01230 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460641.16571 | -0.00818 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000467690903-0283-s_lc.fits` | 2460649.36566 | -0.00795 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460641.15390 | 3865 | 2030 | 2.3132 | 0 / 2 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6347.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:06:37Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:06:40Z: TOI-6347.01 (TIC 467690903, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T23:06:43Z: Gaia DR3 170890362096387200 (type E, P 0.72927 d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:06:45Z: Gaia DR3 170890362096387200 (EB*); TYC 2366-2465-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460639.4725: gap (catalogue 5042 ppm); BJD 2460643.4057: recovered, depth 2030 ± 210 ppm (catalogue 5042 ppm); BJD 2460647.3390: not recovered, depth 2300 ± 191 ppm (catalogue 5042 ppm); BJD 2460651.2723: gap (catalogue 5042 ppm); BJD 2460655.2055: gap (catalogue 5042 ppm); BJD 2460659.1388: not recovered, depth 1600 ± 191 ppm (catalogue 5042 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460641.1539, ΔT = 2.313 d, 0 of 2 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6347.01: Gaia DR3 170890362096388224 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6347.01: dwarf priors not applied — 1.38 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6347.01: 12 Gaia neighbour(s) within 52.5", contamination 1.04%; depth 2030 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 170890362096387200, 10.0", ΔG 5.98); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460641.1539 suspect: manual exclude (in event), scattered light 2 (in event), SAP_BKG z=+97.4 |
| Moving objects at screen-event epochs | not_tested | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | failed | TOI-6347.01: Gaia DR3 170890362096387200    E                              P=0.72927 at 10.0" |
| Object-class guard (SIMBAD) | passed | TOI-6347.01: TYC 2366-2465-1 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6347-01.yaml
python -m cygnus.multi report campaigns/toi-6347-01.yaml
```
