#!/usr/bin/env python
'''Report Glyph name, Number of references (components)'''
__version__ = '0.0.1'
__menuentry__ = 'Not_needed'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = '''
Copyright (c) 2013, SIL International  (http://www.sil.org)
Released under the MIT License (http://sil.mit-license.org)
'''

import fontforge, sys, string
from silfont.fontforge.framework import execute

opts = [
	('-o','--output',{'help': 'Output text file'})
	]


def doit(font, args):
	# Open the output file
	if not args.output : args.output = args.infont.replace('.sfd', 'RefNum.txt')
	print 'Opening ' + args.output
	outf = open(args.output, 'w')

	#*** Main processing

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
