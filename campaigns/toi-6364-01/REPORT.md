<!-- cygnus:generated-draft -->
# Known-object test, TOI-6364.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6364-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4857, calibrate_screen #4831, event_census #4838, fetch_independent #4842, fetch_products #4815, known_signal_recovery #4834, moving_objects #4841, period_aliases #4839, prior_art #4860, residual_screen #4837, stellar_context #4836, variability_guard #4858
- Runner finished (UTC): 2026-09-30T22:31:25Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6364.01 (BJD 2460287.9243: gap (catalogue 13915 ppm); BJD 2460443.2440: recovered, depth 9915 ± 767 ppm (catalogue 13915 ppm); BJD 2460469.1306: recovered, depth 12869 ± 761 ppm (catalogue 13915 ppm); BJD 2460624.4503: gap (catalogue 13915 ppm); BJD 2460650.3370: not recovered, depth 8484 ± 794 ppm (catalogue 13915 ppm)).
Outside the catalogued epoch the screen left 46 threshold entries forming **26 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460312.6017 matches the catalogued transit's depth (12256 vs 9915 ppm), 130.666 d later; 2 of 130 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6364.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 407517154 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 2.732086 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 78.899729 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459899.625001 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 25.8866192 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13915.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.737 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.2114 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | lightcurve | 73 | False | `2968567df4ca2e6e` | True |
| `tess2024114025118-s0078-0000000407517154-0273-s_lc.fits` | lightcurve | 78 | False | `c668ce823450a210` | True |
| `tess2024142205832-s0079-0000000407517154-0274-s_lc.fits` | lightcurve | 79 | False | `86872ed73bac3fb6` | True |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | lightcurve | 85 | False | `6905533385eac4b8` | True |
| `tess2024326142117-s0086-0000000407517154-0283-s_lc.fits` | lightcurve | 86 | False | `b0bbf179523f8ad3` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460287.92429 | gap | 0 | — | 13915 | — |
| `tess2024114025118-s0078-0000000407517154-0273-s_lc.fits` | 2460443.24400 | recovered | 112 | 9915 ± 767 | 13915 | 0.56 |
| `tess2024142205832-s0079-0000000407517154-0274-s_lc.fits` | 2460469.13062 | recovered | 113 | 12869 ± 761 | 13915 | 0.48 |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460624.45034 | gap | 0 | — | 13915 | — |
| `tess2024326142117-s0086-0000000407517154-0283-s_lc.fits` | 2460650.33696 | not_recovered | 113 | 8484 ± 794 | 13915 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2024114025118-s0078-0000000407517154-0273-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2024142205832-s0079-0000000407517154-0274-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024326142117-s0086-0000000407517154-0283-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460312.60168 | -0.02664 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460622.68622 | -0.01974 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.30894 | -0.03875 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.49088 | -0.03184 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.24644 | -0.03163 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.39783 | -0.03007 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.50754 | -0.02918 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.30061 | -0.02893 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.31380 | -0.02893 | 3 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.29019 | -0.02861 | 3 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.37283 | -0.02823 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.46588 | -0.02720 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.47282 | -0.02688 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.27699 | -0.02686 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.48671 | -0.02678 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.23186 | -0.02674 | 3 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.22422 | -0.02625 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.34297 | -0.02603 | 3 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.27283 | -0.02598 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460299.16172 | -0.02457 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000407517154-0268-s_lc.fits` | 2460312.64196 | -0.02290 | 2 | SAP | 1 | no |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460614.03746 | -0.02286 | 2 | PDCSAP | 3 | no |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460616.53611 | -0.01822 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460635.95438 | -0.01717 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460630.00434 | -0.01692 | 2 | SAP | 1, 3 | no |
| `tess2024300212641-s0085-0000000407517154-0282-s_lc.fits` | 2460616.34583 | -0.01689 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460312.60168 | 12256 | 9915 | 130.6658 | 2 / 130 | 130.666, 65.3329 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6364.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:31:11Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:31:14Z: TOI-6364.01 (TIC 407517154, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:31:18Z: Gaia DR3 564577681604547328 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:31:20Z: UCAC4 845-000264 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460287.9243: gap (catalogue 13915 ppm); BJD 2460443.2440: recovered, depth 9915 ± 767 ppm (catalogue 13915 ppm); BJD 2460469.1306: recovered, depth 12869 ± 761 ppm (catalogue 13915 ppm); BJD 2460624.4503: gap (catalogue 13915 ppm); BJD 2460650.3370: not recovered, depth 8484 ± 794 ppm (catalogue 13915 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460312.6017, ΔT = 130.666 d, 2 of 130 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (130.666, 65.3329 d); duration likelihood under Gaia priors (circular orbits) peaks at 65.3 d (weight 0.79) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6364.01: Gaia DR3 564577681604547328 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6364.01: Teff 5114 K, R* 0.79 ± 0.06, M* 0.83 ± 0.08, ρ* 1.71 ± 0.44 ρ☉ (dwarf sequence, M_G 5.80, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6364.01: 6 Gaia neighbour(s) within 52.5", contamination 29.76%; depth 9915 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 564577647244809856, 29.2", ΔG 2.06); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 1 clean; BJD 2460312.6017 suspect: MOM_CENTR2 z=-6.7, POS_CORR1 z=-8.8, POS_CORR2 z=-10.9 |
| Moving objects at screen-event epochs | inconclusive | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 6 light curve × candidate pair(s); aliases supported: none; excluded: none; 12 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-6364.01: Gaia DR3 564577681604547328    ROT                            P=None at 0.2" |
| Object-class guard (SIMBAD) | passed | TOI-6364.01: UCAC4 845-000264 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6364-01.yaml
python -m cygnus.multi report campaigns/toi-6364-01.yaml
```
