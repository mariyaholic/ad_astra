# TOI-7610.01 exoplanet lead retracted — Gaia DR3 SB1 and failed localization

Reviewed 2026-09-27. The former planet lead is retired. Gaia DR3 source
3071787586789910144, the exact target match, has an `SB1` orbital solution in
`gaiadr3.nss_two_body_orbit`: period 90.4224 ± 0.3805 d, eccentricity
0.309 ± 0.095, and primary RV semi-amplitude 12.14 ± 1.31 km/s from 23 accepted
Gaia radial velocities. This is the source of SIMBAD's `SB*` classification;
it was not an unsupported label.

The orbit gives a binary mass function of 0.0144 solar masses. Under the
campaign's 0.743 ± 0.074 solar-mass primary prior and sin(i)=1, the conditional
minimum companion mass is 0.238 solar masses (16th–84th percentile
0.204–0.274 solar masses). The host is therefore a stellar binary. The mass
estimate remains conditional because the original single-star prior is itself
imperfect for a binary; the measured mass function and Gaia SB1 classification
are the direct evidence.

The photometric evidence independently fails the target-source gate. The S99
event at BJD_TDB 2461066.3486 has a difference-image displacement of 2.92
arcsec at 5.71 bootstrap sigma in the separate cached-TPF reduction, consistent
with the stored vetting failure (2.92 arcsec at 5.85 sigma), and MOM_CENTR2
moves by +5.9 local sigma. The S88 reference is inconclusive in the separate
reduction. The two event times are separated by 365.3785 d, or 4.0408 Gaia SB1
periods; the residual from exactly four formal Gaia periods is 3.6889 d
(2.42 times the period-only propagated uncertainty). This interval comparison
does not by itself assign either dip to the binary.

The combination of a confirmed stellar-mass companion and repeated failure to
establish an on-target S99 deficit defeats the original target-planet dossier.
A circumbinary or tertiary transit is not mathematically excluded, and the
photometric feature remains an unresolved anomaly, but it is not carried as an
active exoplanet candidate without a clean source localization and independent
epoch.

Sources and reproduction:

- Official Gaia Archive TAP endpoint
  `https://gea.esac.esa.int/tap-server/tap/sync`; exact Gaia DR3 and four NSS
  queries, retrieval time and returned rows are in
  `../../reports/lead-followup-2026-09-27/catalog_followup.json`.
- Official SIMBAD TAP endpoint
  `https://simbad.cds.unistra.fr/simbad/sim-tap/sync`; the exact identifier and
  bibliography rows trace `UCAC4 433-048726` / Gaia DR3
  3071787586789910144 to Gaia Collaboration et al. (2023), bibcode
  `2023A&A...674A..34G`.
- `../../reports/lead-followup-2026-09-27/toi7610_sb1_check.py` produces the
  mass-function and timing calculations in `toi7610_sb1_results.json` with
  seed 20260927 and 200,000 Monte Carlo draws.
- `../../reports/lead-followup-2026-09-27/independent_tpf_check.py` and
  `independent_tpf_results.json` contain the separate pixel reduction. Original
  measurements and the historical runner output remain in this campaign.

