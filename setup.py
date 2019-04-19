"""
Setup file for awesome-bib-builder
"""

import codecs
import os

from setuptools import find_packages, setup

# Get __version__ from _meta.py
_meta_file = os.path.join("src", "_meta.py")
with open(_meta_file) as f:
    exec(f.read())

DISTNAME = "awesome-bib-builder"
DESCRIPTION = "Tool for generating an awesome README from bib files."
with codecs.open("src/README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

MAINTAINER = __author__
MAINTAINER_EMAIL = __email__
URL = "https://github.com/batflyer/awesome-bayes-net"
LICENSE = __license__
DOWNLOAD_URL = "https://github.com/batflyer/awesome-bayes-net"
VERSION = __version__
CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
]
INSTALL_REQUIRES = ["liquidpy==0.0.6", "bibtexparser==1.1.0"]
EXTRAS_REQUIRE = {"tests": ["pytest", "pytest-cov"], "docs": ["sphinx"]}

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
