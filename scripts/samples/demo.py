#!/usr/bin/env python
'FontForge: Sample module to use with executescript.py and menudemo.py'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge, types, sys

def selGlyphs(data,fontname) :
	# data and fontname are values passed automatically when called as a menu item - see docs for registerMenuItem
	# They are not used by the function

	font = fontforge.activeFont()
	print "Deselecting Glyphs" # Output from print statements will only appear when FF is called via a terminal window
	font.selection.none() # Deselect all to start with
	print "Selecting Glyphs"

	for glyph in font:
		g = font[glyph]
		if glyph.find('LtnCapC') >= 0: # Selects all glyphs with the string in their name
			#print glyph
			font.selection.select(("more",),glyph)

	print "Glyph's selected"

def renameGlyph(data,fontname,old,new) :
	font = fontforge.activeFont()
	g=font[old]
	print g.glyphname
	g.glyphname=new
