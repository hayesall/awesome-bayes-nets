# Copyright © 2019 Alexander L. Hayes
# MIT License

from . import bibparser
from ._meta import __author__, __version__, __copyright__, __license__, __email__

import argparse

PARSER = argparse.ArgumentParser()
ARGS = PARSER.parse_args()

bibparser.run()
