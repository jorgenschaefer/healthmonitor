.PHONY: test test-features setup

DJANGO_SETTINGS_MODULE := healthmonitor.settings
PYTHONPATH := .


test:
	env DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
            PYTHONPATH=$(PYTHONPATH) \
	  coverage run --branch \
            `which django-admin.py` test healthmonitor
	coverage report -m --include="*/healthmonitor/healthmonitor/*" \
	  --fail-under=95

test-features:
	env DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
            PYTHONPATH=$(PYTHONPATH) \
	  django-admin.py test features

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	npm install
