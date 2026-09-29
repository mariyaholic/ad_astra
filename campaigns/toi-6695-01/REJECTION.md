# TOI-6695.01 lead retracted — known TOI-6695 b transits

Reviewed 2026-09-27. The S34 reference and S61 E1 in the former candidate dossier are observations of the published transiting planet TOI-6695 b, not a new companion. The S88 E2 feature remains rejected independently by the campaign's pointing and off-target difference-image checks. This is a known-object recovery (`pipeline_check`), with no surviving candidate from this dossier.

| Event | Local fit BJD_TDB | Published comparison | Difference |
| --- | ---: | --- | ---: |
| S34 reference | 2459249.5428 | NASA Exoplanet Archive TOI-6695 b reference mid-time 2459249.547139 | -6.25 min |
| S61 E1 | 2459973.5382 | Eberhardt thesis Fig. 4.6 labels the TESS S61 t19 transit 2459973.53 (rounded) | +11.8 min to rounded label |

The same thesis labels S34 t10 at 2459249.55. Eberhardt et al. (2025) explicitly analyze TOI-6695 b in TESS S34 and S61 and report TTVs from the near-resonant outer planet. A linear extrapolation of the archive's approximate 80.389-d period misses S61 by about 0.49 d; that is why a static 1-duration period match is unsafe here. The paper's event identity and the sector-specific figure resolve the ambiguity. The thesis figure times are rounded; the minute differences above are not a significance test.

Sources checked 2026-09-27:
- NASA Exoplanet Archive [TOI-6695 system](https://exoplanetarchive.ipac.caltech.edu/overview/TOI-6695); TAP endpoint `https://exoplanetarchive.ipac.caltech.edu/TAP/sync`, query `SELECT pl_name, hostname, pl_orbper, pl_tranmid, pl_trandur FROM pscomppars WHERE hostname='TOI-6695'` (CSV). The row gives TOI-6695 b, 80.389 d, BJD 2459249.547139 and 8.6668849 h.
- [Eberhardt et al. 2025](https://doi.org/10.3847/1538-3881/adc44e), *The Astronomical Journal* 169, 298; [author thesis, Fig. 4.6](https://www.imprs-hd.mpg.de/590565/thesis_Eberhardt.pdf).
- Original event fits and product checks: `vetting/vetting.json`, `vetting/VETTING.md`, `sky_record.json`; exact MAST products and SHA-256 values are in `sky_record.json`.

The automated campaign used `period_days: null` and a single-epoch veto because its queued TOI row omitted a period. The 26 aliases from S34/S61 are therefore an obsolete analysis of known b transits, not candidate periods. The corrected queue/scaffold now refreshes the exact TOI row at claim time and retains its period, while the prior-art step screens repeat event times against published ephemerides and requires a literature/TTV review. A future residual analysis must first veto the full b transit sequence using an uncertainty-aware ephemeris and then establish any signal outside it.
