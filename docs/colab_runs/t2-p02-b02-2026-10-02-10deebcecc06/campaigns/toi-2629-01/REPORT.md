# T2 follow-up: toi-2629-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 6 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460134.4121: not recovered, depth 8805 ± 537 ppm (catalogue 11370 ppm); BJD 2460145.8978: not recovered, depth 7908 ± 520 ppm (catalogue 11370 ppm); BJD 2460157.3835: recovered, depth 8281 ± 514 ppm (catalogue 11370 ppm); BJD 2460168.8691: recovered, depth 6576 ± 535 ppm (catalogue 11370 ppm); BJD 2460180.3548: gap (catalogue 11370 ppm); BJD 2460191.8405: recovered, depth 8182 ± 556 ppm (catalogue 11370 ppm); BJD 2460203.3262: partial, depth 8273 ± 502 ppm (catalogue 11370 ppm); BJD 2460858.0102: recovered, depth 9524 ± 566 ppm (catalogue 11370 ppm); BJD 2460869.4959: gap (catalogue 11370 ppm); BJD 2460880.9816: not recovered, depth -2185 ± 886 ppm (catalogue 11370 ppm); BJD 2460892.4673: recovered, depth 8909 ± 482 ppm (catalogue 11370 ppm); BJD 2460903.9530: recovered, depth 7050 ± 487 ppm (catalogue 11370 ppm); BJD 2460915.4386: recovered, depth 9226 ± 473 ppm (catalogue 11370 ppm); BJD 2460926.9243: recovered, depth 9795 ± 557 ppm (catalogue 11370 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2460857.1918, ΔT = 699.804 d, 13 of 699 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (699.804, 349.902, 233.268, 174.951, 139.961, 116.634, 99.972, 87.4755, 77.756, 69.9804, 63.6186, 58.317 … d); duration likelihood under Gaia priors (circular orbits) peaks at 50 d (weight 0.21) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 20.4″ from the out-of-transit centroid (0.4σ bootstrap); 18.1″ from the catalogue position; 14% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2629.01: Gaia DR3 4647036180550103424 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2629.01: Teff 5777 K, R* 1.23 ± 0.10, M* 1.18 ± 0.12, ρ* 0.64 ± 0.17 ρ☉ (dwarf sequence, M_G 3.88, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2629.01: 4 Gaia neighbour(s) within 52.5", contamination 2.49%; depth 8281 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4647036244973555840, 47.9", ΔG 4.49); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 1 clean; BJD 2460857.1918 suspect: scattered light 2 (in event), MOM_CENTR1 z=+6.3, MOM_CENTR2 z=-7.7, POS_CORR1 z=+11.0, POS_CORR2 z=-10.3, SAP_BKG z=+556.4; BJD 2460857.2043 suspect: scattered light 2 (in event), MOM_CENTR1 z=+7.5, MOM_CENTR2 z=-7.7, POS_CORR1 z=+13.6, POS_CORR2 z=-12.4, SAP_BKG z=+671.7; BJD 2460857.2557 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+8.7, MOM_CENTR2 z=-7.7, POS_CORR1 z=+14.5, POS_CORR2 z=-13.6, SAP_BKG z=+569.0; BJD 2460893.7535 suspect: MOM_CENTR2 z=-5.6, POS_CORR1 z=-6.0, POS_CORR2 z=-7.7, SAP_BKG z=+10.6 |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2629.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2629.01: TOI-2629 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 3 possible published-ephemeris overlap(s) within 1 d (TOI-2629.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 20.4″ from the out-of-transit centroid (0.4σ bootstrap); 18.1″ from the catalogue position; 14% of the deficit in the optimal aperture |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 7.6″ from the out-of-transit centroid (0.2σ bootstrap); 8.0″ from the catalogue position; 16% of the deficit in the optimal aperture |
| Vetting difference-image localization (E3) | inconclusive | difference-image centroid 12.4″ from the out-of-transit centroid (0.2σ bootstrap); 12.6″ from the catalogue position; 9% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | failed | BJD 2460893.753: 59/246 event-free windows at least as deep; resolution 1/246, not a probability of zero; BJD 2460932.987: 18/249 event-free windows at least as deep; resolution 1/249, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460893.753: 50/87 recovered; BJD 2460932.987: 64/82 recovered |
