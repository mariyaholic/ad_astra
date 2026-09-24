import inspect

from astroquery.mast import Tesscut

print("astroquery version:", __import__("astroquery").__version__)
print("get_cutouts:", inspect.signature(Tesscut.get_cutouts))
print("get_sectors:", inspect.signature(Tesscut.get_sectors))
