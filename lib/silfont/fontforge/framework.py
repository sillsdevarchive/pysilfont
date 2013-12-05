#!/usr/bin/python

'''Module to wrap a fontforge type script so that it can be used either standalone
or as a macro within fontforge. Handles commandline attribute parsing.
The module pulls attribute strings from the calling module to help it.'''
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2013, SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Martin Hosken'
__version__ = '0.0.1'

import sys, argparse, shlex, os
import fontforge

def execute(fn, options = None) :
	'''There are various things to do in the calling module/script:
	* Set the docstring for the module/script
	* Optionally set __version__
	* set __menuentry__ for fontforge to add this to the macro menu
	'''
	if fontforge.hasUserInterface() :
		fontforge.registerMenuItem(_worker, None, (fn, options), "Font", None, fn.__module__.__menuentry__)
	else :
		_worker((fn, options))

def _findinlist(l, o) :
	for c, a in enumerate(l) :
		if a[0] == o : return c
	return -1

def _worker(data, font = None) :
	(fn, options) = data
	inui = fontforge.hasUserInterface()
	parser = None
	basemodule = sys.modules[fn.__module__]
	poptions = {}
	if inui : poptions['prog'] = ''
	poptions['description'] = basemodule.__doc__
	if hasattr(basemodule, '__version__') : poptions['epilog'] = "Version: " + basemodule.__version__
	fixedopts = [
		('infont', {'help' : 'Input font file'}),
		('outfont', {'nargs' : '?', 'help' : 'Output font file'})]
	if options :
		for c,o in enumerate(options) :
			test = o[0]
			if 'dest' in o[-1] : test = o[-1]['dest']
			ind = _findinlist(fixedopts, test)
			if ind >= 0 :
				if inui : del options[c]
				else : del fixedopts[ind]
	else :
		options = []
	if not inui :
		for c, o in enumerate(fixedopts) :
			options.insert(c, o)

	if options :
		parser = argparse.ArgumentParser(**poptions)
		for o in options :
			kwds = o[-1]
			parser.add_argument(*o[:-1], **kwds)
	if parser :
		if inui :
			msg = parser.format_help()
			ans = fontforge.askString(basemodule.__menuentry__, msg)
			args = parser.parse_args(shlex.split(ans))       # split using shell rules
		else :
			args = parser.parse_args()
			if hasattr(args, 'infont') :
				font = fontforge.open(os.path.abspath(args.infont))
	else :
		args = None
	f = fn(font, args)
	if f and hasattr(args, 'outfont') :
		print "Saving to "+ args.outfont
		f.save(args.outfont)
