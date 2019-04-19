# `awesome-bib-builder`

This is a small collection of Python scripts which transforms the contents of
`.bib` files into the structured `README.md` at the base of this repository.

## License

Built copies of the `README.md` are released as Public Domain. This software
is released under an MIT License. A copy of the MIT License
is included in this directory.

## Building the README

If you are using `conda` to manage Python environments, you might create a
new environment for this repository.

```bash
$ conda create -n awesome python=3.7
$ conda activate awesome
$ pip install -r src/requirements.txt
```

The easiest way to build a new copy of the README is then to use make:

```bash
$ make clean
$ make
```

## Hacking on `awesome-bib-builder`

The contents of this directory determine how papers are listed and formatted.
Bug reporting or quality-of-life enhancements that make papers easier to
search or display are appreciated.

#### Relevant Documentation

* **BibtexParser** [Documentation](https://bibtexparser.readthedocs.io/en/master/index.html), [PyPi](https://pypi.org/project/bibtexparser/)
* **configparser** [Documentation](https://docs.python.org/3/library/configparser.html)
* **liquidpy** [Documentation](https://pwwang.github.io/liquidpy/), [PyPi](https://pypi.org/project/liquidpy/)

#### Code Style

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

There are a couple extra dependencies beyond those required for building copies
of the README. Mostly these are included to enforce consistent code style:

```bash
$ pip install -r src/requirements-develop.txt
```

Once these are installed, running `make style` will format the `src/` directory.

```bash
$ make style
```

## Future Goals

- [ ] Testing
  - [ ] Unit Tests for functions in `bibparser.py`
  - [ ] Functional Tests for common problems (e.g. format errors in .bib files)
- [ ] Package
  - [ ] Is this package project-specific, or would it be useful to generalize and move it elsewhere?
