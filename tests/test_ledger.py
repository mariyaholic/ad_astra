import pytest

from cygnus.ledger import Ledger, file_sha256


def test_product_registration_idempotent(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    f = tmp_path / "x.bin"
    f.write_bytes(b"hello world")
    cs = file_sha256(f)
    assert cs == hashlib_sha256(f)

    first = led.add_product("MAST", "proj-1", local_path=f, checksum=cs)
    second = led.add_product("MAST", "proj-1", local_path=f, checksum=cs)
    assert first == second
    assert led.count_products("MAST") == 1
    row = led.products("MAST")[0]
    assert row["checksum"] == cs


def hashlib_sha256(path):
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_run_lifecycle(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    run = led.log_run("unit-test", seed=7)
    assert led.run(run)["status"] == "open"
    led.close_run(run, "completed", summary="done")
    r = led.run(run)
    assert r["status"] == "completed" and r["seed"] == 7
    with pytest.raises(ValueError):
        led.close_run(run, "weird")


def test_measurement_links_run_and_candidate(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    run = led.log_run("analysis")
    led.add_candidate("CYG-CAND-2026-001", summary="unit")
    led.add_measurement(
        run,
        "transit_depth",
        420e-6,
        unit="dimensionless_flux_fraction",
        uncertainty=30e-6,
        method="batman_fit",
        candidate_id="CYG-CAND-2026-001",
        product_ids=["proj-1"],
    )
    ms = led.measurements_for_candidate("CYG-CAND-2026-001")
    assert len(ms) == 1
    assert ms[0]["script"] == "analysis"
    assert ms[0]["name"] == "transit_depth"
    assert "proj-1" in ms[0]["product_ids_json"]


def test_prior_art_idempotent_and_colocated(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    cid = "CYG-CAND-2026-002"
    led.add_candidate(cid)
    led.add_prior_art("VSX", "no match in catalogs searched", candidate_id=cid, query="domain=planetary")
    led.add_prior_art("VSX", "no match in catalogs searched", candidate_id=cid, query="domain=planetary")
    rows = led.prior_art_for(cid)
    assert len(rows) == 1 and rows[0]["service"] == "VSX"
    assert led.prior_art_for("") == []  # no cross-contamination from anonymous rows


# ------------------------------------------------------------------ integrity (S1-A)
def test_measurement_requires_an_existing_run(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    with pytest.raises(KeyError, match="no run id=999"):
        led.add_measurement(999, "transit_depth", 1.0)
    assert led.db.execute("SELECT COUNT(*) FROM measurements").fetchone()[0] == 0


def test_close_run_refuses_missing_and_already_closed(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    with pytest.raises(KeyError):
        led.close_run(999, "completed")
    run = led.log_run("unit")
    led.close_run(run, "completed", summary="first")
    with pytest.raises(ValueError, match="already 'completed'"):
        led.close_run(run, "failed", summary="second")
    assert led.run(run)["summary"] == "first"      # the first outcome is not overwritten


def test_readonly_ledger_rejects_writes_and_missing_file(tmp_path):
    import sqlite3

    path = tmp_path / "l.sqlite"
    led = Ledger(path)
    run = led.log_run("unit")
    led.close_run(run, "completed")
    led.close()
    ro = Ledger.open_readonly(path)
    with pytest.raises(sqlite3.OperationalError):
        ro.add_product("MAST", "x")
    with pytest.raises(FileNotFoundError):
        Ledger.open_readonly(tmp_path / "nope.sqlite")


def test_product_ids_are_scoped_by_archive(tmp_path):
    led = Ledger(tmp_path / "l.sqlite")
    a = led.add_product("MAST", "same-id", url="u1")
    b = led.add_product("Gaia", "same-id", url="u2")
    assert a != b
    assert len(led.products()) == 2
    assert led.products("MAST")[0]["url"] == "u1"
    assert led.products("Gaia")[0]["url"] == "u2"


def test_reopen_persists_runs_and_measurements(tmp_path):
    path = tmp_path / "l.sqlite"
    led = Ledger(path)
    run = led.log_run("unit")
    led.add_measurement(run, "depth", 1.0)
    led.close_run(run, "completed")
    led.close()
    again = Ledger(path)
    assert again.run(run)["status"] == "completed"
    assert [m["name"] for m in again.measurements_for_candidate("")] == ["depth"]
