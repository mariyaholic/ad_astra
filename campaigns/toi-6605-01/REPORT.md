<!-- cygnus:generated-draft -->
# Known-object test, TOI-6605.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6605-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4861, calibrate_screen #4843, event_census #4853, fetch_independent #4859, fetch_products #4835, known_signal_recovery #4846, moving_objects #4856, period_aliases #4855, prior_art #4863, residual_screen #4849, stellar_context #4847, variability_guard #4862
- Runner finished (UTC): 2026-09-30T22:31:41Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6605.01 (BJD 2461046.4075: not recovered, depth 3501 ± 1987 ppm (catalogue 14968 ppm); BJD 2461058.7056: gap (catalogue 14968 ppm); BJD 2461071.0038: not recovered, depth 19287 ± 1901 ppm (catalogue 14968 ppm); BJD 2461083.3019: recovered, depth 22145 ± 1440 ppm (catalogue 14968 ppm); BJD 2461095.6000: not recovered, depth 15997 ± 1372 ppm (catalogue 14968 ppm); BJD 2461107.8981: not recovered, depth 17876 ± 1319 ppm (catalogue 14968 ppm); BJD 2461120.1963: not recovered, depth 7117 ± 4547 ppm (catalogue 14968 ppm); BJD 2461132.4944: not recovered, depth 15266 ± 1651 ppm (catalogue 14968 ppm); BJD 2461144.7925: recovered, depth 20814 ± 1665 ppm (catalogue 14968 ppm)).
Outside the catalogued epoch the screen left 18 threshold entries forming **6 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461151.2236 matches the catalogued transit's depth (13347 vs 22145 ppm), 67.921 d later; 1 of 67 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6605.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 263207857 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 230.389105 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -66.264426 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460087.153755 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 12.2981251 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14968.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.98 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.4442 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | lightcurve | 99 | False | `2097c6356a6dbd4b` | True |
| `tess2026033082000-s0100-0000000263207857-0302-s_lc.fits` | lightcurve | 100 | False | `8fe24a4529eaa183` | True |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | lightcurve | 101 | False | `c684e0403ab7932c` | True |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | lightcurve | 102 | False | `2a34000d4261d421` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | 2461046.40751 | not_recovered | 119 | 3501 ± 1987 | 14968 | — |
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | 2461058.70564 | gap | 0 | — | 14968 | — |
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | 2461071.00376 | not_recovered | 120 | 19287 ± 1901 | 14968 | — |
| `tess2026033082000-s0100-0000000263207857-0302-s_lc.fits` | 2461083.30189 | recovered | 119 | 22145 ± 1440 | 14968 | 0.02 |
| `tess2026033082000-s0100-0000000263207857-0302-s_lc.fits` | 2461095.60001 | not_recovered | 120 | 15997 ± 1372 | 14968 | — |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 2461107.89814 | not_recovered | 120 | 17876 ± 1319 | 14968 | — |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 2461120.19626 | not_recovered | 13 | 7117 ± 4547 | 14968 | — |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2461132.49439 | not_recovered | 120 | 15266 ± 1651 | 14968 | — |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2461144.79251 | recovered | 117 | 20814 ± 1665 | 14968 | -0.04 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2026005125623-s0099-0000000263207857-0300-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026033082000-s0100-0000000263207857-0302-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2461151.22360 | -0.05653 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2461127.25081 | -0.05143 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 2461119.86840 | -0.02125 | 3 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 2461119.80451 | -0.02061 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000263207857-0303-s_lc.fits` | 2461119.63783 | -0.01801 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000263207857-0304-s_lc.fits` | 2461127.25636 | -0.01698 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461151.22360 | 13347 | 22145 | 67.9209 | 1 / 67 | 67.9209 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6605.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:31:30Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:31:33Z: TOI-6605.01 (TIC 263207857, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:31:35Z: Gaia DR3 5824848081500823552 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T22:31:37Z: Gaia DR3 5824848841741472512 (*); Gaia DR2 5824848841741473024 (*); UCAC4 119-117477 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2461046.4075: not recovered, depth 3501 ± 1987 ppm (catalogue 14968 ppm); BJD 2461058.7056: gap (catalogue 14968 ppm); BJD 2461071.0038: not recovered, depth 19287 ± 1901 ppm (catalogue 14968 ppm); BJD 2461083.3019: recovered, depth 22145 ± 1440 ppm (catalogue 14968 ppm); BJD 2461095.6000: not recovered, depth 15997 ± 1372 ppm (catalogue 14968 ppm); BJD 2461107.8981: not recovered, depth 17876 ± 1319 ppm (catalogue 14968 ppm); BJD 2461120.1963: not recovered, depth 7117 ± 4547 ppm (catalogue 14968 ppm); BJD 2461132.4944: not recovered, depth 15266 ± 1651 ppm (catalogue 14968 ppm); BJD 2461144.7925: recovered, depth 20814 ± 1665 ppm (catalogue 14968 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2461151.2236, ΔT = 67.921 d, 1 of 67 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (67.9209 d); duration likelihood under Gaia priors (circular orbits) peaks at 67.9 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6605.01: Gaia DR3 5824848841741473024 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6605.01: Teff 5147 K, R* 0.87 ± 0.07, M* 0.91 ± 0.09, ρ* 1.38 ± 0.36 ρ☉ (dwarf sequence, M_G 5.27, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6605.01: 205 Gaia neighbour(s) within 52.5", contamination 80.09%; depth 22145 ppm (measured depth of the recovered catalogued transit); 10 could produce it if fully eclipsed (brightest 5824848841741486848, 37.0", ΔG 0.95); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2461127.2508 suspect: scattered light 2 (in event), argabrightening (within ±0.25 d), earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), POS_CORR2 z=+5.0, SAP_BKG z=+88.0; BJD 2461151.2236 suspect: scattered light 2 (in event), manual exclude (within ±0.25 d), POS_CORR2 z=+7.8, SAP_BKG z=+1218.2 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6605.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6605.01: Gaia DR2 5824848841741473024 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6605-01.yaml
python -m cygnus.multi report campaigns/toi-6605-01.yaml
```
