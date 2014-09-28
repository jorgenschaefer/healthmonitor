# Settings for running the testserver.

import os
from .settings import *  # noqa

STATIC_ROOT = os.path.join(BASE_DIR, "static")
LESSC = os.path.join(BASE_DIR, "node_modules/.bin/lessc")

COMPRESS_PRECOMPILERS = (
    ('text/less', LESSC + ' {infile} {outfile}'),
)
