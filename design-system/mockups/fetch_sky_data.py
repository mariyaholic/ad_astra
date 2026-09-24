"""Fetch the public catalogue data behind the sky-explorer prototype.

Everything the explorer draws comes from one of these recorded sources; each
fetch writes its own provenance (endpoint, query verbatim, UTC time, row count,
SHA-256) into data/PROVENANCE.json.

* Background stars   Yale Bright Star Catalogue, 5th ed. (VizieR V/50), V <= 6.5
* Milky Way glow     Gaia DR3 source counts, G < 11, per HEALPix level-5 cell (ESA Gaia TAP)
* Zoomed star fields Gaia DR3 cones around each Sesame-resolved position (ESA Gaia TAP)
* Planet systems     NASA Exoplanet Archive pscomppars for the project's planet hosts
* Atmospheres       NASA Exoplanet Archive spectra / transitspec / emissionspec for those planets
* Field imagery      CDS hips2fits colour cutouts: Pan-STARRS DR1 (Dec > -29) else 2MASS

Target positions are NOT fetched here: they come from the project's own
docs/tier1_pack/NAME_RESOLUTIONS.json.

Run:  python design-system/mockups/fetch_sky_data.py [--only NAME ...] [--missing]
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

WT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "data"
IMG = OUT / "fields"
PROV = OUT / "PROVENANCE.json"
UA = {"User-Agent": "cygnus-sky-explorer-prototype/0.1 (public-data fetch)"}

GAIA_TAP = "https://gea.esac.esa.int/tap-server/tap/sync"
VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
HIPS2FITS = "https://alasky.cds.unistra.fr/hips-image-services/hips2fits"

# Zoom-field radius per target (deg): clusters get their pack cone radius, stars a small field.
FIELD_RADIUS = {"Pleiades": 1.0, "M44": 1.0, "NGC 5139": 0.5, "NGC 6819": 0.25}
DEFAULT_RADIUS = 0.2
FIELD_GMAX = {"Pleiades": 14.0, "M44": 15.0, "NGC 5139": 16.0}
DEFAULT_GMAX = 17.0

# Exoplanet Archive host names for the project's target names.
EXO_HOSTS = {
    "Pi Mensae": "HD 39091", "HD 209458": "HD 209458", "WASP-12": "WASP-12",
    "TRAPPIST-1": "TRAPPIST-1", "GJ 1214": "GJ 1214", "51 Peg": "51 Peg",
    "AU Mic": "AU Mic", "WASP-126": "WASP-126", "DS Tuc": "DS Tuc A",
    "Iota Horologii": "iot Hor",  # absent from pscomppars on 2026-09-24
    "Proxima Centauri": "Proxima Cen",
}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def tap(url: str, adql: str, timeout: int = 300) -> bytes:
    r = requests.post(url, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
                      headers=UA, timeout=timeout)
    r.raise_for_status()
    return r.content


def record(prov: dict, key: str, **kw) -> None:
    prov[key] = {"retrieved_utc": now(), **kw}
    PROV.write_text(json.dumps(prov, indent=1, ensure_ascii=False), encoding="utf-8")


def fetch_bsc(prov: dict) -> None:
    q = ('SELECT HR, Name, RAJ2000, DEJ2000, Vmag, "B-V" FROM "V/50/catalog" '
         "WHERE Vmag <= 6.5 AND RAJ2000 IS NOT NULL")
    b = tap(VIZIER_TAP, q)
    (OUT / "bsc5.csv").write_bytes(b)
    record(prov, "bsc5.csv", source="Yale Bright Star Catalogue 5th rev. ed. (Hoffleit & Warren 1991), VizieR V/50",
           endpoint=VIZIER_TAP, query=q, rows=b.count(b"\n") - 1, sha256=sha(b),
           terms="VizieR/CDS: free use with acknowledgement of CDS and the catalogue authors")


def fetch_density(prov: dict) -> None:
    q = ("SELECT hpx, COUNT(*) AS n, AVG(x) AS x, AVG(y) AS y, AVG(z) AS z FROM ("
         "SELECT GAIA_HEALPIX_INDEX(5, source_id) AS hpx, COS(RADIANS(dec))*COS(RADIANS(ra)) AS x, "
         "COS(RADIANS(dec))*SIN(RADIANS(ra)) AS y, SIN(RADIANS(dec)) AS z FROM gaiadr3.gaia_source "
         "WHERE phot_g_mean_mag < 11) AS t GROUP BY hpx")
    b = tap(GAIA_TAP, q, timeout=900)
    (OUT / "gaia_density_hpx5_g11.csv").write_bytes(b)
    record(prov, "gaia_density_hpx5_g11.csv", source="Gaia DR3 gaia_source (ESA/Gaia/DPAC)",
           endpoint=GAIA_TAP, query=q, rows=b.count(b"\n") - 1, sha256=sha(b),
           note="cell centre = mean unit vector of member sources",
           terms="ESA Gaia data: CC BY-SA 3.0 IGO; acknowledge ESA/Gaia/DPAC")


def slug(name: str) -> str:
    return "".join(c.lower() if c.isalnum() else "-" for c in name).strip("-").replace("--", "-")


def fetch_fields(prov: dict, targets: dict, only: set[str]) -> None:
    for name, t in targets.items():
        if only and name not in only:
            continue
        r = FIELD_RADIUS.get(name, DEFAULT_RADIUS)
        g = FIELD_GMAX.get(name, DEFAULT_GMAX)
        q = ("SELECT TOP 6000 source_id, ra, dec, phot_g_mean_mag AS g, bp_rp, parallax, pmra, pmdec, "
             "teff_gspphot FROM gaiadr3.gaia_source WHERE 1 = CONTAINS(POINT('ICRS', ra, dec), "
             f"CIRCLE('ICRS', {t['ra_deg']:.8f}, {t['dec_deg']:.8f}, {r})) AND phot_g_mean_mag < {g} "
             "ORDER BY phot_g_mean_mag")
        b = tap(GAIA_TAP, q)
        fn = f"field_{slug(name)}.csv"
        (OUT / fn).write_bytes(b)
        record(prov, fn, source="Gaia DR3 gaia_source (ESA/Gaia/DPAC)", endpoint=GAIA_TAP, query=q,
               rows=b.count(b"\n") - 1, sha256=sha(b), radius_deg=r, g_max=g,
               terms="ESA Gaia data: CC BY-SA 3.0 IGO; acknowledge ESA/Gaia/DPAC")
        print("field", name, b.count(b"\n") - 1)
        time.sleep(1)


def fetch_planets(prov: dict) -> None:
    hosts = ", ".join("'" + h + "'" for h in EXO_HOSTS.values())
    q = ("SELECT hostname, pl_name, pl_letter, pl_orbper, pl_orbsmax, pl_rade, pl_radj, pl_bmasse, pl_orbeccen, "
         "pl_eqt, pl_orbper_reflink, pl_rade_reflink, st_teff, st_rad, st_mass, st_spectype, sy_dist, disc_year, discoverymethod, tran_flag, "
         "pl_dens, pl_insol, pl_ratror, pl_imppar, pl_trandur, pl_orbincl, pl_bmassprov, st_met, st_metratio, st_logg, st_age, st_lum, st_rotp, st_vsin "
         f"FROM pscomppars WHERE hostname IN ({hosts}) ORDER BY hostname, pl_orbper")
    b = tap(EXO_TAP, q)
    (OUT / "planets_pscomppars.csv").write_bytes(b)
    record(prov, "planets_pscomppars.csv", source="NASA Exoplanet Archive, Planetary Systems Composite Parameters",
           endpoint=EXO_TAP, query=q, rows=b.count(b"\n") - 1, sha256=sha(b),
           note="pscomppars mixes values from several references per planet; pl_orbper_reflink and pl_rade_reflink name the period and radius references",
           terms="NASA Exoplanet Archive: public; acknowledge per archive policy")


def fetch_spectra(prov: dict) -> None:
    """Published atmospheric spectra of the project's planets: the catalogue of spectra and the data points."""
    hosts = ", ".join("'" + h + "'" for h in EXO_HOSTS.values())
    names = [r.split(",")[0].strip('"') for r in tap(EXO_TAP, f"SELECT pl_name FROM pscomppars WHERE hostname IN ({hosts})").decode().splitlines()[1:]]
    inlist = ", ".join("'" + n + "'" for n in names)
    queries = {
        "spectra_catalogue.csv": ("NASA Exoplanet Archive, Atmospheric Spectroscopy (spectra)",
            f"SELECT pl_name, spec_type, authors, num_datapoints, instrument, facility, minwavelng, maxwavelng, note, bibcode "
            f"FROM spectra WHERE pl_name IN ({inlist}) ORDER BY pl_name, spec_type, authors"),
        "spectra_transmission.csv": ("NASA Exoplanet Archive, Transit Spectroscopy (transitspec)",
            f"SELECT plntname, centralwavelng, bandwidth, plntransdep, plntransdeperr1, plntransdeperr2, plntransdeplim, "
            f"plnratror, facility, instrument, plntranreflink FROM transitspec WHERE plntname IN ({inlist}) ORDER BY plntname, centralwavelng"),
        "spectra_emission.csv": ("NASA Exoplanet Archive, Emission Spectroscopy (emissionspec)",
            f"SELECT plntname, centralwavelng, bandwidth, especlipdep, especlipdeperr1, especlipdeperr2, especlipdeplim, "
            f"espbritemp, espbritemperr1, espbritemperr2, espbritemplim, facility, instrument, note, plntreflink "
            f"FROM emissionspec WHERE plntname IN ({inlist}) ORDER BY plntname, centralwavelng"),
    }
    for fn, (src, q) in queries.items():
        b = tap(EXO_TAP, q)
        (OUT / fn).write_bytes(b)
        record(prov, fn, source=src, endpoint=EXO_TAP, query=q, rows=b.count(b"\n") - 1, sha256=sha(b),
               note="Published measurements with their references; species identifications are not part of these tables",
               terms="NASA Exoplanet Archive: public; acknowledge per archive policy and cite the listed references")
        print(fn, b.count(b"\n") - 1)


def fetch_images(prov: dict, targets: dict, only: set[str]) -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    for name, t in targets.items():
        if only and name not in only:
            continue
        fov = 2 * FIELD_RADIUS.get(name, DEFAULT_RADIUS)
        hips = "CDS/P/PanSTARRS/DR1/color-z-zg-g" if t["dec_deg"] > -29 else "CDS/P/2MASS/color"
        params = {"hips": hips, "ra": f"{t['ra_deg']:.6f}", "dec": f"{t['dec_deg']:.6f}", "fov": f"{fov:.4f}",
                  "width": 768, "height": 768, "projection": "TAN", "format": "jpg"}
        r = requests.get(HIPS2FITS, params=params, headers=UA, timeout=180)
        r.raise_for_status()
        if not r.headers.get("content-type", "").startswith("image/"):
            raise RuntimeError(f"{name}: unexpected content type {r.headers.get('content-type')}")
        fn = f"fields/{slug(name)}.jpg"
        (OUT / fn).write_bytes(r.content)
        survey = "Pan-STARRS1 DR1 (g, zg, z colour composite)" if "PanSTARRS" in hips else "2MASS (J, H, Ks colour composite)"
        record(prov, fn, source=f"{survey} via CDS hips2fits, HiPS {hips}", endpoint=HIPS2FITS, query=params,
               sha256=sha(r.content), bytes=len(r.content), fov_deg=fov, orientation="north up, east left (TAN)",
               terms=("Pan-STARRS1: public (acknowledge PS1 and STScI/MAST)" if "PanSTARRS" in hips
                      else "2MASS: public (acknowledge UMass and IPAC/Caltech, NASA and NSF)")
               + "; HiPS rendering by CDS")
        print("image", name, len(r.content))
        time.sleep(1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=[])
    ap.add_argument("--skip", nargs="*", default=[], help="bsc density fields planets spectra images")
    ap.add_argument("--missing", action="store_true", help="only targets without a field file yet (new analyses)")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    prov = json.loads(PROV.read_text(encoding="utf-8")) if PROV.exists() else {}
    res = json.loads((WT / "docs" / "tier1_pack" / "NAME_RESOLUTIONS.json").read_text(encoding="utf-8"))
    targets = {k: v for k, v in res.items() if v.get("ok")}
    # targets that analyses declare with explicit positions (sky records) get fields and images too
    import sys
    sys.path.insert(0, str(WT / "src"))
    from cygnus import skyrecord
    for rec in skyrecord.load_records(WT):
        for t in rec.get("targets", []):
            if t["name"] not in targets and "ra_deg" in t:
                targets[t["name"]] = {"ra_deg": t["ra_deg"], "dec_deg": t["dec_deg"]}
    only = set(a.only)
    if a.missing:
        only = {n for n in targets if not (OUT / f"field_{slug(n)}.csv").exists()} or {"<none>"}
        a.skip = list(set(a.skip) | {"bsc", "density", "planets", "spectra"})
    steps = {"bsc": lambda: fetch_bsc(prov), "density": lambda: fetch_density(prov),
             "fields": lambda: fetch_fields(prov, targets, only), "planets": lambda: fetch_planets(prov),
             "spectra": lambda: fetch_spectra(prov),
             "images": lambda: fetch_images(prov, targets, only)}
    for k, fn in steps.items():
        if k in a.skip:
            continue
        try:
            fn()
            print("ok", k)
        except Exception as e:  # record the failure; never fabricate a substitute
            prov[f"FAILED:{k}"] = {"when": now(), "error": repr(e)[:500]}
            PROV.write_text(json.dumps(prov, indent=1, ensure_ascii=False), encoding="utf-8")
            print("FAILED", k, repr(e)[:300])


if __name__ == "__main__":
    main()
