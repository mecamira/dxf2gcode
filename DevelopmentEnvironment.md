# Introduction #

A short overview of how to install the development environment on Windows, and Linux.


# Details #

The new pyQT Beta Version of DXF2GCODE has the following dependencies:
  * Python 2.5 or higher - up to 2.99 (not 3.0 and above)
  * pyQT4

## Choosing an environment for DXF2GCODE development ##

Although we aim to make DXF2GCODE work on all major platforms, we would like it if you test it on other platforms (and report the result back to us). I self develop it on a Mac with XP and Ubuntu8.04/EMC in Virtualbox VM's, and test major changes on all three.

If you plan to work on the code and the user interface, then here are some interpreter versions for Linux, Mac OS, and Windows which give a fairly consistent results:

  * Windows: Python2.7.5 from the PythonX,Y distribution (for addition information of Win7 see http://code.google.com/p/dxf2gcode/wiki/DevelopmentEnvironment_Win7)
  * Ubuntu 8.04: off-the-shelf Python 2.5.2 works ok
  * Mac OS X: the Darwinports python26 package (currently at 2.6.4)

Do not waste time on the Windows Cygwin Python distribution (currently 2.5.2) - it has serious issues with geometry management.

The Python/Aqua delivered with Mac OS 10.x works native (without X11 server), but with some surprises. The Darwinports Python needs X11, but is more consistent with the other versions.