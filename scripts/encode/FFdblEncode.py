#!/usr/bin/env python
#
# FFdblEncode.py
# FontForge: Double encode all glyphs based on double encoding data in a file
# Lines in file should look like: "LtnSmARetrHook",U+F236,U+1D8F
# usage: python FFdblEncode.py [sourcefont.sfd] [input file name] [output file name]
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

# Open the input file
if args>2:
	fn = sys.argv[2]
else:
	fn = fpath+fontn+'DblEnc'+'.txt'

(opath,obase,oext)=splitfn(fn)
if opath == '':
	opath=fpath
if obase == '':
	obase = font
if oext == '':
	oext = '.txt'
fn = opath+obase+oext
print 'Opening ' + fn
inpf = open(fn, "r")


# Open the log file
if args>3:
	fn = sys.argv[3]
else:
	fn = fpath+fontn+'DblEnc'+'.log'

(opath,obase,oext)=splitfn(fn)
if opath == '':
	opath=fpath
if obase == '':
	obase = font
if oext == '':
	oext = '.log'
fn = opath+obase+oext
print 'Opening ' + fn
logf = open(fn, "w")

# Read the lines from the input file
lines = inpf.readlines()
inpf.close()

# Create dbl_encode list from lines
dbl_encode = {}
for line in lines:
	fields = line.strip().split(",") #this should be safe given the format of the DblEnc file
	assert(len(fields) == 3)
	glyphn, pua_usv_str, std_usv_str = fields[0], fields[1], fields[2]
	glyphn = glyphn[1:-1] #slice off quote marks
	pua_usv, std_usv = int(pua_usv_str[2:], 16), int(std_usv_str[2:], 16)
	dbl_encode[glyphn] = [std_usv, pua_usv]

glyphs = dbl_encode.keys()
glyphs.sort()
for glyph in glyphs:
	g = font[glyph]
	ousvs=[g.unicode]
	oalt=g.altuni
	if oalt != None:
		print oalt
		for au in oalt:
			print au
			ousvs.append(au[0]) # (may need to check variant flag)
	dbl = dbl_encode[glyph]
	g.unicode = dbl[0]
	g.altuni = ((dbl[1],),)
	logf.write("encoding for %s changed: %s -> %s\n" % (glyph, ousvs, dbl))
	# fl.UpdateGlyph(glyph_ix)

# fl.UpdateFont()
font.save()
logf.close()

print "done"
