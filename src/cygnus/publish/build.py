"""Static site builder: curated collections + read-only ledger -> ``build/site``.

The build is the publication boundary made executable:

* only ``status: published`` collections produce pages or files;
* withdrawn collections keep their URL as a tombstone with no content;
* item sources are confined by ``safety.resolve_source``;
* downloads are written only for public items with ``download: true``;
* the ledger is opened ``mode=ro`` and only allowlisted fields are rendered;
* a leak scan over the finished output aborts the build on any private path,
  remote name, credential-shaped string or e-mail.
"""

from __future__ import annotations

import csv
import io
import json
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

from .. import __version__
from ..config import WORKTREE, ledger_path
from ..ledger import Ledger
from ..reporting.leads_board import _ORDER as EVIDENCE_ORDER
from . import markdown, sources
from .safety import redact, resolve_source, scan_for_leaks
from .schema import MAX_FILE_BYTES, Collection, Item, PublicationError, load_collections

PKG_DIR = Path(__file__).resolve().parent
TEMPLATES = PKG_DIR / "templates"
STATIC = PKG_DIR / "static"

TYPE_LABELS = {
    "collection": "Collection",
    "document": "Document",
    "dataset": "Dataset",
    "campaign": "Campaign",
    "software": "Software",
    "candidate": "Candidate dossier",
    "measurements": "Measurements",
}
AVAILABILITY_LABELS = {
    "download": "Download available",
    "online": "Read online",
    "link": "Linked to source archive",
    "restricted": "Not public",
    "withdrawn": "Withdrawn",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class BuildConfig:
    worktree: Path = WORKTREE
    publish_root: Path | None = None
    out_dir: Path | None = None
    ledger: Path | None = None
    build_utc: str | None = None

    def __post_init__(self) -> None:
        self.worktree = Path(self.worktree)
        self.publish_root = Path(self.publish_root or self.worktree / "publish")
        self.out_dir = Path(self.out_dir or self.worktree / "build" / "site")
        self.build_utc = self.build_utc or utc_now()


@dataclass
class BuildResult:
    out_dir: Path
    pages: list[str] = field(default_factory=list)
    files: list[dict[str, Any]] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class SiteBuilder:
    def __init__(self, cfg: BuildConfig):
        self.cfg = cfg
        self.site = self._load_site_config()
        self.base = self.site.get("base_path", "/").rstrip("/") + "/"
        self.env = Environment(
            loader=FileSystemLoader(str(TEMPLATES)),
            autoescape=select_autoescape(["html", "j2"]),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.globals.update(url=self.url, fmt_bytes=fmt_bytes, TYPE_LABELS=TYPE_LABELS,
                                AVAILABILITY_LABELS=AVAILABILITY_LABELS, site=self.site,
                                build_utc=cfg.build_utc, version=__version__)
        self.env.filters["short_hash"] = lambda h: (h[:12] + "…") if h and len(h) > 16 else h
        self.env.filters["date"] = lambda ts: ts[:10] if ts else None
        self.env.filters["uniq_links"] = uniq_links
        self.result = BuildResult(out_dir=cfg.out_dir)
        self.ledger: Ledger | None = None
        self.register: list[dict[str, str]] | None = None
        self.register_url: str | None = None
        self.entries: list[dict[str, Any]] = []
        self.page_ids: dict[str, str] = {}
        self._pending_docs: list[tuple[Collection, Item, dict[str, Any]]] = []
        self._pending_campaigns: list[tuple[Collection, Item, dict[str, Any]]] = []
        self._pending_candidates: list[tuple[Collection, Item, dict[str, Any]]] = []
        self._log_runs: list[dict[str, Any]] = []

    # ---------------------------------------------------------------- helpers
    def _load_site_config(self) -> dict[str, Any]:
        path = self.cfg.publish_root / "site.json"
        if not path.is_file():
            raise PublicationError(f"missing {path.name} in publish root")
        return json.loads(path.read_text(encoding="utf-8"))

    def url(self, path: str = "") -> str:
        return self.base + path.lstrip("/")

    def write_page(self, rel: str, template: str, **ctx: Any) -> None:
        html = self.env.get_template(template).render(page_path=rel, **ctx)
        dest = self.cfg.out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        self.result.pages.append(rel)

    def write_file(self, coll: Collection, item_id: str, filename: str, data: bytes,
                   *, label: str, media: str, origin: str) -> dict[str, Any]:
        if len(data) > MAX_FILE_BYTES:
            raise PublicationError(f"{coll.id}/{item_id}/{filename}: {len(data)} bytes exceeds limit")
        rel = f"files/{coll.id}/{item_id}/{filename}"
        dest = self.cfg.out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        info = {"url": self.url(rel), "path": rel, "filename": filename, "bytes": len(data),
                "sha256": sources.sha256_bytes(data), "label": label, "media": media,
                "origin": origin}
        self.result.files.append(info)
        return info

    def claim_page(self, key: str, owner: str) -> None:
        if key in self.page_ids:
            raise PublicationError(f"page {key!r} claimed by both {self.page_ids[key]} and {owner}")
        self.page_ids[key] = owner

    # ------------------------------------------------------------------ build
    def build(self) -> BuildResult:
        cfg = self.cfg
        collections = load_collections(cfg.publish_root)
        led_path = Path(cfg.ledger) if cfg.ledger else ledger_path()
        if led_path.is_file():
            self.ledger = Ledger.open_readonly(led_path)
        else:
            self.result.warnings.append("ledger not found; ledger-backed items render as unavailable")
        try:
            if cfg.out_dir.exists():
                shutil.rmtree(cfg.out_dir)
            cfg.out_dir.mkdir(parents=True)
            shutil.copytree(STATIC, cfg.out_dir / "static")
            self._load_register(collections)
            public = [c for c in collections if c.status == "published"]
            views = [self._collection_view(c) for c in public]
            withdrawn = [c for c in collections if c.status == "withdrawn"]
            for c in collections:
                if c.status == "draft":
                    self.result.skipped.append(f"{c.id} (draft — not built)")
            self._render_all(views, withdrawn)
        finally:
            if self.ledger is not None:
                self.ledger.close()
        leaks = scan_for_leaks(cfg.out_dir)
        if leaks:
            shutil.rmtree(cfg.out_dir)
            raise PublicationError("leak scan failed; output removed:\n" + "\n".join(leaks))
        return self.result

    def _load_register(self, collections: list[Collection]) -> None:
        for c in collections:
            if c.status != "published":
                continue
            for it in c.items:
                if it.kind == "module_register" and it.access == "public":
                    path = resolve_source(self.cfg.worktree, it.kind, it.source)
                    self.register = sources.load_module_register(path, it.params.get("heading", "Layer-2 module register"))
                    self.register_url = self.url(f"collections/{c.id}/#{it.id}")
                    return

    # ------------------------------------------------------ collection model
    def _collection_view(self, c: Collection) -> dict[str, Any]:
        view: dict[str, Any] = {
            "id": c.id, "title": c.title, "type": c.type, "summary": c.summary,
            "published": c.published, "updated": c.updated, "license": c.license,
            "research_status": c.research_status, "citation": c.citation,
            "description_html": markdown.render(redact(c.description_md)).html if c.description_md else None,
            "url": self.url(f"collections/{c.id}/"), "items": [], "related": [],
            "manifest_path": c.manifest_path,
        }
        for it in c.items:
            view["items"].append(self._item_view(c, it))
        total = [i["size"] for i in view["items"] if i.get("size")]
        view["size"] = sum(total) if total else None
        view["downloads"] = [f for i in view["items"] for f in i["files"]]
        view["related_refs"] = list(c.related)
        return view

    def _item_view(self, c: Collection, it: Item) -> dict[str, Any]:
        v: dict[str, Any] = {
            "id": it.id, "kind": it.kind, "title": it.title, "description": it.description,
            "origin": it.origin, "access": it.access, "access_note": it.access_note,
            "license": it.license or c.license, "files": [], "page_url": None,
            "size": None, "data": None, "entry_type": None, "availability": None,
        }
        if it.access == "restricted":
            v["title"] = it.title or it.id
            v["availability"] = "restricted"
            v["entry_type"] = {"document": "document", "campaign": "campaign", "candidate": "candidate"}.get(it.kind, c.type if c.type != "documents" else "document")
            self._add_entry(c, v)
            return v
        loader = getattr(self, f"_item_{it.kind}")
        loader(c, it, v)
        self._add_entry(c, v)
        return v

    def _add_entry(self, c: Collection, v: dict[str, Any]) -> None:
        if v["entry_type"] is None:
            return
        self.entries.append({
            "title": v["title"], "type": v["entry_type"], "summary": v["description"],
            "url": v["page_url"] or self.url(f"collections/{c.id}/#{v['id']}"),
            "collection": c.id, "collection_title": c.title, "date": v.get("date") or c.updated or c.published,
            "size": v["size"], "license": v["license"], "availability": v["availability"],
            "research_status": c.research_status, "origin": v["origin"],
        })

    # item loaders ------------------------------------------------------------
    def _item_document(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        doc = sources.load_document(path)
        self.claim_page(f"documents/{it.id}", c.id)
        v.update(title=it.title or doc["title"], data=doc, size=doc["bytes"], date=doc["maintained"],
                 page_url=self.url(f"documents/{it.id}/"), entry_type="document", availability="online")
        if it.download:
            v["files"].append(self.write_file(c, it.id, doc["filename"], doc["text"].encode("utf-8"),
                                              label="Markdown source (public copy)", media="text/markdown",
                                              origin=it.origin))
            v["availability"] = "download"
        self._pending_docs.append((c, it, v))

    def _item_campaign(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        camp = sources.load_campaign(path, it.params.get("status"))
        self.claim_page(f"campaigns/{camp['id']}", c.id)
        for step in camp["steps"]:
            step["module"] = sources.module_for_step(step["name"], self.register or []) if self.register else None
        v.update(title=it.title or camp["id"], data=camp, size=camp["bytes"],
                 page_url=self.url(f"campaigns/{camp['id']}/"), entry_type="campaign", availability="online")
        if it.download:
            v["files"].append(self.write_file(c, it.id, camp["filename"], camp["text"].encode("utf-8"),
                                              label="Campaign specification (YAML)", media="application/yaml",
                                              origin=it.origin))
            v["availability"] = "download"
        self._pending_campaigns.append((c, it, v))

    def _item_archive_manifest(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        man = sources.load_archive_manifest(path)
        v.update(title=it.title or f"{man['pack_dir']} manifest", data=man, entry_type="dataset",
                 size=man["held_bytes"], date=(man["snapshot_utc"] or "")[:10] or None, availability="link")
        if it.download:
            snap_bytes = path.read_bytes()
            v["files"].append(self.write_file(c, it.id, f"{it.id}.json", snap_bytes,
                                              label="Sanitized manifest (JSON)", media="application/json",
                                              origin="derived"))
            buf = io.StringIO()
            cols = ["product_id", "service", "state", "bytes", "sha256", "md5", "retrieved_utc",
                    "url", "endpoint", "query", "license", "note"]
            w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
            w.writeheader()
            for r in man["rows"]:
                w.writerow({k: r.get(k) for k in cols})
            v["files"].append(self.write_file(c, it.id, f"{it.id}.csv", buf.getvalue().encode("utf-8"),
                                              label="Sanitized manifest (CSV)", media="text/csv",
                                              origin="derived"))

    def _item_ledger_run(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        if self.ledger is None:
            v.update(title=it.title or "Ledger run", availability="restricted",
                     access_note="Ledger unavailable at build time.", entry_type="measurements")
            return
        run = sources.load_ledger_run(self.ledger, int(it.params["run_id"]))
        v.update(title=it.title or f"Run {run['id']} — {run['script']}", data=run,
                 entry_type="measurements", date=(run["started_utc"] or "")[:10], availability="online")
        if it.download:
            v["files"].append(self.write_file(c, it.id, f"{it.id}.json",
                                              (json.dumps(run, indent=1) + "\n").encode("utf-8"),
                                              label="Run and measurements (JSON)", media="application/json",
                                              origin="derived"))
            v["availability"] = "download"
        self._log_runs.append({"collection": c, "item": v, "runs": [run]})

    def _item_ledger_runs(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        if self.ledger is None:
            v.update(title=it.title or "Run log", availability="restricted",
                     access_note="Ledger unavailable at build time.")
            return
        log = sources.load_ledger_runs(self.ledger, it.params["script"])
        v.update(title=it.title or f"Run log — {log['script']}", data=log, availability="online")
        if it.download:
            v["files"].append(self.write_file(c, it.id, f"{it.id}.json",
                                              (json.dumps(log, indent=1) + "\n").encode("utf-8"),
                                              label="Run log (JSON)", media="application/json",
                                              origin="derived"))
        self._log_runs.append({"collection": c, "item": v, "runs": log["runs"]})

    def _item_module_register(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        rows = sources.load_module_register(path, it.params.get("heading", "Layer-2 module register"))
        counts: dict[str, int] = {}
        for r in rows:
            counts[r["status_class"]] = counts.get(r["status_class"], 0) + 1
        v.update(title=it.title or "Module register", data={"rows": rows, "counts": counts,
                 "source": path.name}, entry_type="software", availability="online")

    def _item_candidate(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        cand = sources.load_candidate(path, self.ledger)
        if "/" in cand["id"]:
            raise PublicationError(f"{cand['id']}: '/' is not allowed in a published working ID")
        self.claim_page(f"candidates/{cand['id']}", c.id)
        v.update(title=it.title or cand["id"], data=cand, page_url=self.url(f"candidates/{cand['id']}/"),
                 entry_type="candidate", availability="online")
        if it.download:
            v["files"].append(self.write_file(c, it.id, f"{cand['id']}-dossier.md",
                                              cand["dossier_md"].encode("utf-8"),
                                              label="Dossier (Markdown, generated by cygnus.reporting)",
                                              media="text/markdown", origin="derived"))
            v["availability"] = "download"
        self._pending_candidates.append((c, it, v))

    def _item_file(self, c: Collection, it: Item, v: dict[str, Any]) -> None:
        path = resolve_source(self.cfg.worktree, it.kind, it.source)
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            raise PublicationError(f"{it.source}: {size} bytes exceeds the {MAX_FILE_BYTES}-byte limit")
        v.update(title=it.title or path.name, size=size, entry_type=c.type if c.type in TYPE_LABELS else "dataset",
                 availability="download" if it.download else "restricted")
        if it.download:
            v["files"].append(self.write_file(c, it.id, path.name, path.read_bytes(), label=path.suffix.lstrip(".").upper() + " file",
                                              media="application/octet-stream", origin=it.origin))
        else:
            v["access_note"] = v["access_note"] or "Listed for reference; the file itself is not published."

    # ----------------------------------------------------------------- render
    def _ref_index(self, views: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
        idx: dict[str, dict[str, str]] = {}
        for view in views:
            idx[f"collection:{view['id']}"] = {"title": view["title"], "url": view["url"], "type": "collection"}
            for it in view["items"]:
                if not it["page_url"]:
                    continue
                key = {"document": "document", "campaign": "campaign", "candidate": "candidate"}[it["kind"]]
                ident = it["data"]["id"] if key in ("campaign", "candidate") else it["id"]
                idx[f"{key}:{ident}"] = {"title": it["title"], "url": it["page_url"], "type": key}
        return idx

    def _resolve_related(self, owner: str, refs: list[str], idx: dict[str, dict[str, str]]) -> list[dict[str, str]]:
        out = []
        for ref in refs:
            if ref in idx:
                out.append(idx[ref])
            else:
                self.result.warnings.append(f"{owner}: related ref {ref!r} is not published; omitted")
        return out

    def _render_all(self, views: list[dict[str, Any]], withdrawn: list[Collection]) -> None:
        idx = self._ref_index(views)
        for view in views:
            view["related"] = self._resolve_related(view["id"], view["related_refs"], idx)
            self.entries.append({
                "title": view["title"], "type": "collection", "summary": view["summary"], "url": view["url"],
                "collection": view["id"], "collection_title": view["title"],
                "date": view["updated"] or view["published"], "size": view["size"], "license": view["license"],
                "availability": "download" if view["downloads"] else "online",
                "research_status": view["research_status"], "origin": None, "subtype": view["type"],
            })
        for c in withdrawn:
            self.entries.append({
                "title": c.title, "type": "collection", "summary": c.summary,
                "url": self.url(f"collections/{c.id}/"), "collection": c.id, "collection_title": c.title,
                "date": c.withdrawn["date"], "size": None, "license": None, "availability": "withdrawn",
                "research_status": None, "origin": None, "subtype": c.type,
            })
        # backlinks: which collections reference a page
        backlinks: dict[str, list[dict[str, str]]] = {}
        for view in views:
            for ref in view["related_refs"]:
                backlinks.setdefault(ref, []).append({"title": view["title"], "url": view["url"], "type": "collection"})

        overview = sources.ledger_overview(self.ledger) if self.ledger else None
        campaigns = [v for _, _, v in self._pending_campaigns]
        candidates = sorted((v for _, _, v in self._pending_candidates),
                            key=lambda v: (-EVIDENCE_ORDER.get(v["data"]["evidence_level"], -1), v["data"]["id"]))
        manifests = [(view, it) for view in views for it in view["items"]
                     if it["kind"] == "archive_manifest" and it.get("data")]
        type_counts: dict[str, int] = {}
        for e in self.entries:
            type_counts[e["type"]] = type_counts.get(e["type"], 0) + 1
        common = {"overview": overview}

        for rel in ("index.html", "about/index.html"):   # the deploy bundle puts the sky explorer at the root
            self.write_page(rel, "home.html.j2", views=views, campaigns=campaigns,
                            candidates=candidates, manifests=manifests, type_counts=type_counts, **common)
        entries = sorted(self.entries, key=lambda e: (e["date"] or "", e["title"] or ""), reverse=True)
        self.write_page("repository/index.html", "repository.html.j2", entries=entries,
                        type_counts=type_counts, **common)
        for view in views:
            self.write_page(f"collections/{view['id']}/index.html", "collection.html.j2", c=view,
                            register_url=self.register_url, **common)
        for c in withdrawn:
            self.write_page(f"collections/{c.id}/index.html", "withdrawn.html.j2", c=c, **common)
        for c, it, v in self._pending_docs:
            self.write_page(f"documents/{it.id}/index.html", "document.html.j2", item=v,
                            coll=self._view_for(views, c.id), **common)
        self.write_page("campaigns/index.html", "campaigns.html.j2", campaigns=[
            (self._view_for(views, c.id), v) for c, _, v in self._pending_campaigns], **common)
        for c, it, v in self._pending_campaigns:
            camp = v["data"]
            self.write_page(f"campaigns/{camp['id']}/index.html", "campaign.html.j2", item=v,
                            coll=self._view_for(views, c.id), register_url=self.register_url,
                            backlinks=backlinks.get(f"campaign:{camp['id']}", []), **common)
        self.write_page("candidates/index.html", "candidates.html.j2", candidates=[
            (self._view_for(views, c.id), v) for c, _, v in sorted(
                self._pending_candidates,
                key=lambda t: (-EVIDENCE_ORDER.get(t[2]["data"]["evidence_level"], -1), t[2]["data"]["id"]))],
            **common)
        for c, it, v in self._pending_candidates:
            self.write_page(f"candidates/{v['data']['id']}/index.html", "candidate.html.j2", item=v,
                            coll=self._view_for(views, c.id),
                            backlinks=backlinks.get(f"candidate:{v['data']['id']}", []), **common)
        self.write_page("log/index.html", "log.html.j2", groups=self._log_runs, manifests=manifests, **common)
        methods_path = self.cfg.publish_root / "pages" / "methods.md"
        methods = None
        if methods_path.is_file():
            text = redact(methods_path.read_text(encoding="utf-8")).replace("](/", "](" + self.base)
            methods = markdown.render(text, demote_h1=True)
        self.write_page("methods/index.html", "methods.html.j2", methods=methods, **common)
        self.write_page("404.html", "404.html.j2", **common)
        self._write_catalog(views, withdrawn)

    @staticmethod
    def _view_for(views: list[dict[str, Any]], cid: str) -> dict[str, Any]:
        return next(v for v in views if v["id"] == cid)

    def _write_catalog(self, views: list[dict[str, Any]], withdrawn: list[Collection]) -> None:
        def item_meta(it: dict[str, Any]) -> dict[str, Any]:
            return {k: it[k] for k in ("id", "kind", "title", "description", "origin", "access",
                                       "access_note", "license", "availability", "size")} | {
                "page_url": it["page_url"],
                "files": [{k: f[k] for k in ("url", "filename", "bytes", "sha256", "media", "origin")}
                          for f in it["files"]],
            }

        def coll_meta(view: dict[str, Any]) -> dict[str, Any]:
            return {k: view[k] for k in ("id", "title", "type", "summary", "published", "updated",
                                         "license", "research_status", "citation", "url")} | {
                "status": "published", "related": view["related"],
                "items": [item_meta(i) for i in view["items"]],
            }

        catalog = {
            "schema": "cygnus-publication-catalog/1",
            "site": self.site.get("title"),
            "generator": f"cygnus {__version__} (cygnus.publish)",
            "build_utc": self.cfg.build_utc,
            "collections": [coll_meta(v) for v in views],
            "withdrawn": [{"id": c.id, "title": c.title, "url": self.url(f"collections/{c.id}/"),
                           "withdrawn": c.withdrawn} for c in withdrawn],
        }
        for view in views:
            data = (json.dumps(coll_meta(view), indent=1, ensure_ascii=False) + "\n").encode("utf-8")
            dest = self.cfg.out_dir / "collections" / view["id"] / "collection.json"
            dest.write_bytes(data)
        dest = self.cfg.out_dir / "data" / "catalog.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(catalog, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def build_site(cfg: BuildConfig | None = None) -> BuildResult:
    return SiteBuilder(cfg or BuildConfig()).build()


def uniq_links(links: list[dict[str, str]], exclude: str | None = None) -> list[dict[str, str]]:
    """Drop duplicate links (same URL) and links back to the current page."""
    seen: set[str] = {exclude} if exclude else set()
    out = []
    for link in links:
        if link["url"] not in seen:
            seen.add(link["url"])
            out.append(link)
    return out


def fmt_bytes(n: int | None) -> str | None:
    if n is None:
        return None
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1000 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1000
    return None
