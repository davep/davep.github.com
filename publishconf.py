# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

##############################################################################
# Patch in the things we want for publishing.
SITEURL     = "https://blog.davep.org"
OUTPUT_PATH = "docs"

### publishconf.py ends here
