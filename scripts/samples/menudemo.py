#!/usr/bin/env python
'FontForge: Sample script to add menu items to FF tools menu'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import sys, os
sys.path.append(os.path.join(os.environ['HOME'], 'src/pysilfont/scripts'))
import samples.demo # Loads demo.py module from src/pysilfont/scripts/samples
print "About to register functions" # This will only show if FF is run from a terminal window
# Register function form within demo.py as menu items
fontforge.registerMenuItem(samples.demo.colGlyphs,None,None,"Font",None,"Colour LtnCapA Glyphs");
print "Function registered"

''' This script needs to be copied to one of the folders that FF looks in for scripts to
run when FF is started. With current versions of FF, one is Home/.config/fontforge/python.
You may need to turn on showing hidden files (ctrl-H in Nautilus) before you can see the .config
folder.'''
