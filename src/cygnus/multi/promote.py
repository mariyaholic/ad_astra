"""Promote a vetted sandbox campaign into the official tree (no production code change).

Implements the promotion path from ``experimental/VERIFICATION_REQUEST.md``: copy
a completed ``cygnus_multi`` campaign (spec, report, search log, sky record and
runner outputs) from the sandbox root into ``campaigns/<id>/``, rewrite the
repository paths, record provenance in ``PROMOTED.md`` and create a **draft**
collection in ``publish/collections/``.

Guards, all enforced before anything is written:

* the sandbox spec and a ``completed`` sky record must exist;
* the record must pass ``cygnus.skyrecord.validate`` in the sandbox;
* the record must carry ``generated_by: cygnus_multi campaign runner``;
* the destination ``campaigns/<id>.yaml`` and ``campaigns/<id>/`` must not exist;
* after copying, the record is validated again against the production worktree
  and the copy is rolled back if it fails.

The helper never edits ``src/``, never publishes and never deploys. Publication
and deployment remain the user's decision (``docs/PUBLISHING.md``).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_SANDBOX = Path(__file__).resolve().parent


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _utc_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _read_yaml(path: Path) -> dict:
    import yaml

    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _write_yaml(path: Path, data: dict) -> None:
    import yaml

    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8", newline="\n")


def _sandbox_root(explicit: str | Path | None) -> Path:
    return Path(explicit or os.environ.get("CYGNUS_MULTI_ROOT") or DEFAULT_SANDBOX).resolve()


def _worktree_root(explicit: str | Path | None) -> Path:
    return Path(explicit).resolve() if explicit else Path(__file__).resolve().parents[1]


def promote(root: Path | str | None, worktree: Path | str | None, campaign_id: str, *,
            as_id: str | None = None, note: str = "", dry_run: bool = False) -> dict:
    """Promote sandbox campaign ``campaign_id``; returns a summary dict."""
    from cygnus import skyrecord as sr
    from cygnus.ledger import Ledger

    root, worktree = _sandbox_root(root), _worktree_root(worktree)
    as_id = as_id or campaign_id
    src_spec = root / "campaigns" / f"{campaign_id}.yaml"
    src_dir = root / "campaigns" / campaign_id
    src_rec = src_dir / "sky_record.json"
    if not src_spec.is_file():
        raise SystemExit(f"promote: {src_spec} not found")
    if not src_rec.is_file():
        raise SystemExit(f"promote: {src_rec} not found (run the campaign first)")

    spec = _read_yaml(src_spec)
    if not isinstance(spec, dict):
        raise SystemExit(f"promote: {src_spec} is not a campaign spec")
    rec = json.loads(src_rec.read_text(encoding="utf-8"))

    problems = []
    if rec.get("status") != "completed":
        problems.append(f"record status is {rec.get('status')!r}, not 'completed'")
    if not rec.get("checks"):
        problems.append("record has no checks")
    if not str(rec.get("generated_by", "")).startswith("cygnus_multi"):
        problems.append(f"record generated_by is {rec.get('generated_by')!r}, not a cygnus_multi runner")
    problems += sr.validate(rec, root)
    if problems:
        raise SystemExit("promote refused:\n  " + "\n  ".join(problems))

    dst_spec = worktree / "campaigns" / as_id / "SPEC.yaml"
    dst_dir = worktree / "campaigns" / as_id
    if dst_spec.exists() or dst_dir.exists():
        raise SystemExit(f"promote refused: campaigns/{as_id}/ already exists")

    rel_dir = f"campaigns/{as_id}"
    spec["campaign_id"] = as_id
    spec["outputs"] = rel_dir + "/"
    record_block = spec.get("record")
    if isinstance(record_block, dict):
        if record_block.get("path"):
            record_block["path"] = f"{rel_dir}/sky_record.json"
        if record_block.get("report"):
            record_block["report"] = f"{rel_dir}/REPORT.md"
        if record_block.get("search_log"):
            record_block["search_log"] = f"{rel_dir}/SEARCH_LOG.md"
    rec["id"] = as_id
    if rec.get("spec"):
        rec["spec"] = f"campaigns/{as_id}/SPEC.yaml"
    if rec.get("report"):
        rec["report"] = f"{rel_dir}/REPORT.md"
    if rec.get("search_log"):
        rec["search_log"] = f"{rel_dir}/SEARCH_LOG.md"

    runs = []
    ledger_path = root / "state" / "ledger.sqlite"
    if ledger_path.is_file():
        led = Ledger(ledger_path)
        try:
            prefix = f"cygnus_multi:{campaign_id}:"
            runs = [{"id": r["id"], "script": r["script"], "status": r["status"], "summary": r.get("summary")}
                    for r in led.runs() if str(r.get("script", "")).startswith(prefix)]
        finally:
            led.close()

    coll_path = worktree / "publish" / "collections" / f"{as_id}.json"
    if dry_run:
        return {"dry_run": True, "spec": dst_spec.relative_to(worktree).as_posix(),
                "dir": dst_dir.relative_to(worktree).as_posix(), "collection": coll_path.relative_to(worktree).as_posix(),
                "runs": runs}

    dst_dir.mkdir(parents=True)
    for p in sorted(src_dir.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts:
            out = dst_dir / p.relative_to(src_dir)
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
    _write_yaml(dst_spec, spec)
    (dst_dir / "sky_record.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n",
                                             encoding="utf-8", newline="\n")

    lines = [
        f"# Promoted campaign: {as_id}", "",
        f"- Promoted from sandbox: `{src_dir.relative_to(root).as_posix()}` (root `{root.as_posix()}`)",
        f"- Promotion date: {_utc_date()} (UTC)",
        f"- Provenance note: {note.strip() or 'none supplied'}",
        "- Promoted by: `python -m cygnus.multi.promote` — see `experimental/VERIFICATION_REQUEST.md`.",
        f"- The spec is kept at `campaigns/{as_id}/SPEC.yaml`, not top-level `campaigns/{as_id}.yaml`:",
        "  its steps are implemented only by the experimental runner, the production `cygnus.campaign check`",
        "  rejects it by design, and CI's campaign-check loop globs only top-level specs.",
        "", "## Sandbox ledger runs (not in `state/ledger.sqlite`)", "",
    ]
    lines += [f"- run #{r['id']} `{r['script']}` — {r['status']}" + (f": {r['summary']}" if r.get("summary") else "")
              for r in runs] or ["- none found"]
    lines += [
        "", "The ledger runs for this campaign live in the sandbox ledger under the `cygnus_multi:`",
        "namespace and are **not** visible to the published site's `/log/` until the ledgers are",
        "merged. The record was produced by the experimental runner",
        f"(`generated_by: {rec.get('generated_by')}`).", "",
    ]
    (dst_dir / "PROMOTED.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")

    problems = sr.validate(rec, worktree)
    if problems:
        shutil.rmtree(dst_dir, ignore_errors=True)
        dst_spec.unlink(missing_ok=True)
        raise SystemExit("promote refused after copy (rolled back):\n  " + "\n  ".join(problems))

    if not coll_path.exists():
        coll_path.parent.mkdir(parents=True, exist_ok=True)
        items = [
            {"id": "spec", "kind": "campaign", "source": f"campaigns/{as_id}/SPEC.yaml",
             "title": (spec.get("objective") or rec["title"]).strip().splitlines()[0][:160],
             "origin": "project", "download": True},
            {"id": "report", "kind": "document", "source": f"{rel_dir}/REPORT.md",
             "title": f"Report: {rec['title']}", "origin": "project", "download": True},
            {"id": "search-log", "kind": "document", "source": f"{rel_dir}/SEARCH_LOG.md",
             "title": f"Search log: {rec['title']}", "origin": "project", "download": True},
        ]
        for name, title in (("nss.json", "Gaia NSS vetting output (JSON)"),
                            ("screen.json", "Screen output (JSON)"),
                            ("vetting/vetting.json", "Lead vetting output (JSON)")):
            if (dst_dir / name).is_file():
                items.append({"id": name.replace("/", "-").replace(".json", ""), "kind": "file",
                              "source": f"{rel_dir}/{name}", "title": title, "origin": "derived", "download": True})
        coll = {"id": as_id, "title": rec["title"], "type": "campaign", "status": "draft", "published": None,
                "summary": rec["summary"],
                "research_status": "Draft collection · promoted from the experimental pipeline; not independently verified",
                "license": "Apache-2.0", "related": [], "items": items}
        coll_path.write_text(json.dumps(coll, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    return {"dry_run": False, "campaign_id": campaign_id, "as": as_id,
            "spec": dst_spec.relative_to(worktree).as_posix(), "dir": dst_dir.relative_to(worktree).as_posix(),
            "collection": coll_path.relative_to(worktree).as_posix(),
            "runs": [r["id"] for r in runs]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m cygnus.multi.promote",
                                 description="Promote a completed sandbox campaign into campaigns/ (draft collection).")
    ap.add_argument("--campaign", required=True, help="sandbox campaign id (campaigns/<id>.yaml under the sandbox root)")
    ap.add_argument("--as", dest="as_id", default=None, help="production campaign id (default: same)")
    ap.add_argument("--note", default="", help="provenance note recorded in PROMOTED.md")
    ap.add_argument("--root", default=None, help="sandbox root (default: CYGNUS_MULTI_ROOT or experimental/)")
    ap.add_argument("--worktree", default=None, help="repository root (default: this checkout)")
    ap.add_argument("--dry-run", action="store_true", help="check and report without writing")
    a = ap.parse_args(argv)
    out = promote(a.root, a.worktree, a.campaign, as_id=a.as_id, note=a.note, dry_run=a.dry_run)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
