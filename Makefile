.PHONY: test test-features done setup

test:
	coverage run --branch \
          `which django-admin.py` test healthmonitor \
	  --settings=healthmonitor.settings_devel_fast
	coverage report -m \
          --include="*/healthmonitor/healthmonitor/*" \
	  --omit="*/migrations/*" \
	  --fail-under=95

test-features:
	django-admin.py test features --settings=healthmonitor.settings_devel

done: test test-features
	django-admin makemigrations --dry-run --noinput --no-color \
	  --settings=healthmonitor.settings_devel \
	  | grep -q "^No changes detected"
	flake8 --exclude="migrations" healthmonitor

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	npm install

runserver:
	django-admin migrate --settings=healthmonitor.settings_devel
	django-admin runserver --settings=healthmonitor.settings_devel
