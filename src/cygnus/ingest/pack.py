"""Ledger-backed campaign pack builder for Cygnus ingest.

Binds together:

* **staging** under the scratch root (nonsynced, disposable — AGENTS.md);
* the Cygnus **Ledger** (SQLite provenance: products/runs/measurements);
* per-service **byte budgets** so a campaign stays finite and reviewable;
* **manifests** (per-service JSON/CSV + a master CSV) that travel with the
  pack and act as the checksum authority after local copies are deleted.

Retention policy (user instruction, 2026-09-24): bulky staged files are
deleted locally once uploaded to ``cygnus:Cygnus`` and verified; Drive hosts
the data. ``PULLBACK``: never run ``rclone sync`` from an emptied staging
dir — it would mirror the emptiness and delete the Drive copy. Always use
``rclone copy`` for top-ups.

Manifest row states:

* ``local``        — product fetched and currently present on disk;
* ``drive_only``   — uploaded + verified, local copy deleted;
* ``excluded``     — seen/identified but not fetched (budget, size, error);
* ``failed``       — fetch attempted and raised (error text recorded).

No row is invented: every row cites the endpoint/URL it came from.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..config import scratch_dir
from ..ledger import Ledger
from .netio import fetch_to_file, md5_file, sha256_file

_PACK_ROOT_NAME = "tier1_pack"

MANIFEST_FIELDS = [
    "service",
    "pack_dir",
    "product_id",
    "dest_rel",
    "state",
    "bytes",
    "sha256",
    "md5",
    "retrieved_utc",
    "url",
    "endpoint",
    "query",
    "license",
    "truncated",
    "extra_json",
    "note",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _short(v: Any, n: int = 240) -> str:
    s = "" if v is None else str(v)
    return s if len(s) <= n else s[: n - 3] + "..."


class PackBuilder:
    """Coordinates a finite, provenance-logged pack for a set of services."""

    def __init__(
        self,
        ledger: Ledger,
        *,
        pack_root: Path | None = None,
        budgets: dict[str, float] | None = None,
        dirmap: dict[str, str] | None = None,
        quiet: bool = False,
    ) -> None:
        self.ledger = ledger
        self.root = Path(pack_root) if pack_root else scratch_dir(_PACK_ROOT_NAME)
        self.root.mkdir(parents=True, exist_ok=True)
        # budgets: service key -> byte cap (float GB accepted; stored as bytes)
        self.budgets = {k: int(v * (1 << 30)) for k, v in (budgets or {}).items()}
        # dirmap: service key -> upload directory name (e.g. mast -> 01_mast).
        # Staged files live under the upload dir so manifests travel with data.
        self.dirmap = dict(dirmap or {})
        self._svc_bytes: dict[str, int] = {}
        self._rows: dict[str, list[dict[str, Any]]] = {}
        self._logs: dict[str, list[str]] = {}
        self.quiet = quiet

    # ------------------------------------------------------------- plumbing
    def pack_dir(self, service: str) -> Path:
        p = self.root / self.dirmap.get(service, service)
        p.mkdir(parents=True, exist_ok=True)
        return p

    def log(self, service: str, text: str) -> None:
        line = f"[{now_iso()}] [{service}] {text}"
        self._logs.setdefault(service, []).append(line)
        if not self.quiet:
            print(line, flush=True)

    def bytes_used(self, service: str) -> int:
        return self._svc_bytes.get(service, 0)

    def budget_left(self, service: str) -> int | None:
        cap = self.budgets.get(service)
        if cap is None:
            return None
        return max(0, cap - self.bytes_used(service))

    # ----------------------------------------------------------- fetch APIs
    def try_fetch(
        self,
        service: str,
        product_id: str,
        *,
        url: str,
        dest_rel: str,
        endpoint: str,
        query: str = "",
        license_: str = "",
        extra: dict[str, Any] | None = None,
        size_hint: int | None = None,
        max_bytes: int | None = None,
        **fetch_kwargs: Any,
    ) -> dict[str, Any] | None:
        """Download (or reuse/upload-only-skip) one product; returns manifest row."""
        svc_dir = self.pack_dir(service)
        dest = svc_dir / dest_rel

        # Idempotency: already-staged file with matching ledger checksum is reused.
        prior = self.ledger.products(service) if self.ledger else []
        for row in prior:
            if row["product_id"] != product_id:
                continue
            if row["checksum"] and dest.exists() and dest.stat().st_size > 0:
                try:
                    if sha256_file(dest) == row["checksum"]:
                        mrow = self.register(
                            service, product_id, path=dest, url=url, endpoint=endpoint,
                            query=query, license_=license_ or row["license"] or "",
                            extra=extra, note="reused from prior staged run (checksum match)",
                        )
                        self.log(service, f"REUSE (staged match): {product_id}")
                        return mrow
                except OSError:
                    pass
            break

        for row in prior:
            if row["product_id"] == product_id:
                ex = {}
                try:
                    ex = json.loads(row["extra_json"] or "{}")
                except Exception:
                    ex = {}
                if ex.get("state") == "drive_only":
                    mrow = self._row(
                        service, product_id, dest_rel=dest_rel or (ex.get("dest_rel") or ""),
                        state="drive_only", url=url or row["url"] or "",
                        endpoint=endpoint, query=query, license_=license_ or row["license"] or "",
                        extra=ex, sha256=row["checksum"],
                        retrieved=row["retrieved_utc"],
                        note="uploaded+verified previously; local copy removed (Drive hosts it)",
                    )
                    self._rows.setdefault(service, []).append(mrow)
                    self.log(service, f"SKIP (drive_only): {product_id}")
                    return mrow
                break

        # Budget guard on the expected size before starting.
        left = self.budget_left(service)
        if left is not None and size_hint is not None and size_hint > left:
            mrow = self._row(
                service, product_id, dest_rel=dest_rel, state="excluded", url=url,
                endpoint=endpoint, query=query, license_=license_, extra=extra,
                note=f"would exceed service budget ({size_hint} > {left} bytes free); not fetched",
            )
            self._rows.setdefault(service, []).append(mrow)
            self.log(service, f"EXCLUDE (budget): {product_id} size_hint={size_hint}")
            return mrow

        try:
            res = fetch_to_file(
                url,
                dest,
                max_bytes=max_bytes if max_bytes is not None else left,
                **fetch_kwargs,
            )
        except Exception as exc:  # noqa: BLE001 - record every failure per AGENTS.md
            mrow = self._row(
                service, product_id, dest_rel=dest_rel, state="failed", url=url,
                endpoint=endpoint, query=query, license_=license_, extra=extra,
                note=f"fetch error: {type(exc).__name__}: {_short(exc, 500)}",
            )
            self._rows.setdefault(service, []).append(mrow)
            self.log(service, f"FAIL: {product_id}: {type(exc).__name__}")
            return mrow

        path = Path(res["path"])
        if res["truncated"]:
            mrow = self._row(
                service, product_id, dest_rel=dest_rel, state="failed", url=url,
                endpoint=endpoint, query=query, license_=license_, extra=extra,
                path=path, sha256=sha256_file(path), md5=md5_file(path), bytes_=res["bytes"],
                note=res["note"],
            )
            self._rows.setdefault(service, []).append(mrow)
            self.log(service, f"TRUNCATED (cap): {product_id} at {res['bytes']} bytes")
            return mrow

        mrow = self.register(
            service, product_id, path=path, url=url, endpoint=endpoint, query=query,
            license_=license_, extra=extra, note=res.get("note", ""),
        )
        return mrow

    def register(
        self,
        service: str,
        product_id: str,
        *,
        path: Path,
        url: str,
        endpoint: str,
        query: str = "",
        license_: str = "",
        extra: dict[str, Any] | None = None,
        note: str = "",
    ) -> dict[str, Any]:
        """Register an existing local file as a product; returns manifest row."""
        dest_rel = path.relative_to(self.pack_dir(service)).as_posix()
        bytes_ = path.stat().st_size
        sha256 = sha256_file(path)
        md5 = md5_file(path)
        mrow = self._row(
            service, product_id, dest_rel=dest_rel, state="local",
            url=url, endpoint=endpoint, query=query, license_=license_,
            extra=extra, path=path, sha256=sha256, md5=md5, bytes_=bytes_, note=note,
        )
        self._rows.setdefault(service, []).append(mrow)
        self._svc_bytes[service] = self.bytes_used(service) + bytes_
        if self.ledger is not None:
            ex = dict(extra or {})
            ex.update({"pack_dir": service, "dest_rel": dest_rel, "md5": md5})
            self.ledger.add_product(
                archive=service,
                product_id=product_id,
                url=url,
                local_path=str(path),
                checksum=sha256,
                license_=license_ or None,
                extra=ex,
            )
        self.log(service, f"OK: {product_id} ({bytes_} bytes)")
        return mrow

    def register_table(
        self,
        service: str,
        product_id: str,
        *,
        path: Path,
        endpoint: str,
        query: str,
        license_: str = "",
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Register a table resulting from an explicit query (TAP/ADQL)."""
        return self.register(
            service, product_id, path=path, url=endpoint, endpoint=endpoint,
            query=query, license_=license_, extra=extra,
        )

    # ------------------------------------------------------------- manifests
    def _row(
        self,
        service: str,
        product_id: str,
        *,
        dest_rel: str,
        state: str,
        url: str,
        endpoint: str,
        query: str,
        license_: str,
        extra: dict[str, Any] | None = None,
        path: Path | None = None,
        bytes_: int | None = None,
        sha256: str | None = None,
        md5: str | None = None,
        retrieved: str | None = None,
        note: str = "",
    ) -> dict[str, Any]:
        return {
            "service": service,
            "pack_dir": service,
            "product_id": product_id,
            "dest_rel": (
                path.relative_to(self.pack_dir(service)).as_posix()
                if path is not None
                else str(dest_rel).replace("\\", "/")
            ),
            "state": state,
            "bytes": bytes_ if bytes_ is not None else "",
            "sha256": sha256 or "",
            "md5": md5 or "",
            "retrieved_utc": retrieved or now_iso(),
            "url": _short(url, 900),
            "endpoint": _short(endpoint, 900),
            "query": _short(query, 4800),
            "license": license_ or "",
            "truncated": "",
            "extra_json": json.dumps(extra or {}, sort_keys=True),
            "note": _short(note, 900),
        }

    def rows(self, service: str) -> list[dict[str, Any]]:
        return self._rows.get(service, [])

    def all_rows(self) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for svc in sorted(self._rows):
            out.extend(self._rows[svc])
        return out

    def write_manifest(self, service: str) -> Path:
        svc_dir = self.pack_dir(service)
        rows = self.rows(service)
        json_path = svc_dir / "MANIFEST.json"
        csv_path = svc_dir / "MANIFEST.csv"
        json_path.write_text(
            json.dumps(rows, indent=1, ensure_ascii=True), encoding="utf-8"
        )
        with open(csv_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=MANIFEST_FIELDS, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for r in rows:
                clean = dict(r)
                clean["query"] = clean["query"].replace("\n", " ").replace("\r", " ")
                clean["url"] = clean["url"].replace("\n", " ")
                w.writerow({k: clean.get(k, "") for k in MANIFEST_FIELDS})
        return json_path

    def write_master(self, dest: str | Path | None = None) -> Path:
        out = Path(dest) if dest else self.root / "MASTER_MANIFEST.csv"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=MANIFEST_FIELDS, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for r in self.all_rows():
                clean = dict(r)
                clean["query"] = clean["query"].replace("\n", " ").replace("\r", " ")
                w.writerow({k: clean.get(k, "") for k in MANIFEST_FIELDS})
        return out

    def run_config_sha(self, payload: dict[str, Any]) -> str:
        blob = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha1(blob).hexdigest()

    def write_search_log(self, dest: str | Path | None = None) -> Path:
        out = Path(dest) if dest else self.root / "SEARCH_LOG.md"
        lines = ["# CYGNUS Tier-1 pack — search log (machine-written)", ""]
        for svc in sorted(self._logs):
            lines.append(f"## {svc}")
            lines.append("")
            lines.extend("    " + ln for ln in self._logs[svc])
            lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")
        return out

    # ------------------------------------------------------------ retention
    def delete_local(self, service: str, *, require_verified: bool = True) -> int:
        """Remove staged files for a service that is Drive-hosted.

        Callers must have verified the Drive copy (e.g. ``rclone check``) —
        ``require_verified`` insists that every ``local`` row already carries the
        verifier's ``verified_md5`` marker (the one ``verify_remote_upload``
        writes). The ledger rows are marked ``state=drive_only`` so a later pack
        run does not re-download them.
        """
        rows = self.rows(service)
        unverified = [
            r for r in rows
            if r["state"] == "local" and "verified_md5" not in (r["note"] or "")
        ]
        if unverified and require_verified:
            raise RuntimeError(
                f"refusing local delete: {len(unverified)} unverified rows in {service}"
            )
        n = 0
        for r in rows:
            if r["state"] not in ("local", "drive_only"):
                continue
            p = self.pack_dir(service) / r["dest_rel"]
            if p.is_file():
                p.unlink()
                n += 1
                r["state"] = "drive_only"
                r["note"] = (r["note"] or "") + "; local copy deleted after verified upload"
            elif r["state"] == "local":
                r["state"] = "drive_only"
                r["note"] = (r["note"] or "") + "; local copy already absent (treated as drive-hosted)"
        # ledger: flip local_path -> state note
        if self.ledger is not None:
            for r in rows:
                try:
                    ex = json.loads(r["extra_json"] or "{}")
                except Exception:
                    ex = {}
                if r["state"] == "drive_only":
                    ex["state"] = "drive_only"
                    ex["local_deleted_utc"] = now_iso()
                    self.ledger.add_product(
                        archive=service,
                        product_id=r["product_id"],
                        checksum=r["sha256"] or None,
                        url=r["url"] or None,
                        local_path=None,
                        extra=ex,
                    )
            self.ledger.db.commit()
        if n:
            self.log(service, f"RETENTION: deleted {n} local files after verified upload")
        return n


def ledger_products_csv(ledger: Ledger, dest: str | Path) -> Path:
    """Export the ledger products table as CSV for the Drive provenance copy."""
    import io
    import json as _json

    out = Path(dest)
    out.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, quoting=csv.QUOTE_MINIMAL)
    heads = [
        "id", "archive", "product_id", "url", "local_path", "checksum_sha256",
        "license", "retrieved_utc", "last_seen_utc", "extra_json",
    ]
    w.writerow(heads)
    for row in ledger.products():
        w.writerow([
            row["id"], row["archive"], row["product_id"], row["url"], row["local_path"],
            row["checksum"], row["license"], row["retrieved_utc"], row["last_seen_utc"],
            _json.dumps(_json.loads(row["extra_json"] or "{}"), sort_keys=True)[:4000],
        ])
    out.write_text(buf.getvalue(), encoding="utf-8")
    return out


# ----------------------------------------------------------------------- verify + retire


def _manifest_paths(pack_root: Path, pack_dir_name: str) -> tuple[Path, Path]:
    d = Path(pack_root) / pack_dir_name
    return d / "MANIFEST.json", d / "MANIFEST.csv"


def _write_manifest_files(rows: list[dict[str, Any]], pack_root: Path, pack_dir_name: str) -> None:
    jpath, cpath = _manifest_paths(pack_root, pack_dir_name)
    jpath.parent.mkdir(parents=True, exist_ok=True)
    jpath.write_text(json.dumps(rows, indent=1, ensure_ascii=True), encoding="utf-8")
    with open(cpath, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            clean = dict(r)
            clean["query"] = clean["query"].replace("\n", " ").replace("\r", " ")
            w.writerow({k: clean.get(k, "") for k in MANIFEST_FIELDS})


def verify_remote_upload(
    pack_root: str | Path,
    pack_dir_name: str,
    remote_dir: str,
    *,
    rclone_exe: str = "rclone",
    ledger: Ledger | None = None,
) -> dict[str, Any]:
    """Verify a Drive upload against the service MANIFEST rows via ``rclone md5sum``.

    Requires every manifest row that carries an md5 (states local/drive_only)
    to appear in the remote listing with the same md5. Unverified/mismatched
    rows are reported; **no local file is ever deleted by this function**.
    Rows that pass get ``note`` suffixed ``verified_md5`` (manifest rewritten).
    """
    import subprocess

    jpath, _ = _manifest_paths(pack_root, pack_dir_name)
    rows = json.loads(jpath.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [rclone_exe, "md5sum", "-q", remote_dir],
        capture_output=True, text=True, timeout=1800,
    )
    remote_map: dict[str, str] = {}
    for line in (proc.stdout or "").splitlines():
        line = line.rstrip("\n")
        if not line:
            continue
        try:
            md5, rest = line.split("  ", 1) if "  " in line else (line.split()[0], " ".join(line.split()[1:]))
            parts = rest.split(None, 1)
            path = parts[1] if len(parts) > 1 else parts[0]
            remote_map[path.replace("\\", "/")] = md5.strip()
        except Exception:
            continue
    result = {"service": pack_dir_name, "remote_dir": remote_dir,
              "checked": 0, "verified": 0, "missing": [], "mismatched": [], "details": []}
    for r in rows:
        if r.get("md5") and r.get("state") in ("local", "drive_only"):
            result["checked"] += 1
            rel = (r["dest_rel"] or "").replace("\\", "/")
            if not rel:
                result["missing"].append(r["product_id"])
                continue
            rmd5 = remote_map.get(rel)
            if rmd5 is None:
                result["missing"].append(r["product_id"])
            elif rmd5 != r["md5"]:
                result["mismatched"].append(r["product_id"])
            else:
                result["verified"] += 1
                r["note"] = ((r["note"] or "") + f"; verified_md5@{remote_dir}").lstrip(" ;")
                result["details"].append(r["product_id"])
    result["ok"] = (proc.returncode == 0 and result["checked"] > 0
                    and result["checked"] == result["verified"])
    _write_manifest_files(rows, pack_root, pack_dir_name)
    if ledger is not None and result["ok"]:
        for r in rows:
            if r.get("md5") and r.get("state") in ("local", "drive_only"):
                try:
                    ex = json.loads(r.get("extra_json") or "{}")
                except Exception:
                    ex = {}
                ex["drive_verified_utc"] = now_iso()
                ex["dest_rel"] = r["dest_rel"]
                ledger.add_product(archive=r["service"], product_id=r["product_id"],
                                   checksum=r["sha256"] or None, url=r["url"] or None, extra=ex)
    return result


def retire_local_copies(pack_root: str | Path, pack_dir_name: str, *, ledger: Ledger | None = None) -> int:
    """Delete local copies for rows already marked ``verified_md5``.

    Refuses to run unless every ``local`` row with an md5 is verified. Updates
    manifest row states to ``drive_only`` (and the ledger when provided).
    """
    jpath, _ = _manifest_paths(pack_root, pack_dir_name)
    rows = json.loads(jpath.read_text(encoding="utf-8"))
    # Fail closed: every local row must carry the verifier's marker, including rows with no
    # md5 (which md5sum cannot verify). A hashless local row is never silently deleted.
    need = [r for r in rows
            if r.get("state") == "local" and "verified_md5" not in (r["note"] or "")]
    if need:
        raise RuntimeError(
            f"retire refused for {pack_dir_name}: {len(need)} rows not yet verified "
            f"(e.g. {need[0]['product_id']})"
        )
    base = (Path(pack_root) / pack_dir_name).resolve()
    n = 0
    for r in rows:
        rel = (r["dest_rel"] or "").replace("\\", "/")
        p = (base / rel).resolve()
        if not p.is_relative_to(base):
            raise RuntimeError(f"retire refused for {pack_dir_name}: unsafe dest_rel {r['dest_rel']!r}")
        if r.get("state") == "local" and p.is_file():
            p.unlink()
            n += 1
        if r.get("state") == "local":
            r["state"] = "drive_only"
            r["note"] = ((r["note"] or "") + f"; local_deleted@{now_iso()}").lstrip(" ;")
    _write_manifest_files(rows, pack_root, pack_dir_name)
    if ledger is not None:
        for r in rows:
            if r.get("state") == "drive_only":
                try:
                    ex = json.loads(r.get("extra_json") or "{}")
                except Exception:
                    ex = {}
                ex["state"] = "drive_only"
                ex["local_deleted_utc"] = now_iso()
                ex["dest_rel"] = r["dest_rel"]
                ledger.mark_product_drive_only(r["service"], r["product_id"], extra=ex)
    return n
