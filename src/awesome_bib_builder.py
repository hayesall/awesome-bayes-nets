# Copyright © 2019 Alexander L. Hayes
# MIT License

"""
awesome_bib_builder
===================

Parses contents of ``bib/*.bib`` files, creating citations.
"""

from .reference import Reference
from .bibliography import Bibliography

from liquid import Liquid
import os


def run(
    template="static/README.md", bib_directory="bib", output="README.md", quiet=False
):
    """
    Parse .bib files (bib_directory), sort them, insert them into the template
    (template), then write them to a file (output).

    :arg quiet: If true, silence all status messages.
    """

    _verbose = not quiet

    if _verbose:
        print("📖 Reading *.bib files in {0}".format(bib_directory))

    _references = []

    for file in os.listdir(bib_directory):
        _references.append(Reference.load(bib_directory, file))

    biblio = Bibliography(_references, verbose=_verbose)

    TOC_PAPERS_BY_YEAR = biblio.create_toc_papers_by_year()
    TOC_PAPERS_BY_TOPIC = biblio.create_toc_topics()
    PAPERS_BY_YEAR = biblio.create_papers_by_year_list()
    PAPERS_BY_TOPIC = biblio.create_topics_list()

    # TODO: Create a section for `Algorithms`
    ALGORITHMS = []

    if _verbose:
        print("📜 Reading template: {0}".format(template))

    with open(template, "r") as fh:
        readme = fh.read()

    if _verbose:
        print("✍️ Rendering new copy of {0}".format(output))

    liq = Liquid(readme)
    ret = liq.render(
        toc_papers_by_year=TOC_PAPERS_BY_YEAR,
        toc_papers_by_topic=TOC_PAPERS_BY_TOPIC,
        papers_by_year=PAPERS_BY_YEAR,
        papers_by_topic=PAPERS_BY_TOPIC,
    )

    if _verbose:
        print("💾 Saving {0}".format(output))

    # TODO: Use the built-in file handler for liquid.
    with open(output, "w") as fh:
        fh.write(ret)
