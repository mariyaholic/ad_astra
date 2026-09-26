"""Live probes of every archive adapter (L3; ``python -m cygnus.multi archives --check all``).

Each probe asks one adapter a question whose answer is known to be non-empty, and reports a
service-aware status:

* ``ok`` — the service answered with the expected content;
* ``empty`` — it answered, but without the expected content (worth a look; not a code failure);
* ``unavailable`` — it could not be reached or refused (an outage: inconclusive, never failed);
* ``error`` — the adapter itself raised something unexpected (a code bug to investigate).

Probe positions are read from a committed campaign spec (a TOI position from the NASA Exoplanet
Archive) or computed live (Ceres from JPL Horizons), never typed in, so a probe cannot drift from
real sky coordinates.
"""

from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Any, Callable

from cygnus.config import WORKTREE

PROBE_SPEC = "campaigns/toi-2666-01.yaml"      # a bright TESS target with SPOC light curves, Gaia, SIMBAD entries
CERES_EPOCH_JD = 2460000.5                     # 2023-02-25 00:00 UT


def probe_target(root: Path = WORKTREE):
    import yaml

    from .archives.base import Target

    t = yaml.safe_load((root / PROBE_SPEC).read_text(encoding="utf-8"))["targets"][0]
    return Target.from_mapping(t)


def horizons_positions(text: str) -> list[dict]:
    """(UT, RA, Dec, APmag) rows between $$SOE and $$EOE of a Horizons observer table in degrees."""
    m = re.search(r"\$\$SOE(.*?)\$\$EOE", text, re.S)
    out = []
    for line in (m.group(1).strip().splitlines() if m else []):
        parts = line.split()
        try:
            out.append({"utc": f"{parts[0]} {parts[1]}", "ra_deg": float(parts[2]), "dec_deg": float(parts[3]),
                        "apmag": float(parts[4])})
        except (IndexError, ValueError):
            continue
    return out


def _rows(refs) -> int:
    return sum(len((r.extra or {}).get("rows") or []) for r in refs)


def _ceres(get) -> tuple[dict | None, str]:
    from .archives.base import Target

    refs = get("horizons").discover(Target(name="Ceres", ra_deg=0.0, dec_deg=0.0), command="'1;'", epochs_jd=[CERES_EPOCH_JD])
    pos = horizons_positions(str(refs[0].extra.get("text", "")))
    return (pos[0], "Horizons ephemeris of (1) Ceres") if pos else (None, "Horizons answered without an ephemeris row")


def _probes() -> dict[str, Callable[[Any, Any], tuple[bool, str]]]:
    """name -> f(get, target) -> (expected content present?, detail)."""
    from astropy.time import Time

    from .archives.base import Target

    def rows(name, **opts):
        def f(get, t):
            n = _rows(get(name).discover(t, **opts))
            return n > 0, f"{n} row(s)"
        return f

    def refs_(name, **opts):
        def f(get, t):
            refs = get(name).discover(t, **opts)
            return bool(refs), f"{len(refs)} product ref(s)" + (f", first {refs[0].product_id}" if refs else "")
        return f

    def status(name):
        def f(get, t):
            refs = get(name).discover(t)
            return bool(refs), f"{len(refs)} status product(s)"
        return f

    def horizons(get, t):
        pos, why = _ceres(get)
        return pos is not None, (f"Ceres at JD {CERES_EPOCH_JD}: RA {pos['ra_deg']:.4f} Dec {pos['dec_deg']:.4f}" if pos else why)

    def skybot(get, t):
        pos, why = _ceres(get)
        if pos is None:
            return False, why
        iso = Time(CERES_EPOCH_JD, format="jd", scale="utc").isot
        refs = get("skybot").discover(Target(name="ceres-field", ra_deg=pos["ra_deg"], dec_deg=pos["dec_deg"]),
                                      epoch_iso=iso, radius_arcsec=120)
        names = [str(r.get("Name", "")) for ref in refs for r in (ref.extra.get("rows") or [])]
        return any("Ceres" in n for n in names), f"{len(names)} object(s) at Ceres' Horizons position: {', '.join(names[:5])}"

    def mpc(get, t):
        from .archives.base import Target as T

        refs = get("mpc").discover(T(name="1998 SF36", ra_deg=0.0, dec_deg=0.0), output_format=["OBS80"])
        import json

        from .archives.solar_system import _n_obs

        rec = json.loads(refs[0].extra["text"])
        rec = rec[0] if isinstance(rec, list) and rec else rec
        n = _n_obs(rec.get("OBS80")) if isinstance(rec, dict) else 0
        return n > 0, f"1998 SF36 (Itokawa): {n} OBS80 observation line(s)"

    def fetched(name, **opts):
        def f(get, t):
            import tempfile

            a = get(name)
            ref = a.discover(t, **opts)[0]
            with tempfile.TemporaryDirectory() as d:
                p = a.fetch(ref, Path(d) / "probe.fits", timeout_s=120)
                head = p.read_bytes()[:6]
                return head == b"SIMPLE", f"{p.stat().st_size} bytes FITS from {ref.product_id}"
        return f

    def sbdb(get, t):
        import json

        from .archives.base import Target as T

        refs = get("sbdb").discover(T(name="Ceres", ra_deg=0.0, dec_deg=0.0))
        d = json.loads(refs[0].extra["text"])
        name = (d.get("object") or {}).get("fullname", "")
        return "Ceres" in name, f"SBDB object {name!r}"

    def ztf(get, t):
        import tempfile

        a = get("irsa")
        ref = a.discover(t, mode="ztf", radius_arcsec=5)[0]
        with tempfile.TemporaryDirectory() as d:
            p = a.fetch(ref, Path(d) / "ztf.vot", timeout_s=180)
            head = p.read_bytes()[:400]
            return head.lstrip().startswith(b"<?xml") or b"VOTABLE" in head, f"{p.stat().st_size} bytes, starts {head[:40]!r}"

    return {
        "mast": refs_("mast", limit=2), "gaia": rows("gaia", radius_arcsec=30), "simbad": rows("simbad", radius_arcsec=30),
        "vizier": rows("vizier", radius_arcsec=30, table="II/246/out"), "ned": rows("ned", radius_arcsec=60),
        "irsa": rows("irsa", radius_arcsec=10), "exoarchive": rows("exoarchive", mode="toi"),
        "eso": refs_("eso", radius_arcsec=60), "skyview": fetched("skyview", size_deg=0.05, pixels=50),
        "legacysurvey": fetched("legacysurvey", size_arcsec=30.0),
        "horizons": horizons, "sbdb": sbdb, "skybot": skybot, "mpc": mpc, "astdys": status("astdys"),
        "earthdata": status("earthdata"), "copernicus": status("copernicus"), "asf": status("asf"), "usgs": status("usgs"),
        "firms": status("firms"), "worldview": status("worldview"), "microobservatory": status("microobservatory"),
        "skynet": status("skynet"), "irsa-ztf": ztf,
    }


PROBE_NAMES = ("mast", "gaia", "simbad", "vizier", "ned", "irsa", "irsa-ztf", "exoarchive", "eso", "skyview",
               "legacysurvey", "horizons", "sbdb", "skybot", "mpc", "astdys", "earthdata", "copernicus", "asf",
               "usgs", "firms", "worldview", "microobservatory", "skynet")


def run_probe(name: str, *, get=None, target=None) -> dict:
    from .archives import base

    get = get or base.get
    probes = _probes()
    if name not in probes:
        return {"archive": name, "state": "error", "detail": f"no probe defined for {name!r}"}
    t0 = time.time()
    try:
        ok, detail = probes[name](get, target or probe_target())
        state = "ok" if ok else "empty"
    except base.AdapterUnavailable as exc:
        state, detail = "unavailable", str(exc)[:300]
    except (base.AdapterError, OSError, TimeoutError) as exc:
        state, detail = "unavailable", f"{type(exc).__name__}: {str(exc)[:300]}"
    except RuntimeError as exc:
        # the adapters' HTTP layer raises RuntimeError("HTTP <code> ...") for a refused request: an outage, not a bug
        state = "unavailable" if str(exc).startswith("HTTP ") else "error"
        detail = f"{type(exc).__name__}: {str(exc)[:300]}"
    except Exception as exc:  # noqa: BLE001 - an adapter bug, reported as such
        state, detail = "error", f"{type(exc).__name__}: {str(exc)[:300]}"
    return {"archive": name, "state": state, "detail": detail, "seconds": round(time.time() - t0, 1)}
