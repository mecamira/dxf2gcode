# Introduction #
This wiki page gives a overview about the Intention of different section and variable names which allows configuration of the postprocessor.

## Using different Postprocessor files ##
While the tool is not directly integrated it is possible to have different postprocessor configuration files. You can choose between all valid postprocessor configuration files stored in the \postpro\_config directory.

## Postprocessor Version ##
This description is valid for the dxf2gcode pyQt4 Version starting with svn rev. 417 dated August 2013.

# Explanation of the Sections #
Do not edit any section or variable names, this will result in Import errors while dxf2gcode is initialising.
```
#  Section and variable names must be valid Python identifiers
#      do not use whitespace in names 

# do not edit the following section name:
```
This is the introduction of the postprocessor file. There is no Need to Change it.

## Version ##
```
[Version]
    
    # do not edit the following value:
    config_version = 2
```

This section is intended for changes of the prostprocessor file itself. While the tool evolves over time this counter will be increased to indicate that the configuration of the postprocessor was changed.

## General ##
```
[General]
    output_format = .ngx
    output_text = G-CODE for EMC2
    output_type = g-code
```

This three configurations are shown in the save file dialog and are used by the user to differentiate between the possibly different postprocessor configurations.
```
    abs_export = False
    cancel_cc_for_depth = False
    cc_outside_the_piece = True
    export_ccw_arcs_only = False
    max_arc_radius = 10000.0
```

  * abs\_export possible values are True and False. This may be used for G90 or G91 code which switches between absolute and relative coordinates.
  * cancel\_cc\_for\_depth; possible values are True and False. If the cutter compensation is used e.g. G41 or G42 this option may cancel the compensation while the depth (Z-Axis) is used and enable the compensation again after the depth is reached.
  * cc\_outside\_the\_piece; possible values are True and False. If the cutter compensation is used this will cancel the cutter compensation with G40 after the tool is retracted to the retraction area.
  * export\_ccw\_arcs\_only; possible values are True and False. This my be used for the export to dxf which only accepts arcs which are in counterclockwise direction. Turning this on for normal G-Code will cause in unintended outputs.
  * max\_arc\_radius; this values indicated which arc's with radius higher then this value will be exported as a line.

```
    code_begin = G21 (Unit in mm) G90 (Absolute distance mode) G64 P0.001 (Exact Path 0.001 tol.) G17 G40 (Cancel diameter comp.) G49 (Cancel length comp.)
    code_end = M2 (Prgram end)
```
This is code which will be written at the very begin and end of the exported file.

## Number Format ##
```
[Number_Format]
    pre_decimals = 4
    post_decimals = 3
    decimal_seperator = .
    pre_decimal_zero_padding = False
    post_decimal_zero_padding = True
    signed_values = False
```
This is the section which enables the user to change the formatting of the eported numbers. This example has a fixed length for the numbers:
e.g.
' 100.000'
'  10.000'
'   1.000'
  * pre\_decimals; gives the identation for the values.
  * post\_decimals; gives the accuracy of the output after which will be rounded.
  * decimal\_seperator; give the separator which is used (e.g. (.) or (,))
  * pre\_decimal\_zero\_padding; If true all values will be given with zeros up to pre\_decimals (e.g. 0001.000)
  * post\_decimal\_zero\_padding; If false e.g. 1.000 will be given as 1 only.
  * signed\_values; if True 1.000 will be givne as +1.000

## Line Numbers ##
```
[Line_Numbers]
    use_line_nrs = False
    line_nrs_begin = 10
    line_nrs_step = 10
```
Enables the user to have lines numbers for the exported G-Code.

## Program ##
```
[Program]
    tool_change = T%tool_nr M6%nlS%speed%nl
    feed_change = F%feed%nl
    rap_pos_plane = G0 X%XE Y%YE%nl
    rap_pos_depth = G0 Z%ZE %nl
    lin_mov_plane = G1 X%XE Y%YE%nl
    lin_mov_depth = G1 Z%ZE%nl
    arc_int_cw = G2 X%XE Y%YE I%I J%J%nl
    arc_int_ccw = G3 X%XE Y%YE I%I J%J%nl
    cutter_comp_off = G40%nl
    cutter_comp_left = G41%nl
    cutter_comp_right = G42%nl
    pre_shape_cut = M3 M8%nl
    post_shape_cut = M9 M5%nl
    comment = %nl(%comment)%nl
```
This section gives the format how different actions of the export have to be interpreted. These actions will be done for each export of a shape, line, arc, tool change, feed change etc.

  * tool\_change; this will be done after each layer. If different tools are used.
  * feed\_change; this will be done after each change between cutting in plane or depth
  * rap\_pos\_plane; this will be done between each shape to cut.
  * rap\_pos\_depth;
  * lin\_mov\_plane;
  * lin\_mov\_plane;
  * arc\_int\_cw;
  * arc\_int\_ccw;
  * cutter\_comp\_off;
  * cutter\_comp\_left;
  * cutter\_comp\_right;
  * pre\_shape\_cut; This will be done before starting to cut a shape/ contour.
  * post\_shape\_cut; This will be donw after cutting a shape or contour.
  * comment; at some places during the export more comments are given to make the code better readable.

The following section gives the possible key words which may be used in the actions explained above.

|"%feed"|The feed rate used|
|:------|:-----------------|
|"%speed"|The tool speed used|
|"%tool\_nr"|The tool Nr.used|
|"%nl"|New line to be included|
|"%XE"|The X position at the end|
|"%-XE"|The negative X position at the end|
|"%XA"|The X position at the begin|
|"%-XA"|The negative X position at the end|
|"%YE"|The Y position at the end|
|"%-YE"|The negative Y position at the end|
|"%YA"|The Y position at the begin|
|"%-YA"|The negative Y position at the end|
|"%ZE"|The Z position at the end|
|"%-ZE"|The negative Z position at the end|
|"%I"|The distance between Start and Centre in X|
|"%-I"|The neg. dis. between Start and Centre in X|
|"%J"|The distance between Start and Centre in Y|
|"%-J"|The neg. dis. between Start and Centre in Y|
|"%XO"|The X Centre of an Arc|
|"%-XO"|The negative X Centre of an Arc|
|"%YO"|The Y Centre of an Arc|
|"%-YO"|The negative Y Centre of an Arc|
|"%R"| The radius of an Arc|
|"%AngA"|The starting angle of an Arc in deg.|
|"%-AngA"|The negative starting angle of an Arc in deg.|
|"%AngE"|The end angle of an Arc in deg.|
|"%-AngE"|The negative end angle of an Arc in deg.|
|"%comment"|The given comment in the code|

## Examples ##
### Postprocessor Configuration Styrofoam ###
This is a configuration that will ignore the Z-Axis and turn "the spindle" (i.e. the heat of the hot wire) on before any movement and turn turn it off right before the end of the program. You will find it in a seperate Wiki Page.

### How to replace the Axis Letters ###
For using different Axis just replace the leading letters.
e.g. replace axes Y by Z:
```
rap_pos_plane = G0 X%XE Y%YE%nl
rap_pos_plane = G0 X%XE Z%YE%nl
```