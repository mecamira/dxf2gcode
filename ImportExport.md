## Introduction ##
About the DXF2GCODE  import and export functions

### Structure of a DXF file ###
This is just a minimal introduction into DXF to help understand what dxf2gcode does.  For a more detailed reference, see the  [[DXF description](http://de.wikipedia.org/wiki/Drawing_Interchange_Format|Wikipedia)] and the  [[DXF specification](http://usa.autodesk.com/adsk/servlet/item?siteID=123112&id=12272454&linkID=10809853|Autodesk)]; some DXF terms are used here in parentheses.

A DXF file contains basic geometrical elements (entities) like points, lines, arcs, circles, polylines, text etc. It may also contain reusable elements (blocks) constructed from these primitives. Such blocks can be inserted  into a drawing several times; these are called inserts. An example would be a door knob block, which would be inserted on all doors in a drawing. Think of it as a macro.

Entities are organized into planes (layers). In a typical CAD program like AutoCAD or Qcad, layers can be  selectively enabled or disabled. Every entity belongs to exactly one layer and may have attributes like  coordinates, colors, line style, and thickness. There is always a default layer named '0', and optionally many more named layers. Besides a name, layers can have attributes, just like entities.  Entities on a layer either have their own attributes, or they inherit an attribute from the layer attribute, for instance the layer color.

At the top level a DXF file is organized into sections which contain blocks, layers, the entities etc.

### Reading the DXF file ###
DXF2GCODE reads a DXF file as follows:

  * the sections (blocks, layers, entities) are read
  * any referenced blocks are resolved into inserts (the block reference is replaced by the entities it contains - much like a macro expansion)
  * all entities are converted into lists of lines and arcs.
  * points are preserved, but not treated in any special way.

The last step is quite involved but CNC machines typically support only lines and arcs. Note that curves like splines or ellipses are also transformed into lists of arcs, not approximated by polylines like by other programs.

### How Shapes are built during import ###
For cutting, continuous ''shapes'' are needed. Not everything that ''looks'' continuous on the screen of your CAD program actually ''is'' a continuous shape. Take for example a rectangle - it might be a polyline with four segments and coinciding start and end points. However, it might be also for distinct lines. And those might be on different layers - but you might not be able to tell just by looking at the screen. Some basic shapes, such as circles and ellipses, clearly are continuous. Also, a standalone points is considered a shape. But in the case of the rectangle example this is not at all obvious.

To construct shapes, DXF2GCODE checks all entities belonging to a layer whether they coincide - meaning either "identical coordinates" or "close enough". Sometimes you might consider a shape as continuous but it turns up as separate shapes after import.  This can be seen when you try to select it - just part of the shape is highlighted. In this case it might have been split because they were not considered "close enough" - or the parts reside in different layers. In this case, it might help increasing the parameters which define "close enough", these are:

  * Option->Set tolerances->Tolerance for common points (default 0.01mm)
  * Option->Set tolerances->Tolerance for curve fitting (default 0.01mm)

They can be set in the config file:

```
[Import Parameters]
point_tolerance = 0.01
fitting_tolerance = 0.01
```
Those entities which pass these tests '''and''' are in the same layer are now collected into a new shape. Since during import complex shapes were transformed into arcs and lines, a shape is just a list of lines and/or arcs. A point is always a shape of its own.


### How Splines are converted ###
The tool comprises a dedicated algorithm to convert a spline to arcs and lines by a biarc Fitting algorithm.
  * Reducing the amount of Points which are generated
  * Increases the accuracy
  * May incease the Speed during cutting
  * and enables the CNC Maschine to use G41 and G42 even with a spline

Since the Import may face some Problems there are several checks of splines integrated. This is controlled by the following variable in the config file. In order to have all checks choose the value 3.
```
[Import Parameters]
spline_check = 3
```



### Choosing shapes for export ###
If all you need is exporting a complete drawing to G-Code, then you just select File->Read DXF and Export->Write G-Code and you are done. If not, you need to choose the shapes for selective export.

How DXF2GCODE does this is a bit involved but actually quite elegant. The trap I fell into was: I select shapes with shift-button click and select Export->Write G-Code, and I'm done - it doesn't quite work this way; a selection in the drawing area isn't what will be exported.

It helps to view it this way:

  * A shape is either ''enabled'' or ''disabled'' for export.
  * Initially all shapes are enabled for export (except shapes on ignored and break layers, see LayerControl)
  * An ''enabled'' shape is displayed in the drawing area as a black line.
  * A ''disabled'' shape is either ''displayed'' as a gray line or ''invisible'', depending on the View->Show disabled shapes setting.
  * A ''displayed'' shape can be selected or added to a selection by the usual means:
    * mouse-click to select a shape
    * shift-mouse click to add the shape to the current selection
    * draw a rectangle around shapes while pressing the mouse, which selects all shapes within the rectangle
  * A selection may now be:
    * inverted - all other unselected, enabled shapes are now selected (not the disabled gray ones though!)
    * enabled for export by Context menu->enable selection (right-click)
    * disabled for export by Context menu->disable selection

A enabled shape is displayed red if selected; a disabled shape is displayed in blue on selection. If View->Show disabled shapes is off, disabled shapes are hidden and hence cannot be selected. To enable an already disabled and hidden shape for  export, you might want to turn on View->Show disabled shapes at least temporarily.

''and coming soon: The Postprocessor..''