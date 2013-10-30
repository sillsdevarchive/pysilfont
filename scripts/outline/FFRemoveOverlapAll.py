#!/usr/bin/env python

'''FFRemoveOverlapAll.py
FontForge: Remove overlap on all glyphs in font
usage: python FFRemoveOverlapAll.py [sourcefont.sfd] [output file name]'''
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'
__version__ = '0.0.1'
__menuentry__ = 'FFRemoveOverlapAll'

from silfont.fontforge.framework import execute

def doit(source, args) :
	for glyph in source:
		source[glyph].removeOverlap()
	return source

execute(doit)
