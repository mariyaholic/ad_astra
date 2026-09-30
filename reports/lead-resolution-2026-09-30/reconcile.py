"""Reconcile this dated evidence packet while preserving frozen campaign numerics.

Run only after reviewing REPORT.md and measured JSON outputs. Idempotent
updates retain superseded narrative as explicitly labelled history; current
dossiers are emitted here rather than regenerating old analysis directories.
"""

from pathlib import Path
import hashlib
import json

from cygnus.candidate_record import CandidateRecord
from cygnus.ledger import Ledger
from cygnus.reporting.dossier import emit_dossier_markdown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main():
    photo = load(HERE / "photometry.json")
    cuts = load(HERE / "cutout_manifest.json")
    prfs = load(HERE / "prf_manifest.json")
    loc = load(HERE / "ffi_localization.json")
    config = load(HERE / "config.json")
    rv = load(HERE / "harps_profiles.json")
    relative = load(HERE / "relative_spectra.json")
    spectra = load(HERE / "spectra_manifest.json")
    bundles = load(HERE / "harps_rv.json")
    aligned = load(HERE / "ccf_alignment.json")
    precision = {
        g["mask"]: g["harps_precision_validation"]["rms_pipeline_difference_kms"] * 1000
        for g in aligned["groups"]
        if g["instrument"] == "HARPS" and g["harps_precision_validation"]
    }
    mask_products = load(HERE / "mask_manifest.json")["products"]
    koa = load(HERE / "koa_product_screen.json")
    koa_parts = []
    for product in koa["products"]:
        for kind, key, url in (
            ("raw prefix", "header_prefix", product["raw_request"]["url"]),
            (
                "calibration association list",
                "calibration_list",
                product["calibration_list"].get("url"),
            ),
        ):
            part = product[key]
            if part.get("sha256"):
                koa_parts.append(
                    {
                        "id": product["koaid"]
                        + "#"
                        + (
                            "prefix-65536-bytes"
                            if key == "header_prefix"
                            else "associated-calibration-list"
                        ),
                        "archive": "KOA HIRES " + kind,
                        "sha256": part["sha256"],
                        "url": url,
                    }
                )
    text = {
        "toi-224-01": "A new Sector107 FFI dip repeats near the conditional 31.57966184-day timing family, but its 0.618-arcsec displacement at a 4.71 block-bootstrap ratio leaves localization inconclusive. Gaia records a 49.801-km/s robust RV range over21 accepted transits, GOF41.54 and RUWE9.18; SOAR literature resolves a close companion and favors an eclipsing binary. S106 remains rejected. A clean single-star planet interpretation is unsupported; which component eclipses and its orbit remain unresolved. Unverified lead.",
        "toi-2666-01": "S35/S99 V-shaped dips persist under independent baseline choices. Zhang2024 primary Keck/HIRES evidence identifies HIP45621/TOI2666 as a spectroscopic binary with35-km/s component separation, corroborating the close-companion alternative. The later eclipse is not linked to a solved stellar orbit. Earlier S8 FFI tests robustly exclude0 of52 historical aliases across exposure integration and timing slack; noisy reductions cannot supply a clean nondetection. Unverified event interpretation; binarity independently established.",
        "toi-3500-02": "S64/S90 dips persist, but official UPDATED_2.0 TESS PRFs do not assign the deficit robustly between the0.18-pixel-separated Gaia A/B pair. Source preference reverses with allowed registration and1/3/5-percent model floors; static PRF residuals exceed nominal interpolation accuracy. S101 remains rejected and supplies no period preference. All16 baseline aliases remain open; Gaia RV summaries provide no orbit or companion-mass bound. Unverified lead.",
    }
    next_tests = {
        "toi-224-01": "Resolve the S107 significant subpixel displacement with component-aware PRF/registration and same-CCD/pointing controls. Obtain or recover phase-spread component velocities; fit a binary orbit before assigning the eclipse or companion mass. New repeat timing alone is insufficient.",
        "toi-2666-01": "Recover multi-epoch component spectra/RVs of HD80133/HIP45621 and fit an SB2 orbit against the observed eclipse times. No S8 alias exclusion is robust; do not restore a single-star radius or infer a planet from the light curve alone.",
        "toi-3500-02": "Use validated empirical sector PRFs or resolved time-series photometry for A/B; seek another clean event or component RV series. Retain all16 aliases, exclude S101 from period evidence, and do not treat catalog RV range as an orbital semiamplitude.",
    }
    text["toi-3500-02"] += (
        " Six public HARPS epochs span111.785days with87.507m/s corrected-RV range. A conditional circular50.0446-day fit gives signedK about39m/s but six epochs, line-width correlation and unresolved source identity prevent confirmation or alias rejection. Eighteen further HARPS and six FEROS products returnHTTP401. A relative-spectrum attempt on23 FEROS and6 HARPS spectra fails the independent HARPS precision check (168m/s RMS); derived shifts are not accepted orbital velocities."
    )
    text["toi-2666-01"] += (
        " Two public FEROS spectra from2006/2009 were retrieved; their relative-shift blocks disagree by53km/s, so no usable component velocities or orbit are claimed."
    )
    next_tests["toi-3500-02"] += (
        " Improve and validate line-mask/continuum spectral RV extraction; test the50.0446-day hypothesis against activity and blended components using additional accessible spectra."
    )
    text["toi-3500-02"] += (
        f" A completed31-input line-mask rerun gives HARPS CCF-alignment disagreement RMS{precision['R50G2']:.4f}m/s (R50G2) and{precision['K0']:.4f}m/s (K0), both failing the10m/s requirement. FEROS midpoint barycentric replacement deltas are roughly-103 to+173m/s; release products also lack simultaneous-reference drift correction and usable ERR arrays. FEROS profile shifts remain unvalidated."
    )
    text["toi-2666-01"] += (
        " A bounded public Keck HIRES coordinate query returns three raw observations from1998/2021; exact-name selection returns zero. Documented public access recovered all three primary header prefixes: each TARGNAME is80133, consistent with intended HD80133 targeting. Iodine is out for1998/February2021 and in forMay2021. KOA lists18/59/58 associated calibrations; suitability, acquired component identity and component velocities remain untested. No full science or calibration FITS was downloaded; no extra velocities or orbit are claimed."
    )
    next_tests["toi-2666-01"] += (
        " Screen the three public KOA raw observations for exact-source identity and science-grade calibration before extracting component velocities."
    )
    ids = {
        "toi-224-01": "CYG-2026-09-TOI224.01",
        "toi-2666-01": "CYG-2026-09-TOI2666.01",
        "toi-3500-02": "CYG-2026-09-TOI3500.02",
    }
    ledger = Ledger()
    combined = b"".join(
        (HERE / f).read_bytes()
        for f in (
            "config.json",
            "photometry.json",
            "ffi_localization.json",
            "calibrated_prf.json",
            "archive_refresh.json",
            "toi2666_s8_aliases.json",
            "harps_profiles.json",
            "relative_spectra.json",
            "rv_name_archive.json",
            "mask_manifest.json",
            "masked_spectra.json",
            "ccf_alignment.json",
            "feros_barycentric_audit.json",
            "koa_hires_archive.json",
            "koa_product_screen.json",
        )
    )
    digest = hashlib.sha256(combined).hexdigest()
    existing = ledger.completed_run("lead-resolution-2026-09-30:reconciliation", digest)
    run_id = (
        existing["id"]
        if existing
        else ledger.log_run(
            "lead-resolution-2026-09-30:reconciliation",
            config_hash=digest,
            seed=config["seed"],
        )
    )
    for p in cuts + prfs + mask_products + koa_parts:
        ledger.add_product(
            p["archive"],
            p["id"],
            checksum=p["sha256"],
            url=p.get("url"),
            extra={"report": "reports/lead-resolution-2026-09-30/REPORT.md"},
        )
    science = {
        p["datalink"]: p for p in spectra["products"] if p["state"] == "downloaded"
    }
    ccfs = {
        c["sha256"]: {
            "id": p["id"] + "#" + c["member"],
            "archive": "ESO HARPS ancillary CCF",
            "sha256": c["sha256"],
            "url": p["url"],
        }
        for p in bundles["products"]
        for c in p.get("ccfs", [])
    }
    for p in list(science.values()) + list(ccfs.values()):
        ledger.add_product(
            p["archive"],
            p["id"],
            checksum=p["sha256"],
            url=p.get("url"),
            extra={"report": "reports/lead-resolution-2026-09-30/REPORT.md"},
        )
    if not existing:
        ledger.add_measurement(
            run_id,
            "S107 descriptive box depth",
            loc["box_measurement"]["depth_ppm"],
            unit="ppm",
            candidate_id=ids["toi-224-01"],
            product_ids=[cuts[0]["id"]],
            method="fixed-duration quadratic joint box; no physical transit fit",
        )
        ledger.add_measurement(
            run_id,
            "S107 difference-source displacement",
            loc["offset_arcsec"],
            unit="arcsec",
            candidate_id=ids["toi-224-01"],
            product_ids=[cuts[0]["id"]],
            method="length-five residual-block bootstrap; localization inconclusive",
            notes="4.71 bootstrap ratio; no WCS/PRF covariance",
        )
        ledger.close_run(
            run_id,
            "completed",
            "Evidence packet registered;3 unresolved event interpretations remain Unverified; no discovery or completed-goal claim",
        )
    for lead in config["leads"]:
        slug = lead["slug"]
        cid = ids[slug]
        path = ROOT / "publish/candidates" / (cid + ".json")
        data = load(path)
        data["measured"].setdefault(
            "superseded_bottom_line_2026-09-27",
            {
                "value": data["bottom_line"],
                "method": "historical narrative; superseded by2026-09-30 follow-up; original measurements retained",
            },
        )
        data["bottom_line"] = text[slug]
        data["next_test"] = next_tests[slug]
        data["provenance"]["2026-09-30 follow-up"] = (
            "reports/lead-resolution-2026-09-30/REPORT.md; exact queries/checksums in companion JSON outputs"
        )
        data["reproduction"]["2026-09-30"] = (
            "python reports/lead-resolution-2026-09-30/resolve_leads.py --help; config.json; see REPORT.md for ordered modes and validation"
        )
        data["catalog_audit"][
            "2026-09-30 primary literature and exact-source refresh"
        ] = "reports/lead-resolution-2026-09-30/PRIOR_ART_AUDIT.md; archive_refresh.json. Companion/binary evidence is not an event-time matched orbit."
        data["audit"]["2026-09-30 SAP/PDCSAP baseline persistence"] = "passed"
        data["audit"]["2026-09-30 fixed-epoch injection sensitivity"] = "passed"
        data["audit"]["2026-09-30 search-wide false-alarm calibration"] = "not_tested"
        if slug == "toi-3500-02":
            data["audit"]["Line-mask CCF precision validation"] = "failed"
            data["audit"]["FEROS precision calibration"] = "inconclusive"
            data["audit"]["HARPS six-epoch pipeline RV retrieval"] = "passed"
            data["audit"]["Relative-spectrum precision validation"] = "failed"
            data["audit"]["RV orbit and activity discrimination"] = "inconclusive"
            data["measured"]["HARPS descriptive RV range"] = {
                "value": rv["range_kms"],
                "unit": "km/s",
                "method": "six pipeline RVC epochs; range is not orbitalK or mass",
            }
        if slug == "toi-2666-01":
            data["audit"]["Two-epoch FEROS component-RV extraction"] = "failed"
            data["audit"]["KOA three raw-prefix access"] = "passed"
            data["audit"]["KOA calibrated component velocities"] = "not_tested"
        if slug == "toi-224-01":
            data["audit"]["future-sector alias test"] = "inconclusive"
            data["audit"]["S107 repeat signal"] = "passed"
            data["audit"]["S107 source localization"] = "inconclusive"
            data["audit"]["single-star host interpretation"] = "failed"
            data["measured"]["S107 descriptive depth_ppm"] = {
                "value": loc["box_measurement"]["depth_ppm"],
                "unit": "ppm",
                "method": "fixed1.2473h box; no physical radius inference",
            }
            data["measured"]["S107 difference offset"] = {
                "value": loc["offset_arcsec"],
                "unit": "arcsec",
                "method": "4.71 block-bootstrap ratio; localization inconclusive",
            }
            data["competing"].insert(
                0,
                "Close stellar companion / hierarchical eclipsing system strongly supported by SOAR and Gaia RV variability; no solved orbit identifies the eclipsed component.",
            ) if not any(
                "hierarchical eclipsing system strongly" in x for x in data["competing"]
            ) else None
        elif slug == "toi-2666-01":
            data["audit"]["single-star host interpretation"] = "failed"
            data["audit"]["S8 alias exclusions across reduction variations"] = (
                "inconclusive"
            )
            if not any("Zhang2024" in x for x in data["competing"]):
                data["competing"].insert(
                    0,
                    "Spectroscopic stellar binary independently identified by Zhang2024 Keck/HIRES; unresolved component orbit remains the leading alternative to a planet interpretation.",
                )
        else:
            data["audit"]["calibrated two-source PRF2026-09-30"] = "inconclusive"
        record = CandidateRecord.from_dict(data)
        record.validate_strict()
        write(path, data)
        ledger.set_candidate(cid, summary=text[slug], evidence_level="unverified_lead")
        (HERE / (slug + "-DOSSIER.md")).write_text(
            emit_dossier_markdown(record, ledger) + "\n", encoding="utf-8"
        )
        # Annotate frozen reports/dossiers; do not regenerate their numerical content.
        notice = f"<!-- follow-up-2026-09-30 -->\n> Historical analysis below. Current evidence and dossier: [2026-09-30 follow-up](../../reports/lead-resolution-2026-09-30/REPORT.md). {text[slug]}\n\n"
        for name in ("REPORT.md", "DOSSIER.md", "SEARCH_LOG.md"):
            old = ROOT / "campaigns" / slug / name
            if old.exists() and "<!-- follow-up-2026-09-30 -->" not in old.read_text(
                encoding="utf-8"
            ):
                old.write_text(
                    notice + old.read_text(encoding="utf-8"), encoding="utf-8"
                )
        old = ROOT / "campaigns" / slug / "sky_record.json"
        baseline = load(old)
        baseline.setdefault("historical_summary_before_2026-09-30", baseline["summary"])
        baseline["summary"] = text[slug]
        baseline["checks"] = [
            c for c in baseline["checks"] if c["name"] != "Dated follow-up2026-09-30"
        ]
        baseline["checks"].append(
            {
                "name": "Dated follow-up2026-09-30",
                "state": "inconclusive",
                "note": text[slug]
                + " See reports/lead-resolution-2026-09-30; frozen original run products/measurements retained.",
            }
        )
        write(old, baseline)
    collection = ROOT / "publish/collections/cygnus-candidates-2026-09.json"
    data = load(collection)
    data["summary"] = (
        "Three unresolved event interpretations remain Unverified after2026-09-30: TOI224 has a new FFI repeat but unresolved localization and strong binary evidence; TOI2666 is a literature spectroscopic binary; calibrated PRFs do not resolve TOI3500. Two previous leads remain retracted. No planet is established."
    )
    data["description_md"] = (
        data["summary"]
        + " Current follow-up: reports/lead-resolution-2026-09-30/REPORT.md. Research resumed at the user's request after the historical pause checkpoint; complete proof/disproof remains outstanding."
    )
    data["research_status"] = (
        "3 unresolved event interpretations; binary evidence strengthened; no evidence promotion"
    )
    for it in data["items"]:
        cid = Path(it["source"]).stem
        it["description"] = text[next(s for s, v in ids.items() if v == cid)]
    write(collection, data)
    previous_record = load(ROOT / "reports/lead-followup-2026-09-27/sky_record.json")
    tpf_products = [
        p
        for p in previous_record["products"]
        if "0443666343" in p["id"] and ("s0064" in p["id"] or "s0090" in p["id"])
    ]
    products = [
        {k: p[k] for k in ("id", "archive", "sha256")}
        for p in photo["products"]
        + cuts
        + prfs
        + tpf_products
        + mask_products
        + koa_parts
    ]
    products.extend(
        {k: p[k] for k in ("id", "archive", "sha256")}
        for p in list(science.values()) + list(ccfs.values())
    )
    record = {
        "schema": "cygnus.sky_record/1",
        "id": "lead-resolution-2026-09-30",
        "title": "Three-lead binary, FFI and calibrated-PRF resolution campaign",
        "kind": "bounded follow-up analysis",
        "status": "completed",
        "outcome": "lead",
        "evidence": "Unverified lead",
        "date": "2026-09-30",
        "summary": data["summary"],
        "spec": None,
        "report": "reports/lead-resolution-2026-09-30/REPORT.md",
        "search_log": "reports/lead-resolution-2026-09-30/SEARCH_LOG.md",
        "targets": previous_record["targets"][:3],
        "products": products,
        "checks": [
            {
                "name": "Exact TOI/Gaia source refresh",
                "state": "passed",
                "note": "Live queries and rows; exact source identities; no NSS orbital solution returned.",
            },
            {
                "name": "TESS selection/control health",
                "state": "passed",
                "note": "Strict, loosened/cone and sector queries answered; control returns50 observations.",
            },
            {
                "name": "Cached LC baseline persistence",
                "state": "passed",
                "note": "48 product/channel/baseline variants; accepted events persist.",
            },
            {
                "name": "Fixed-window sensitivity",
                "state": "passed",
                "note": "4800/4800 cached-LC box injections recovered; not blind-search completeness.",
            },
            {
                "name": "S107 repeat photometry",
                "state": "passed",
                "note": "New FFI repeat; two apertures and baseline degrees.",
            },
            {
                "name": "S107 difference localization",
                "state": "inconclusive",
                "note": "0.618arcsec/4.71 bootstrap ratio; close companion and calibration covariance unresolved.",
            },
            {
                "name": "TOI224 single-star interpretation",
                "state": "failed",
                "note": "SOAR companion; Gaia RV variability and highRUWE invalidate clean single-star prior; orbit not solved.",
            },
            {
                "name": "TOI2666 single-star interpretation",
                "state": "failed",
                "note": "Primary Keck/HIRES spectroscopic binary; no event-time matched orbit.",
            },
            {
                "name": "S8 alias exclusions",
                "state": "inconclusive",
                "note": "0/52 robust conditional exclusions; coarse cadence and baseline excursions.",
            },
            {
                "name": "TOI3500 calibrated PRF source assignment",
                "state": "inconclusive",
                "note": "Source preference changes; static PRF residuals exceed nominal interpolation accuracy.",
            },
            {
                "name": "ESO target spectra access",
                "state": "passed",
                "note": "Exact-name query supersedes spatial timeout:31 unique public science spectra cached (TOI3500:6HARPS/23FEROS;TOI2666:2FEROS).24 furtherTOI3500 science products returnHTTP401. Bound name search finds noTOI224 rows; not a general absence claim.",
            },
            {
                "name": "HARPS RV orbit identity",
                "state": "inconclusive",
                "note": "Six pipeline epochs:87.507m/s range; circular50.0446d fit near39m/s; activity/source identity unresolved; no alias excluded.",
            },
            {
                "name": "Relative-spectrum RV validation",
                "state": "failed",
                "note": f"Independent pipeline comparison RMS={relative['validation']['rms_difference_kms']:.6f}km/s, exceeds0.01km/s precision requirement. FEROS block shifts disagree; no derivedRV orbit claimed.",
            },
            {
                "name": "Line-mask CCF precision validation",
                "state": "failed",
                "note": f"Completed cached rerun31/31uniqueinputs (29profiles/2retainedfailures); hash-linked CCF alignment HARPS five non-reference differences RMS{precision['R50G2']:.4f}/{precision['K0']:.4f}m/s forR50G2/K0, both exceed10m/s. Prior partial generation retained as labelled history. Line-count band weighting is a heuristic because mask widths differ; FEROS precision remains unvalidated.",
            },
            {
                "name": "FEROS precision calibration",
                "state": "inconclusive",
                "note": "25 original products audited. Stored barycentric correction already applied; midpoint replacement deltas forTOI3500 approximately-103 to+173m/s. Photon-weighted timestamps, optical correction cross terms and drift calibration remain unresolved; no corrected stellarRV claimed.",
            },
            {
                "name": "Public Keck HIRES metadata screen",
                "state": "passed",
                "note": "Five bounded public TAP queries answered; TOI2666 coordinate box returns3 raw1998/2021 rows, exact-name0; TOI224/3500 coordinate boxes0; positive control1. This is metadata access, not verified source identity or component velocities.",
            },
            {
                "name": "KOA three-product header and calibration association access",
                "state": "passed",
                "note": "Three65536-byte raw prefixes and association lists retrieved anonymously; all primary headers parsed withTARGNAME80133.18/59/58association rows. Prefix hashes are not full FITS checksums; no calibration applied or componentRV measured.",
            },
            {
                "name": "KOA acquired component identity and science calibration",
                "state": "inconclusive",
                "note": "Intended target supported byTARGNAME; Gaia-to-archive offsets9.361/1.505/2.883arcsec are field/telescope-coordinate comparisons. Calibration applicability, extraction and iodine modelling remain untested; no event-matched SB2 orbit.",
            },
            {
                "name": "Binary orbit/eclipse identity",
                "state": "not_tested",
                "note": "No component-aware phase-spanning RV orbit fit for current event trains.",
            },
            {
                "name": "New-event same-CCD/pointing/moving-object audit",
                "state": "not_tested",
                "note": "S107 event has no completed control-field or ephemeris audit.",
            },
            {
                "name": "Search-wide FAP and physical-profile completeness",
                "state": "not_tested",
                "note": "Finite local nulls/fixed boxes cannot calibrate original survey search.",
            },
        ],
    }
    write(HERE / "sky_record.json", record)
    write(
        HERE / "ledger_registration.json",
        {
            "run_id": run_id,
            "config_results_sha256": digest,
            "scope": "local ledger evidence reconciliation; no external publication",
        },
    )
    audit = HERE / "PRIOR_ART_AUDIT.md"
    audit_text = audit.read_text(encoding="utf-8")
    audit_text = audit_text.replace(
        "21 RV visibility periods", "21 accepted RV transits in 15 visibility periods"
    )
    audit_text = audit_text.replace(
        "20 RV visibility periods", "20 accepted RV transits in 13 visibility periods"
    )
    audit_text = audit_text.replace(
        "22 periods", "22 accepted RV transits in 14 visibility periods"
    )
    audit.write_text(audit_text, encoding="utf-8")
    ledger.close()
    print(
        "Three canonical candidates reconciled; original numeric outputs preserved; run",
        run_id,
    )


if __name__ == "__main__":
    main()
