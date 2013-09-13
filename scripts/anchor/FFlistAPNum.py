#!/usr/bin/env python
#
# FFlistAPNum.py
# FontForge: Report Glyph name, number of anchors - sorted by number of anchors
# usage: python FFlistAPNum.py [sourcefont.sfd] [output file name]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013 SIL International
# Released under the MIT License (http://en.wikipedia.org/wiki/MIT_License)

import fontforge, sys

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

def AP_cmp(a, b): # Comparision to sort first by number of attachment points) then by Glyph name
	c = cmp(a[1], b[1])
	if c != 0:
		return c
	else:
		return cmp(a[0], b[0])

args = len(sys.argv)

# Open the font
if args>1:
	fn = sys.argv[1]
else:
	fn = "/home/david/RFS/GenBasR.sfd"

(fpath,fontn,fext) = splitfn(fn)
fn = fpath+fontn+'.sfd'
print 'Opening ' + fn
font = fontforge.open(fn)

# Open the output file
if args>2:
	fn = sys.argv[2]
else:
	fn = fpath+fontn+'AncNum'+'.txt'

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

# Make a list of glyphs and number of anchor points
AP_lst = []
for glyph in font:
	AP_lst.append( [glyph, len(font[glyph].anchorPoints)] )
# Sort by numb of APs then glyphname
AP_lst.sort(AP_cmp)
for AP in AP_lst:
	outf.write("%s,%s\n" % (AP[0], AP[1]))

outf.close()
print "done"
