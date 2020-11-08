# Copyright © 2019 Alexander L. Hayes
# MIT License

import pytest
from src.reference import Reference

import bibtexparser

bibtex1 = """@ARTICLE{Cesar2013,
  author = {Jean César},
  title = {An amazing title},
  year = {2013},
  volume = {12},
  pages = {12--23},
  journal = {Nice Journal},
  abstract = {This is an abstract. This line should be long enough to test
     multilines...},
  comments = {A comment},
  keywords = {keyword1, keyword2},
  note = "structure-learning",
}
"""

bibtex2 = """@ARTICLE{Cesar2013,
  author = {Jean César},
  title = {An amazing title},
  year = {2013},
  volume = {12},
  pages = {12--23},
  journal = {Nice Journal},
  abstract = {This is an abstract. This line should be long enough to test
     multilines...},
  comments = {A comment},
  keywords = {keyword1, keyword2},
  url = "https://example.com",
}
"""

bibtex3 = """@ARTICLE{Cesar2013,
  author = {Jean César},
  title = {An amazing title},
  year = {2013},
  volume = {12},
  pages = {12--23},
  journal = {Nice Journal},
  abstract = {This is an abstract. This line should be long enough to test
     multilines...},
  comments = {A comment},
  keywords = {keyword1, keyword2},
  note = "parameter-learning",
  url = "https://example.com",
}
"""

bibtex4 = """@article{chow1968approximating,
  title={Approximating Discrete Probability Distributions with Dependence Trees},
  author={Chow, C and Liu, Cong},
  journal={IEEE Transactions on Information Theory},
  volume={14},
  number={3},
  pages={462--467},
  year={1968},
  publisher={IEEE},
  note="theory",
  url="https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf",
}
"""

bibtex5 = """@article{chow1968approximating,
  title={Approximating Discrete Probability Distributions with Dependence Trees},
  author={Chow, C and Liu, Cong},
  journal={IEEE Transactions on Information Theory},
  volume={14},
  number={3},
  pages={462--467},
  year={1968},
  publisher={IEEE},
  note="structure-learning",
  url="https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf",
}
"""


def test_reference_1():
    example = bibtexparser.loads(bibtex1)
    ref = Reference(example, "bib", "example.bib")
    assert ref.author == "Jean César"
    assert ref.title == "An amazing title"
    assert ref.year == 2013
    assert ref.journal == "Nice Journal"
    assert ref.url is None
    assert ref.note == "structure-learning"
    assert ref.file_location[0] == "bib"
    assert ref.file_location[1] == "example.bib"


def test_reference_2():
    example = bibtexparser.loads(bibtex2)
    ref = Reference(example, "bib", "example.bib")
    assert ref.author == "Jean César"
    assert ref.title == "An amazing title"
    assert ref.year == 2013
    assert ref.journal == "Nice Journal"
    assert ref.url == "https://example.com"
    assert ref.note == "Unclassified"
    assert ref.file_location[0] == "bib"
    assert ref.file_location[1] == "example.bib"


def test_reference_3():
    example = bibtexparser.loads(bibtex3)
    ref = Reference(example, "bibdir", "2013_cesar.bib")
    assert ref.author == "Jean César"
    assert ref.title == "An amazing title"
    assert ref.year == 2013
    assert ref.journal == "Nice Journal"
    assert ref.url == "https://example.com"
    assert ref.note == "parameter-learning"
    assert ref.file_location[0] == "bibdir"
    assert ref.file_location[1] == "2013_cesar.bib"


def test_reference_4():
    example = bibtexparser.loads(bibtex4)
    ref = Reference(example, "bib", "1968_chow.bib")
    assert ref.author == "Chow, C and Liu, Cong"
    _expected = (
        "Approximating Discrete Probability " "Distributions with Dependence Trees"
    )
    assert ref.title == _expected
    assert ref.year == 1968
    assert ref.journal == "IEEE Transactions on Information Theory"
    assert ref.url == "https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf"
    assert ref.note == "theory"
    assert ref.file_location[0] == "bib"
    assert ref.file_location[1] == "1968_chow.bib"


def test_get_names_1():
    example = bibtexparser.loads(bibtex1)
    ref = Reference(example, "bibdir", "2013_cesar.bib")
    _names = ref.get_names()
    assert _names == ["César, Jean"]


def test_get_names_2():
    example = bibtexparser.loads(bibtex4)
    ref = Reference(example, "bib", "1968_chow.bib")
    _names = ref.get_names()
    assert _names == ["Chow, C", "Liu, Cong"]


def test_load_1():
    ref = Reference.load("bib/1968", "1968_chow.bib")
    _names = ref.get_names()
    assert _names == ["Chow, C.", "Liu, C."]


def test_load_2():
    ref = Reference.load("bib/1968", "1968_chow.bib")
    assert ref.author == "C. Chow and C. Liu"
    _expected = (
        "Approximating Discrete Probability " "Distributions with Dependence Trees"
    )
    assert ref.title == _expected
    assert ref.year == 1968
    assert ref.journal == "IEEE Transactions on Information Theory"
    assert ref.url == "https://doi.org/10.1109/TIT.1968.1054142"
    assert ref.note == "theory"
    assert ref.file_location[0] == "bib/1968"
    assert ref.file_location[1] == "1968_chow.bib"


def test_formatting_1():
    example = bibtexparser.loads(bibtex1)
    ref = Reference(example, "bibdir", "2013_cesar.bib")
    _expected = (
        'Jean César. (2013). "An amazing title." Nice Journal. '
        "[`2013_cesar.bib`](bibdir/2013_cesar.bib)"
    )
    assert str(ref) == _expected


def test_formatting_2():
    example = bibtexparser.loads(bibtex4)
    ref = Reference(example, "bib", "1968_chow.bib")
    _expected = (
        'Chow, C and Liu, Cong. (1968). "[Approximating Discrete Probability '
        "Distributions with Dependence Trees]"
        '(https://ieeexplore.ieee.org/iel5/18/22639/01054142.pdf)."'
        " IEEE Transactions on Information Theory. [`1968_chow.bib`]"
        "(bib/1968_chow.bib)"
    )
    assert str(ref) == _expected
