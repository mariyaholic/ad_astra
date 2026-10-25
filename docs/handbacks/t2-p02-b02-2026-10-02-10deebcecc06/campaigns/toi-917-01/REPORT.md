# T2 follow-up: toi-917-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 5 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2459104.5631: recovered, depth 3722 ± 202 ppm (catalogue 5967 ppm); BJD 2459130.9757: recovered, depth 3810 ± 199 ppm (catalogue 5967 ppm); BJD 2460187.4818: recovered, depth 2805 ± 196 ppm (catalogue 5967 ppm); BJD 2460927.0361: recovered, depth 3847 ± 324 ppm (catalogue 5967 ppm); BJD 2460953.4487: recovered, depth 4128 ± 199 ppm (catalogue 5967 ppm); BJD 2460979.8614: recovered, depth 4489 ± 204 ppm (catalogue 5967 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459141.6075, ΔT = 37.051 d, 0 of 37 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-917.01: Gaia DR3 4723782641924962688 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-917.01: dwarf priors not applied — 1.84 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-917.01: 5 Gaia neighbour(s) within 52.5", contamination 9.57%; depth 3722 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 4723782538845747712, 37.6", ΔG 2.76); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2459141.6075 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), SAP_BKG z=+25.7 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-917.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-917.01: TOI-917 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | failed | BJD 2459141.608: 234/279 event-free windows at least as deep; resolution 1/279, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2459141.608: 29/94 recovered |
