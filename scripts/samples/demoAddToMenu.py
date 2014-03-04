#!/usr/bin/env python
'FontForge: Sample script to add menu items to FF tools menu'
__url__ = 'http://projects.palaso.org/projects/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import sys, os, fontforge
sys.path.append(os.path.join(os.environ['HOME'], 'src/pysilfont/scripts'))
import  samples.demoFunctions, samples.demoCallFunctions # Loads demo.py module from src/pysilfont/scripts/samples

def toolMenuFunction(font,functionGroup) : samples.demoCallFunctions.callFunctions(functionGroup)

funcList=samples.demoFunctions.functionList()

for functionGroup in funcList:
	menuType = funcList[functionGroup][0]
	fontforge.registerMenuItem(toolMenuFunction,None,functionGroup,menuType,None,functionGroup);
	print functionGroup, " registered"

''' This script needs to be called from one of the folders that FF looks in for scripts to
run when FF is started. With current versions of FF, one is Home/.config/fontforge/python.
You may need to turn on showing hidden files (ctrl-H in Nautilus) before you can see the .config
folder.  Within there create a one-line python script, say call sampledemo.py containing a call
to this script, eg:

execfile("/home/david/src/pysilfont/scripts/samples/menudemo.py")
'''
