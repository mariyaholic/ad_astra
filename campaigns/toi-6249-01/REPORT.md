<!-- cygnus:generated-draft -->
# Known-object test, TOI-6249.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6249-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5224, calibrate_screen #5216, event_census #5220, fetch_independent #5223, fetch_products #5215, known_signal_recovery #5217, moving_objects #5222, period_aliases #5221, prior_art #5226, residual_screen #5219, stellar_context #5218, variability_guard #5225
- Runner finished (UTC): 2026-10-02T06:16:05Z

## Bottom line

Positive control **failed**: BJD 2458853.4700: not recovered, depth 1392 ± 57 ppm (catalogue 1690 ppm); BJD 2459945.4723: not recovered, depth 1357 ± 52 ppm (catalogue 1690 ppm).
Outside the catalogued epoch the screen left 103 threshold entries forming **25 distinct event(s)**, **19 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6249.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 456260074 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 101.492034 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 66.890644 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458853.470005 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1092.002299 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 1689.5997267 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.604929 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.0449 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-06-05 12:03:22 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019357164649-s0020-0000000456260074-0165-s_lc.fits` | lightcurve | 20 | True | `697792fe08e25673` | False |
| `tess2022357055054-s0060-0000000456260074-0249-s_lc.fits` | lightcurve | 60 | False | `7aa7cc7c82d8aad2` | False |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | lightcurve | 73 | False | `6d0dd10278ee1754` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019357164649-s0020-0000000456260074-0165-s_lc.fits` | 2458853.47001 | not_recovered | 168 | 1392 ± 57 | 1690 | — |
| `tess2022357055054-s0060-0000000456260074-0249-s_lc.fits` | 2459945.47230 | not_recovered | 168 | 1357 ± 52 | 1690 | — |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | — | epoch not in this light curve | — | — | 1690 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019357164649-s0020-0000000456260074-0165-s_lc.fits` | — | False |  |  |
| `tess2022357055054-s0060-0000000456260074-0249-s_lc.fits` | — | False |  |  |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.93148 | -0.00334 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.83425 | -0.00320 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460293.00231 | -0.00279 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.95092 | -0.00250 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.94259 | -0.00234 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.97176 | -0.00232 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.93703 | -0.00231 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.92245 | -0.00226 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.82731 | -0.00224 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.91342 | -0.00220 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.99815 | -0.00220 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.85439 | -0.00215 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460308.70521 | -0.00215 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.88842 | -0.00214 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.84953 | -0.00207 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.86481 | -0.00207 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460308.73854 | -0.00206 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.89675 | -0.00195 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.98287 | -0.00188 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460291.87590 | -0.00340 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460312.48157 | -0.00252 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.87384 | -0.00203 | 3 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460292.90370 | -0.00197 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460293.15787 | -0.00190 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023341045131-s0073-0000000456260074-0268-s_lc.fits` | 2460291.55645 | -0.00182 | 2 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6249.01**

- NASA_Exoplanet_Archive (done, 2026-10-02): no match in NASA_Exoplanet_Archive within 30" as of 2026-10-02T06:15:58Z
- TESS_TOI (done, 2026-10-02): 2 match(es) in TESS_TOI within 30" as of 2026-10-02T06:16:00Z: TOI-6249.01 (TIC 456260074, disposition PC); TOI-6249.02 (TIC 456260074, disposition PC)
- VSX (done, 2026-10-02): no match in VSX within 30" as of 2026-10-02T06:16:02Z
- SIMBAD (done, 2026-10-02): 1 match(es) in SIMBAD within 30" as of 2026-10-02T06:16:04Z: TOI-6249 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2458853.4700: not recovered, depth 1392 ± 57 ppm (catalogue 1690 ppm); BJD 2459945.4723: not recovered, depth 1357 ± 52 ppm (catalogue 1690 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (none, none, ≤2.5; ≤ 0 persistent null events outside the veto); 2 light curve(s) have no usable cadence outside the veto (the veto window covers all of the data; no k* exists there) |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6249.01: Gaia DR3 1102667161725388160 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6249.01: Teff 4885 K, R* 0.75 ± 0.06, M* 0.77 ± 0.08, ρ* 1.84 ± 0.48 ρ☉ (dwarf sequence, M_G 6.25, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6249.01: 6 Gaia neighbour(s) within 52.5", contamination 5.34%; depth 1690 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 1102667088709563648, 46.2", ΔG 3.99); a centroid test is needed |
| Pointing and quality census per event | failed | 19 persistent event(s), 8 clean; BJD 2460292.8273 suspect: MOM_CENTR1 z=+5.3, SAP_BKG z=+10.5; BJD 2460292.8343 suspect: SAP_BKG z=+10.2; BJD 2460292.8495 suspect: SAP_BKG z=+9.8; BJD 2460292.8544 suspect: SAP_BKG z=+9.0 |
| Moving objects at screen-event epochs | inconclusive | 19 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6249.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6249.01: TOI-6249 otype * (star_or_other) at 0.5" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6249-01.yaml
python -m cygnus.multi report campaigns/toi-6249-01.yaml
```
