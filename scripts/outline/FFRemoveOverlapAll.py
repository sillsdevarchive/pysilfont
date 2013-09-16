#!/usr/bin/env python
#
# FFRemoveOverlapAll.py
# FontForge: Remove overlap on all glyphs in font
# Written by Victor Gaultney
# usage: python FFRemoveOverlapAll.py [sourcefont.sfd] [resultfont.sfd]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013, SIL International (http://www.sil.org)
# Released under the MIT License (http://sil.mit-license.org)

import sys, fontforge

source = fontforge.open(sys.argv[1])
result = sys.argv[2]

for glyph in source:
	source[glyph].removeOverlap()
source.save(result)