# Fabric file for the health monitor.
#
# This should only be used for deployment tasks. make should be
# sufficient for development.

import os

from fabric.api import env, task, roles, lcd, local, run, put

BASE_DIR = os.path.dirname(__file__)

env.path = ":".join([
    '/home/forcer/bin/',
    os.path.join(BASE_DIR, "node_modules/.bin/")
])
env.roledefs = {
    'production': ['healthmonitor@loki']
}


@task
@roles('production')
def deploy():
    run("test -d venv || pyvenv-3.4 venv")
    run("test -f venv/lib/python3.4/site-packages/_healthmonitor.pth || "
        "echo $HOME/lib > venv/lib/python3.4/site-packages/_healthmonitor.pth")
    run("mkdir -p health.jorgenschaefer.de/static/")
    run("mkdir -p lib/")

    local("git archive -o deploy.tar.gz HEAD")
    put("deploy.tar.gz")
    local("rm deploy.tar.gz")
    run("tar -C lib/ -xzf deploy.tar.gz")
    run("rm deploy.tar.gz")

    run("venv/bin/pip install -qr lib/requirements.txt")
    run("venv/bin/django-admin migrate --noinput "
        "--settings=healthmonitor.settings_production")
    run("venv/bin/django-admin collectstatic --noinput "
        "--settings=healthmonitor.settings_production")

    with lcd("healthmonitor/core/static/"):
        local("bower install --production")
    local("tar -C healthmonitor/core/static/ -c bower_components/ "
          "-zf bower_components.tar.gz")
    put("bower_components.tar.gz")
    local("rm bower_components.tar.gz")
    run("tar -C health.jorgenschaefer.de/static/ -xzf bower_components.tar.gz")
    run("tar -C lib/healthmonitor/core/static/ -xzf bower_components.tar.gz")
    run("rm bower_components.tar.gz")

    local("make compress")
    local("tar -C static -c CACHE -zf compressed_cache.tar.gz")
    put("compressed_cache.tar.gz")
    local("rm compressed_cache.tar.gz")
    run("tar -C health.jorgenschaefer.de/static/ -xzf compressed_cache.tar.gz")
    run("rm compressed_cache.tar.gz")

    run("sudo /usr/bin/supervisorctl restart healthmonitor")
