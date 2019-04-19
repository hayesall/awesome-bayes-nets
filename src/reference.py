# Copyright © 2019 Alexander L. Hayes
# MIT License


from bibtexparser.customization import getnames
import bibtexparser
import os


class Reference:
    """
    Internal representation of a BibTeX .bib file.

    :param bibtexparser.bibdatabase.BibDatabase db: Database

    The following four entries are strictly required to be in a .bib file:

    - "author"
    - "title"
    - "year"
    - "journal"

    Example:

    .. code-block:: python

        import bibtexparser

        with open("bib/1968_chow.bib", "r") as fh:
            _citation = bibtexparser.load(fh)

        db = Reference(_citation)
    """

    def __init__(self, db, bib_directory, file_name):
        self.db = db.entries[0]
        self.file_location = (bib_directory, file_name)
        self._make_data_keys(db.entries[0])

    def _make_data_keys(self, db):
        """
        Extract keys from db, creating references to keys in the dictionary.
        """

        self.author = db["author"]
        self.title = db["title"]
        self.year = int(db["year"])
        self.journal = db["journal"]

        # A "url" is not strictly required.
        if db.get("url"):
            self.url = db["url"]
        else:
            self.url = None

        # A "note" is not strictly required.
        if db.get("note"):
            self.note = db["note"]
        else:
            self.note = "Unclassified"

    @staticmethod
    def load(bib_directory, file_name):
        """
        Create an instance of Reference from a directory and a file_name.

        :param str bib_directory: Directory where bib file is stored.
        :param str file_name: Name of .bib file.

        .. code-block:: python

            >>> from src.reference import Reference
            >>> db = Reference.load("bib", "1968_chow.bib")
        """
        with open(os.path.join(bib_directory, file_name), "r") as fh:
            _citation = bibtexparser.load(fh)

        return Reference(_citation, bib_directory, file_name)

    def get_names(self):
        """
        Get a list of names from the reference.

        .. code-block:: python

            >>> with open("bib/1968_chow.bib", "r") as fh:
            ...    _citation = bibtexparser.load(fh)
            >>> db = Reference(_citation)
            >>> print(db.get_names())
            ['Friedman, Nir', 'Geiger, Dan', 'Goldszmidt, Moises']
        """
        return getnames(
            [i.strip() for i in self.db["author"].replace("\n", " ").split(" and ")]
        )

    def __repr__(self):
        if self.url:
            return '{0}. ({1}). "[{2}]({6})." {3}. [`{4}`]({5})'.format(
                self.author,
                self.year,
                self.title,
                self.journal,
                self.file_location[1],
                os.path.join(self.file_location[0], self.file_location[1]),
                self.url,
            )
        else:
            return '{0}. ({1}). "{2}." {3}. [`{4}`]({5})'.format(
                self.author,
                self.year,
                self.title,
                self.journal,
                self.file_location[1],
                os.path.join(self.file_location[0], self.file_location[1]),
            )
