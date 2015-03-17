**Note**
Because of the change in the Google Dowload Service new versions of DXF2GCODE can be dowloaded from https://sourceforge.net/projects/dxf2gcode/files/

**Table of Contents**


# IMPORTANT  NOTICE #
This Projekt will be moved to SourceForge
[Projekt on SourceForge.net](http://sourceforge.net/projects/dxf2gcode/)

WIKI is already moved to [WIKI on SourceForge.net](http://sourceforge.net/p/dxf2gcode/wiki/browse_pages/)

Issue Tracking is also moved to[Tickets on SourceForge.net](http://sourceforge.net/p/dxf2gcode/tickets/)

# Introduction #

## License ##
This program is written in Python and is published under the GNU license.

## Purpose ##
The program converts a 2D dxf drawing to CNC machine compatible G-Code.

## Screenshot ##
![http://dxf2gcode.googlecode.com/svn/Pictures/DXF2GCODE_2013-08-24_screenshot_1.jpg](http://dxf2gcode.googlecode.com/svn/Pictures/DXF2GCODE_2013-08-24_screenshot_1.jpg)

# Features #
## Import ##
  * Block and Insert import fully supported
  * Spline import with convert to Arc and Line elements to reduce geometry count
  * Ellipse import with convert to Arc elements

## Export ##
  * Entire DXF can be scaled, moved and rotated
  * Implements the travelling salesman problem to optimize cutting order of shapes
  * Very flexible postprocessor with the opportunity to have several postprocessor files for export (not possible for LinuxCNC integration)
  * DXF export possible with specialised postprocessor script (Available on SVN Server)

## Others ##
  * Possible integration in LinuxCNC
  * Easy to edit for special purpose applications
  * etc.

# News #
New Beta Version with pyQT4 GUI available for download.


# Links #
http://www.cncecke.de/forum/showthread.php?t=31326