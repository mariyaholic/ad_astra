"""Tier gating: which tools a target may use, decided by its current record state.

Most targets end at T0 (cheap screen). A target reaches costlier tools only by surviving the previous
tier's gates. The tier is DERIVED from the sky record (outcome, check states, optional
``rejected_events``), never asserted by hand, so it cannot drift from the evidence.

  T0 screen        every target        SPOC light curve only: known-signal control, residual screen, prior-art gate
  T1 triage        outcome == lead     aliases, event measurement/nulls, Gaia exact-source + NSS, moving objects
  T2 vet           passes T1 gates     pixel/TPF/FFI localization, neighbour LCs, injection-recovery, alias coverage
  T3 discriminate  passes T2 gates     PRF source fit, archive-spectra probe, RV fits (bulk data; needs a budget)
  T4 confirm       passes T3 + sky     spectral extraction behind the precision gate (needs user go-ahead)
  closed           decisive evidence   only the rejection note remains

Gates (2026-09-30, reviewed by the Opus adviser; AGENTS.md lead-promotion gate):
  T1->T2  aliases run; catalogue cross-match passed; an event-time comparison vs known ephemerides RUN
          (passed/inconclusive; a position-only match never clears an event); null not failed/untested.
  T2->T3  localization PASSED on every *defining* event (events not marked rejected) and no other localization
          check failed; blend census passed; calibrated null passed; event-epoch null exceedance (k/N) passed; spec supplies budget + discriminating_question.
  T3->T4  T3 + an independent-sky check passed (a second reduction of the same pixels is NOT independent)
          + evidence >= Vetted candidate.
  closed  event identified as a known signal, VSX collision failed, every defining event rejected,
          REJECTION.md exists, or abandoned.
Every check name in a record must map to a role in GATE_CHECKS (or IGNORED); a test enforces this.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

TIERS = ("T0", "T1", "T2", "T3", "T4")

TOOLS = {
    "T0": ["target_queue", "fetch_products", "calibrate_screen", "known_signal_recovery", "residual_screen",
           "prior_art (event-time gate)"],
    "T1": ["period_aliases", "event_census", "analysis.events.box_measure/null_exceedance", "stellar_context",
           "multi.nss + archives.spectroscopy.gaia_exact_source", "moving_objects", "alias_cross_instrument"],
    "T2": ["campaign vet (TPF difference image)", "analysis.pixels", "analysis.localize.block_bootstrap_offset",
           "FFI/TESScut cutout", "analysis.events.injection_recovery/classify_aliases"],
    "T3": ["analysis.prf.profile_source_preference", "archives eso(names=)/koa metadata", "analysis.rv",
           "analysis.timing.barycentric_audit", "public spectra download (budgeted)"],
    "T4": ["analysis.spectra (behind precision_gate)", "KOA/ESO calibrations", "follow-up proposal draft"],
}
COST = {"T0": "light", "T1": "light", "T2": "medium", "T3": "heavy", "T4": "heavy"}
NEEDS_APPROVAL = {"T3": "budget + discriminating_question in the spec", "T4": "user go-ahead"}

# Steps that require a tier before they run (the runner skips them as not_tested otherwise).
STEP_TIER = {"vet": "T2", "event_null": "T2", "prf_source_fit": "T3", "spectra_download": "T3", "rv_fit": "T3", "spectra_extract": "T4"}

# --- anchored check registry: (regex on the full check name, role) --------------------------------------
# roles: loc_event (per-event localization; group 1 = event label), loc_other, pointing_census, null, aliases,
#        catalogue (position-only), event_time (comparison vs known ephemerides; passed = no coincidence),
#        identity (passed = event IS a known signal), vsx (failed = collision), guard, moving, blend,
#        independent_sky, context (informational)
GATE_CHECKS: list[tuple[str, str]] = [
    (r"^Vetting difference-image localization \((E\d+)\)$", "loc_event"),
    (r"^Independent cached TPF localization\b", "loc_other"),          # same pixels: never 'independent sky'
    (r"^Difference-image centroids / blend audit$", "loc_other"),
    (r"^Transit centroid / difference image / blend audit$", "loc_other"),
    (r"^Two-source Gaussian-PSF sensitivity grid\b", "loc_other"),
    (r"^Pointing and quality census per event$", "pointing_census"),
    (r"^Pointing / (centroid-)?jitter correlation$", "pointing_census_ts"),
    (r"^Calibrated false-alarm threshold\b|^Red-noise-aware null\b", "null"),
    (r"^Event-epoch null exceedance\b", "null_event"),          # k/N at the event epoch (T2 tool, gates T3)
    (r"^Event-depth injection-recovery$", "injection"),         # recovery at the event depth (gates T4)
    (r"^Period aliases\b", "aliases"),
    (r"^Catalogue cross-match$", "catalogue"),
    (r"^Event-time comparison vs published ephemerides$", "event_time"),
    (r"^Published event-time identity\b", "identity"),
    (r"^Variable-catalogue collision \(VSX\)$", "vsx"),
    (r"^Object-class guard \(SIMBAD\)$", "guard"),
    (r"^Moving objects at screen-event epochs$", "moving"),
    (r"^Blend and dilution census\b", "blend"),
    (r"^Independent repetition\b|^Independent-epoch confirmation\b|^Independent epoch / instrument$", "independent_sky"),
]
_REGISTRY = [(re.compile(p), r) for p, r in GATE_CHECKS]
# named informational checks that never gate a tier
IGNORED = re.compile(
    r"^(Product integrity|Known-signal recovery|Light-curve suitability|Target-to-Gaia|Stellar priors|Synthetic signal|"
    r"Alternative detrending|Literature \(ADS\)|Radial-velocity / literature|Dated follow-up|Context products|"
    r"Cadence quality|Proper-motion propagation|Source checks|Gaia NSS|Gaia DR3 spectroscopic|Earlier ad-hoc|"
    r"Binary mass-function|PDC versus SAP)")

_RANK = {"failed": 3, "inconclusive": 2, "not_tested": 1, "passed": 0}


def classify(name: str) -> tuple[str, str | None] | None:
    """(role, event label or None) for a check name; None if unmapped (a test fails on that)."""
    for rx, role in _REGISTRY:
        m = rx.search(name)
        if m:
            return role, (m.group(1) if m.groups() else None)
    return ("info", None) if IGNORED.search(name) else None


def unmapped_checks(records: list[dict]) -> set[str]:
    return {c.get("name", "") for r in records for c in r.get("checks", []) if classify(c.get("name", "")) is None}


@dataclass
class TierDecision:
    tier: str
    allowed: list[str]
    next_tier: str | None
    blockers: list[str] = field(default_factory=list)
    reason: str = ""
    cost: str = "light"
    needs_approval: str | None = None
    localization: str | None = None
    defining_events: list[str] = field(default_factory=list)

    def as_dict(self):
        return self.__dict__.copy()


def _by_role(checks):
    roles: dict[str, list[tuple[str, str, str | None]]] = {}
    for c in checks:
        cl = classify(c.get("name", ""))
        if cl:
            roles.setdefault(cl[0], []).append((c.get("name", ""), c.get("state", "not_tested"), cl[1]))
    return roles


def _worst(states):
    return max(states, key=lambda s: _RANK.get(s, 1)) if states else "not_tested"


def localization_state(roles, rejected):
    """Worst state over defining events (per-event) and other localization checks; a failure on a
    rejected event is reported elsewhere but does not block."""
    events = {}
    for _, s, ev in roles.get("loc_event", []):
        if ev not in rejected:
            events.setdefault(ev, []).append(s)
    defining = sorted(events)
    per = [_worst(v) for v in events.values()]
    other = [s for _, s, _ in roles.get("loc_other", [])]
    if any(s != "not_tested" for s in per + other):     # untouched template placeholders don't count once real work exists
        other = [s for s in other if s != "not_tested"]
    if "failed" in per or "failed" in other:
        return "failed", defining
    if not defining or any(s in ("inconclusive", "not_tested") for s in per + other):
        return "inconclusive", defining
    return "passed", defining


def _has(roles, role, ok=("passed", "inconclusive")):
    return any(s in ok for _, s, _ in roles.get(role, []))


def decide(record: dict, *, spec: dict | None = None, rejection_note: bool = False) -> TierDecision:
    """Current tier and what stands between the target and the next one, from a sky-record dict.

    ``spec`` (optional) is the campaign spec: T3 needs ``budget`` and ``discriminating_question`` there.
    ``rejection_note`` = a REJECTION.md exists for the target.
    """
    checks = record.get("checks", [])
    roles = _by_role(checks)
    outcome, evidence = record.get("outcome"), record.get("evidence")
    rejected = set(record.get("rejected_events", []))

    def closed(why):
        return TierDecision("closed", [], None, [], why)

    if record.get("status") == "abandoned" or rejection_note:
        return closed("abandoned or REJECTION.md present; only the rejection note remains")
    if any(s == "passed" for _, s, _ in roles.get("identity", [])):
        return closed("event identified as a known signal (event-time identity passed)")
    if any(s == "failed" for _, s, _ in roles.get("vsx", [])) or \
       any(s == "failed" for _, s, _ in roles.get("event_time", [])):
        return closed("known-variable/ephemeris collision (failed)")
    loc, defining = localization_state(roles, rejected)
    all_events = {ev for _, _, ev in roles.get("loc_event", [])}
    if all_events and not defining:
        return closed("every localized event is marked rejected")

    if outcome not in ("lead", "candidate"):
        b = ["no persistent repeat event (outcome != lead)"]
        if record.get("status") != "completed":
            b.insert(0, "T0 not completed")
        return TierDecision("T0", TOOLS["T0"], None, b, "screen only; escalate only on a persistent repeat event",
                            COST["T0"])

    blockers: list[str] = []
    tier = "T1"
    # ---- T1 -> T2
    if not _has(roles, "aliases"):
        blockers.append("period aliases not run")
    if not any(s == "passed" for _, s, _ in roles.get("catalogue", [])):
        blockers.append("catalogue cross-match not passed")
    if not _has(roles, "event_time"):
        blockers.append("event-time comparison vs known ephemerides not recorded (position-only match never clears)")
    if not _has(roles, "null"):
        blockers.append("null/false-alarm test not run or failed")
    if not _has(roles, "moving"):
        blockers.append("moving-object check not run")
    if not blockers:
        tier = "T2"
        # ---- T2 -> T3
        if loc != "passed":
            blockers.append(f"localization {loc} on defining events {defining or 'none'} (T2 vet must pass first)")
        if not any(s == "passed" for _, s, _ in roles.get("blend", [])):
            blockers.append("blend census not passed")
        if not any(s == "passed" for _, s, _ in roles.get("null", [])):
            blockers.append("calibrated null inconclusive: needs a passed result before heavy tools")
        if not any(s == "passed" for _, s, _ in roles.get("null_event", [])):
            blockers.append("event-epoch null exceedance (k/N) not passed: run the event_null step at T2")
        if spec is not None and not (spec.get("budget") and spec.get("discriminating_question")):
            blockers.append("spec lacks budget and discriminating_question (T3)")
        if not blockers:
            tier = "T3"
            # ---- T3 -> T4
            t4 = []
            if not any(s == "passed" for _, s, _ in roles.get("injection", [])):
                t4.append("event-depth injection-recovery not passed")
            if not any(s == "passed" for _, s, _ in roles.get("independent_sky", [])):
                t4.append("no independent-sky check passed (same-pixel reductions do not count)")
            if evidence not in ("Vetted candidate", "Independently supported candidate", "Established object/phenomenon"):
                t4.append("evidence level below Vetted candidate")
            if not t4:
                tier = "T4"
            else:
                blockers = t4
    nxt = TIERS[TIERS.index(tier) + 1] if tier != "T4" else None
    return TierDecision(tier, [t for k in TIERS[:TIERS.index(tier) + 1] for t in TOOLS[k]], nxt, blockers,
                        f"outcome={outcome}, evidence={evidence}", COST[tier], NEEDS_APPROVAL.get(tier),
                        loc, defining)


def decide_campaign(root: Path, campaign_id: str, spec: dict | None = None) -> TierDecision:
    """decide() for a campaign directory, including REJECTION.md detection."""
    import json
    d = Path(root) / "campaigns" / campaign_id
    rec = json.loads((d / "sky_record.json").read_text(encoding="utf-8"))
    return decide(rec, spec=spec, rejection_note=(d / "REJECTION.md").exists())


def rank(tier: str) -> int:
    return TIERS.index(tier) if tier in TIERS else -1


def require_tier(record: dict, needed: str, *, spec: dict | None = None, rejection_note: bool = False) -> None:
    """Raise unless the target has earned ``needed``."""
    d = decide(record, spec=spec, rejection_note=rejection_note)
    if d.tier == "closed" or rank(needed) > rank(d.tier):
        raise PermissionError(f"target is at {d.tier}; {needed} not earned ({'; '.join(d.blockers) or d.reason})")


def gate_step(step: str, record: dict, override: dict | None = None, *, spec: dict | None = None,
              rejection_note: bool = False) -> tuple[bool, str]:
    """(allowed, message) for a step in STEP_TIER. ``override`` = {tier, reason, approved_by, date}; T4 needs approved_by."""
    need = STEP_TIER.get(step)
    if need is None:
        return True, ""
    d = decide(record, spec=spec, rejection_note=rejection_note)
    if d.tier != "closed" and rank(d.tier) >= rank(need):
        return True, ""
    if override and override.get("reason") and rank(override.get("tier", "")) >= rank(need) and \
            (need != "T4" or override.get("approved_by")):
        return True, f"tier override recorded ({override['reason']}; by {override.get('approved_by', 'unrecorded')})"
    return False, f"tier gate: target at {d.tier}, {step} needs {need} ({'; '.join(d.blockers) or d.reason})"


def summarize(records: list[dict]) -> dict:
    """Counts per tier over single-target campaign records (multi-target report records are not tiered)."""
    out: dict[str, int] = {}
    for r in records:
        t = decide(r).tier
        out[t] = out.get(t, 0) + 1
    return out
