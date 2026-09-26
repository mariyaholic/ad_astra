"""Where Cygnus data lives, in a form every CLI, harness and notebook can find.

Different harnesses reach the same Google Drive differently: one has an rclone remote called
``gdrive:``, another ``cygnus:``, a Colab runtime mounts ``/content/drive/MyDrive``. Remote names are
local configuration, so nothing shared may depend on them. Two rules make locations portable:

1. **Logical paths.** Every stored location is named by its path *inside the Drive folder*
   ``Cygnus/`` (``colab_runs/<batch>``, ``batches/<batch>``, ``data/tier1``). Each harness resolves
   that folder with :func:`resolve_route`: ``$CYGNUS_DRIVE`` if set (an rclone spec such as
   ``gdrive:Cygnus`` or a directory such as ``/content/drive/MyDrive/Cygnus``), else the Colab mount,
   else the first rclone Drive remote that has a ``Cygnus/`` folder.
2. **A committed index.** ``storage/locations.jsonl`` (one JSON object per line, in git, so every
   harness sees it) records each location: what wrote it and how, its manifest checksum, a browser
   link that opens it for the Drive owner, and which access routes were checked and could or could
   not see it. The same entry is written beside the data as ``LOCATION.json``.

Why visibility is recorded rather than assumed: a Drive token with the ``drive.file`` scope sees only
files created by the same OAuth app. Files a Colab ``drive.mount()`` writes are created by Colab's
app, so an rclone ``drive.file`` token does not see them (checked 2026-09-26: exit 3, directory not
found), while a broader token elsewhere does. :func:`check` records what *this* harness sees.

CLI: ``python -m cygnus.storage where | list | check [ID] | upload LOCAL PATH --kind K | add FILE``.
Nothing here reads or writes Drive outside ``Cygnus/``.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Callable
from urllib.parse import quote

from .config import WORKTREE, scratch_dir

DRIVE_FOLDER = "Cygnus"
INDEX = WORKTREE / "storage" / "locations.jsonl"
LOCATION_FILE = "LOCATION.json"
MANIFEST_NAME = "MANIFEST.sha256"
COLAB_MYDRIVE = Path("/content/drive/MyDrive")
KINDS = ("colab_run", "batch", "tier1_pack", "other")
# One writer kind per top-level area. A drive.file token cannot see folders another app created, so
# if both kinds wrote the same area, rclone would create a second, same-named folder beside the
# mount's (Drive allows duplicate names) and the logical path would stop meaning one place.
AREA_WRITER = {"colab_runs": "path", "batches": "rclone", "data": "rclone"}
SCHEMA = "cygnus.storage_location/1"

Runner = Callable[..., subprocess.CompletedProcess]


class StorageError(RuntimeError):
    pass


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def logical(path: str) -> str:
    """Normalise a location path relative to ``Cygnus/``; refuse anything that could leave it."""
    p = str(path).replace("\\", "/").strip("/")
    if p.startswith(DRIVE_FOLDER + "/"):
        p = p[len(DRIVE_FOLDER) + 1:]
    parts = PurePosixPath(p).parts
    if not p or p == DRIVE_FOLDER or any(x in ("..", ".") for x in parts) or ":" in p:
        raise StorageError(f"{path!r} is not a path inside {DRIVE_FOLDER}/")
    return "/".join(parts)


def search_url(path: str) -> str:
    """A Drive search for the location's folder name: works for the owner in any browser, no IDs."""
    return "https://drive.google.com/drive/search?q=" + quote(PurePosixPath(logical(path)).name)


def folder_url(folder_id: str | None) -> str | None:
    return f"https://drive.google.com/drive/folders/{folder_id}" if folder_id else None


# --------------------------------------------------------------------------- routes
@dataclass(frozen=True)
class Route:
    """How this harness reaches ``Cygnus/``: ``kind`` is ``rclone`` (``base`` = ``remote:Cygnus``) or
    ``path`` (``base`` = a directory); ``how`` says how it was found."""

    kind: str
    base: str
    how: str

    @property
    def label(self) -> str:
        """A harness-neutral description for visibility records (no host names or local paths)."""
        if self.kind == "rclone":
            return f"rclone remote {self.base.split(':', 1)[0]}:"
        return "Colab drive.mount" if self.base.startswith(str(COLAB_MYDRIVE)) else "mounted folder"

    def join(self, path: str) -> str:
        rel = logical(path)
        return f"{self.base.rstrip('/')}/{rel}" if self.kind == "rclone" else str(Path(self.base) / rel)


def _is_rclone_spec(value: str) -> bool:
    # "gdrive:Cygnus" is an rclone spec; "G:/My Drive/Cygnus" and "C:\\x" are Windows paths
    return bool(re.match(r"^[A-Za-z0-9_.\- ]{2,}:", value)) and not re.match(r"^[A-Za-z]:[\\/]", value)


def _rclone(args: list[str], run: Runner, timeout: int = 300) -> subprocess.CompletedProcess:
    if run is subprocess.run and not shutil.which("rclone"):
        raise StorageError("rclone is not on PATH")
    return run(["rclone", *args], capture_output=True, text=True, timeout=timeout)


def resolve_route(env: dict | None = None, run: Runner = subprocess.run,
                  colab_mydrive: Path = COLAB_MYDRIVE) -> Route | None:
    env = os.environ if env is None else env
    value = (env.get("CYGNUS_DRIVE") or "").strip()
    if value:
        if _is_rclone_spec(value):
            return Route("rclone", value.rstrip("/"), "CYGNUS_DRIVE")
        return Route("path", str(Path(value)), "CYGNUS_DRIVE")
    if (colab_mydrive / DRIVE_FOLDER).is_dir():
        return Route("path", str(colab_mydrive / DRIVE_FOLDER), "Colab mount")
    try:
        out = _rclone(["listremotes", "--long"], run, timeout=60)
    except (StorageError, OSError, subprocess.TimeoutExpired):
        return None
    for line in out.stdout.splitlines():
        name, _, kind = line.partition(":")
        if kind.strip() != "drive":
            continue
        probe = _rclone(["lsf", f"{name}:{DRIVE_FOLDER}", "--max-depth", "1"], run, timeout=120)
        if probe.returncode == 0:
            return Route("rclone", f"{name}:{DRIVE_FOLDER}", "rclone auto-detect")
    return None


def require_route(**kw) -> Route:
    route = resolve_route(**kw)
    if route is None:
        raise StorageError("no route to the Drive folder Cygnus/ in this harness: set CYGNUS_DRIVE to an "
                           "rclone spec (e.g. gdrive:Cygnus) or a mounted directory")
    return route


def visible(route: Route, path: str, run: Runner = subprocess.run) -> bool:
    if route.kind == "path":
        return Path(route.join(path)).is_dir()
    return _rclone(["lsf", route.join(path), "--max-depth", "1"], run, timeout=120).returncode == 0


def remote_hashes(route: Route, path: str, run: Runner = subprocess.run) -> dict[str, str]:
    """``{relative POSIX path: sha256}`` of every file under the location, as the route reads it."""
    if route.kind == "path":
        from .colab import sha256_file

        root = Path(route.join(path))
        return {f.relative_to(root).as_posix(): sha256_file(f) for f in sorted(root.rglob("*")) if f.is_file()}
    out = _rclone(["hashsum", "sha256", route.join(path)], run, timeout=900)
    if out.returncode != 0:
        raise StorageError(f"rclone hashsum failed for {route.join(path)}: {out.stderr.strip()[-300:]}")
    rows = (ln.split(None, 1) for ln in out.stdout.splitlines() if ln.strip())
    return {name.strip(): h for h, name in rows}


def folder_id(route: Route, path: str, run: Runner = subprocess.run) -> str | None:
    """The Drive folder ID of a location, when the route can tell (rclone: from the parent listing;
    a Colab mount: the ``user.drive.id`` extended attribute). ``None`` when it cannot."""
    rel = logical(path)
    if route.kind == "path":
        try:
            return os.getxattr(route.join(rel), "user.drive.id").decode() or None  # type: ignore[attr-defined]
        except (AttributeError, OSError):
            return None
    parent, name = str(PurePosixPath(rel).parent), PurePosixPath(rel).name
    target = route.base if parent == "." else route.join(parent)
    out = _rclone(["lsjson", target, "--dirs-only"], run, timeout=120)
    if out.returncode != 0:
        return None
    for item in json.loads(out.stdout or "[]"):
        if item.get("Name") == name:
            return item.get("ID")
    return None


# --------------------------------------------------------------------------- index
def read_index(index: Path = INDEX) -> list[dict]:
    if not index.is_file():
        return []
    return [json.loads(ln) for ln in index.read_text(encoding="utf-8").splitlines() if ln.strip()]


def write_index(entries: list[dict], index: Path = INDEX) -> Path:
    index.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(json.dumps(e, sort_keys=True, ensure_ascii=False) + "\n"
                   for e in sorted(entries, key=lambda e: e["id"]))
    index.write_text(body, encoding="utf-8", newline="\n")
    return index


def validate(entry: dict) -> dict:
    missing = [k for k in ("id", "kind", "drive_path", "created_utc", "writer", "producer") if not entry.get(k)]
    if missing:
        raise StorageError(f"location entry lacks {missing}")
    if entry["kind"] not in KINDS:
        raise StorageError(f"kind {entry['kind']!r} not in {KINDS}")
    if entry["id"] != logical(entry["id"]) or entry["drive_path"] != f"{DRIVE_FOLDER}/{entry['id']}":
        raise StorageError(f"id/drive_path mismatch: {entry['id']!r} vs {entry['drive_path']!r}")
    local = entry.get("local_copy")
    if local is not None and not str(local).startswith("scratch:"):
        raise StorageError("local_copy must be scratch-relative ('scratch:<path>'), never a machine path")
    for key in ("links",):
        for url in (entry.get(key) or {}).values():
            if url and not str(url).startswith("https://drive.google.com/"):
                raise StorageError(f"unexpected link {url!r}")
    return entry


def make_entry(path: str, *, kind: str, writer: str, producer: str, commit: str | None = None,
               manifest_sha256: str | None = None, files: int | None = None, drive_folder_id: str | None = None,
               local_copy: str | None = None, notes: str | None = None, created_utc: str | None = None) -> dict:
    rel = logical(path)
    return validate({
        "schema": SCHEMA, "id": rel, "kind": kind, "drive_path": f"{DRIVE_FOLDER}/{rel}",
        "created_utc": created_utc or utc_now(), "writer": writer, "producer": producer, "commit": commit,
        "manifest_sha256": manifest_sha256, "files": files, "drive_folder_id": drive_folder_id,
        "links": {"folder": folder_url(drive_folder_id), "search": search_url(rel)},
        "local_copy": local_copy, "visible_via": {}, "notes": notes,
    })


def upsert(entry: dict, index: Path = INDEX) -> dict:
    """Add or update an entry; visibility observations already recorded are kept and merged."""
    validate(entry)
    entries = read_index(index)
    old = next((e for e in entries if e["id"] == entry["id"]), None)
    if old:
        merged = {**old, **{k: v for k, v in entry.items() if v not in (None, {}, "")}}
        merged["visible_via"] = {**old.get("visible_via", {}), **entry.get("visible_via", {})}
        if merged.get("drive_folder_id"):
            merged["links"] = {"folder": folder_url(merged["drive_folder_id"]), "search": search_url(merged["id"])}
        entry = merged
    write_index([e for e in entries if e["id"] != entry["id"]] + [entry], index)
    return entry


def record_visibility(entry_id: str, label: str, seen: bool, index: Path = INDEX, note: str | None = None) -> dict:
    entries = read_index(index)
    entry = next((e for e in entries if e["id"] == logical(entry_id)), None)
    if entry is None:
        raise StorageError(f"no location {entry_id!r} in {index.name}")
    obs = {"state": "visible" if seen else "not_visible", "utc": utc_now()}
    if note:
        obs["note"] = note
    entry.setdefault("visible_via", {})[label] = obs
    write_index(entries, index)
    return entry


def scratch_relative(local: Path) -> str | None:
    try:
        return "scratch:" + Path(local).resolve().relative_to(scratch_dir().resolve()).as_posix()
    except ValueError:
        return None


# --------------------------------------------------------------------------- upload
def upload(local: Path, path: str, *, kind: str, producer: str, route: Route | None = None,
           run: Runner = subprocess.run, commit: str | None = None, notes: str | None = None,
           index: Path = INDEX) -> dict:
    """Copy a local directory to ``Cygnus/<path>`` through this harness's route, verify every file's
    SHA-256 *as read back from Drive*, write ``LOCATION.json`` beside it and record it in the index.

    A manifest (``MANIFEST.sha256``) is written into ``local`` first when it has none. Refuses to
    overwrite a location whose remote files differ from the local ones."""
    from .colab import build_manifest, read_manifest, sha256_file, write_manifest

    local = Path(local)
    if not local.is_dir():
        raise StorageError(f"{local} is not a directory")
    route = route or require_route(run=run)
    rel = logical(path)
    area = rel.split("/", 1)[0]
    if area not in AREA_WRITER:
        raise StorageError(f"unknown area {area!r}: use one of {sorted(AREA_WRITER)} (docs/STORAGE.md)")
    if AREA_WRITER[area] != route.kind:
        raise StorageError(f"{area}/ is written only through a {AREA_WRITER[area]} route; this harness reaches "
                           f"Drive through {route.label} (a second, same-named folder would appear)")
    man_path = local / MANIFEST_NAME
    if not man_path.is_file():
        files = [p.relative_to(local).as_posix() for p in local.rglob("*")
                 if p.is_file() and p.name not in (MANIFEST_NAME, LOCATION_FILE)]
        write_manifest(man_path, build_manifest(local, files), comment=f"Cygnus/{rel}; written by cygnus.storage")
    manifest = read_manifest(man_path)
    if route.kind == "path":
        shutil.copytree(local, route.join(rel), dirs_exist_ok=True)
    else:
        out = _rclone(["copy", str(local), route.join(rel), "--checksum", "--immutable"], run, timeout=3600)
        if out.returncode != 0:
            raise StorageError(f"rclone copy failed: {out.stderr.strip()[-400:]}")
    seen = remote_hashes(route, rel, run)
    bad = sorted(f for f, h in manifest.items() if seen.get(f) != h)
    if bad:
        raise StorageError(f"{len(bad)} file(s) not read back identically from {route.label} Cygnus/{rel}: {bad[:5]}")
    entry = make_entry(rel, kind=kind, writer=route.label, producer=producer, commit=commit,
                       manifest_sha256=sha256_file(man_path), files=len(manifest),
                       drive_folder_id=folder_id(route, rel, run), local_copy=scratch_relative(local), notes=notes)
    entry["visible_via"] = {route.label: {"state": "visible", "utc": utc_now(),
                                          "note": f"{len(manifest)} file(s) read back, SHA-256 identical"}}
    loc = local / LOCATION_FILE
    loc.write_text(json.dumps(entry, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if route.kind == "path":
        shutil.copyfile(loc, Path(route.join(rel)) / LOCATION_FILE)
    else:
        out = _rclone(["copyto", str(loc), route.join(f"{rel}/{LOCATION_FILE}")], run, timeout=300)
        if out.returncode != 0:
            raise StorageError(f"could not write {LOCATION_FILE}: {out.stderr.strip()[-300:]}")
    return upsert(entry, index)


# --------------------------------------------------------------------------- CLI
def _table(entries: list[dict]) -> str:
    lines = []
    for e in entries:
        link = e["links"].get("folder") or e["links"]["search"]
        vis = ", ".join(f"{k}: {v['state']}" for k, v in sorted(e.get("visible_via", {}).items())) or "unchecked"
        lines.append(f"{e['id']}  [{e['kind']}; {e['files'] or '?'} file(s); written by {e['writer']}]\n"
                     f"    {link}\n    visibility: {vis}")
    return "\n".join(lines) or "(no locations recorded)"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m cygnus.storage", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("where", help="show how this harness reaches Cygnus/ and where scratch is")
    sub.add_parser("list", help="every recorded location, with links and visibility")
    c = sub.add_parser("check", help="record whether this harness can see each location (or one)")
    c.add_argument("id", nargs="?")
    u = sub.add_parser("upload", help="copy a local directory to Cygnus/<path>, verify, record")
    u.add_argument("local")
    u.add_argument("path")
    u.add_argument("--kind", required=True, choices=KINDS)
    u.add_argument("--producer", required=True, help="what produced it, e.g. 'cygnus.batch suite-2026-09-26'")
    u.add_argument("--commit")
    u.add_argument("--notes")
    a = sub.add_parser("add", help="record an entry from a LOCATION.json (e.g. written by the Colab notebook)")
    a.add_argument("file")
    args = ap.parse_args(argv)

    if args.cmd == "where":
        route = resolve_route()
        print(json.dumps({"route": None if route is None else {"kind": route.kind, "base": route.base,
                                                               "found_by": route.how, "label": route.label},
                          "index": str(INDEX.relative_to(WORKTREE).as_posix()), "locations": len(read_index())},
                         indent=1))
        return 0 if route else 1
    if args.cmd == "list":
        print(_table(read_index()))
        return 0
    if args.cmd == "check":
        route = require_route()
        ids = [logical(args.id)] if args.id else [e["id"] for e in read_index()]
        for i in ids:
            seen = visible(route, i)
            record_visibility(i, route.label, seen)
            print(f"{'visible    ' if seen else 'NOT visible'}  {i}  via {route.label}")
        return 0
    if args.cmd == "upload":
        e = upload(Path(args.local), args.path, kind=args.kind, producer=args.producer,
                   commit=args.commit, notes=args.notes)
        print(_table([e]))
        return 0
    if args.cmd == "add":
        entry = json.loads(Path(args.file).read_text(encoding="utf-8"))
        print(_table([upsert(entry)]))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
