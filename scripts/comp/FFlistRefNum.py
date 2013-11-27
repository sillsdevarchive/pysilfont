#!/usr/bin/env python
'FontForge: Report Glyph name, Number of references (components)'
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


def doit(font, args):
	if not args.output : args.output = args.infont.replace('.sfd', 'RefNum.txt')
	print 'Opening ' + args.output
	outf = open(args.output, 'w')

	outf.write("# glyphs with number of components\n\n")
	for glyph in font:
		gname=font[glyph].glyphname
		ref = font[glyph].references
		if ref is None:
			n=0
		else:
			n=len(ref)
		outf.write("%s %i\n" % (gname,n))

	outf.close()

	print "Done!"

execute(doit, options = opts)
