# T2 follow-up: toi-2952-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 5 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460020.3063: recovered, depth 13570 ± 585 ppm (catalogue 13750 ppm); BJD 2460031.0908: recovered, depth 12431 ± 600 ppm (catalogue 13750 ppm); BJD 2460041.8753: recovered, depth 13754 ± 686 ppm (catalogue 13750 ppm); BJD 2460052.6598: recovered, depth 13663 ± 606 ppm (catalogue 13750 ppm); BJD 2460063.4443: recovered, depth 13586 ± 592 ppm (catalogue 13750 ppm); BJD 2460074.2288: recovered, depth 13626 ± 679 ppm (catalogue 13750 ppm); BJD 2460085.0133: recovered, depth 13589 ± 685 ppm (catalogue 13750 ppm); BJD 2460095.7977: gap (catalogue 13750 ppm); BJD 2460721.2984: recovered, depth 13546 ± 611 ppm (catalogue 13750 ppm); BJD 2460732.0829: recovered, depth 13292 ± 659 ppm (catalogue 13750 ppm); BJD 2460742.8674: recovered, depth 12475 ± 635 ppm (catalogue 13750 ppm); BJD 2460753.6518: recovered, depth 12269 ± 651 ppm (catalogue 13750 ppm); BJD 2460764.4363: recovered, depth 12820 ± 597 ppm (catalogue 13750 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2460093.8219, ΔT = 73.528 d, 0 of 73 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2952.01: Gaia DR3 5223714464361866496 at 0.00" (propagated 2016.0 → J2015.5; 0.05" unpropagated, proper-motion shift 0.05") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2952.01: Teff 3529 K, R* 0.48 ± 0.04, M* 0.47 ± 0.05, ρ* 4.24 ± 1.10 ρ☉ (dwarf sequence, M_G 9.00, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2952.01: 29 Gaia neighbour(s) within 52.5", contamination 16.85%; depth 13570 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 5223711509424369408, 47.4", ΔG 3.43); a centroid test is needed |
| Pointing and quality census per event | failed | 5 persistent event(s), 0 clean; BJD 2460041.6056 suspect: MOM_CENTR1 z=+8.4, MOM_CENTR2 z=+6.9, POS_CORR1 z=+10.1, POS_CORR2 z=+11.1, SAP_BKG z=+9.7; BJD 2460093.8219 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+61.3; BJD 2460093.8803 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+73.8; BJD 2460093.8858 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+75.1 |
| Moving objects at screen-event epochs | passed | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2952.01: Gaia DR3 5223714464361866496   ROT                            P=None at 2.0" |
| Object-class guard (SIMBAD) | passed | TOI-2952.01: TOI-2952 otype PM* (star_or_other) at 1.5" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2460093.822: 238/269 event-free windows at least as deep; resolution 1/269, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2460093.822: 27/94 recovered |
