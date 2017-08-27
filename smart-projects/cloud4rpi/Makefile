.PHONY: init style lint test clean release

build: init style lint test

init:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

style:
	pep8 --show-source --show-pep8 .

lint:
	pylint --rcfile=.pylintrc --reports=n cloud4rpi/*.py test/*.py examples/*.py

test:
	python -m unittest discover test

ci: style lint test

clean:
	rm -rf build/*
	rm -rf *.egg-info/*
	rm -rf dist/*

release: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*
