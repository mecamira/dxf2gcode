# Introduction #

The steps discussed in this wiki are only for users who want to make changes to DXF2GCODE; for normal use: just follow http://code.google.com/p/dxf2gcode/wiki/Installation

note:
The method described below is based on installing all the the modules one by one,
therefore the easiest way is to only install
Python(x,y)-2.7.5.0.exe (which contains already all the used modules)
https://code.google.com/p/pythonxy/

# Installing Python #

First download the required programs then install them as stated in �Setup� (below �Required Programs�)

## Required Programs ##
(the program names between brackets are the ones I had chosen)

(1) Python
http://www.python.org/download/releases/2.7.5/
(Windows x86 MSI Installer (2.7.5))

(2) pywin32 -- This name can be a bit confusing for 64bit users, but there is also a 64bit version of it, which is also named pywin32
http://sourceforge.net/projects/pywin32/files/pywin32/
(pywin32-218.win32-py2.7.exe)

(3) pyreadline-2.0
https://pypi.python.org/pypi/pyreadline/2.0
(pyreadline-2.0.win32.exe)

(4) PyQt4
http://www.riverbankcomputing.com/software/pyqt/download
(PyQt4-4.10.2-gpl-Py2.7-Qt4.8.4-x32.exe)

(5) pyinstaller-2.0
http://sourceforge.net/projects/pyinstaller/files/?source=navbar
(pyinstaller-2.0.zip)

(6) upx - optional, although, highly advised if you want the executable to be relatively small; in combination with pyinstaller-2.0 it will be almost 3 times smaller
http://upx.sourceforge.net/#downloadupx
(upx309w.zip)

## Setup ##
(1) Install Python 2.7.5 - for convenience just install it to the directory
```
C:\Python27
```

(2) Install pywin32

(3) Install pyreadline-2.0 (since for windows it's not automatically available)

(4) Install PyQt4 to the exact same folder as where Python is located
```
C:\Python27
```

(5) extract pyinstaller-2.0 to
```
C:\Python27\pyinstaller-2.0
```
(this is not a necessarily location for the pyinstaller, but since the �make\_exe.py� has this location as default, it might be just as easy to place it at this location as well)

(6) Extract upx to
```
C:\Python27\pyinstaller-2.0\upx309w
```
(again this location can be chosen freely but by default this location is used in �make\_exe.py�)


# Making an Executable #

Before every build delete the following two folders: "build", and "dist" (the first time you want to build these sub-directories should not be present).

Open "IDLE (Python GUI)" (probably located at Start->All Programs->Python 2.7) -> Open the file "make\_exe.py" -> Press F5 to run it.
Before going on wait till it shows READY.

Now it will make build folder which probably contains a "warndxf2gcode.txt" file. This file will most likely tell you are missing all kind of modules. Just ignore this file (The reason for it is that pyinstaller has some faults, which probably originated from the previous version, where you first had to make a spec and then do a build).

Go back to "IDLE (Python GUI)" and run "make\_exe.py" again (Press F5) - again wait till it shows READY.

Now it has created (if everything went well) a dist folder which contains a folder named dxf2gcode. In this newly created dxf2gcode folder add the Bitmap and Language folder located in the main directory.

Now you can run your just created dxf2gcode.exe (first time you run it: it will create, if it's not present, the config folder; therefore you are most likely to have it run twice)

Note: if you want to use upx just  uncomment the line stated  in �make\_exe.py�
