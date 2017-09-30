publish: clean
	python setup.py sdist upload

clean:
	#rm -rf Adafruit_BBIO.* build dist
	rm -f *.pyo
	rm -f *.egg
tests:
	py.test

build:
	python setup.py build --force

install: build
	python setup.py install --force