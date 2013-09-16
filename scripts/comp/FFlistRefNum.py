#!/usr/bin/env python
#
# FFlistRefNum.py
# FontForge: Report Glyph name, Number of references (components)
# usage: python FFlistRefNum.py [sourcefont.sfd] [output file name]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013, SIL International  (http://www.sil.org)
# Released under the MIT License (http://sil.mit-license.org)

import fontforge, sys, string

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
	fn = fpath+fontn+'NumRef'+'.txt'

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
