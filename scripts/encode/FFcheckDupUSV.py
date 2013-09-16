#!/usr/bin/env python
#
# FFcheckDupUSV.py
# FontForge: Check for duplicate USVs in unicode or altuni fields
# usage: python FFcheckDupUSV.py [sourcefont.sfd] [output file name]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013 SIL International
# Released under the MIT License (http://en.wikipedia.org/wiki/MIT_License)

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

def UniStr(u):
	if u:
		return "U+" + string.zfill(string.upper(hex(u)[2:]), 4)

	else:
		return "No USV" #length same as above

def AddUSV(usvs,usv,glyph):
	if not usvs.has_key(usv):

		usvs[usv] = [glyph]
	else:
		usvs[usv].append(glyph)

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
	fn = fpath+fontn+'DupUSV'+'.txt'

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

#** Main processing#

# Process unicode and altunicode for all glyphs
usvs={}
for glyph in font:
	g = font[glyph]
	if g.unicode != -1:
		usv=UniStr(g.unicode)
		AddUSV(usvs,usv,glyph)
	# Check any alternate usvs
	altuni=g.altuni
	if altuni != None:
		for au in altuni:
			usv=UniStr(au[0]) # (may need to check variant flag)
			AddUSV(usvs,usv,glyph + ' (alt)')

items = usvs.items()
items = filter(lambda x: len(x[1]) > 1, items)
items.sort()

for i in items:
	usv = i[0]
	print usv + ' has duplicates'
	gl = i[1]
	glyphs = gl[0]
	for j in range(1,len(gl)):
		glyphs = glyphs + ', ' + gl[j]

	outf.write('%s: %s\n' % (usv,glyphs))

outf.close()

print "Done!"
