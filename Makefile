# Copyright © 2019 Alexander L. Hayes
# MIT License

.PHONY : clean all

# Rules for building pages.
all : README.md index.html
README.md:
	@echo Building README.md
	python -m src
index.html: README.md
	@echo Creating an index.html page from README.md
	pandoc README.md --to=html5 --output=index.html --css=static/github.css --highlight-style=haddock --self-contained --metadata pagetitle=awesome-bayes-nets

# Remove built pages.
clean:
	rm -f README.md index.html

# Rules for automated testing, code style, and linting.
test:
	pytest --cov=src src
style:
	black src/
	pycodestyle --max-line-length=100 src/
	npm test
