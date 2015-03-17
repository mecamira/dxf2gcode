Copy&Paste the configuration below into a file called `source/postpro_config/styrofoam.cfg`

```
# Configuration file for styrofoam cutter output:
# * no movement in Z-Axis
# * 
# by Robert Lichtenberger, 2014

#  Section and variable names must be valid Python identifiers
#      do not use whitespace in names 

# do not edit the following section name:
[Version]
    
    # do not edit the following value:
    config_version = 4

[General]
    output_format = .ngc
    output_text = styrofoam cutting G-CODE for LinuxCNC 
    output_type = g-code
    
    abs_export = True
    cancel_cc_for_depth = False
    cc_outside_the_piece = True
    export_ccw_arcs_only = False
    max_arc_radius = 10000.0
    
    code_begin_units_mm = G21 (Units in millimeters)
    code_begin_units_in = G20 (Units in inches)
    code_begin = G90 (Absolute programming) G64 (Default cutting) G17 (XY plane) G40 (Cancel radius comp.) G49 (Cancel length comp.) M3 M8 M0 (turn on heat then pause)
    code_end = M9 M5 (turn off heat) M2 (Program end)

[Number_Format]
    pre_decimals = 4
    post_decimals = 3
    decimal_seperator = .
    pre_decimal_zero_padding = False
    post_decimal_zero_padding = True
    signed_values = False

[Line_Numbers]
    use_line_nrs = False
    line_nrs_begin = 10
    line_nrs_step = 10

[Program]
    tool_change = T%tool_nr M6%nlS%speed
    feed_change = F%feed%nl
    rap_pos_plane = G0 X%XE Y%YE%nl
    rap_pos_depth = 
    lin_mov_plane = G1 X%XE Y%YE%nl
    lin_mov_depth = 
    arc_int_cw = G2 X%XE Y%YE I%I J%J%nl
    arc_int_ccw = G3 X%XE Y%YE I%I J%J%nl
    cutter_comp_off = G40%nl
    cutter_comp_left = G41%nl
    cutter_comp_right = G42%nl
    pre_shape_cut = 
    post_shape_cut = 
    comment = %nl(%comment)%nl
```