# Four-lead archive and localization verification — 2026-09-27

> **Superseded for same-epoch pixel localization:** `reports/lead-followup-2026-09-27/REPORT.md` reruns the cached TPF measurements with an independent aperture/local-peak implementation. This archive metadata screen remains the provenance record for its MAST and Exoplanet Archive queries.

## Bottom line

The false TOI-6695.01 lead has been retracted separately. These four remain **Unverified leads**. A live MAST metadata screen found only the sectors already in their campaigns; no new SPOC LC epoch was available in this query, so it adds no independent transit confirmation or falsification. Live NASA Exoplanet Archive TOI and confirmed-planet cone queries returned no one-day linear-ephemeris overlap for the accepted events, but missing ephemerides, TTVs and literature remain open. Re-evaluation of stored TPF difference-image measurements failed TOI-7610 E1 localization and TOI-224 E4 localization; TOI-3500 E2 is a rejected artifact and contributes no alias preference.

| Rank / lead | Accepted event BJD_TDB | MAST SPOC LC sectors (metadata only) | Current deciding concern | Next test |
|---|---:|---|---|---|
| 1 / TOI-224.01 — four-event timing, but high RUWE and E4 localization/pointing failures | 2459092.1803 | S2, S29, S69, S96, S106 | E4 S106 9.55 arcsec at 7.07 bootstrap sigma; E2 S69 0.52 arcsec at 3.62 sigma is inconclusive; E1/E3 small offsets pass. | Independent TPF/PRF extraction at the four epochs; resolve RUWE 9.18; test a genuinely new sector or phase-spread RV. |
| 2 / TOI-2666.01 — two deep events, binary/planet mass degeneracy; RV is decisive | 2461049.1644 | S35, S61, S99 | Accepted E1 S99 difference-image offset 0.37 arcsec at 0.75 bootstrap sigma; other mass/blend tests remain open. | Obtain or find multiple RV epochs, then jointly fit activity and eclipse; one RV visit is not decisive. |
| 3 / TOI-7610.01 — two events but localization fails and SIMBAD SB* remains unexplained | 2461066.3486 | S88, S99 | E1 S99 offset 2.92 arcsec at 5.85 bootstrap sigma now fails; MOM_CENTR2 +5.9 local sigma; S88 reference target offset 2.6 arcsec at 6.8 sigma also needs PRF/registration review. | Repeat both S88/S99 difference images with PRF/registration/aperture variations and trace the SB* classification; seek RV. |
| 4 / TOI-3500.02 — E1 clean; close 3.71-arcsec co-moving neighbour and 16 aliases remain | 2460757.3199 | S37, S64, S90, S101 | E1 S90 offset 0.35 arcsec at 0.66 sigma passes; E2 S101 6.74 arcsec at 11.50 sigma fails and cannot select an alias. | Simultaneous two-source PRF fit for target and 3.71-arcsec neighbour in S64/S90; keep all 16 aliases. |

## Tests performed

- Reclassified the stored `vetting/vetting.json` difference-image offsets using both angular displacement and bootstrap significance. This changes E1 of TOI-7610 to **failed**, E4 of TOI-224 to **failed**, E2 of TOI-224 to **inconclusive**, and rejected E2 of TOI-3500 to **failed**. No new pixel extraction was performed, so PRF and registration systematics are unresolved.
- Retained local random-epoch statistics as descriptive only (300 draws per event). Zero exceedances do not calibrate a search-wide false-alarm probability. Phase-0.5 non-detections in partially covered alias sets are inconclusive for the full family.
- Re-read the canonical candidate records and regenerated the four dossiers; all remain at Unverified lead. No new RV, high-resolution imaging, full-frame photometry or independent epoch was analyzed.

## Reproduction

The source entries are the four `campaigns/toi-224-01.yaml`, `campaigns/toi-2666-01.yaml`, `campaigns/toi-3500-02.yaml` and `campaigns/toi-7610-01.yaml` specs and each target’s `vetting/vetting.json`; exact input product IDs/checksums are in their `sky_record.json`. Metadata was queried with `cygnus.multi.archives.astronomy.MastAdapter.discover(Target.from_mapping(spec["targets"][0]), limit=200)`. Event-time rows came from `cygnus.priorart.catalogue_audit(..., services=["NASA_Exoplanet_Archive", "TESS_TOI"])` and `event_ephemeris_screen(event_bjd, rows)`. The stored JSON outputs make these queries and their results inspectable without recontacting services. Localization state is `cygnus.campaign.vet.difference_image_localization_state(offset_from_oot_centroid_arcsec, oot_offset_over_sigma)`. No random seed was used in the metadata screen; original TPF bootstrap seeds remain in the campaign vetting code and records. Environment: Python 3.13.3, cygnus 0.1.0, astropy 8.0.1, numpy 2.3.4, scipy 1.18.0, requests 2.34.2, PyYAML 6.0.2. Validation: final `python -m pytest -q` (644 passed, 37 deselected) and `python -m cygnus.publish check` (570 pages, 578 public files) on 2026-09-27.

## Disposition

Rank follows information per effort, not evidence level. No candidate is promoted by this pass. TOI-224 is first for new coverage/host resolution; TOI-2666 next for phase-spread RV; TOI-7610 needs source localization before a candidate route; TOI-3500 needs a two-source fit before period preference. See `docs/LEAD_PURSUIT_PLAN_2026-09-27.md` for kill and promotion gates.
