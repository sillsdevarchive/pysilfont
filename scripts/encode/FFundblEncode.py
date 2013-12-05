#!/usr/bin/env python
'''FontForge: Re-encode double-encoded glyphs based on double encoding data in a file
Lines in file should look like: "LtnSmARetrHook",U+F236,U+1D8F'''
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge
from silfont.fontforge.framework import execute

opts = [
	('-i','--input',{'help': 'Input CSV text file'}),
	('-o','--output',{'dest': 'outfont', 'help': 'Output the font here'}),
	('-l','--log',{'help': 'Log file to output'})]

def doit(font, args) :
	if not args.input : args.input = args.infont.replace('.sfd', 'DblEnc.txt')
	if not args.log : args.log = args.infont.replace('.sfd', 'DblEnc.log')
	print 'Opening ' + args.input
	inpf = open(args.input, 'r')
	print 'Opening ' + args.log
	logf = open(args.log, 'w')
# Create dbl_encode list from the input file
	dbl_encode = {}
	for line in inpf.readlines():
		glyphn, pua_usv_str, std_usv_str = line.strip().split(",")  # will exception if not 3 elements
		if glyphn[0] in '"\'' : glyphn = glyphn[1:-1]               # slice off quote marks, if present
		pua_usv, std_usv = int(pua_usv_str[2:], 16), int(std_usv_str[2:], 16)
		dbl_encode[glyphn] = [std_usv, pua_usv]
	inpf.close()

	for glyph in sorted(dbl_encode.keys()):
		logf.write (reincode(font,glyph,dbl_encode[glyph][0]))
		logf.write (reincode(font,glyph+"Dep",dbl_encode[glyph][1]))
	logf.close()
	return font

def reincode(font,glyph,usv):
	if glyph not in font:
		return ("Glyph %s not in font\n" % (glyph))
	g = font[glyph]
	ousvs=[g.unicode]
	oalt=g.altuni
	if oalt != None:
		for au in oalt:
			ousvs.append(au[0]) # (may need to check variant flag)
	g.unicode = usv
	g.altuni = None
	return ("encoding for %s changed: %s -> %s\n" % (glyph, ousvs, usv))

execute(doit, options=opts)
