"""Solar-system context adapters (DATA_SOURCES.md section 5).

These are *context* services: they return ephemerides, orbital elements or
known-object checks rather than telescope products to analyse. They implement
``discover`` as a table product and set a ``context`` flag so the runner knows
they are cross-checks, not light curves.
"""

from __future__ import annotations

import json
from pathlib import Path

from .base import AdapterUnavailable, ArchiveAdapter, ProductRef, Target, as_products, register

HORIZONS_API = "https://ssd.jpl.nasa.gov/api/horizons.api"
SBDB_API = "https://ssd-api.jpl.nasa.gov/sbdb.api"
MPC = "https://minorplanetcenter.net"
MPC_DATA = "https://data.minorplanetcenter.net"
ASTDYS = "https://newton.spacedys.com/astdys"


def _text_product(pid: str, text: str, description: str) -> dict:
    return {"product_id": pid, "format": "text", "url": None, "description": description,
            "text": text, "inline": True}


class _ContextAdapter(ArchiveAdapter):
    """Base for services whose 'product' is an inline text/CSV blob."""

    context = True

    def fetch(self, ref: ProductRef, dest, *, timeout_s: float = 120.0):
        if ref.extra.get("inline"):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(str(ref.extra.get("text", "")), encoding="utf-8")
            return dest
        return super().fetch(ref, dest, timeout_s=timeout_s)


@register
class HorizonsAdapter(_ContextAdapter):
    name = "horizons"
    description = "JPL Horizons ephemerides (small bodies, solar-system prospects)"
    formats = ("text",)
    capabilities = ("ephemeris", "context")
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, command: str | None = None, **opts) -> list[ProductRef]:
        try:
            params = {"format": "text", "COMMAND": command or f"'{target.name}'", "OBJ_DATA": "'YES'", "MAKE_EPHEM": "'NO'"}
            r = self.http_get(HORIZONS_API, params=params, timeout=60.0)
            r.raise_for_status()
            txt = r.text
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"Horizons failed: {type(exc).__name__}: {exc}") from exc
        return as_products([_text_product(f"horizons_{target.name.replace(' ', '_')}.txt", txt,
                                          f"JPL Horizons object data for {target.name}")], self.name, "text")


@register
class SbdbAdapter(_ContextAdapter):
    name = "sbdb"
    description = "JPL Small-Body Database orbital elements and fit parameters"
    formats = ("json", "text")
    capabilities = ("orbit", "context")
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get(SBDB_API, params={"sstr": target.name}, timeout=60.0)
            r.raise_for_status()
            txt = r.text
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"SBDB failed: {type(exc).__name__}: {exc}") from exc
        return as_products([_text_product(f"sbdb_{target.name.replace(' ', '_')}.json", txt,
                                          f"JPL SBDB elements for {target.name}")], self.name, "text")


@register
class MpcAdapter(_ContextAdapter):
    """Minor Planet Center known-object checks.

    The public site ``minorplanetcenter.net`` is unreachable from some hosts
    (STATUS 2026-09-25); the MPC **data API** at ``data.minorplanetcenter.net``
    answers, so observations are queried there. The API expects a GET carrying a
    JSON body — ``GET /api/get-obs`` with ``{"desigs": [name]}``.
    """

    name = "mpc"
    description = "Minor Planet Center observations via data.minorplanetcenter.net (main site may be unreachable)"
    formats = ("json",)
    capabilities = ("known_objects", "context")
    verified = "[V 2026-09-25]"

    def discover(self, target: Target, *, limit: int = 1, desig: str | None = None, **opts) -> list[ProductRef]:
        desig = desig or target.name
        try:
            r = self.http_get_body(f"{MPC_DATA}/api/get-obs", {"desigs": [desig]}, timeout=60.0)
            r.raise_for_status()
            txt = r.text
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"MPC data API failed for {desig!r}: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"mpc_obs_{desig.replace(' ', '_')}.json", "format": "json", "url": None,
                             "description": f"MPC observations for {desig} (data.minorplanetcenter.net/api/get-obs)",
                             "text": txt, "inline": True}], self.name, "json")

    def fetch(self, ref: ProductRef, dest, *, timeout_s: float = 120.0):
        if ref.extra.get("inline"):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(str(ref.extra.get("text", "")), encoding="utf-8")
            return dest
        return super().fetch(ref, dest, timeout_s=timeout_s)

    def source_checks(self, target, ref, path, product=None):
        """Parse the MPC payload and count the observation records returned."""
        from .base import SourceCheck

        checks = super().source_checks(target, ref, path, product)
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            rows = data if isinstance(data, list) else [data]
            n_obs = sum(len(r.get("OBS80") or r.get("OBS_DF") or r.get("XML") or []) if isinstance(r, dict) else 0 for r in rows)
            checks.append(SourceCheck("MPC observation records", "passed" if rows else "inconclusive",
                                      f"{len(rows)} object record(s), {n_obs} observation entr(ies) via the data API"))
        except Exception as exc:  # noqa: BLE001
            checks.append(SourceCheck("MPC observation records", "failed", f"{type(exc).__name__}: {str(exc)[:160]}"))
        return checks


@register
class AstDysAdapter(_ContextAdapter):
    name = "astdys"
    description = "AstDyS / NEODyS independent orbit solutions"
    formats = ("text",)
    capabilities = ("orbit", "context")
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get(ASTDYS + "/", timeout=30.0)
            r.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"AstDyS unreachable: {type(exc).__name__}: {exc}") from exc
        return as_products([_text_product(f"astdys_{target.name.replace(' ', '_')}.txt",
                                          "AstDyS reachable; query the object page for elements",
                                          "AstDyS reachability marker")], self.name, "text")


@register
class SkybotAdapter(_ContextAdapter):
    """IMCCE SkyBoT / SkyBoT via the Miriade TAP-ish service (astroquery.imcce when installed).

    Discovery requires an observation epoch; without one it raises
    ``AdapterUnavailable`` rather than guessing.
    """

    name = "skybot"
    description = "IMCCE SkyBoT known-solar-system-object cone search at an observation epoch"
    formats = ("csv", "table")
    capabilities = ("known_objects", "context")
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 100, epoch_iso: str | None = None,
                 radius_arcsec: float = 10.0, **opts) -> list[ProductRef]:
        if epoch_iso is None:
            raise AdapterUnavailable("SkyBoT needs epoch_iso (encoded trails are epoch-dependent)")
        try:
            from astroquery.imcce import Skybot  # type: ignore
            import astropy.units as u
            from astropy.coordinates import SkyCoord
            from astropy.time import Time

            coord = SkyCoord(target.ra_deg * u.deg, target.dec_deg * u.deg, frame="icrs")
            try:
                table = Skybot.cone_search(coord, u.Quantity(radius_arcsec, u.arcsec), Time(epoch_iso, scale="utc"))
            except RuntimeError as exc:
                # astroquery raises when the field holds no known object: that is a result (no match), not an outage
                if "No solar system object was found" not in str(exc):
                    raise
                table = None
            rows = [] if table is None else [{c: str(table[c][i]) for c in table.colnames} for i in range(len(table))]
        except ImportError as exc:
            raise AdapterUnavailable(f"astroquery.imcce not installed: {exc}") from exc
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"SkyBoT failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"skybot_{target.name.replace(' ', '_')}.csv", "format": "csv",
                             "description": f"SkyBoT cone {radius_arcsec:g}\" at {epoch_iso} ({len(rows)} rows)",
                             "rows": rows, "inline": True}], self.name, "csv")