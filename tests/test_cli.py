import json

from cygnus import cli


def test_doctor_returns_healthy_json(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "s"))
    monkeypatch.setenv("CYGNUS_LEDGER", str(tmp_path / "l.sqlite"))
    rc = cli.main(["doctor", "--full"])
    out = capsys.readouterr().out
    data = json.loads(out)
    assert data["scratch"]["writable"] is True
    assert data["ledger"]["open"] is True
    assert "astroquery" in data["optional_stack"]
    assert rc == 0


def test_cli_render_dossier(tmp_path, capsys):
    from cygnus.candidate_record import CandidateRecord

    rec = CandidateRecord(
        candidate_id="CYG-TEST-2026-001",
        provenance={"workspace_note": "cli test fixture"},
        audit={"sanity": "passed"},
    )
    p = rec.save(tmp_path / "rec.json")
    rc = cli.main(["dossier", str(p)])
    out = capsys.readouterr().out
    assert "CYGNUS CANDIDATE DOSSIER" in out
    assert rc == 0
