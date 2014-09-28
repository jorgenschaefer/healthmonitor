.PHONY: test test-features done setup

test:
	coverage run --branch \
          `which django-admin.py` test healthmonitor
	coverage report -m \
          --include="*/healthmonitor/healthmonitor/*" \
	  --omit="*/migrations/*" \
	  --fail-under=95

test-features:
	django-admin.py test features

done: test test-features
	django-admin makemigrations --dry-run --noinput --no-color \
	  | grep -q "^No changes detected"
	flake8 --exclude="migrations" healthmonitor

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	npm install

testserver:
	django-admin runserver
