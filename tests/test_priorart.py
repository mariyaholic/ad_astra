from cygnus.candidate_record import CandidateRecord
from cygnus.priorart import SERVICES_BY_DOMAIN, apply_gate, check_skybot


def _record(cid="CYG-CAND-2026-003"):
    return CandidateRecord(
        candidate_id=cid,
        provenance={"coordinates_icrs": "14:39:01 -80:31:00 (epoch not yet propagated)"},
    )


def test_offline_gate_records_not_tested_never_passed(ledger_factory):
    led = ledger_factory()
    rec = _record()
    results = apply_gate(rec, domain="planetary", ledger=led)
    assert results  # services were enumerated
    assert all(res.startswith("not_tested") for res in results.values())
    rows = led.prior_art_for(rec.candidate_id)
    assert len(rows) == len(results)


def test_domain_service_lists_cover_planetary_and_solar_system():
    assert "NASA_Exoplanet_Archive" in SERVICES_BY_DOMAIN["planetary"]
    assert {"MPC", "SkyBoT", "NEOCP"} <= set(SERVICES_BY_DOMAIN["solar_system"])


def test_skybot_requires_epoch_inputs():
    out = check_skybot(None, None, None)
    assert out.startswith("not_tested (SkyBoT requires ra/dec/epoch inputs)")


def test_gate_never_fabricates_matches_offline(ledger_factory):
    led = ledger_factory()
    rec = _record("CYG-CAND-2026-004")
    results = apply_gate(rec, domain="solar_system", ledger=led, allow_network=False)
    assert "match" not in str(results).lower().replace("not_tested (offline", "")
    rows = led.prior_art_for(rec.candidate_id)
    assert rows and all(r["result"].startswith("not_tested") for r in rows)
