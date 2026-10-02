<!-- cygnus:generated-draft -->
# Known-object test, TOI-4259.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4259-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4354, calibrate_screen #4327, event_census #4332, fetch_independent #4338, fetch_products #4321, known_signal_recovery #4329, moving_objects #4334, period_aliases #4333, prior_art #4357, residual_screen #4331, stellar_context #4330, variability_guard #4355
- Runner finished (UTC): 2026-09-30T21:49:15Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4259.01 (BJD 2459963.4567: gap (catalogue 11334 ppm); BJD 2459972.4179: recovered, depth 6984 ± 375 ppm (catalogue 11334 ppm); BJD 2459981.3792: recovered, depth 4734 ± 459 ppm (catalogue 11334 ppm); BJD 2459990.3405: recovered, depth 3449 ± 593 ppm (catalogue 11334 ppm); BJD 2459999.3017: recovered, depth 7152 ± 422 ppm (catalogue 11334 ppm); BJD 2460008.2630: recovered, depth 5663 ± 422 ppm (catalogue 11334 ppm); BJD 2460698.2802: recovered, depth 1818 ± 373 ppm (catalogue 11334 ppm); BJD 2460707.2415: recovered, depth 3147 ± 429 ppm (catalogue 11334 ppm); BJD 2460716.2027: recovered, depth 3395 ± 403 ppm (catalogue 11334 ppm); BJD 2460725.1640: recovered, depth 326 ± 459 ppm (catalogue 11334 ppm); BJD 2460734.1253: recovered, depth 737 ± 401 ppm (catalogue 11334 ppm); BJD 2460743.0865: recovered, depth 1268 ± 411 ppm (catalogue 11334 ppm)).
Outside the catalogued epoch the screen left 49 threshold entries forming **29 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460005.4740 matches the catalogued transit's depth (5384 vs 6984 ppm), 33.057 d later; 0 of 33 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4259.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 268643535 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 117.330048 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -51.261706 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459963.456678 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 8.9612626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11333.9389745 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.8325932 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.9452 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-06 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | lightcurve | 61 | True | `966f4469e2e8abd0` | True |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | lightcurve | 62 | False | `e470cebe318723c0` | True |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | lightcurve | 88 | False | `02d01afdfcab0a7a` | True |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | lightcurve | 89 | False | `6f7c959192b62a45` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | 2459963.45668 | gap | 0 | — | 11334 | — |
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | 2459972.41794 | recovered | 55 | 6984 ± 375 | 11334 | -0.02 |
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | 2459981.37920 | recovered | 54 | 4734 ± 459 | 11334 | 0.03 |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459990.34047 | recovered | 55 | 3449 ± 593 | 11334 | 0.01 |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459999.30173 | recovered | 55 | 7152 ± 422 | 11334 | 0.07 |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460008.26299 | recovered | 55 | 5663 ± 422 | 11334 | -0.00 |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460698.28021 | recovered | 55 | 1818 ± 373 | 11334 | 1.01 |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460707.24147 | recovered | 55 | 3147 ± 429 | 11334 | 1.10 |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460716.20274 | recovered | 55 | 3395 ± 403 | 11334 | 0.84 |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | 2460725.16400 | recovered | 55 | 326 ± 459 | 11334 | 1.12 |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | 2460734.12526 | recovered | 55 | 737 ± 401 | 11334 | 1.27 |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | 2460743.08652 | recovered | 55 | 1268 ± 411 | 11334 | 1.21 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000268643535-0250-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025042113628-s0089-0000000268643535-0286-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460005.47402 | -0.01443 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.56147 | -0.01409 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.86702 | -0.01481 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.47120 | -0.01409 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.27675 | -0.01325 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460005.41013 | -0.01317 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.74341 | -0.01305 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.58936 | -0.01284 | 2 | PDCSAP | 1, 2 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2460009.58369 | -0.01268 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.61853 | -0.01264 | 2 | PDCSAP | 1, 2 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.67270 | -0.01253 | 2 | PDCSAP | 2 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.46992 | -0.01228 | 2 | PDCSAP | 1, 2 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.53936 | -0.01176 | 2 | PDCSAP | 1, 2 | no |
| `tess2023043185947-s0062-0000000268643535-0254-s_lc.fits` | 2459989.66853 | -0.01131 | 2 | PDCSAP | 1, 2 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.99549 | -0.01123 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.67048 | -0.01067 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.86493 | -0.00995 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460712.00104 | -0.00983 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.91285 | -0.00957 | 3 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.67743 | -0.00956 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460692.72722 | -0.00950 | 2 | PDCSAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460704.66070 | -0.00941 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.82604 | -0.00936 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460693.43139 | -0.00931 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460716.02189 | -0.00911 | 2 | PDCSAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460711.70590 | -0.00890 | 5 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460693.35778 | -0.00886 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460693.35084 | -0.00862 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000268643535-0285-s_lc.fits` | 2460717.27189 | -0.00835 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460005.47402 | 5384 | 6984 | 33.0570 | 0 / 33 |  |
| 2460009.56147 | 5894 | 6984 | 37.1444 | 0 / 37 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4259.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:49:07Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:49:10Z: TOI-4259.01 (TIC 268643535, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:49:12Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:49:13Z: TOI-4259.01 (Pl?); TOI-4259 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459963.4567: gap (catalogue 11334 ppm); BJD 2459972.4179: recovered, depth 6984 ± 375 ppm (catalogue 11334 ppm); BJD 2459981.3792: recovered, depth 4734 ± 459 ppm (catalogue 11334 ppm); BJD 2459990.3405: recovered, depth 3449 ± 593 ppm (catalogue 11334 ppm); BJD 2459999.3017: recovered, depth 7152 ± 422 ppm (catalogue 11334 ppm); BJD 2460008.2630: recovered, depth 5663 ± 422 ppm (catalogue 11334 ppm); BJD 2460698.2802: recovered, depth 1818 ± 373 ppm (catalogue 11334 ppm); BJD 2460707.2415: recovered, depth 3147 ± 429 ppm (catalogue 11334 ppm); BJD 2460716.2027: recovered, depth 3395 ± 403 ppm (catalogue 11334 ppm); BJD 2460725.1640: recovered, depth 326 ± 459 ppm (catalogue 11334 ppm); BJD 2460734.1253: recovered, depth 737 ± 401 ppm (catalogue 11334 ppm); BJD 2460743.0865: recovered, depth 1268 ± 411 ppm (catalogue 11334 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2460005.4740, ΔT = 33.057 d, 0 of 33 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4259.01: Gaia DR3 5492893117202616832 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4259.01: Teff 5466 K, R* 1.06 ± 0.09, M* 1.03 ± 0.10, ρ* 0.86 ± 0.22 ρ☉ (dwarf sequence, M_G 4.45, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4259.01: 23 Gaia neighbour(s) within 52.5", contamination 18.47%; depth 6984 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 5492893052782309888, 35.2", ΔG 2.22); a centroid test is needed |
| Pointing and quality census per event | passed | 2 persistent event(s), 2 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-4259.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4259.01: TOI-4259 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4259-01.yaml
python -m cygnus.multi report campaigns/toi-4259-01.yaml
```
