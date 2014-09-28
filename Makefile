.PHONY: test test-features check devel clean runserver

PYVENV := pyvenv-3.4
VIRTUALENV := ${WORKON_HOME}/healthmonitor/
PIP :=  $(VIRTUALENV)/bin/pip
DJANGOADMIN := $(VIRTUALENV)/bin/django-admin
NPM := npm
FLAKE8 := $(VIRTUALENV)/bin/flake8
COVERAGE := $(VIRTUALENV)/bin/coverage
PTHFILE := $(VIRTUALENV)/lib/python3.4/site-packages/_healthmonitor.pth

test:
	$(COVERAGE) run --branch \
          $(DJANGOADMIN) test healthmonitor \
	  --settings=healthmonitor.settings_devel_fast
	$(COVERAGE) report -m \
          --include="*/healthmonitor/healthmonitor/*" \
	  --omit="*/migrations/*" \
	  --fail-under=95

test-features:
	$(DJANGOADMIN) test features --settings=healthmonitor.settings_devel

check: test test-features
	$(DJANGOADMIN) makemigrations --dry-run --noinput --no-color \
	  --settings=healthmonitor.settings_devel \
	  | grep -q "^No changes detected"
	$(FLAKE8) --exclude="migrations" healthmonitor

devel:
	test -d $(VIRTUALENV) || $(PYVENV) $(VIRTUALENV)
	test -f $(PTHFILE) || echo `pwd` > $(PTHFILE)

	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	$(NPM) install
	cd healthmonitor/core/static/ ; \
	  ../../../node_modules/.bin/bower install --production

clean:
	find -name '*.pyc' -delete
	find -name '__pycache__' -delete
	rm -rf node_modules/
	rm -rf healthmonitor/core/static/bower_components/
	rm -rf static/

compress:
	$(DJANGOADMIN) compress --force --settings=healthmonitor.settings_devel

migrations:
	$(DJANGOADMIN) makemigrations --settings=healthmonitor.settings_devel

runserver:
	$(DJANGOADMIN) migrate --settings=healthmonitor.settings_devel
	$(DJANGOADMIN) runserver --settings=healthmonitor.settings_devel
