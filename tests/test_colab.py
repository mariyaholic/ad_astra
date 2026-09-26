"""``cygnus.colab``: manifests, git-backed file selection and the baseline/vs-run comparison.

Offline only: no network, no Colab, no Drive, no ledger. The git-backed helpers run real ``git`` in
a temporary repository (skipped only if git is not installed); everything else is plain files under
``tmp_path``. The notebook itself is checked statically, exactly as ``tests/test_analysis_notebook.py``
checks the read-only reanalysis pilot: no cell is executed.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from cygnus import colab

NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "cygnus_batch_colab.ipynb"
NO_GIT = shutil.which("git") is None
needs_git = pytest.mark.skipif(NO_GIT, reason="git is not installed")


# --------------------------------------------------------------------------- fixtures
def _write(root: Path, rel: str, document) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    text = document if isinstance(document, str) else json.dumps(document, indent=1)
    path.write_text(text, encoding="utf-8")
    return path


def _git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], check=check, capture_output=True, text=True)


def _git_repo(tmp_path: Path) -> Path:
    """A repository with one commit, one ignored file and one untracked-but-committable file."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    (repo / ".gitignore").write_text("*.fits\nstate/\nscratch/\n", encoding="utf-8")
    _write(repo, "campaigns/toi-1-01/REPORT.md", "# report\n")
    _write(repo, "campaigns/toi-1-01/tic1/sector35/screen.json", {"rows": 10})
    _write(repo, "campaigns/toi-1-01/tic1/sector35/big.fits", "not really a FITS file\n")
    _write(repo, "state/batches/b1/journal.jsonl", "{}\n")
    _git(repo, "add", "-A")
    _git(repo, "-c", "user.email=test@example.invalid", "-c", "user.name=Cygnus test",
         "commit", "-q", "-m", "one")
    return repo


def _residual(*, k_mad=10.0, entries=6, state="passed", run_id=2258, **extra) -> dict:
    """One runner-step document with the shape of the committed ones (paths, hashes, notes, labels)."""
    document = {
        "step": "residual_screen", "run_id": run_id, "config_hash": "57b6734a13c0b1b1",
        "finished_utc": "2026-09-26T05:14:24Z", "notes": ["runner note"], "outcome": None,
        "result": {
            "per_product": {"p-s0035.fits": {
                "k_mad": k_mad, "entries": entries, "channel_mode": "SAP+PDCSAP",
                "dir": "campaigns/toi-1-01/tic1/sector35",
                "systematics_model": {"method": "integral to first zero crossing",
                                      "caveat": "a correlated systematic can mimic a dip"}}},
            "entries_outside_veto_total": 59,
        },
        "checks": {"Calibrated false-alarm threshold (sign-flip null)":
                   {"state": state, "note": "k* = 10 (calibrated)", "step": "residual_screen"}},
    }
    document.update(extra)
    return document


def _record(*, outcome="lead", state="passed") -> dict:
    return {
        "schema": "cygnus.sky_record/1", "id": "toi-1-01", "status": "completed",
        "outcome": outcome, "evidence": "Unverified lead" if outcome == "lead" else None,
        "date": "2026-09-26", "title": "Known-object test, TOI-1.01",
        "summary": "Known-object test on TOI-1.01: positive control …",
        "spec": "campaigns/toi-1-01.yaml", "report": "campaigns/toi-1-01/REPORT.md",
        "targets": [{"name": "TOI-1.01", "ra_deg": 10.0, "dec_deg": 20.0, "frame": "ICRS",
                     "epoch": "J2015.5", "position_source": "NASA Exoplanet Archive TOI table"}],
        "products": [{"id": "p-s0035.fits", "archive": "MAST", "sha256": "a" * 64, "format": "spoc_lc"}],
        "checks": [{"name": "Product integrity (SHA-256)", "state": state,
                    "note": "1 product(s) from MAST checksummed",
                    "source": "campaign runner, step fetch_products"}],
    }


def _campaign(root: Path, *, residual=None, record=None, extra=()) -> Path:
    """A committed-shape campaign directory: runner outputs, sky record, per-sector file, report."""
    root.mkdir(parents=True, exist_ok=True)
    _write(root, "runner/residual_screen.json", residual or _residual())
    _write(root, "sky_record.json", record or _record())
    _write(root, "tic1/sector35/screen.json",
           {"rows": 17997, "usable": 13613, "input": {"file": "p-s0035.fits", "sha256": "a" * 64}})
    _write(root, "REPORT.md", "# report\n")
    for rel, document in extra:
        _write(root, rel, document)
    return root


# --------------------------------------------------------------------------- checksums and manifests
def test_sha256_file_matches_hashlib(tmp_path):
    path = tmp_path / "blob.bin"
    payload = bytes(range(256)) * 5000          # > 1 MiB, so the block loop is exercised
    path.write_bytes(payload)
    assert colab.sha256_file(path) == hashlib.sha256(payload).hexdigest()


def test_manifest_round_trip_and_every_kind_of_tamper(tmp_path):
    root = tmp_path / "shipped"
    _write(root, "ledger.sqlite", "sqlite-bytes\n")
    _write(root, "state/batches/b1/journal.jsonl", '{"event": "end"}\n')
    _write(root, "state/colab/b1/EQUIVALENCE.md", "# equivalence\n")
    manifest = colab.build_manifest(root, ["ledger.sqlite", "state/batches/b1", "state/colab/b1"])
    assert list(manifest) == ["ledger.sqlite", "state/batches/b1/journal.jsonl",
                              "state/colab/b1/EQUIVALENCE.md"]
    path = colab.write_manifest(root / colab.MANIFEST_NAME, manifest, comment="batch b1")
    assert colab.read_manifest(path) == manifest
    assert path.read_text(encoding="utf-8").startswith("# batch b1\n")
    assert colab.verify_manifest(path, root) == []

    _write(root, "state/colab/b1/EQUIVALENCE.md", "# equivalence, edited\n")     # tampered
    problems = colab.verify_manifest(path, root)
    assert len(problems) == 1 and problems[0].startswith("checksum mismatch: state/colab/b1/EQUIVALENCE.md")
    assert manifest["state/colab/b1/EQUIVALENCE.md"] in problems[0]

    (root / "state/batches/b1/journal.jsonl").unlink()                          # missing
    _write(root, "state/batches/b1/extra.log", "unlisted\n")                    # unlisted
    problems = colab.verify_manifest(path, root)
    assert any(p == "missing: state/batches/b1/journal.jsonl" for p in problems)
    assert any(p == "unlisted file: state/batches/b1/extra.log" for p in problems)
    assert len(problems) == 3                                                   # mismatch, missing, extra

    # the manifest file itself, the probe directory and anything else named are explicit opt-outs
    (root / colab.MANIFEST_NAME).write_text("", encoding="utf-8")
    _write(root, "_probe/probe.txt", "sentinel\n")
    cleaned = colab.verify_manifest(colab.read_manifest(path), root, ignore_extra=["_probe/*"])
    assert not any("MANIFEST" in p or "_probe" in p for p in cleaned)


def test_verify_manifest_reports_a_missing_root_and_parses_only_real_manifests(tmp_path):
    assert colab.verify_manifest({"a": "0" * 64}, tmp_path / "not-there") == \
        [f"root is missing: {(tmp_path / 'not-there').as_posix()}"]
    bad = tmp_path / "bad.txt"
    bad.write_text("not-a-hash  a/b\n", encoding="utf-8")
    with pytest.raises(ValueError, match="not a '<sha256>"):
        colab.read_manifest(bad)
    duplicate = tmp_path / "dup.txt"
    duplicate.write_text(f"{'0' * 64}  a\n{'1' * 64}  a\n", encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate entry"):
        colab.read_manifest(duplicate)
    with pytest.raises(FileNotFoundError, match="nothing to include"):
        colab.build_manifest(tmp_path, ["absent/"])


# --------------------------------------------------------------------------- git-backed selection
@needs_git
def test_committed_files_asks_git_and_honours_gitignore(tmp_path):
    repo = _git_repo(tmp_path)
    _write(repo, "campaigns/toi-1-01/tic1/sector35/normalized_series.csv", "t,flux\n")
    files = colab.committed_files(repo, ["campaigns/toi-1-01", "state"])
    assert "campaigns/toi-1-01/REPORT.md" in files
    assert "campaigns/toi-1-01/tic1/sector35/screen.json" in files
    assert "campaigns/toi-1-01/tic1/sector35/normalized_series.csv" in files    # untracked, not ignored
    assert "campaigns/toi-1-01/tic1/sector35/big.fits" not in files             # ignored: *.fits
    assert not [f for f in files if f.startswith(("state/", "scratch/"))]       # ignored directories
    assert files == sorted(files)
    # an explicitly tracked file is listed even when a later .gitignore would cover it
    _git(repo, "add", "-f", "campaigns/toi-1-01/tic1/sector35/big.fits")
    assert "campaigns/toi-1-01/tic1/sector35/big.fits" in colab.committed_files(repo, ["campaigns"])
    with pytest.raises(ValueError, match="outside the repository"):
        colab.committed_files(repo, [tmp_path / "elsewhere"])
    with pytest.raises(ValueError, match="at least one path"):
        colab.committed_files(repo, [])


@needs_git
def test_extract_git_archive_is_read_only_and_pinned(tmp_path):
    repo = _git_repo(tmp_path)
    first = _git(repo, "rev-parse", "HEAD").stdout.strip()
    _write(repo, "campaigns/toi-1-01/tic1/sector35/screen.json", {"rows": 999})   # a later commit
    _git(repo, "add", "-A")
    _git(repo, "-c", "user.email=test@example.invalid", "-c", "user.name=Cygnus test",
         "commit", "-q", "-m", "two")

    dest = tmp_path / "baseline"
    landed = colab.extract_git_archive(repo, first, ["campaigns/toi-1-01"], dest)
    assert landed == ["campaigns/toi-1-01/REPORT.md",
                      "campaigns/toi-1-01/tic1/sector35/screen.json"]
    assert json.loads((dest / "campaigns/toi-1-01/tic1/sector35/screen.json").read_text()) == {"rows": 10}
    # the working tree still holds the newer commit: the baseline is a copy, not a checkout
    assert json.loads((repo / "campaigns/toi-1-01/tic1/sector35/screen.json").read_text()) == {"rows": 999}
    with pytest.raises(RuntimeError, match="git archive"):
        colab.extract_git_archive(repo, "0" * 40, ["campaigns"], tmp_path / "nope")


# --------------------------------------------------------------------------- comparison
def test_compare_identical_trees_reports_no_differences(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01")
    cand = _campaign(tmp_path / "cand" / "toi-1-01")
    result = colab.compare_campaigns(base, cand)
    assert result["status"] == "identical" and result["identical"] is True
    assert result["science"] == [] and result["bookkeeping"] == []
    assert result["counts"]["files_compared"] == 3        # runner step, sky record, per-sector file
    assert result["counts"]["leaves_compared"] > 20
    assert result["counts"]["not_compared"] == 1
    assert result["not_compared"][0]["file"] == "REPORT.md"
    assert result["rules"]["note"].startswith("a leaf is bookkeeping")
    assert "None." in colab.render_report(result)


def test_compare_classifies_every_bookkeeping_difference_and_no_science(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01")
    moved = _residual(
        run_id=900, config_hash="deadbeefdeadbeef", finished_utc="2026-09-27T01:00:00Z",
        notes=["a different runner note"], date="2026-09-27")
    moved["result"]["per_product"]["p-s0035.fits"]["dir"] = "content-scratch/tic1/sector35"
    moved["result"]["per_product"]["p-s0035.fits"]["path"] = "scratch:campaign_toi-1-01/p-s0035.fits"
    moved["result"]["per_product"]["p-s0035.fits"]["workdir"] = "/content/scratch/campaign_toi-1-01"
    moved["result"]["per_product"]["p-s0035.fits"]["fetched_now"] = True
    moved["result"]["per_product"]["p-s0035.fits"]["pinned"] = False
    moved["result"]["per_product"]["p-s0035.fits"]["sha256"] = "b" * 64
    moved["result"]["per_product"]["p-s0035.fits"]["systematics_model"]["caveat"] = "reworded caveat"
    moved["checks"]["Calibrated false-alarm threshold (sign-flip null)"]["note"] = "reworded note"
    record = _record()
    record["date"] = "2026-09-27"
    record["summary"] = "reworded summary"
    record["targets"][0]["position_source"] = "TOI table (re-verified)"
    record["products"][0]["sha256"] = "c" * 64                   # a checksum: bookkeeping by policy
    cand = _campaign(tmp_path / "cand" / "toi-1-01", residual=moved, record=record,
                     extra=[("state/colab/b1/notes.md", "not compared by request\n")])
    result = colab.compare_campaigns(base, cand, ignore_files=["state/*"])
    assert result["status"] == "bookkeeping_only", result["science"]
    assert result["science"] == []
    leaves = {entry["leaf"]: entry["reason"] for entry in result["bookkeeping"]}
    assert leaves["/run_id"].startswith("run bookkeeping")
    assert leaves["/config_hash"].startswith("run bookkeeping")
    assert leaves["/finished_utc"].startswith("run bookkeeping")
    assert leaves["/date"].startswith("run bookkeeping")
    assert leaves["/notes[0]"].startswith("free-text interpretation")
    assert leaves["/result/per_product/p-s0035.fits/sha256"].startswith("run bookkeeping")
    assert leaves["/result/per_product/p-s0035.fits/path"].startswith("path or locator")
    assert leaves["/result/per_product/p-s0035.fits/dir"].startswith("path or locator")
    assert leaves["/result/per_product/p-s0035.fits/workdir"].startswith("absolute or private path")
    assert leaves["/result/per_product/p-s0035.fits/fetched_now"].startswith("run bookkeeping")
    assert leaves["/result/per_product/p-s0035.fits/systematics_model/caveat"] \
        .startswith("free-text interpretation")
    assert leaves["/checks/Calibrated false-alarm threshold (sign-flip null)/note"] \
        .startswith("free-text interpretation")
    assert leaves["/targets[0]/position_source"].startswith("reference-frame or provenance label")
    assert leaves["/products[0]/sha256"].startswith("run bookkeeping")
    assert result["counts"]["science"] == 0
    assert result["ignored_files"] == [{"file": "state/colab/b1/notes.md",
                                        "reason": "listed in ignore_files="}]
    assert result["counts"]["not_compared"] == 1


def test_compare_reports_real_science_differences_with_their_leaves(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01")
    moved = _residual(k_mad=3.5, entries=9, state="failed")
    moved["result"]["entries_outside_veto_total"] = 61
    moved["result"]["per_product"]["p-s0035.fits"]["channel_mode"] = "single"
    moved["result"]["per_product"]["p-s0035.fits"]["systematics_model"]["method"] = "other method"
    del moved["result"]["per_product"]["p-s0035.fits"]["entries"]
    moved["outcome"] = ["nonsense"]                     # None -> list: a changed type
    moved["states"] = ["recovered"]                     # a key only the candidate has
    record = _record(outcome="null_result", state="not_tested")
    record["checks"].append({"name": "Alternative detrending", "state": "not_tested"})   # 1 -> 2
    cand = _campaign(tmp_path / "cand" / "toi-1-01", residual=moved, record=record)
    result = colab.compare_campaigns(base, cand)
    assert result["status"] == "science_differences" and result["identical"] is False
    leaves = {entry["leaf"] for entry in result["science"]}
    assert {"/result/per_product/p-s0035.fits/k_mad", "/result/per_product/p-s0035.fits/entries",
            "/result/per_product/p-s0035.fits/channel_mode",
            "/result/per_product/p-s0035.fits/systematics_model/method",
            "/result/entries_outside_veto_total", "/outcome", "/checks[0]/state",
            "/states", "/checks"} <= leaves
    assert any("key only in the baseline" in (e.get("note") or "") and
               e["leaf"].endswith("/entries") for e in result["science"])
    assert any("key only in the candidate" in (e.get("note") or "") and e["leaf"] == "/states"
               for e in result["science"])
    assert any(entry["leaf"] == "/checks" and entry["note"] == "list length differs"
               and entry["baseline"] == "1" and entry["candidate"] == "2" for entry in result["science"])
    assert any(entry["leaf"] == "/outcome" and entry["note"].startswith("type changed")
               for entry in result["science"])
    assert all("reason" not in entry for entry in result["science"])
    assert {entry["file"] for entry in result["science"] if entry["leaf"].startswith("/result")} == \
        {"runner/residual_screen.json"}
    rendered = colab.render_report(result, title="toi-1-01")
    assert "k_mad" in rendered and "**science_differences**" in rendered


def test_compare_lists_files_present_on_one_side_only(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01",
                     extra=[("runner/period_aliases.json", {"candidates": []})])
    cand = _campaign(tmp_path / "cand" / "toi-1-01",
                     extra=[("vetting/vetting.json", {"verdict": "keep"})])
    result = colab.compare_campaigns(base, cand)
    assert result["files_only_in_baseline"] == ["runner/period_aliases.json"]
    assert result["files_only_in_candidate"] == ["vetting/vetting.json"]
    assert result["status"] == "science_differences"
    rendered = colab.render_report(result)
    assert "runner/period_aliases.json" in rendered and "vetting/vetting.json" in rendered

    # vetting.json is written by `cygnus.campaign vet`, which a batch run does not do: excluding it
    # is explicit, and the report says so. An ignored difference is still a difference, so the two
    # trees are "bookkeeping_only", never "identical".
    quiet = colab.compare_campaigns(base, cand, ignore_files=["runner/period_aliases.json",
                                                             "vetting/*"])
    assert quiet["status"] == "bookkeeping_only" and quiet["science"] == []
    assert [entry["file"] for entry in quiet["ignored_files"]] == ["runner/period_aliases.json",
                                                                   "vetting/vetting.json"]
    assert "`vetting/vetting.json`" in colab.render_report(quiet)


def test_compare_ignore_patterns_and_problems_are_explicit(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01")
    cand = _campaign(tmp_path / "cand" / "toi-1-01", residual=_residual(k_mad=99.0))
    result = colab.compare_campaigns(base, cand,
                                     ignore=["*/result/per_product/*/k_mad"])
    assert result["status"] == "bookkeeping_only" and result["science"] == []
    assert [entry["reason"] for entry in result["ignored"]] == \
        ["listed in ignore= as '*/result/per_product/*/k_mad'"]
    assert result["ignore"] == ["*/result/per_product/*/k_mad"]

    missing = colab.compare_campaigns(tmp_path / "absent", cand)
    assert missing["status"] == "incomplete" and missing["counts"]["science"] == 0
    assert missing["problems"] == [f"baseline directory is missing: {(tmp_path / 'absent').as_posix()}"]
    assert "Problems" in colab.render_report(missing)

    _write(base, "runner/truncated.json", "{not json")
    _write(cand, "runner/truncated.json", "{not json")
    broken = colab.compare_campaigns(base, cand)
    assert broken["status"] == "incomplete"
    assert any("not comparable JSON" in problem for problem in broken["problems"])


def test_compare_keeps_bare_product_names_as_science_and_nan_as_equal(tmp_path):
    nan_base = _campaign(tmp_path / "nan-base" / "toi-1-01")
    nan_same = _campaign(tmp_path / "nan-same" / "toi-1-01")
    for root in (nan_base, nan_same):
        _write(root, "runner/residual_screen.json", _residual(k_mad=float("nan")))
    assert colab.compare_campaigns(nan_base, nan_same)["status"] == "identical"   # NaN == NaN here

    base = _campaign(tmp_path / "base" / "toi-1-01")
    other = _campaign(tmp_path / "other" / "toi-1-01")
    # a bare product name under `file` identifies what was analysed: science, not a path
    _write(other, "tic1/sector35/screen.json",
           {"rows": 17997, "usable": 13613, "input": {"file": "another-product.fits"}})
    result = colab.compare_campaigns(base, other)
    assert [entry["leaf"] for entry in result["science"]] == ["/input/file"]
    assert result["status"] == "science_differences"
    # ... but a *path-like* value under the same key is a locator, and the missing checksum key is
    # run bookkeeping, so nothing science is left
    _write(other, "tic1/sector35/screen.json",
           {"rows": 17997, "usable": 13613,
            "input": {"file": "campaigns/toi-1-01/tic1/sector35/screen.json"}})
    quiet = colab.compare_campaigns(base, other)
    assert quiet["status"] == "bookkeeping_only" and quiet["science"] == []
    assert {entry["reason"] for entry in quiet["bookkeeping"]} == \
        {"path or locator: 'file'", "run bookkeeping: 'sha256'"}


def test_numeric_tolerance_is_opt_in_and_records_its_evidence(tmp_path):
    """Round-off must be reported, never waved through and never confused with science."""
    # The strict default: even a 1e-11 relative difference is a science difference.
    base = _campaign(tmp_path / "base" / "toi-1-01")
    close = _campaign(tmp_path / "close" / "toi-1-01", residual=_residual(k_mad=10.0 + 1e-10))
    strict = colab.compare_campaigns(base, close)
    assert strict["status"] == "science_differences" and strict["numeric_rtol"] is None
    assert [entry["leaf"] for entry in strict["science"]] == ["/result/per_product/p-s0035.fits/k_mad"]
    assert strict["counts"]["numerical"] == 0

    # With a declared tolerance the same difference is reported under 'numerical', with the exact
    # relative difference and the tolerance named in the entry itself.
    tolerant = colab.compare_campaigns(base, close, numeric_rtol=1e-8)
    assert tolerant["status"] == "bookkeeping_only" and tolerant["numeric_rtol"] == 1e-8
    assert tolerant["science"] == [] and tolerant["counts"]["numerical"] == 1
    entry = tolerant["numerical"][0]
    assert entry["leaf"] == "/result/per_product/p-s0035.fits/k_mad"
    assert isinstance(entry["relative"], float) and entry["relative"] < 1e-8
    assert "1e-08" in entry["note"] or "1e-8" in entry["note"]
    assert "declared numeric tolerance" in colab.render_report(tolerant)
    assert "largest is" in colab.render_report(tolerant)

    # A difference beyond the declared tolerance is still science, and the entry stays listed.
    beyond = _campaign(tmp_path / "beyond" / "toi-1-01", residual=_residual(k_mad=10.5))
    result = colab.compare_campaigns(base, beyond, numeric_rtol=1e-8)
    assert result["status"] == "science_differences" and result["counts"]["numerical"] == 0
    assert [entry["leaf"] for entry in result["science"]] == ["/result/per_product/p-s0035.fits/k_mad"]

    # An ignore= pattern outranks the tolerance: the ignored leaf lands in 'ignored', named.
    both = colab.compare_campaigns(base, close, numeric_rtol=1e-8,
                                   ignore=["*/result/per_product/*/k_mad"])
    assert both["science"] == [] and both["numerical"] == []
    assert [entry["reason"] for entry in both["ignored"]] == \
        ["listed in ignore= as '*/result/per_product/*/k_mad'"]


def test_render_report_truncates_long_lists_and_escapes_table_pipes(tmp_path):
    base = _campaign(tmp_path / "base" / "toi-1-01")
    moved = _residual()
    moved["checks"]["Calibrated false-alarm threshold (sign-flip null)"]["note"] = "an | odd | note"
    for index in range(6):
        moved[f"extra_{index}"] = index
    cand = _campaign(tmp_path / "cand" / "toi-1-01", residual=moved)
    result = colab.compare_campaigns(base, cand, max_items=2)
    rendered = colab.render_report(result)
    assert "\\| odd \\|" in rendered
    assert "more (see the machine-readable report)" in rendered
    assert result["max_items"] == 2


# --------------------------------------------------------------------------- the notebook, statically
def _notebook() -> dict:
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))


def test_batch_notebook_is_nbformat_v4_and_has_no_saved_outputs_or_credentials():
    document = _notebook()
    assert document["nbformat"] == 4
    assert document["nbformat_minor"] >= 5
    assert document["cells"], "the notebook has no cells"
    seen: set[str] = set()
    for index, cell in enumerate(document["cells"]):
        assert cell["cell_type"] in {"code", "markdown"}
        assert isinstance(cell["source"], list)
        assert cell["id"] and cell["id"] not in seen, f"cell {index} has a missing or duplicate id"
        seen.add(cell["id"])
        if cell["cell_type"] == "code":
            assert cell["outputs"] == [], f"saved notebook outputs in cell {index}"
            assert cell["execution_count"] is None
            compile("".join(cell["source"]), f"colab-cell-{index}", "exec")
    text = "\n".join("".join(cell["source"]) for cell in document["cells"])
    # The two workstation-path prefixes are assembled from chr(92) so that this guard file does not
    # itself contain the absolute paths it forbids (AGENTS.md: no private storage paths in new files).
    backslash = chr(92)
    for forbidden in ("D:" + backslash, "C:" + backslash + "Users" + backslash, "rclone.conf",
                      "refresh_token", "client_secret", "BEGIN PRIVATE KEY", "AIza"):
        assert forbidden not in text, f"the notebook contains {forbidden!r}"


def test_batch_notebook_states_the_pinned_route_guards_and_ledger_decision():
    document = _notebook()
    code = "\n".join("".join(cell["source"]) for cell in document["cells"]
                     if cell["cell_type"] == "code")
    prose = "\n".join("".join(cell["source"]) for cell in document["cells"]
                      if cell["cell_type"] == "markdown")
    assert "drive.mount('/content/drive')" in code
    assert "SET_MOUNTED_CYGNUS_ROOT" in code and "SET_PINNED_COMMIT" in code
    assert "7f155719674f7279080d7c54dcfe480d8688715e" in code and "rev-parse" in code
    assert "[test,mast" in code and "pytest" in code
    assert "'/content/scratch'" in code and "CYGNUS_SCRATCH" in code
    assert "colab_runs" in code and "_probe" in code and "rclone lsf" in code
    assert "cygnus.multi" in code and "archives" in code
    assert "'--jobs', '3'" in code and "cygnus.batch" in code
    assert "compare_campaigns" in code and "EQUIVALENCE.md" in code
    assert "build_manifest" in code and "verify_manifest" in code
    assert "committed_files" in code and "SET_OVERWRITE_COMMITTED_RECORDS" in code
    assert "read-only single-product pilot" in prose or "read-only" in prose
    assert "never merged" in prose or "never merged" in code
    assert "Resources panel" in prose and "compute units" in prose
    assert "rclone copy" not in code and "rclone sync" not in code
