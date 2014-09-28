# Settings for running unittests. These are optimized for speed.

from .settings_devel import *  # noqa

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = []
MIGRATION_MODULES = {
    "weight": "healthmonitor.migrations_not_used_in_tests"
}
