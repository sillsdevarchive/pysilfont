#!/usr/bin/env python

'''Remove overlap on all glyphs in font'''
__menuentry__ = 'FFRemoveOverlapAll'
__author__ = 'Victor Gaultney'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = '''
Copyright (c) 2013, SIL International (http://www.sil.org)
Released under the MIT License (http://sil.mit-license.org)
'''

import sys, fontforge
from silfont.fontforge.framework import execute

def doit(source, args) :
	for glyph in source:
		source[glyph].removeOverlap()
	return source

execute(doit)
