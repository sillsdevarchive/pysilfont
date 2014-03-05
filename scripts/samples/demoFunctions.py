#!/usr/bin/env python
'FontForge: Sample functions to call from other demo scripts'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge

def colLtnAGlyphs() :

	font = fontforge.activeFont()
	print "Toggling colour of glyphs with LtnCapA in their name"
	for glyph in font:
		g = font[glyph]
		if glyph.find('LtnCapA') >= 0:
			if g.color <> 0x00FF00:
				g.color = 0x00FF00 # Green
			else :
				 g.color = 0xFFFFFF # White

	print "Glyph's coloured"

def markOverlaps() :
	# Toggle oolour all Glyphs with overlaps
	font = fontforge.activeFont()
	print "Toggling colour of glyphs where contours overlap"
	for glyph in font:
		g = font[glyph]
		if g.selfIntersects() :
			if g.color <> 0xFF0000:
				g.color = 0xFF0000 # Red
			else :
				g.color = 0xFFFFFF # White

	print "Glyph's coloured"

def clearColours() :
	font = fontforge.activeFont()
	for glyph in font :
		g = font[glyph]
		g.color = 0xFFFFFF

def functionList() :
	''' Returns a dictionary to be used by demoCallFunctions.py either when adding
	items to the FontForge Tools menu or calling a group of similar functions via
	Execute,Script. The dictionary is indexed by a group name which could be used as
	Tools menu entry or to reference the group of functions.
	For each group there is a tuple consisting of the Tools menu type (Font or Glyph)
	then one tuple per function.
	For each function in the group there a tuple as follows:
			Function name
			Label for the individual function in dialog box called from Tools menu
			Actual function object'''
	funcList = {
		"Colour Glyphs":("Font",
		("colLtnAGlyphs","Colour Latin A Glyphs",colLtnAGlyphs),
		("markOverlaps","Mark Overlaps",markOverlaps),
		("clearColours","Clear all colours",clearColours)),
		"Another Group":("Font",
		("markOverlaps","Mark Overlaps",markOverlaps))}
	return funcList



