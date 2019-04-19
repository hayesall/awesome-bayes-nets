# Copyright © 2019 Alexander L. Hayes
# MIT License


class Bibliography:
    """
    A Bibliography is a collection of References.

    :arg references: A list of `reference.Reference` objects.
    :arg _verbose: Print status messages.
    """

    def __init__(self, references, verbose=False):
        self.references = references
        self._verbose = verbose

        # Private internal data structures.
        self._references_by_year = sorted(
            self.references, key=(lambda r: r.year), reverse=True
        )
        self._build_topics_dictionary(references)

    def _build_topics_dictionary(self, references):
        _topics = dict()
        for paper in references:
            if _topics.get(paper.note):
                _topics[paper.note].append(paper)
            else:
                _topics[paper.note] = [paper]
        self._topics = _topics

    def create_toc_papers_by_year(self):
        """
        Create "Contents" entries for each year found in `self.references`

        :return: A string representing the README contents for papers.
        """
        _toc_by_year = ""

        _years = set()
        for entry in self._references_by_year:
            _years.add(entry.year)
        _years = sorted(list(_years), reverse=True)

        for entry in _years[:-1]:
            _toc_by_year += "    - [{0}](#{0})\n".format(entry)
        _toc_by_year += "    - [{0}](#{0})".format(_years[-1])

        return _toc_by_year

    def create_papers_by_year_list(self):
        """
        Create the "Papers by Year" section by sorting `self.references` by
        year.

        :return: A string representing the "Papers by Year" section.
        """

        _papers_by_year = self._references_by_year
        _papers_by_year_str = ""
        _previous_year = 0
        _i = 1

        for paper in _papers_by_year:
            if paper.year != _previous_year:
                _papers_by_year_str += "\n### {0}\n\n".format(paper.year)
                _i = 1
                _papers_by_year_str += "{0}. {1}\n".format(_i, paper)
                _previous_year = paper.year
            else:
                _papers_by_year_str += "{0}. {1}\n".format(_i, paper)
            _i += 1
        return _papers_by_year_str

    def create_toc_topics(self):
        """
        Create "Contents" entries for each topic in `self._topics`

        :return: A string representing the "Contents" section for topics.
        """
        _topics_toc_str = ""
        _topic_keys = list(self._topics.keys())

        for entry in _topic_keys[:-1]:
            _topics_toc_str += "    - [{0}](#{0})\n".format(entry.lower())
        _topics_toc_str += "    - [{0}](#{0})".format(_topic_keys[-1].lower())

        return _topics_toc_str

    def create_topics_list(self):
        """
        Create "Papers by Topic" section by sorting `self.references` and
        grouping by topic.

        :return: A string representing the "Papers by Topic" section.
        """
        _topics_str = ""
        _topic_keys = list(self._topics.keys())

        for key in _topic_keys:
            _topics_str += "\n### {0}\n\n".format(key.lower())
            _i = 1
            for entry in self._topics[key]:
                _topics_str += "{0}. {1}\n".format(_i, entry)
                _i += 1
        return _topics_str
