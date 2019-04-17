# Copyright © 2019 Alexander L. Hayes
# MIT License

readme:
	python -m src
style:
	black src/
	pycodestyle --max-line-length=100 src/
clean:
	rm -f README.md
