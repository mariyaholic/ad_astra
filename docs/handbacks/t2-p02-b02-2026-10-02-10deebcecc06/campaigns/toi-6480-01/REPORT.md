# T2 follow-up: toi-6480-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 6 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460010.4460: recovered, depth 5765 ± 266 ppm (catalogue 6713 ppm); BJD 2459260.2064: recovered, depth 4824 ± 275 ppm (catalogue 6713 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 17%, 0%, 50%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2459976.7039, ΔT = 33.769 d, 0 of 33 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | failed | Worst defining-event pixel localization: difference-image centroid 132.1″ from the out-of-transit centroid (6.2σ bootstrap); 3.5″ from the catalogue position; 40% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6480.01: Gaia DR3 5521142457140038144 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6480.01: Teff 6325 K, R* 1.41 ± 0.11, M* 1.29 ± 0.13, ρ* 0.46 ± 0.12 ρ☉ (dwarf sequence, M_G 3.43, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6480.01: 60 Gaia neighbour(s) within 52.5", contamination 23.72%; depth 5765 ppm (measured depth of the recovered catalogued transit); 12 could produce it if fully eclipsed (brightest 5521142392725789312, 37.2", ΔG 2.24); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 5 clean; BJD 2459974.8803 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=+8.5, POS_CORR2 z=+11.6, SAP_BKG z=+844.5; BJD 2459976.7039 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+1328.8; BJD 2460690.1612 suspect: earth point (in event), manual exclude (in event), momentum dump (in event), scattered light 2 (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6480.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6480.01: UCAC4 231-024537 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E2) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E3) | failed | difference-image centroid 132.1″ from the out-of-transit centroid (6.2σ bootstrap); 3.5″ from the catalogue position; 40% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2460713.764: 0/263 event-free windows at least as deep; resolution 1/263, not a probability of zero; BJD 2460713.793: 0/251 event-free windows at least as deep; resolution 1/251, not a probability of zero; BJD 2460713.807: 0/244 event-free windows at least as deep; resolution 1/244, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2460713.764: 87/87 recovered; BJD 2460713.793: 81/81 recovered; BJD 2460713.807: 81/81 recovered |
