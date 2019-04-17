# Copyright © 2019 Alexander L. Hayes
# MIT License

"""
bibparser
=========

Parses contents of ``bib/*.bib`` files, creating citations.
"""

from .reference import Reference
from .bibliography import Bibliography

import configparser
import bibtexparser
from liquid import Liquid
import os


# TODO: config parameters would make more sense in __main__
#       perhaps set variables in main that are passed to bibparser.run()
CONFIG = configparser.ConfigParser()
CONFIG.read("config.toml")
TEMPLATE = CONFIG["DEFAULT"]["template"]
BIBDIR = CONFIG["DEFAULT"]["bibtex"]
OUTPUTDIR = CONFIG["DEFAULT"]["output"]


def build_references():
    """
    Build a list of references by iterating over the contents of a bibtex
    directory.
    """

    _references = []
    _reference_years = set()
    _topics = dict()

    for file in os.listdir(BIBDIR):

        with open(os.path.join(BIBDIR, file), "r") as fh:
            _citation = bibtexparser.load(fh)

        if _citation.entries[0].get("url"):
            _reference = Reference(
                _citation.entries[0]["author"],
                _citation.entries[0]["title"],
                _citation.entries[0]["year"],
                _citation.entries[0]["journal"],
                (file, os.path.join(BIBDIR, file)),
                _citation.entries[0]["url"],
            )
        else:
            _reference = Reference(
                _citation.entries[0]["author"],
                _citation.entries[0]["title"],
                _citation.entries[0]["year"],
                _citation.entries[0]["journal"],
                (file, os.path.join(BIBDIR, file)),
                None,
            )

        _references.append(_reference)
        _reference_years.add(int(_citation.entries[0]["year"]))

        _topic = _citation.entries[0]["note"]

        if _topics.get(_topic):
            _topics[_topic].append(_reference)
        else:
            _topics[_topic] = [_reference]

    return _references, _reference_years, _topics


def run():

    _references, _reference_years, _topics = build_references()

    # TODO: Convert to a  Method for `Bibliography`
    toc_papers_by_year = sorted(_reference_years, reverse=True)

    def create_toc_papers_by_year(toc_papers_by_year):
        _toc_by_year = ""
        for entry in toc_papers_by_year[:-1]:
            _toc_by_year += "    1. [{0}](#{0})\n".format(entry)
        _toc_by_year += "    1. [{0}](#{0})".format(toc_papers_by_year[-1])
        return _toc_by_year

    TOC_PAPERS_BY_YEAR = create_toc_papers_by_year(toc_papers_by_year)
    ###

    # TODO: Convert to a Method for `Bibliography`
    _papers_by_year = sorted(_references, key=(lambda r: r.year), reverse=True)

    def create_papers_by_year_list(papers_by_year):
        _papers_by_year = ""
        _previous_year = 0
        for entry in papers_by_year:
            if entry.year != _previous_year:
                _papers_by_year += "\n#### {0}\n\n".format(entry.year)
                _papers_by_year += "1. {0}\n".format(entry)
                _previous_year = entry.year
            else:
                _papers_by_year += "1. {0}\n".format(entry)
        return _papers_by_year

    PAPERS_BY_YEAR = create_papers_by_year_list(_papers_by_year)
    ###

    ###
    def create_toc_topics(topics):
        _topics = ""
        _topic_keys = list(topics.keys())
        for entry in _topic_keys[:-1]:
            _topics += "    1. [{0}](#{0})\n".format(entry)
        _topics += "    1. [{0}](#{0})".format(_topic_keys[-1])
        return _topics

    ###
    TOC_PAPERS_BY_TOPIC = create_toc_topics(_topics)

    ###
    def create_topics_list(topics):
        _topics = ""
        _topic_keys = list(topics.keys())
        for key in _topic_keys:
            _topics += "\n#### {0}\n\n".format(key)
            for entry in topics[key]:
                _topics += "1. {0}\n".format(entry)
        return _topics

    ###
    PAPERS_BY_TOPIC = create_topics_list(_topics)

    # TODO: Create a section for `Algorithms`
    ALGORITHMS = []

    with open("static/README.md", "r") as fh:
        readme = fh.read()

    liq = Liquid(readme)
    ret = liq.render(
        toc_papers_by_year=TOC_PAPERS_BY_YEAR,
        toc_papers_by_topic=TOC_PAPERS_BY_TOPIC,
        papers_by_year=PAPERS_BY_YEAR,
        papers_by_topic=PAPERS_BY_TOPIC,
    )

    # TODO: Use the built-in file handler for liquid.
    with open(OUTPUTDIR, "w") as fh:
        fh.write(ret)
