"""simplegui Setup Script

   Copyright (c) 2013 Florian Berger <fberger@florian-berger.de>
"""

# This file is part of simplegui.
#
# simplegui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# simplegui is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with simplegui.  If not, see <http://www.gnu.org/licenses/>.

# Work started on 29. Jan 2013.

from distutils.core import setup

import simplegui

SCRIPTS = []

EXECUTABLES = []

try:
    import cx_Freeze

    setup = cx_Freeze.setup

    EXECUTABLES = [cx_Freeze.Executable(path) for path in SCRIPTS]

except ImportError:

    print("Warning: the cx_Freeze module could not be imported. You will not be able to build binary packages.")

LONG_DESCRIPTION = ""

# Python 2.x doesn't honour the 'package_dir' and 'package_data' arguments to
# setup() when building an 'sdist'. Generate MANIFEST.in containing the
# necessary files.
#
print("regenerating MANIFEST.in for Python 2.x")
MANIFEST = open("MANIFEST.in", "wt")
MANIFEST.write("include COPYING")
MANIFEST.close()

setup(name = "simplegui",
      version = simplegui.VERSION,
      author = "Florian Berger",
      author_email = "fberger@florian-berger.de",
      url = "http://florian-berger.de/en/software/simplegui",
      description = "simplegui - Simplified GUI generation using Tkinter",
      long_description = LONG_DESCRIPTION,
      license = "GPL",
      py_modules = ["simplegui"],
      packages = [],
      requires = [],
      provides = ["simplegui"],
      scripts = SCRIPTS,
      executables = EXECUTABLES)
