#!/usr/bin/env python
'FontForge: Sample module various sample functions'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import sys, os, fontforge
sys.path.append(os.path.join(os.environ['HOME'], 'src/pysilfont/scripts'))
import  samples.demoFunctions # Loads demo.py module from src/pysilfont/scripts/samples
reload (samples.demoFunctions) # Reload the demo module each time you execute the script to pick up any recent edits

def callFunctions(functionGroup) :
	funcList=samples.demoFunctions.functionList()[functionGroup]
	i=0
	for tuple in funcList :
		print i
		if i == 0 :
			pass # Font/Glyph parameter not relevant here
		elif i == 1 :
			functionDescs=[tuple[1]]
			functions=[tuple[2]]
		else :
			functionDescs.append(tuple[1])
			functions.append(tuple[2])
		i=i+1

	if i == 2 : # Only one function in the group, so just call the function
		functions[0]()
	else :
		functionNum=fontforge.ask(functionGroup,"Please choose the function to run",functionDescs)
		functions[functionNum]()
