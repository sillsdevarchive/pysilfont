#!/usr/bin/env python
'FontForge: List all gyphs with encoding and name'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge, sys, string
from silfont.fontforge.framework import execute

opts = [
	('-o','--output',{'help': 'Output text file'})
	]

def doit(font, args) :
	if not args.output : args.output = args.infont.replace('.sfd', 'Gnames.txt')
	print 'Opening ' + args.output
	outf = open(args.output, 'w')

	# Process unicode and altunicode for all glyphs
	usvs={}
	for glyph in font:
		g = font[glyph]
		outf.write('%s: %s, %s\n' % (glyph, g.encoding, g.glyphname))

	outf.close()
	print "Done!"

execute(doit, options = opts)
