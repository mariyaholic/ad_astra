# T2 follow-up: toi-5615-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 6 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2459919.2529: recovered, depth 8903 ± 590 ppm (catalogue 13190 ppm); BJD 2459931.0202: partial, depth 8207 ± 573 ppm (catalogue 13190 ppm); BJD 2460295.8056: recovered, depth 9272 ± 594 ppm (catalogue 13190 ppm); BJD 2460307.5728: recovered, depth 8051 ± 640 ppm (catalogue 13190 ppm); BJD 2460319.3401: gap (catalogue 13190 ppm); BJD 2460331.1074: gap (catalogue 13190 ppm); BJD 2460342.8747: gap (catalogue 13190 ppm); BJD 2460354.6419: recovered, depth 9432 ± 800 ppm (catalogue 13190 ppm); BJD 2460366.4092: not recovered, depth 6386 ± 718 ppm (catalogue 13190 ppm); BJD 2460437.0128: recovered, depth 8448 ± 589 ppm (catalogue 13190 ppm); BJD 2460448.7801: not recovered, depth 7408 ± 659 ppm (catalogue 13190 ppm); BJD 2460460.5474: recovered, depth 7465 ± 716 ppm (catalogue 13190 ppm); BJD 2460472.3146: recovered, depth 8907 ± 663 ppm (catalogue 13190 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460317.6719, ΔT = 398.399 d, 4 of 398 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (398.399, 199.199, 99.5996, 56.9141 d); duration likelihood under Gaia priors (circular orbits) peaks at 56.9 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5615.01: Gaia DR3 1709550919731994240 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5615.01: Teff 6021 K, R* 1.14 ± 0.09, M* 1.08 ± 0.11, ρ* 0.73 ± 0.19 ρ☉ (dwarf sequence, M_G 4.21, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5615.01: 6 Gaia neighbour(s) within 52.5", contamination 13.29%; depth 8903 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 1709550541774872064, 30.5", ΔG 2.55); a centroid test is needed |
| Pointing and quality census per event | failed | 4 persistent event(s), 0 clean; BJD 2460289.6066 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+16.9; BJD 2460317.6719 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+10.4; BJD 2460339.4843 suspect: MOM_CENTR1 z=+8.4, POS_CORR1 z=+11.1; BJD 2460339.5162 suspect: MOM_CENTR1 z=+8.0, POS_CORR1 z=+10.1 |
| Moving objects at screen-event epochs | passed | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF failed: ) |
| Variable-catalogue collision (VSX) | passed | TOI-5615.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5615.01: UCAC4 851-012195 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E2) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2460339.484: 49/196 event-free windows at least as deep; resolution 1/196, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2460339.484: 45/67 recovered |
