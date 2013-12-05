#!/usr/bin/env python
'Set Gylph names to standard PostScript names based on values in the gsi.xml file.'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge, sys, string, xml.sax
from silfont.fontforge import XmlFF
from silfont.fontforge.framework import execute

opts = [
	('-i','--input',{'help': 'Input gsi.xml file'}),
	('-o','--output',{'dest': 'outfont', 'help': 'Output the font here'}),
	('-l','--log',{'help': 'Log file to output'})]

def doit(font, args) :
	if not args.log : args.log = args.infont.replace('.sfd', 'setPSnames.log')
	print 'Opening ' + args.log
	logf = open(args.log, 'w')
# Parse the glyph supplemental info file
	if not args.input : args.input = args.infont.replace('.sfd', 'gsi.xml')
	parser = xml.sax.make_parser()
	handler = XmlFF.CollectXmlInfo()
	parser.setContentHandler(handler)
	parser.parse(args.input)
	gsi_dict = handler.get_data_dict()

# Rename the glyphs
	for glyph in font:
		g = font[glyph]
		sil_name = g.glyphname
		ps_nm = None
		try:
			if gsi_dict[sil_name].glyph_active == u"0": #skip inactive glyphs
				continue
			ps_nm = gsi_dict[sil_name].ps_name_value.encode() #encode() converts from Unicode string to std string
			g.glyphname = ps_nm
			logf.write("Glyph renamed - SIL Name: %s  PS Name: %s\n" % (sil_name, ps_nm))
		except:
			print "Glyph not renamed - SIL Name: %s" % sil_name
			logf.write("** Glyph not renamed - SIL Name: %s  PS Name: %s\n" % (sil_name, ps_nm))

	logf.close()
	return font

def UniStr(u):
	if u:
		return "U+{0:04X}".format(u)
	else:
		return "No USV" #length same as above

execute(doit, options = opts)
