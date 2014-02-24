#!/usr/bin/env python
'FontForge: Sample code to paste into the "Execute Script" dialog'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import sys, os
sys.path.append(os.path.join(os.environ['HOME'], 'src/pysilfont/scripts'))
import samples.demo # Loads demo.py module from src/pysilfont/scripts/samples
reload (samples.demo) # Reload the demo module each time you execute the script to pick up any recent edits
from samples.demo import * # Loads the individual functions (in this case just selGlyphs) so they can just be called by name
colGlyphs(None,None) # Run the colGyphs function
#renameGlyph(None,None,"LtnCapA","LtnCapAA")

'''Suggested usage:
Open the "Execure Script" dialog (from the FF File menu or press ctrl+.)
Paste just the code section this (from "import" to "selGlyphs()") into there
Run it and see how it selects all glyphs with 'LtnCap' in their name.
Edit demo.py and alter the string in "glyph.find('LtnCap')"
Execute the script again and see that different glpyhs are selected
Make copies of this script and demo.py, strip out all my excess comments etc and start
coding your own functions

If you want to see the output from print statements (or use commands like raw_input),
then start FF from a terminal window rather than the desktop launcher.

When starting from a terminal window, you can also specify the font to use,
eg $ fontforge /home/david/RFS/GenBasR.sfd'''