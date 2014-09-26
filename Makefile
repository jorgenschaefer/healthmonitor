.PHONY: test feature-test

test:
	django-admin.py test --pythonpath=. --settings=healthmonitor.settings

test-features:
	python features/run.py

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	npm install
