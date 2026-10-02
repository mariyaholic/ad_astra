<!-- cygnus:generated-draft -->
# Known-object test, TOI-2248.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2248-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4583, calibrate_screen #4546, event_census #4556, fetch_independent #4572, fetch_products #4532, known_signal_recovery #4548, moving_objects #4569, period_aliases #4557, prior_art #4586, residual_screen #4553, stellar_context #4551, variability_guard #4584
- Runner finished (UTC): 2026-09-30T22:02:31Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2248.01 (BJD 2460077.7065: recovered, depth 5501 ± 151 ppm (catalogue 3710 ppm); BJD 2460015.5440: not recovered, depth -331 ± 156 ppm (catalogue 3710 ppm)).
Outside the catalogued epoch the screen left 231 threshold entries forming **110 distinct event(s)**, **14 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460013.7633 matches the catalogued transit's depth (3122 vs 5501 ppm), 63.925 d later; 1 of 63 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2248.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 179580045 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 80.624017 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -70.254329 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460077.706461 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 62.1624516 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 3710.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.319 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.4653 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-04-25 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | lightcurve | 65 | True | `fc6a7dac86e3bddf` | True |
| `tess2023018032328-s0061-0000000179580045-0250-s_lc.fits` | lightcurve | 61 | False | `5cc9ea0f7abef6f4` | True |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | lightcurve | 62 | False | `a9c474c56d6fb89f` | True |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | lightcurve | 63 | False | `9ff9f9edee3f0003` | True |
| `tess2023096110322-s0064-0000000179580045-0257-s_lc.fits` | lightcurve | 64 | False | `fa1090639e2239af` | True |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | lightcurve | 66 | False | `bc12fe4559e2e9a3` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460077.70646 | recovered | 129 | 5501 ± 151 | 3710 | -0.42 |
| `tess2023018032328-s0061-0000000179580045-0250-s_lc.fits` | — | epoch not in this light curve | — | — | 3710 | — |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 3710 | — |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460015.54401 | not_recovered | 106 | -331 ± 156 | 3710 | — |
| `tess2023096110322-s0064-0000000179580045-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 3710 | — |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 3710 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023018032328-s0061-0000000179580045-0250-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023096110322-s0064-0000000179580045-0257-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 10000, 4h: 5000, 8h: 5000 |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.41764 | -0.00708 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.82237 | -0.00647 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.83001 | -0.00626 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | 2460100.92928 | -0.00591 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000179580045-0260-s_lc.fits` | 2460123.47939 | -0.00583 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.76334 | -0.00579 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460040.75519 | -0.00573 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.87168 | -0.00572 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.93696 | -0.00545 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.88696 | -0.00539 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.71612 | -0.00522 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460011.18000 | -0.00488 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460028.28843 | -0.00485 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460037.40100 | -0.00476 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.89265 | -0.00700 | 4 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.80653 | -0.00698 | 5 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.78626 | -0.00684 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.87876 | -0.00678 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.25414 | -0.00675 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.31348 | -0.00668 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.88709 | -0.00662 | 5 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.33153 | -0.00653 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.85350 | -0.00634 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.86670 | -0.00627 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.29858 | -0.00626 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.84997 | -0.00619 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460006.94805 | -0.00614 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.86209 | -0.00614 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460007.14666 | -0.00607 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.84656 | -0.00606 | 3 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460006.96471 | -0.00603 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.83709 | -0.00591 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.82876 | -0.00590 | 4 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.40792 | -0.00589 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.73014 | -0.00578 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.82042 | -0.00577 | 4 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.78292 | -0.00571 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.97225 | -0.00571 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.81108 | -0.00568 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.40142 | -0.00568 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.90792 | -0.00562 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.76524 | -0.00558 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.11486 | -0.00558 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.84959 | -0.00555 | 4 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.88140 | -0.00555 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.27723 | -0.00553 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.84403 | -0.00547 | 4 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.77042 | -0.00546 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.89890 | -0.00546 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.39473 | -0.00545 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.81802 | -0.00544 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.37042 | -0.00543 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.86196 | -0.00541 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460007.25221 | -0.00540 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.65559 | -0.00533 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.91045 | -0.00533 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.81948 | -0.00529 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.87390 | -0.00526 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.34750 | -0.00525 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.74820 | -0.00524 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.44681 | -0.00523 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460007.33971 | -0.00518 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.91209 | -0.00516 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.74112 | -0.00512 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.89163 | -0.00510 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.75767 | -0.00508 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.78330 | -0.00504 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.70653 | -0.00503 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.71126 | -0.00503 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.95281 | -0.00502 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.74997 | -0.00500 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.83886 | -0.00500 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.83475 | -0.00497 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.73071 | -0.00496 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.10414 | -0.00488 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.66057 | -0.00488 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.27914 | -0.00487 | 8 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.87086 | -0.00487 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.76670 | -0.00486 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.33614 | -0.00485 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.93153 | -0.00485 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.37736 | -0.00483 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460035.47043 | -0.00482 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.57181 | -0.00481 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.78336 | -0.00481 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.26392 | -0.00480 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.32598 | -0.00478 | 4 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.79390 | -0.00478 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460089.88059 | -0.00477 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.60571 | -0.00476 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.38431 | -0.00475 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460006.70499 | -0.00475 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.25362 | -0.00475 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.40236 | -0.00474 | 4 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460007.02582 | -0.00473 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.70362 | -0.00473 | 4 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460039.89962 | -0.00465 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460040.49824 | -0.00465 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.77862 | -0.00464 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.64959 | -0.00463 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.24303 | -0.00461 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.31386 | -0.00450 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460006.89110 | -0.00449 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000179580045-0254-s_lc.fits` | 2460013.89668 | -0.00446 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460040.59616 | -0.00445 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.90376 | -0.00441 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460040.39963 | -0.00433 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460083.26247 | -0.00432 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000179580045-0259-s_lc.fits` | 2460082.88608 | -0.00432 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000179580045-0255-s_lc.fits` | 2460033.34264 | -0.00418 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460013.76334 | 3122 | 5501 | 63.9255 | 1 / 63 | 63.9255 |
| 2460013.82237 | 3273 | 5501 | 63.8664 | 1 / 63 | 63.8664 |
| 2460013.83001 | 3276 | 5501 | 63.8588 | 1 / 63 | 63.8588 |
| 2460013.87168 | 3031 | 5501 | 63.8171 | 1 / 63 | 63.8171 |
| 2460013.88696 | 2751 | 5501 | 63.8019 | 1 / 63 | 63.8019 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2248.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:02:20Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:02:22Z: TOI-2248.01 (TIC 179580045, disposition PC)
- VSX (done, 2026-09-30): 2 match(es) in VSX within 30" as of 2026-09-30T22:02:25Z: Gaia DR3 4657936734607265280 (type E, P 0.90052 d); Gaia DR3 4657936768966921984 (type SR|M, P 231.0 d)
- SIMBAD (done, 2026-09-30): 8 match(es) in SIMBAD within 30" as of 2026-09-30T22:02:27Z: OGLE LMC-LPV-47528 (LP*); Gaia DR3 4657936734607265280 (EB*); HD 269454 (*); EROS2-star lm001-6m-24386 (LP*); OGLE LMC-SC21 183402 (RR*); TIC 179580052 (*); OGLE LMC-LPV-47373 (LP*); OGLE LMC-LPV-47282 (LP*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460077.7065: recovered, depth 5501 ± 151 ppm (catalogue 3710 ppm); BJD 2460015.5440: not recovered, depth -331 ± 156 ppm (catalogue 3710 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 0%, 10%, 40%, 30%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2460013.7633, ΔT = 63.925 d, 1 of 63 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (63.9255 d); duration likelihood under Gaia priors (circular orbits) peaks at 63.9 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2248.01: Gaia DR3 4657936807635403648 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2248.01: Teff 6716 K, R* 1.63 ± 0.13, M* 1.47 ± 0.15, ρ* 0.34 ± 0.09 ρ☉ (dwarf sequence, M_G 2.85, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2248.01: 497 Gaia neighbour(s) within 52.5", contamination 17.82%; depth 5501 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 4657936768966921984, 10.1", ΔG 5.00); a centroid test is needed |
| Pointing and quality census per event | failed | 14 persistent event(s), 3 clean; BJD 2460013.7161 suspect: manual exclude (in event), SAP_BKG z=+58.7; BJD 2460013.7633 suspect: manual exclude (in event), POS_CORR1 z=-6.2, SAP_BKG z=+109.1; BJD 2460013.8224 suspect: manual exclude (in event), MOM_CENTR1 z=-5.2, POS_CORR1 z=-7.4, SAP_BKG z=+139.0; BJD 2460013.8300 suspect: manual exclude (in event), MOM_CENTR1 z=-5.3, POS_CORR1 z=-7.5, SAP_BKG z=+145.0 |
| Moving objects at screen-event epochs | passed | 14 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2248.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2248.01: HD 269454 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2248-01.yaml
python -m cygnus.multi report campaigns/toi-2248-01.yaml
```
