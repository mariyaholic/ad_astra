# T2 follow-up: toi-5699-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 2 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460452.7747: recovered, depth 1985 ± 116 ppm (catalogue 3736 ppm); BJD 2460474.7930: gap (catalogue 3736 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460477.8066, ΔT = 25.026 d, 1 of 25 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (25.0261 d); duration likelihood under Gaia priors (circular orbits) peaks at 25 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 25.8″ from the out-of-transit centroid (1.3σ bootstrap); 26.8″ from the catalogue position; 24% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5699.01: Gaia DR3 1312418074378025600 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5699.01: Teff 5993 K, R* 1.41 ± 0.11, M* 1.28 ± 0.13, ρ* 0.46 ± 0.12 ρ☉ (dwarf sequence, M_G 3.44, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-5699.01: 4 Gaia neighbour(s) within 52.5", contamination 0.09%; depth 1985 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 4 persistent event(s), 0 clean; BJD 2460473.5442 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+17.8, MOM_CENTR2 z=-11.2, POS_CORR1 z=+15.0, POS_CORR2 z=-12.7, SAP_BKG z=+10.8; BJD 2460477.8066 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+5.5, POS_CORR1 z=+5.6, POS_CORR2 z=-6.2, SAP_BKG z=+338.7; BJD 2460477.8275 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-5.7, POS_CORR1 z=+5.0, POS_CORR2 z=-6.0, SAP_BKG z=+214.4; BJD 2460477.8400 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+5.2, MOM_CENTR2 z=-6.3, POS_CORR1 z=+5.1, POS_CORR2 z=-5.8, SAP_BKG z=+157.0 |
| Moving objects at screen-event epochs | inconclusive | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-5699.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5699.01: TYC 2582-2794-1 otype * (star_or_other) at 0.6" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 25.8″ from the out-of-transit centroid (1.3σ bootstrap); 26.8″ from the catalogue position; 24% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | passed | BJD 2460477.807: 0/162 event-free windows at least as deep; resolution 1/162, not a probability of zero; BJD 2460477.827: 3/167 event-free windows at least as deep; resolution 1/167, not a probability of zero; BJD 2460477.840: 7/177 event-free windows at least as deep; resolution 1/177, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460477.807: 47/48 recovered; BJD 2460477.827: 46/51 recovered; BJD 2460477.840: 46/55 recovered |
