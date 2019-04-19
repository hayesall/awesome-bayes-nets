# Copyright © 2019 Alexander L. Hayes
# MIT License

from src.bibliography import Bibliography
from src.reference import Reference
from src.tests.test_reference import bibtex1, bibtex2, bibtex3, bibtex4, bibtex5
import bibtexparser
import pytest


def test_initialize_bibliography():
    _references = []
    for ref in [bibtex1, bibtex2, bibtex3, bibtex4, bibtex5]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)
    assert len(biblio.references) == 5
    assert biblio._verbose is False
    assert list(biblio._topics.keys()) == [
        "structure-learning",
        "Unclassified",
        "parameter-learning",
        "theory",
    ]


def test_build_toc_papers_by_year_1():
    _references = []
    for ref in [bibtex1, bibtex2, bibtex3, bibtex4]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    toc_years = biblio.create_toc_papers_by_year()
    assert toc_years == "    - [2013](#2013)\n    - [1968](#1968)"


def test_build_toc_papers_by_year_2():
    _references = []
    for ref in [bibtex1, bibtex2, bibtex3]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    toc_years = biblio.create_toc_papers_by_year()
    assert toc_years == "    - [2013](#2013)"


def test_build_toc_papers_by_year_3():
    _references = []
    for ref in [bibtex3, bibtex4]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    toc_years = biblio.create_toc_papers_by_year()
    assert toc_years == "    - [2013](#2013)\n    - [1968](#1968)"


def test_build_toc_topics_1():
    _references = []
    for ref in [bibtex1, bibtex2, bibtex3, bibtex4, bibtex5]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    toc_topics = biblio.create_toc_topics()

    _expected = (
        "    - [structure-learning](#structure-learning)\n"
        "    - [unclassified](#unclassified)\n"
        "    - [parameter-learning](#parameter-learning)\n"
        "    - [theory](#theory)"
    )

    assert toc_topics == _expected


def test_build_toc_topics_2():
    _references = []
    for ref in [bibtex1, bibtex3]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    toc_topics = biblio.create_toc_topics()

    _expected = (
        "    - [structure-learning](#structure-learning)\n"
        "    - [parameter-learning](#parameter-learning)"
    )

    assert toc_topics == _expected


def test_create_papers_by_year_list_1():
    _references = []
    for ref in [bibtex1, bibtex3]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    papers_by_year = biblio.create_papers_by_year_list()

    _expected = (
        "\n### 2013\n\n"
        '1. Jean César. (2013). "An amazing title." Nice Journal. '
        "[`bibfile`](bibpath/bibfile)\n"
        '2. Jean César. (2013). "[An amazing title](https://example.com)."'
        " Nice Journal. "
        "[`bibfile`](bibpath/bibfile)\n"
    )

    assert papers_by_year == _expected


def test_create_papers_by_year_list_2():
    _references = []
    for ref in [bibtex2, bibtex4]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    papers_by_year = biblio.create_papers_by_year_list()

    _expected = (
        "\n### 2013\n\n"
        '1. Jean César. (2013). "[An amazing title](https://example.com)."'
        " Nice Journal. "
        "[`bibfile`](bibpath/bibfile)\n"
        "\n### 1968\n\n"
        '1. Chow, C and Liu, Cong. (1968). "[Approximating Discrete Probability '
        "Distributions with Dependence Trees]"
        '(https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf)."'
        " IEEE Transactions on Information Theory. [`bibfile`]"
        "(bibpath/bibfile)\n"
    )

    assert papers_by_year == _expected


def test_create_papers_by_year_list_3():
    _references = []
    for ref in [bibtex2, bibtex4, bibtex5]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    papers_by_year = biblio.create_papers_by_year_list()

    _expected = (
        "\n### 2013\n\n"
        '1. Jean César. (2013). "[An amazing title](https://example.com)."'
        " Nice Journal. "
        "[`bibfile`](bibpath/bibfile)\n"
        "\n### 1968\n\n"
        '1. Chow, C and Liu, Cong. (1968). "[Approximating Discrete Probability '
        "Distributions with Dependence Trees]"
        '(https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf)."'
        " IEEE Transactions on Information Theory. [`bibfile`]"
        "(bibpath/bibfile)\n"
        '2. Chow, C and Liu, Cong. (1968). "[Approximating Discrete Probability '
        "Distributions with Dependence Trees]"
        '(https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf)."'
        " IEEE Transactions on Information Theory. [`bibfile`]"
        "(bibpath/bibfile)\n"
    )

    assert papers_by_year == _expected


def test_create_topics_list():
    _references = []
    for ref in [bibtex2, bibtex4]:
        _ref_str = bibtexparser.loads(ref)
        _references.append(Reference(_ref_str, "bibpath", "bibfile"))
    biblio = Bibliography(_references)

    papers_by_topic = biblio.create_topics_list()

    _expected = (
        "\n### unclassified\n\n"
        '1. Jean César. (2013). "[An amazing title](https://example.com)."'
        " Nice Journal. "
        "[`bibfile`](bibpath/bibfile)\n"
        "\n### theory\n\n"
        '1. Chow, C and Liu, Cong. (1968). "[Approximating Discrete Probability '
        "Distributions with Dependence Trees]"
        '(https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf)."'
        " IEEE Transactions on Information Theory. [`bibfile`]"
        "(bibpath/bibfile)\n"
    )

    assert papers_by_topic == _expected
