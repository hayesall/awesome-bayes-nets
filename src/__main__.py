# Copyright © 2019 Alexander L. Hayes
# MIT License

"""
Builds a copy of README.md from .bib files and a template.

By default, all parameters are loaded in from config.ini.
Using an optional argument will overwrite the value specified
in the config file.
"""

from . import awesome_bib_builder
from ._meta import __version__, __copyright__, __license__, __email__

import argparse
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")
TEMPLATE = CONFIG["DEFAULT"]["template"]
BIBDIR = CONFIG["DEFAULT"]["bib_directory"]
OUTPUT = CONFIG["DEFAULT"]["output"]
QUIET = CONFIG["cli"].getboolean("quiet")

PARSER = argparse.ArgumentParser(
    prog="awesome-bib-builder@{0}".format(__version__),
    description=__doc__,
    epilog="{0} ({1}). Distributed under the terms of the {2} License.".format(
        __copyright__, __email__, __license__
    ),
)
PARSER.add_argument(
    "-o", "--output", help="Set the output file location.", default=None
)
PARSER.add_argument(
    "-q", "--quiet", help="Silence all status messages.", action="store_true"
)

ARGS = PARSER.parse_args()

if ARGS.output:
    OUTPUT = ARGS.output
QUIET = ARGS.quiet | QUIET

awesome_bib_builder.run(
    template=TEMPLATE, bib_directory=BIBDIR, output=OUTPUT, quiet=QUIET
)
