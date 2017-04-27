#!/usr/bin/env python

import os
import sys

# If running from a git repository, insert the repository into sys.path
# so that sawtooth_xo is imported from there.
if os.path.exists(os.path.join(os.path.dirname(__file__), "..", ".git")):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sawtooth_ac.ac_cli import main_wrapper

if __name__ == '__main__':
    main_wrapper()
