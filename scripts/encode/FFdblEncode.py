#!/usr/bin/env python
#
# FFdblEncode.py
# FontForge: Double encode all glyphs based on double encoding data in a file
# Lines in file should look like: "LtnSmARetrHook",U+F236,U+1D8F
# usage: python FFdblEncode.py [sourcefont.sfd] [input file name] [output file name]
# from http://projects.palaso.org/projects/pysilfont
#
# Copyright (c) 2013, SIL International  (http://www.sil.org)
# Released under the MIT License (http://sil.mit-license.org)

import fontforge, sys, string, os.path

def splitfn(fn): # Split filename into path, base and extension
	p = os.path.split(fn)
	f = os.path.splitext(p[1])
	return (p[0], f[0], os.path.extsep + f[1])

def UniStr(u):
	if u:
		return "U+{0:04X}".format(u)
	else:
		return "No USV" #length same as above

args = len(sys.argv)

# Open the font
if args>1:
	fn = sys.argv[1]
else:
	# urrgh, we'll deal with this later when we do argument parsing
	fn = "/home/david/RFS/testdata/GenBasR.sfd"

(fpath,fontn,fext) = splitfn(fn)
fn = os.path.join(fpath, fontn+'.sfd')  # to be precise os.path.join(fpath, fontn + os.path.extsep + 'sfd')
print 'Opening ' + fn
font = fontforge.open(fn)

# Open the input file
if args>2:
	fn = sys.argv[2]
else:
	fn = os.path.join(fpath, fontn+'DblEnc'+'.txt')

(opath,obase,oext)=splitfn(fn)
fn = os.path.join(opath or fpath, (obase or fbase) + (oext or '.txt'))
print 'Opening ' + fn
inpf = open(fn, "r")


# Open the log file
if args>3:
	fn = sys.argv[3]
else:
	fn = fpath+fontn+'DblEnc'+'.log'

(opath,obase,oext)=splitfn(fn)
fn = os.path.join(opath or fpath, (obase or fbase) + (oext or '.log'))
fn = opath+obase+oext
print 'Opening ' + fn
logf = open(fn, "w")

# Create dbl_encode list from lines
dbl_encode = {}
for line in inpf.readlines() :
	glyphn, pua_usv_str, std_usv_str = line.strip().split(",")  # will exception if not 3 elements
	if glyphn[0] in '"\'' : glyphn = glyphn[1:-1]               # slice off quote marks, if present
	pua_usv, std_usv = int(pua_usv_str[2:], 16), int(std_usv_str[2:], 16)
	dbl_encode[glyphn] = [std_usv, pua_usv]
inpf.close()

for glyph in sorted(dbl_encode.keys()) :
	if glyph not in font : continue         # ignore missing glyphs (assuming you want this)
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
	g.altuni = ((dbl[1],),)     # maybe easier as a list [[dbl[1]]] if it works
	logf.write("encoding for %s changed: %s -> %s\n" % (glyph, ousvs, dbl))
	# fl.UpdateGlyph(glyph_ix)

# fl.UpdateFont()
font.save()
logf.close()

print "done"
