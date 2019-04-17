# Copyright © 2019 Alexander L. Hayes
# MIT License


class Reference:
    """
    A BibTeX Reference refers to a book or research paper.
    """

    def __init__(self, author, title, year, journal, file_location):
        self.author = author
        self.title = title
        self.year = int(year)
        self.journal = journal
        self.location = file_location

    def __repr__(self):
        return '{0}. ({1}). "{2}." {3}. [`{4}`]({5})'.format(
            self.author,
            self.year,
            self.title,
            self.journal,
            self.location[0],
            self.location[1],
        )
