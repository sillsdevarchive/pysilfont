#!/usr/bin/env python
#
# FFRemoveOverlapAll.py
# FontForge: Remove overlap on all glyphs in font
# Written by Victor Gaultney
# usage: python FFRemoveOverlapAll.py [sourcefont.sfd] [resultfont.sfd]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013, SIL International
# Released under the MIT license cited below:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys, fontforge

source = fontforge.open(sys.argv[1])
result = sys.argv[2]

for glyph in source:
	source[glyph].removeOverlap()
source.save(result)