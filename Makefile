.PHONY: test test-features done setup

test:
	coverage run --branch \
          `which django-admin.py` test healthmonitor
	coverage report -m --include="*/healthmonitor/healthmonitor/*" \
	  --fail-under=95

test-features:
	django-admin.py test features

done: test test-features
	flake8 healthmonitor

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	npm install
