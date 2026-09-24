import warnings

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.mast import Tesscut

coord = SkyCoord(219.757 * u.deg, -80.531 * u.deg, frame="icrs")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    sectors = Tesscut.get_sectors(coordinates=coord)
    print("sectors columns:", sectors.colnames if hasattr(sectors, "colnames") else type(sectors))
    print(sectors)

    hduls = Tesscut.get_cutouts(coordinates=coord, size=5, sector=1)
    print("n cutouts:", len(hduls))
    for hdul in hduls:
        print("primary:", dict(datum for datum in hdul[0].header.items() if datum[0] in ("SECTOR", "CAMERA", "CCD", "TELESCOP", "OBJECT")))
        print("ext cols:", [h.name for h in hdul])
