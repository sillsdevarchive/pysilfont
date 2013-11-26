#!/usr/bin/env python
'''List all the data in FontForge glyph object(s) in key, value pairs'''
__version__ = '0.0.1'
__menuentry__ = 'Not_needed'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = '''
Copyright (c) 2013, SIL International  (http://www.sil.org)
Released under the MIT License (http://sil.mit-license.org)
'''

import fontforge, types,sys
from silfont.fontforge.framework import execute

opts = [
	('-o','--output',{'help': 'Output text file'})
	]

def doit(font, args) :
	if not args.output : args.output = args.infont.replace('.sfd', 'glyphinfo.txt')
	print 'Opening ' + args.output
	outf = open(args.output, 'w')

	glyphn = raw_input("Glyph name or number: ")

	while glyphn:

		isglyph=True
		if not(glyphn in font):
			try:
				glyphn=int(glyphn)
			except ValueError:
				isglyph=False
			else:
				if not(glyphn in font):
					isglyph=False

		if isglyph:
			g=font[glyphn]
			outf.write("\n%s\n\n" % glyphn)
			# Write to file all normal key,value pairs - exclude __ and built in functions
			for k in dir(g):
				if k[0:2] == "__": continue
				attrk=getattr(g,k)
				if attrk is None: continue
				tk=type(attrk)
				if tk == types.BuiltinFunctionType: continue
				if k == "ttinstrs": # ttinstr values are not printable characters
					outf.write("%s,%s\n" % (k,"<has values>"))
				else:
					outf.write("%s,%s\n" % (k,attrk))
			# Write out all normal keys where value is none
			for k in dir(g):
				attrk=getattr(g,k)
				if attrk is None:
					outf.write("%s,%s\n" % (k,attrk))
		else:
			print "Invalid glyph"

		glyphn = raw_input("Glyph name or number: ")
	print "done"
	outf.close

execute(doit, options = opts)