# Introduction #

Since dxf2gcode does not save any kind of file itself all required input data for G-Code generation is taken from the .dxf File.

By naming Layers in the .dxf file in special ways you can easily influence how shapes in these layers are translated to G-Code.


# Milling parameters #

By using **MILL:** as a prefix to your layer name you can define milling parameters by using one of the following identifiers (taken from https://groups.google.com/forum/#!topic/dxf2gcode-users/q3hPQkN2OCo ):
```
    # mill options
    mill_depth_identifiers = MillDepth, Md, TiefeGesamt, Tg
    slice_depth_identifiers = SliceDepth, Sd, TiefeZustellung, Tz
    start_mill_depth_identifiers = StartMillDepth, SMd, StartTiefe, St
    retract_identifiers = RetractHeight, Rh, FreifahrHohe, FFh
    safe_margin_identifiers = SafeMargin, Sm, SicherheitsHoehe, Sh
    f_g1_plane_identifiers = FeedXY, Fxy, VorschubXY, Vxy, F
    f_g1_depth_identifiers = FeedZ, Fz, VorschubZ, Vz

    #Tool Options
    tool_nr_identifiers = ToolNr, Tn, T, WerkzeugNummer, Wn
    tool_diameter_identifiers = ToolDiameter, Td, WerkzeugDurchmesser, Wd
    spindle_speed_identifiers = SpindleSpeed, Drehzahl, RPM, UPM, S
    start_radius_identifiers = StartRadius, Sr
```

Example:

**`MILL: 1 Md: 2 Sd: 2 FeedXY: 400 FeedZ: 200`**

This will cut shapes on the layer 2 mm deep (in one pass, since Sd == Md) using 400 mm / minute speed for X/Y movement and 200 mm / minute for Z movement.

Tip:
**You can combine workpieces for different materials in one .dxf file, just put all the pieces that belong to one kind of material (e.g. thickness of plywood) onto one layer.**

# Ignored layers #

If you start your layer name with **IGNORE:**, the shapes in it will be disabled by default (i.e. the checkboxes in the Entities/Layers tab will be deselected by default).

Example:

**`IGNORE: Helper`**

This defines a helper - layer that may contain orientation lines, etc.

Tip:
**You can use this prefix for layers that contain measurements, orientation lines or other content that is important for the .dxf drawing to understand but not required for milling**

# Breaking layers #

It is common practice to not entirely mill out workpieces but leave small gaps in the milling path (in German this is called "Frässtäge" or "Stützbrücken", if anyone knows the correct technical term for that in english please edit/comment).
The reason behind this is that without these gaps the workpiece may be kicked away or take damage in another way by the milling head.

It is of course totally feasible to produce these gaps by simple making them in the .dxf file with the CAD software. This however has the disadvantage that the blueprint of your workpiece is now inerspersed with gaps and shapes are no longer closed.

dxf2gcode allows to define the gaps as intersection points between lines of shapes to mill and lines of shapes on a breaking layer. If a shape to mill is intersected exactly two times by a shape on a breaking layer, a gap will be introduced.
This allows for gaps to be introduces as rectangles on the breaking layer. The image below has a magenta breaking layer and a white layer defining the workpiece.

![https://lh6.googleusercontent.com/-MzmeNlgC5rg/Uu4Ra-qwNwI/AAAAAAAACCg/PGOyXf3choI/s320/Spant.png](https://lh6.googleusercontent.com/-MzmeNlgC5rg/Uu4Ra-qwNwI/AAAAAAAACCg/PGOyXf3choI/s320/Spant.png)

Breaking layers are defined by the prefix **BREAKS:** in the layer name.

Note that some parameters from the 'Milling parameters' section above apply to the breaking layer as well:
**FeedZ (or Fz, VorschubZ, Vz) will define the speed the milling head is retracted at the beginning and reinserted at the end of the gap.** FeedXY (Fxy, VorschubXY, Vxy, F) will define the speed the milling head is passing the gap
**MillDepth (Md, TiefeGesamt, Tg) will define the height the milling head will have while passing the gap. This allows to pass the workpiece completely (Md > 0) or just prevent from cutting all the way through (Md < 0 but bigger than Md from your milling layer).**

Example:

  * **`BREAKS: 1 Md: -1 FeedZ: 200 FeedXY: 400`** will retract the milling head at 200 mm/minute until it is 1 mm below the surface, then go to the end point of the gap with a 400 mm/minute feed and finally lower the milling head to the original depth with 200 mm/minute.
  * An example .dxf file can be found at https://docs.google.com/uc?export=download&id=0B2negA0eQERDek01WDNXSVc2T1U. It contains a single rectangle to be milled out of a 3 mm plywood sheet. It contains four gaps (one on each side) where the milling is reduced to only 1 mm, thus leaving 2 mm of plywood to keep the workpiece in place.

# Drilling layers #

Milling machines can also be used for drilling holes in the workpiece. To achieve this with dxf2gcode you have to draw points on a drilling layer.

Drilling layers are defined by the prefix **DRILL:** in the layer name.

Drilling layers can have all the parameters specified unter Milling parameters above, thus defining how deep (MillDepth) or how fast (FeedZ) the hole should be drilled. Also the given ToolDiameter will be used to visualize the hole.