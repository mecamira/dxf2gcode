# Introduction #

This page tells you how to install the program on Windows and Linux


# Installation on Windows #

There are two ways to install the program on Windows:
  * You can use the packed executable file which doesn't require any installation. Just extract the files to the folder you want
  * Install the code and a Python distribution. A python version of at least 2.5 is recommended. The code doesn't work with the new Python version 3.0

The new pyQT Beta Version of DXF2GCODE has the following dependencies:
  * Python 2.5 or higher - up to 2.99 (not 3.0 and above)
  * pyQT4


# Installation on Linux #

There is no installer for Linux. Just put the code where ever you want and run the dxf2gcode.py (the name is dependent on the version you use) file. All files of the program should be in the same folder so Python can find the modules.


## Integration in EMC 2.2 and Axis ##
(1) The executable file and all related files must be in the /usr/bin/ folder otherwise Axis can't find the file.


Another method is to make a symbolic link in the /usr/bin/ folder to the executable file located in a different folder (that's how I do it, remember the name may be different depending on the version)
```
 sudo ln -s /SOMEWHERE/...../dxf2gcode_tkinter/dxf2gcode.py /usr/bin/dxf2gcode.py 
```
To make the link executable you must type the following code
```
sudo chmod a+x /usr/bin/dxf2gcode.py
```
(2) Change the AXIS Config File to tell the machine you want to associate all dxf files with dxf2gcode. On my machine the file is located at:
home/ICH/emc2/configs/Meine-Maschine/Meine-Maschine.ini

You need to change the Section [FILTER](FILTER.md) to the following (maybe you want to add the Editor also):
```
[FILTER] 
PROGRAM_EXTENSION =.dxf  2D ACad/QCad Drawing
dxf = dxf2gcode.py 
PROGRAM_FILTER = python 
PROGRAM_EXTENSION = *.py Python Script
[DISPLAY]
EDITOR = gedit
```

(3) Now there is only one thing left to do. You need to tell DXF2GCODE to write to the standard output of Unix. The Config file can be found, depending on the version, in different folders. The newest version produces the Config folder in the same folder where the dxf2gcode executable is located (not the symbolic link). Please change the write to stdout option as shown below.

```
[Export Parameters]
write_to_stdout = 1
```

## Failure Messages and Solutions ##
```
bash: ./dxf2gcode_b02.py:
 /usr/bin/python^M: bad interpreter: No such file or directory
```
The file may contain carriage return characters. Therefore you need to convert those files first.

In bash, the files can be converted conveniently by the following lines:
```
mkdir clean
for var in $( ls dxf2gcode*.py );
do  cat $var | tr -d "\r" > clean/$var;
done
mv clean/* ./
rmdir clean/
```

Make the file executable
```
chmod +x dxf2gcode.py
```



# Installation on Mac OS X #

Same requirements as Linux. Known-to-work recent versions of Python can be obtained from:

  * Python: http://www.python.org/download/releases/2.6.4/