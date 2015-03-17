# Introduction #

Because of the change in the Google Dowload Service the new versions of DXF2GCODE can be dowloaded from https://sourceforge.net/projects/dxf2gcode/files/

# Upcomming #
This is a beta Version intended for further testing by the community. If you find any issues please Report them with the Issue Tracking System of Google code:
http://code.google.com/p/dxf2gcode/issues/list
or use the forum:
https://groups.google.com/forum/#!forum/dxf2gcode-users

  * Still working of the cutter compensation Topic. Maybe we get something here.

# Current release #

2015-02-04
This is a beta Version intended for further testing by the community. If you find any issues please Report them with the Issue Tracking System of Google code:
http://code.google.com/p/dxf2gcode/issues/list
or use the forum:
https://groups.google.com/forum/#!forum/dxf2gcode-users

Biggest changes compared to 2014-2-12
  * Updated the license
  * Filenames can contain special characters
  * Drag-Knife (swivel knife) option added - see GUI or config file [General](General.md) machine\_type = option('milling', 'drag\_knife')
  * French language support
  * Break layers algorithm fixed
  * Layer commands can now have a different separator instead of : (which is not officially supported in a DXF file) - see config file [Layer\_Options](Layer_Options.md) idfloatseparator
  * ..