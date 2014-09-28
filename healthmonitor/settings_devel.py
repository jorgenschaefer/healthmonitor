# Settings for running the testserver.

import os
from .settings import *  # noqa

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "bower_components"),
)
