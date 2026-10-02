<!-- cygnus:generated-draft -->
# Known-object test, TOI-2876.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2876-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5197, calibrate_screen #5180, event_census #5186, fetch_independent #5195, fetch_products #5176, known_signal_recovery #5182, moving_objects #5188, period_aliases #5187, prior_art #5201, residual_screen #5185, stellar_context #5183, variability_guard #5198
- Runner finished (UTC): 2026-09-30T23:06:48Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2876.01 (BJD 2460665.7811: recovered, depth 4581 ± 473 ppm (catalogue 9530 ppm); BJD 2460672.0808: recovered, depth 7045 ± 421 ppm (catalogue 9530 ppm); BJD 2460678.3804: gap (catalogue 9530 ppm); BJD 2460684.6800: recovered, depth 8047 ± 434 ppm (catalogue 9530 ppm)).
Outside the catalogued epoch the screen left 20 threshold entries forming **5 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460679.5101 matches the catalogued transit's depth (3371 vs 4581 ppm), 13.721 d later; 1 of 13 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2876.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 10827386 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 110.247353 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -21.114638 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459248.364238 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 6.2996307 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9530.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.918 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7038 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | lightcurve | 87 | False | `32f2a81856c5b5af` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460665.78115 | recovered | 57 | 4581 ± 473 | 9530 | 0.19 |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460672.08078 | recovered | 58 | 7045 ± 421 | 9530 | 0.17 |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460678.38041 | gap | 0 | — | 9530 | — |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460684.68004 | recovered | 57 | 8047 ± 434 | 9530 | 0.12 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460679.51009 | -0.01172 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460676.21976 | -0.00928 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460679.34481 | -0.01143 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460679.56287 | -0.00979 | 2 | PDCSAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000010827386-0284-s_lc.fits` | 2460688.60047 | -0.00892 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460679.51009 | 3371 | 4581 | 13.7212 | 1 / 13 | 13.7212 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2876.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:06:36Z: TOI-2876 b (host TOI-2876)
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:06:40Z: TOI-2876.01 (TIC 10827386, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T23:06:43Z
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T23:06:45Z: Gaia DR3 2929750922377143424 (*); TOI-2876 (*); TOI-2876.01 (Pl)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460665.7811: recovered, depth 4581 ± 473 ppm (catalogue 9530 ppm); BJD 2460672.0808: recovered, depth 7045 ± 421 ppm (catalogue 9530 ppm); BJD 2460678.3804: gap (catalogue 9530 ppm); BJD 2460684.6800: recovered, depth 8047 ± 434 ppm (catalogue 9530 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460679.5101, ΔT = 13.721 d, 1 of 13 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (13.7212 d); duration likelihood under Gaia priors (circular orbits) peaks at 13.7 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2876.01: Gaia DR3 2929750922377138816 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2876.01: Teff 5135 K, R* 0.82 ± 0.07, M* 0.88 ± 0.09, ρ* 1.60 ± 0.42 ρ☉ (dwarf sequence, M_G 5.52, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2876.01: 59 Gaia neighbour(s) within 52.5", contamination 28.23%; depth 4581 ppm (measured depth of the recovered catalogued transit); 9 could produce it if fully eclipsed (brightest 2929750922377143424, 23.4", ΔG 2.11); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460676.2198 suspect: manual exclude (within ±0.25 d), POS_CORR2 z=-7.3, SAP_BKG z=+341.1; BJD 2460679.5101 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+22.7 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 1 light curve × candidate pair(s); aliases supported: none; excluded: none; 1 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-2876.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2876.01: TOI-2876 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2876-01.yaml
python -m cygnus.multi report campaigns/toi-2876-01.yaml
```
