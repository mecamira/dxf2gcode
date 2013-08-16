#!/usr/bin/python

import os, sys
import subprocess

pyinpfad = "C:/Python27/pyinstaller-2.0/pyinstaller.py"

pyt = "C:/Python27/pythonw.exe"
filepfad= os.path.realpath(os.path.dirname(sys.argv[0]))
exemakepfad=filepfad
file = "dxf2gcode"
icon= "%s/dxf2gcode_pyQt4_ui/images/DXF2GCODE-001.ico" %filepfad
upxdir="C:/Python27/pyinstaller-2.0/upx309w"

options=("--noconsole --upx-dir=%s --icon=%s" %(upxdir, icon)) #uncomment to use uxp
#options=("--noconsole --icon=%s" %(icon)) #comment to use uxp
print options

#Verzwichniss wechseln
#Change Directory
exemakepfad = unicode( exemakepfad, "utf-8" )
os.chdir(exemakepfad.encode( "utf-8" ))


cmd=("%s %s %s %s/%s.py" %(pyt,pyinpfad,options,filepfad,file))
print cmd
retcode=subprocess.call(cmd)

#cmd=("%s %s/Build.py %s/%s.spec" %(pyt,pyinpfad,exemakepfad,file))
#print cmd
#retcode=subprocess.call(cmd)

print "\n!!!!!!!Do not forget the Bitmaps and Language folder!!!!!!"
print "\nREADY"
