#!/usr/bin/env python
#
# FFlistGlyphinfo.py
# FontForge: List all the data in a FF glyph object in key, value pairs
# usage: python FFlistGlyphinfo.py [sourcefont.sfd] [output file name]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013 SIL International
# Released under the MIT License (http://en.wikipedia.org/wiki/MIT_License)

import fontforge, types,sys

def splitfn(fn): # Split filename into path, base and extension
	fsplit = fn.split("/")
	fpath=""
	j=len(fsplit)-1
	for i in range(0,j):
		fpath = fpath + fsplit[i] + '/'
	fn = fsplit[j] # Now just has base + extension
	fsplit = fn.split(".")
	fbase = fsplit[0] # Assume no .'s in base
	if len(fsplit) == 1:
		fext=""
	else:
		fext = "." + fsplit[1]
	return (fpath,fbase,fext)

args = len(sys.argv)

# Open the font
if args>1:
	fn = sys.argv[1]
else:
	fn = "/home/david/RFS/testdata/GenBasR.sfd"

(fpath,fontn,fext) = splitfn(fn)
fn = fpath+fontn+'.sfd'
print 'Opening ' + fn
font = fontforge.open(fn)

# Open the output file
if args>2:
	fn = sys.argv[2]
else:
	fn = fpath+fontn+'Glyphinfo'+'.txt'

(opath,obase,oext)=splitfn(fn)
if opath == '':
	opath=fpath
if obase == '':
	obase = font
if oext == '':
	oext = '.txt'
fn = opath+obase+oext
print 'Opening ' + fn
outf = open(fn, "w")

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
			if k[0:2] == "__":
				continue
			attrk=getattr(g,k)
			if attrk is None:
				continue
			tk=type(attrk)
			if tk == types.BuiltinFunctionType:
				continue
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

outf.close()
print "done"