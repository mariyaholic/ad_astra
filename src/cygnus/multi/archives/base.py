"""Archive adapter framework for the multi-archive campaign runner (``cygnus.multi``).

Design goals
------------

* One uniform contract every archive implements: discover products for a target,
  download one product to a local path, and read it into an in-memory object.
* No import-time network or heavy dependency: adapters import ``requests`` /
  ``astroquery`` / ``astropy`` inside methods, so the module imports on a bare
  interpreter and unit tests run offline with injected fetchers.
* Provenance is carried by the caller (runner/ledger), never invented here: an
  unavailable service raises :class:`AdapterUnavailable` or returns ``[]`` with a
  recorded reason; it never fabricates rows.

The registry is populated by :func:`register` and queried by :func:`get` /
:func:`available` / :func:`all_adapters`. ``cygnus.multi.archives`` imports each
adapter module so importing the package registers them.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


class AdapterError(RuntimeError):
    """Base class for adapter failures."""


class AdapterUnavailable(AdapterError):
    """The archive cannot be reached or a required dependency is missing.

    Callers record this as *not tested*; it is never downgraded to 'no match'.
    """


@dataclass(frozen=True)
class ProductRef:
    """A single addressable archive product, before download.

    ``format`` selects the reader (see ``cygnus.multi.readers``); ``kind`` says
    whether the product is an analysable time series, an image, a table or free
    text. ``url`` may be ``None`` when an adapter resolves the real URL lazily in
    :meth:`fetch`. ``extra`` carries adapter-specific metadata (TIC, sector, band,
    brick, ...) that the runner copies into the ledger and the sky record.
    """

    archive: str
    product_id: str
    url: str | None = None
    format: str = "fits_table"
    kind: str = "lightcurve"
    description: str = ""
    expected_sha256: str | None = None
    size_bytes: int | None = None
    extra: Mapping[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "archive": self.archive,
            "product_id": self.product_id,
            "url": self.url,
            "format": self.format,
            "kind": self.kind,
            "description": self.description,
            "expected_sha256": self.expected_sha256,
            "size_bytes": self.size_bytes,
            "extra": dict(self.extra),
        }


KIND_BY_FORMAT = {
    "spoc_lc": "lightcurve", "tess_lc": "lightcurve", "kepler_lc": "lightcurve",
    "csv_lc": "lightcurve", "ztf_lc": "lightcurve",
    "fits_image": "image", "coadd_image": "image", "fits_cube": "image",
    "csv": "table", "votable": "table", "table": "table", "json": "table",
    "text": "text",
    "rv_table": "table", "eso_spectrum": "spectrum",
}


def kind_for_format(fmt: str) -> str:
    """Map a product format to its analysis kind (unknown formats are treated as light curves)."""
    return KIND_BY_FORMAT.get(fmt, "lightcurve")


@dataclass(frozen=True)
class SourceCheck:
    """One source-specific check on a fetched product (never a bare 'passed' by default)."""

    name: str
    state: str          # passed | failed | inconclusive | not_tested
    note: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {"name": self.name, "state": self.state, "note": self.note}


@dataclass
class Target:
    """A position on the sky plus the catalogue numbers an adapter may need."""

    name: str
    ra_deg: float
    dec_deg: float
    tic: int | None = None
    t0_bjd: float | None = None
    period_days: float | None = None
    depth_ppm: float | None = None
    duration_h: float | None = None
    mag: float | None = None
    extra: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, m: Mapping[str, Any]) -> "Target":
        return cls(
            name=str(m["name"]),
            ra_deg=float(m["ra_deg"]),
            dec_deg=float(m["dec_deg"]),
            tic=int(m["tic"]) if m.get("tic") not in (None, "") else None,
            t0_bjd=_f(m.get("t0_bjd")),
            period_days=_f(m.get("period_days")),
            depth_ppm=_f(m.get("depth_ppm")),
            duration_h=_f(m.get("duration_h")),
            mag=_f(m.get("tmag") if m.get("tmag") is not None else m.get("mag")),
            extra={k: v for k, v in m.items() if k not in
                   {"name", "ra_deg", "dec_deg", "tic", "t0_bjd", "period_days", "depth_ppm", "duration_h", "tmag", "mag"}},
        )


def _f(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


class ArchiveAdapter(ABC):
    """Contract for one archive integration.

    Subclasses set :attr:`name` (the stable identifier used in specs and the
    ledger) and :attr:`formats` (the product ``format`` strings they serve), and
    implement :meth:`discover`, :meth:`fetch` and optionally :meth:`read`.
    """

    name: str = ""
    #: human description shown in ``cygnus.multi.archives.summary()``
    description: str = ""
    #: product format strings this adapter can return
    formats: tuple[str, ...] = ("fits_table",)
    #: what can be done with this archive's products, e.g. ``lightcurve``, ``image``,
    #: ``catalog``, ``ephemeris``, ``astrometry``, ``observing``
    capabilities: tuple[str, ...] = ("context",)
    #: DATA_SOURCES.md tag ([V] verified live, [K] knowledge-based)
    verified: str = "[K]"
    #: True when ``discover(limit=...)`` caps catalogue *rows* (TAP TOP) rather than the number of products
    row_limited: bool = False

    def __init__(self, *, session: Any = None, discover_fn: Callable[..., list] | None = None,
                 fetch_fn: Callable[..., Path] | None = None, http: Callable[..., Any] | None = None):
        # injectable seams for offline tests
        self._session = session
        self._discover_fn = discover_fn
        self._fetch_fn = fetch_fn
        self._http = http

    # ------------------------------------------------------------------ contract
    @abstractmethod
    def discover(self, target: Target, *, limit: int = 5, **opts: Any) -> list[ProductRef]:
        """Return up to ``limit`` products for ``target`` (newest/most relevant first).

        Return ``[]`` when the archive genuinely has nothing for this target;
        raise :class:`AdapterUnavailable` when the service cannot be queried, so
        the caller can distinguish 'no product' from 'not tested'.
        """

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 180.0) -> Path:
        """Download ``ref`` to ``dest`` and return the path. Resumable by default."""
        if self._fetch_fn is not None:
            return Path(self._fetch_fn(ref, dest))
        if not ref.url:
            raise AdapterError(f"{self.name}:{ref.product_id}: no URL to fetch")
        from cygnus.ingest.netio import fetch_to_file  # shared resumable downloader (stdlib+requests)

        fetch_to_file(ref.url, dest, timeout_s=timeout_s)
        return Path(dest)

    def read(self, path: Path, ref: ProductRef) -> Any:
        """Read a downloaded product. Default: dispatch through ``cygnus.multi.readers``."""
        from ..readers import read_product

        return read_product(path, fmt=ref.format, ref=ref)

    def source_checks(self, target: Target | None, ref: ProductRef, path: Path,
                      product: Mapping[str, Any] | None = None) -> list[SourceCheck]:
        """Source-specific checks on one fetched product.

        The default dispatches by product kind through ``cygnus.multi.source_checks``
        (table, image, light curve, text, json), so every archive gets an honest
        integrity check; adapters override for archive-specific meaning (Gaia
        astrometric flags, MPC observations, and so on).
        """
        from .. import source_checks as sc

        product = product or {}
        kind = product.get("kind") or kind_for_format(ref.format)
        source = self.name
        if kind == "table":
            return sc.table_checks(path, target, kind=f"{source} catalogue")
        if kind == "image":
            return sc.image_checks(path, source=source)
        if kind == "lightcurve":
            return sc.lightcurve_checks(path, fmt=ref.format, source=source)
        if ref.format == "json":
            return sc.json_checks(path, source=source)
        return sc.text_checks(path, source=source)

    def capabilities_list(self) -> list[str]:
        """Declared capabilities, or those implied by the formats it serves."""
        if self.capabilities != ("context",):
            return list(self.capabilities)
        caps: list[str] = []
        for f in self.formats:
            c = {"lightcurve": "lightcurve", "image": "image", "table": "catalog", "text": "context"}.get(
                kind_for_format(f), "context")
            if c not in caps:
                caps.append(c)
        return caps

    # ------------------------------------------------------------------ helpers
    def _session_or_new(self):
        if self._session is not None:
            return self._session
        import requests

        self._session = requests.Session()
        self._session.headers.update({"User-Agent": "cygnus-multi/0.1 (archive adapters)"})
        return self._session

    def http_post(self, url: str, data: dict, *, timeout: float = 120.0, headers: dict | None = None):
        if self._http is not None:
            return self._http(url, data=data, timeout=timeout, headers=headers)
        return self._session_or_new().post(url, data=data, timeout=timeout, headers=headers)

    def http_get(self, url: str, *, params: dict | None = None, timeout: float = 120.0, headers: dict | None = None):
        if self._http is not None:
            return self._http(url, params=params, timeout=timeout, headers=headers)
        return self._session_or_new().get(url, params=params, timeout=timeout, headers=headers)

    def http_get_body(self, url: str, body: Mapping[str, Any], *, timeout: float = 120.0):
        """GET with a JSON body (MPC's data API requires this method/body combination)."""
        import json

        headers = {"Content-Type": "application/json"}
        if self._http is not None:
            return self._http(url, data=json.dumps(body), headers=headers, timeout=timeout)
        return self._session_or_new().get(url, data=json.dumps(body), headers=headers, timeout=timeout)

    def tap_csv(self, url: str, adql: str, *, timeout: float = 120.0) -> list[dict]:
        """Run an ADQL query against a TAP ``/sync`` CSV endpoint and return rows as dicts.

        Raises :class:`AdapterError` on a TAP XML error body (which would otherwise
        parse as zero rows and be misread as 'no match').
        """
        import csv
        import io

        r = self.http_post(url, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
                           timeout=timeout)
        r.raise_for_status()
        body = r.text.lstrip()
        # a TAP service reports errors in a VOTable or as plain text with HTTP 200; a CSV answer always has a header
        if not body or body.startswith("<") or body[:6].upper().startswith(("ERROR", "FATAL")):
            raise AdapterError(f"TAP error from {url}: {body[:300] or 'empty response body'}")
        return list(csv.DictReader(io.StringIO(r.text)))


# ---------------------------------------------------------------------- registry
_REGISTRY: dict[str, ArchiveAdapter] = {}
_FACTORIES: dict[str, Callable[..., ArchiveAdapter]] = {}


def register(adapter_cls: type[ArchiveAdapter] | ArchiveAdapter) -> type[ArchiveAdapter]:
    """Register an adapter class (instantiated lazily via :func:`get`) or a ready instance."""
    if isinstance(adapter_cls, ArchiveAdapter):
        inst = adapter_cls
        if not inst.name:
            raise ValueError("adapter instance has no name")
        _REGISTRY[inst.name] = inst
        return type(inst)
    if not adapter_cls.name:
        raise ValueError(f"{adapter_cls.__name__} has no name")
    _FACTORIES[adapter_cls.name] = adapter_cls
    return adapter_cls


def get(name: str, **kwargs: Any) -> ArchiveAdapter:
    """Return the adapter registered under ``name`` (instance built on first use)."""
    if name in _REGISTRY and not kwargs:
        return _REGISTRY[name]
    if name in _REGISTRY and kwargs:
        return type(_REGISTRY[name])(**kwargs)
    if name not in _FACTORIES:
        raise KeyError(f"no archive adapter {name!r}; known: {', '.join(sorted(set(_REGISTRY) | set(_FACTORIES)))}")
    inst = _FACTORIES[name](**kwargs)
    if not kwargs:
        _REGISTRY[name] = inst
    return inst


def all_adapters() -> dict[str, ArchiveAdapter]:
    names = sorted(set(_REGISTRY) | set(_FACTORIES))
    return {n: get(n) for n in names}


def available() -> list[str]:
    """Names of every registered adapter."""
    return sorted(set(_REGISTRY) | set(_FACTORIES))


def summary() -> list[dict[str, Any]]:
    out = []
    for name in available():
        a = get(name)
        out.append({"name": name, "description": a.description, "formats": list(a.formats),
                    "capabilities": a.capabilities_list(), "verified": a.verified})
    return out


def as_products(rows: Iterable[Mapping[str, Any]], archive: str, fmt: str) -> list[ProductRef]:
    """Build ProductRefs from raw adapter rows without inventing fields."""
    return [
        ProductRef(
            archive=archive,
            product_id=str(r["product_id"]),
            url=r.get("url"),
            format=r.get("format", fmt),
            kind=r.get("kind") or kind_for_format(r.get("format", fmt)),
            description=str(r.get("description", "")),
            expected_sha256=r.get("expected_sha256"),
            size_bytes=r.get("size_bytes"),
            extra={k: v for k, v in r.items() if k not in
                   {"product_id", "url", "format", "kind", "description", "expected_sha256", "size_bytes"}},
        )
        for r in rows
    ]