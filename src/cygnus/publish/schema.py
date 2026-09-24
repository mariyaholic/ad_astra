"""Publication manifest schema — the explicit boundary between the private
research store and the public site.

Nothing reaches the site unless an operator lists it in a collection file
under ``publish/collections/<id>.json`` with ``"status": "published"``.
Everything else — the full ledger, scratch, Drive, credentials — stays
private by default. See ``docs/PUBLISHING.md``.

Vocabulary:

* ``status``  (collection): ``draft`` (not built) | ``published`` |
  ``withdrawn`` (tombstone page at the same URL, no files);
* ``access``  (item): ``public`` | ``restricted`` (listed with a reason, never
  served);
* ``origin``  (item): ``project`` (authored here) | ``derived`` (computed here
  from other data) | ``third_party`` (archive products — linked, never
  redistributed unless ``redistribution_ok`` is set after a license check).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

COLLECTION_TYPES = ("documents", "dataset", "campaign", "software", "candidates", "measurements")
PUBLICATION_STATUSES = ("draft", "published", "withdrawn")
ACCESS_STATES = ("public", "restricted")
ORIGINS = ("project", "derived", "third_party")
ITEM_KINDS = (
    "document",          # worktree Markdown rendered as a page (redacted)
    "campaign",          # campaigns/*.yaml spec
    "archive_manifest",  # sanitized manifest snapshot under publish/data/
    "ledger_run",        # one ledger run + its measurements (read-only)
    "ledger_runs",       # all runs of one script (search log)
    "module_register",   # module/status table from a Markdown section
    "candidate",         # CandidateRecord JSON under publish/candidates/
    "file",              # an operator-supplied file under publish/files/
)

# Kinds whose ``source`` must be a file, and the extensions each accepts.
SOURCE_EXTENSIONS: dict[str, tuple[str, ...]] = {
    "document": (".md",),
    "campaign": (".yaml", ".yml"),
    "archive_manifest": (".json",),
    "module_register": (".md",),
    "candidate": (".json",),
    "file": (".csv", ".json", ".md", ".txt", ".yaml", ".yml", ".fits", ".png",
             ".jpg", ".jpeg", ".svg", ".pdf", ".zip", ".ecsv", ".vot", ".xml"),
}

MAX_FILE_BYTES = 50 * 1024 * 1024  # per published file; raise deliberately, not silently


class PublicationError(ValueError):
    """A collection or item would violate the publication rules."""


@dataclass
class Item:
    id: str
    kind: str
    title: str | None = None
    source: str | None = None
    description: str | None = None
    origin: str = "project"
    access: str = "public"
    access_note: str | None = None
    download: bool = False
    redistribution_ok: bool = False
    license: str | None = None
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class Collection:
    id: str
    title: str
    type: str
    status: str
    summary: str
    items: list[Item]
    published: str | None = None
    updated: str | None = None
    description_md: str | None = None
    research_status: str | None = None
    license: str | None = None
    citation: str | None = None
    related: list[str] = field(default_factory=list)
    withdrawn: dict[str, str] | None = None
    manifest_path: str | None = None

    @property
    def is_public(self) -> bool:
        return self.status == "published"


_ITEM_KEYS = {
    "id", "kind", "title", "source", "description", "origin", "access",
    "access_note", "download", "redistribution_ok", "license", "params",
}
_COLL_KEYS = {
    "id", "title", "type", "status", "summary", "items", "published", "updated",
    "description_md", "research_status", "license", "citation", "related",
    "withdrawn",
}


def _need(cond: bool, errors: list[str], msg: str) -> None:
    if not cond:
        errors.append(msg)


def parse_item(raw: dict[str, Any], where: str, errors: list[str]) -> Item | None:
    unknown = set(raw) - _ITEM_KEYS
    _need(not unknown, errors, f"{where}: unknown item keys {sorted(unknown)}")
    iid = raw.get("id", "")
    _need(isinstance(iid, str) and bool(SLUG_RE.match(iid)), errors,
          f"{where}: item id {iid!r} must be a lowercase slug")
    kind = raw.get("kind")
    _need(kind in ITEM_KINDS, errors, f"{where}: kind {kind!r} not in {ITEM_KINDS}")
    origin = raw.get("origin", "project")
    _need(origin in ORIGINS, errors, f"{where}: origin {origin!r} not in {ORIGINS}")
    access = raw.get("access", "public")
    _need(access in ACCESS_STATES, errors, f"{where}: access {access!r} not in {ACCESS_STATES}")
    if access == "restricted":
        _need(bool(raw.get("access_note")), errors,
              f"{where}: restricted items need an access_note explaining why")
    if kind in SOURCE_EXTENSIONS:
        src = raw.get("source")
        _need(isinstance(src, str) and bool(src), errors, f"{where}: kind {kind} requires 'source'")
        if isinstance(src, str) and src:
            _need(src.lower().endswith(SOURCE_EXTENSIONS[kind]), errors,
                  f"{where}: source {src!r} extension not allowed for {kind}")
    if raw.get("download") and origin == "third_party" and not raw.get("redistribution_ok"):
        errors.append(
            f"{where}: third-party material cannot be downloadable without "
            "'redistribution_ok': true (record the license check first)"
        )
    if errors and any(e.startswith(where + ":") for e in errors):
        return None
    return Item(
        id=iid, kind=kind, title=raw.get("title"), source=raw.get("source"),
        description=raw.get("description"), origin=origin, access=access,
        access_note=raw.get("access_note"), download=bool(raw.get("download")),
        redistribution_ok=bool(raw.get("redistribution_ok")), license=raw.get("license"),
        params=dict(raw.get("params") or {}),
    )


def parse_collection(raw: dict[str, Any], where: str = "collection") -> Collection:
    """Validate one collection dict; raise PublicationError listing every problem."""
    errors: list[str] = []
    unknown = set(raw) - _COLL_KEYS
    _need(not unknown, errors, f"{where}: unknown keys {sorted(unknown)}")
    cid = raw.get("id", "")
    _need(isinstance(cid, str) and bool(SLUG_RE.match(cid)), errors,
          f"{where}: id {cid!r} must be a lowercase slug (it becomes a permanent URL)")
    for key in ("title", "summary"):
        _need(isinstance(raw.get(key), str) and raw[key].strip() != "", errors,
              f"{where}: '{key}' is required")
    ctype = raw.get("type")
    _need(ctype in COLLECTION_TYPES, errors, f"{where}: type {ctype!r} not in {COLLECTION_TYPES}")
    status = raw.get("status")
    _need(status in PUBLICATION_STATUSES, errors,
          f"{where}: status {status!r} not in {PUBLICATION_STATUSES}")
    for key in ("published", "updated"):
        if raw.get(key) is not None:
            _need(bool(DATE_RE.match(str(raw[key]))), errors, f"{where}: {key} must be YYYY-MM-DD")
    if status == "published":
        _need(bool(raw.get("published")), errors, f"{where}: published collections need a 'published' date")
    if status == "withdrawn":
        wd = raw.get("withdrawn") or {}
        _need(bool(DATE_RE.match(str(wd.get("date", "")))) and bool(wd.get("reason")), errors,
              f"{where}: withdrawn collections need withdrawn.date (YYYY-MM-DD) and withdrawn.reason")
    items: list[Item] = []
    seen: set[str] = set()
    for i, raw_item in enumerate(raw.get("items") or []):
        item = parse_item(raw_item, f"{where}.items[{i}]", errors)
        if item is not None:
            _need(item.id not in seen, errors, f"{where}: duplicate item id {item.id!r}")
            seen.add(item.id)
            items.append(item)
    if errors:
        raise PublicationError("\n".join(errors))
    return Collection(
        id=cid, title=raw["title"], type=ctype, status=status, summary=raw["summary"],
        items=items, published=raw.get("published"), updated=raw.get("updated"),
        description_md=raw.get("description_md"), research_status=raw.get("research_status"),
        license=raw.get("license"), citation=raw.get("citation"),
        related=list(raw.get("related") or []), withdrawn=raw.get("withdrawn"),
    )


def load_collections(publish_root: Path) -> list[Collection]:
    """Load every ``collections/*.json``; file stem must equal the id."""
    out: list[Collection] = []
    errors: list[str] = []
    for path in sorted((publish_root / "collections").glob("*.json")):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            coll = parse_collection(raw, where=path.name)
            if coll.id != path.stem:
                raise PublicationError(f"{path.name}: file name must match id {coll.id!r}")
            coll.manifest_path = f"publish/collections/{path.name}"
            out.append(coll)
        except (PublicationError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
    if errors:
        raise PublicationError("\n".join(errors))
    return out
