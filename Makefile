.PHONY: deps, test

deps:
	python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt

test:
	PYTHONPATH=. python3 tests/test_suite.py
