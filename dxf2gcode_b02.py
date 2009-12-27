#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
#
#dxf2gcode_b02.py
#Programmers:   Christian Kohloeffel
#               Vinzenz Schulz
#
#Distributed under the terms of the GPL (GNU Public License)
#
#dxf2gcode is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#About Dialog
#First Version of dxf2gcode Hopefully all works as it should
#Compiled with --onefile --noconsole --upx --tk dxf2gcode_b02.py


import sys, os

#Delete loaded modules from memory
if globals().has_key('init_modules'):
    for m in [x for x in sys.modules.keys() if x not in init_modules]:
        del(sys.modules[m]) 

# some button bindings differ on Mac OS
platform = ""  
if os.name == "posix" and sys.platform == "darwin":
    platform = "mac"
# in case more per-platform determination warts are needed, fill in here:
 
from config import ConfigClass, PostprocessorClass
from point import PointClass
from shape import ShapeClass, EntitieContentClass
from notebook import MyNotebookClass, LayerContentClass
from dxf_import import ReadDXF 
from tsp_opt import TSPoptimize
import locale

#===============================================================================
# Added the Cutter Compensation here
#===============================================================================
from ccomp_chrisko import ShapeOffsetClass


from math import radians, degrees

import webbrowser, gettext, tempfile, subprocess
from Tkconstants import END, ALL, N, S, E, W, RIDGE, DISABLED, NORMAL, ACTIVE, \
LEFT
from tkMessageBox import showwarning
from Tkinter import Tk, IntVar, DoubleVar, Canvas, Menu, Frame, Label, Entry, \
Text, Scrollbar, Toplevel, Button
from tkFileDialog import askopenfile, asksaveasfilename
from tkSimpleDialog import askfloat
from Canvas import Rectangle, Line, Oval, Arc

# Global Variables
APPNAME = "dxf2gcode"
VERSION = "TKINTER Beta 02"
DATE = "2009-11-16"

# Get folder of the main program
FOLDER = os.path.dirname(os.path.abspath(sys.argv[0])).replace("\\", "/")
if os.path.islink(sys.argv[0]):
    FOLDER = os.path.dirname(os.readlink(sys.argv[0]))
    

# List of supported languages
langs = []

#Get default language of the system
lc, encoding = locale.getdefaultlocale()

#If there is a default language use it
if (lc):
    langs = [lc]

# Herausfinden welche sprachen wir haben
language = os.environ.get('LANGUAGE', None)
"""langage comes back something like en_CA:en_US:en_GB:en
on linuxy systems, on Win32 it's nothing, so we need to
split it up into a list"""
if (language):

    langs += language.split(":")

"""Now add on to the back of the list the translations that we
know that we have, our defaults"""
langs += []

"""Now langs is a list of all of the languages that we are going
to try to use.  First we check the default, then what the system
told us, and finally the 'known' list"""

gettext.bindtextdomain(APPNAME, FOLDER)
gettext.textdomain(APPNAME)
# Get the language to use
trans = gettext.translation(APPNAME, localedir='languages', languages=langs, fallback=True)
trans.install()

class MyMainWindow:
    """
    This is Main GUI Window of DXF2GCODE it includes all other GUI's and DXF 
    Imports.
    
    """

    def __init__(self, load_filename=None):
        """
        The function can be used with an addition parameter for the filename to
        display after startup
        """

        self.master = master
        self.menu = None
        self.filemenu = None
        self.exportmenu = None
        self.optionmenu = None
        self.helpmenu = None
        self.viewemnu = None
            
        #Skalierung der Kontur
        self.cont_scale = 1.0
        
        #Verschiebung der Kontur
        self.cont_dx = 0.0
        self.cont_dy = 0.0
        
        #Rotieren um den WP zero
        self.rotate = 0.0
        
        #Uebergabe des load_filenames falls von EMC gestartet
        self.load_filename = load_filename

        #Linker Rahmen erstellen, in welchen sp�ter die Eingabefelder kommen       
        self.frame_l = Frame(master) 
        self.frame_l.grid(row=0, column=0, rowspan=2,
                           padx=4, pady=4, sticky=N + E + W)
        
        #Erstellen des Canvas Rahmens
        self.frame_c = Frame(master, relief=RIDGE, bd=2)
        self.frame_c.grid(row=0, column=1,
                          padx=4, pady=4, sticky=N + E + S + W)
        
        #Unterer Rahmen erstellen mit der Lisbox + Scrollbar zur Darstellung 
        #der Ereignisse.
        self.frame_u = Frame(master) 
        self.frame_u.grid(row=1, column=1, padx=4, sticky=N + E + W + S)
        #Erstellen des Statusfenster
        self.textbox = TextboxClass(frame=self.frame_u, master=self.master)

        #Voreininstellungen fuer das Programm laden
        self.config = ConfigClass(self.textbox, FOLDER, APPNAME)

        #PostprocessorClass initialisieren (Voreinstellungen aus Config)
        self.postpro = PostprocessorClass(self.config, self.textbox, FOLDER,
                                           APPNAME, VERSION, DATE)

        self.master.columnconfigure(0, weight=0)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=0)
            

        #Erstellen de Eingabefelder und des Canvas
        self.MyNotebook = MyNotebookClass(self.frame_l, self.config, self.postpro, [])
        self.Canvas = CanvasClass(self.frame_c, self)

        #Erstellen der Canvas Content Klasse & Bezug in Canvas Klasse
        self.CanvasContent = CanvasContentClass(self.Canvas,
                                              self.textbox,
                                              self.config,
                                              self.MyNotebook)
        
        self.MyNotebook.CanvasContent = self.CanvasContent
        self.Canvas.Content = self.CanvasContent

        #Erstellen des Fenster Menus
        self.create_window_menu()        
        
        #Falls ein load_filename_uebergeben wurde
        if not(self.load_filename is None):
            #Zuerst alle ausstehenden Events und Callbacks ausfuehren (sonst klappts beim Laden nicht)
            self.Canvas.canvas.update()
            self.Load_File()

    def create_window_menu(self):
        """
        Creates the menu of the main window
        """
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.filemenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=_("File"), menu=self.filemenu)
        self.filemenu.add_command(label=_("Read DXF"), command=self.Get_Load_File)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=_("Exit"), command=self.ende)

        self.exportmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=_("Export"), menu=self.exportmenu)
        self.exportmenu.add_command(label=_("Write G-Code"), command=self.Write_GCode)
        #Disabled bis was gelesen wurde
        self.exportmenu.entryconfig(0, state=DISABLED)

        self.viewmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=_("View"), menu=self.viewmenu)
        self.viewmenu.add_checkbutton(label=_("Show workpiece zero"), \
                                      variable=self.CanvasContent.toggle_wp_zero, \
                                      command=self.CanvasContent.plot_wp_zero)
        self.viewmenu.add_checkbutton(label=_("Show all path directions"), \
                                      variable=self.CanvasContent.toggle_start_stop, \
                                      command=self.CanvasContent.plot_cut_info)
        self.viewmenu.add_checkbutton(label=_("Show disabled shapes"), \
                                      variable=self.CanvasContent.toggle_show_disabled, \
                                      command=self.CanvasContent.show_disabled)
            
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label=_('Autoscale'), command=self.Canvas.autoscale)

        #Menupunkt einfuegen zum loeschen der Route
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label=_('Delete Route'), command=self.del_route_and_menuentry)         

        #Disabled bis was gelesen wurde
        self.viewmenu.entryconfig(0, state=DISABLED)
        self.viewmenu.entryconfig(1, state=DISABLED)
        self.viewmenu.entryconfig(2, state=DISABLED)
        self.viewmenu.entryconfig(4, state=DISABLED)
        self.viewmenu.entryconfig(6, state=DISABLED)

        self.optionmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=_("Options"), menu=self.optionmenu)
        self.optionmenu.add_command(label=_("Set tolerances"), command=self.Get_Cont_Tol)
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label=_("Scale contours"), command=self.Get_Cont_Scale)
        self.optionmenu.add_command(label=_("Move workpiece zero"), command=self.Move_WP_zero)
        self.optionmenu.add_command(label=_("Rotate contours"), command=self.Rotate_Cont)
        self.optionmenu.entryconfig(2, state=DISABLED)
        self.optionmenu.entryconfig(3, state=DISABLED)
        self.optionmenu.entryconfig(4, state=DISABLED)
        
        
        self.helpmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=_("Help"), menu=self.helpmenu)
        self.helpmenu.add_command(label=_("About..."), command=self.Show_About)

    # Callback des Menu Punkts File Laden
    def Get_Load_File(self):
        """
        Generates the load file browser and save the filename into 
        self.load_filename
        """
        #Auswahl des zu ladenden Files
        myFormats = [(_('Supported files'), '*.dxf *.ps *.pdf'), \
                     (_('AutoCAD / QCAD Drawing'), '*.dxf'), \
                     (_('Postscript File'), '.ps'), \
                     (_('PDF File'), '.pdf'), \
                     (_('All File'), '*.*') ]
        inidir = self.config.load_path
        filename = askopenfile(initialdir=inidir, \
                               filetypes=myFormats)
        #Falls abgebrochen wurde
        if not filename:
            return
        else:
            self.load_filename = filename.name

        self.Load_File()

    def Load_File(self):
        """
        Loads the defined file of self.load_filename also calls the command to 
        make the plot in self.CanvasContent.makeplot.
        """

        #Dateiendung pruefen
        (name, ext) = os.path.splitext(self.load_filename)

        if ext.lower() == ".dxf":
            filename = self.load_filename
            
        elif (ext.lower() == ".ps")or(ext.lower() == ".pdf"):
            self.textbox.prt(_("\nSending Postscript/PDF to pstoedit"))
            
            # tempor�re Datei erzeugen
            filename = os.path.join(tempfile.gettempdir(), 'dxf2gcode_temp.dxf').encode("cp1252")
            
            pstoedit_cmd = self.config.pstoedit_cmd.encode("cp1252") #"C:\Program Files (x86)\pstoedit\pstoedit.exe"
            pstoedit_opt = eval(self.config.pstoedit_opt) #['-f','dxf','-mm']
            
            #print pstoedit_opt
            
            ps_filename = os.path.normcase(self.load_filename.encode("cp1252"))

            cmd = [(('%s') % pstoedit_cmd)] + pstoedit_opt + [(('%s') % ps_filename), (('%s') % filename)]

            #print cmd
    
            retcode = subprocess.call(cmd)
            #print retcode

        self.textbox.text.delete(7.0, END)
        self.textbox.prt(_('\nLoading file: %s') % self.load_filename)
        
        self.values = ReadDXF(filename, self.config, self.textbox)
        
        #Ausgabe der Informationen im Text Fenster
        self.textbox.prt(_('\nLoaded layers: %s') % len(self.values.layers))
        self.textbox.prt(_('\nLoaded blocks: %s') % len(self.values.blocks.Entities))
        for i in range(len(self.values.blocks.Entities)):
            layers = self.values.blocks.Entities[i].get_used_layers()
            self.textbox.prt(_('\nBlock %i includes %i Geometries, reduced to %i Contours, used layers: %s ')\
                               % (i, len(self.values.blocks.Entities[i].geo), len(self.values.blocks.Entities[i].cont), layers))
        layers = self.values.entities.get_used_layers()
        insert_nr = self.values.entities.get_insert_nr()
        self.textbox.prt(_('\nLoaded %i Entities geometries, reduced to %i Contours, used layers: %s ,Number of inserts: %i') \
                             % (len(self.values.entities.geo), len(self.values.entities.cont), layers, insert_nr))

        #Skalierung der Kontur
        self.cont_scale = 1.0
        
        #Verschiebung der Kontur
        self.cont_dx = 0.0
        self.cont_dy = 0.0
        
        #Rotieren um den WP zero
        self.rotate = 0.0

        #Disabled bis was gelesen wurde
        self.viewmenu.entryconfig(0, state=NORMAL)
        self.viewmenu.entryconfig(1, state=NORMAL)
        self.viewmenu.entryconfig(2, state=NORMAL)
        self.viewmenu.entryconfig(4, state=NORMAL)

        #Disabled bis was gelesen wurde
        self.exportmenu.entryconfig(0, state=NORMAL)

        #Disabled bis was gelesen wurde
        self.optionmenu.entryconfig(2, state=NORMAL)
        self.optionmenu.entryconfig(3, state=NORMAL)     
        self.optionmenu.entryconfig(4, state=NORMAL) 

        #Ausdrucken der Werte        
        self.CanvasContent.makeplot(self.values,
                                    p0=PointClass(x=self.cont_dx, y=self.cont_dy),
                                    pb=PointClass(x=0, y=0),
                                    sca=[self.cont_scale, self.cont_scale, self.cont_scale],
                                    rot=self.rotate)

        #Loeschen alter Route Menues
        self.del_route_and_menuentry()
            
    def Get_Cont_Tol(self):
        """
        Called of the main menu when the contour tolerance menu entry is pusehd. 
        If the values are changed the whole file is reloaded.
        """
        #self.CanvasContent.makeplot

        #Dialog fuer die Toleranzvoreinstellungen oeffnen      
        title = _('Contour tolerances')
        label = (_("Tolerance for common points [mm]:"), \
               _("Tolerance for curve fitting [mm]:"))
        value = (self.config.points_tolerance.get(), self.config.fitting_tolerance.get())
        dialog = VariableDialogWindow(self.master, title, label, value)
        self.config.points_tolerance.set(dialog.result[0])
        self.config.fitting_tolerance.set(dialog.result[1])
        
        #Falls noch kein File geladen wurde nichts machen
        if self.load_filename is None:
            return
        self.Load_File()
        self.textbox.prt(_("\nSet new Contour tolerances (Pts: %0.3f, Fit: %0.3f) reloaded file")\
                              % (dialog.result[0], dialog.result[1]))
        
    def Get_Cont_Scale(self): 
        """
        Called from the main menu when the contour scale menu entry is pusehd. 
        If the values are changed the whole file is reloaded.
        """            
        value = askfloat(_('Scale Contours'), _('Set the scale factor'), \
                                initialvalue=self.cont_scale)
        #Abfrage ob Cancel gedrueckt wurde
        if value is None:
            return
        
        self.cont_scale = value
        
        #Falls noch kein File geladen wurde nichts machen
        self.textbox.prt(_("\nScaled Contours by factor %0.3f") % self.cont_scale)

        #Neu ausdrucken
        self.CanvasContent.makeplot(self.values,
                                    p0=PointClass(x=self.cont_dx, y=self.cont_dy),
                                    pb=PointClass(x=0, y=0),
                                    sca=[self.cont_scale, self.cont_scale, self.cont_scale],
                                    rot=self.rotate)       
    def Rotate_Cont(self):
        """
        Called from the main menu when the rotated contour menu entry is pusehd. 
        If the values are changed the whole file is reloaded.
        """ 
                
        value = askfloat(_('Rotate Contours'), _('Set the Angle [deg]'), \
                                initialvalue=degrees(self.rotate))
        #Abfrage ob Cancel gedrueckt wurde
        if value is None:
            return
        
        self.rotate = radians(value)
        
        #Falls noch kein File geladen wurde nichts machen
        self.textbox.prt(_("\nRotated Contours by %0.3f deg") % degrees(self.rotate))

        #Neu ausdrucken
        self.CanvasContent.makeplot(self.values,
                                    p0=PointClass(x=self.cont_dx, y=self.cont_dy),
                                    pb=PointClass(x=0, y=0),
                                    sca=[self.cont_scale, self.cont_scale, self.cont_scale],
                                    rot=self.rotate)       
        
        
    def Move_WP_zero(self):
        """
        Called from the main menu when the offset (Move Workpiece Zero) menu 
        entry is pusehd. If the values are changed the whole file is reloaded.
        """ 

        #Dialog mit den definierten Parametern oeffnen       
        title = _('Workpiece zero offset')
        label = ((_("Offset %s axis by mm:") % self.config.ax1_letter), \
               (_("Offset %s axis by mm:") % self.config.ax2_letter))
        value = (self.cont_dx, self.cont_dy)
        dialog = VariableDialogWindow(self.master, title, label, value)

        #Abbruch wenn nicht uebergeben wurde
        if dialog.result == False:
            return
        
        self.cont_dx = dialog.result[0]
        self.cont_dy = dialog.result[1]

        #Falls noch kein File geladen wurde nichts machen
        self.textbox.prt(_("\nWorpiece zero offset: %s %0.2f; %s %0.2f") \
                              % (self.config.ax1_letter, self.cont_dx,
                                self.config.ax2_letter, self.cont_dy))

        #Neu ausdrucken
        self.CanvasContent.makeplot(self.values,
                                    p0=PointClass(x=self.cont_dx, y=self.cont_dy),
                                    pb=PointClass(x=0, y=0),
                                    sca=[self.cont_scale, self.cont_scale, self.cont_scale],
                                    rot=self.rotate)


    # Callback des Menu Punkts Exportieren
    def Write_GCode(self):
        """
        Will be called if the Export Button is pressed. This function is the 
        main function of the dxf export.
        """
        
        #Config & postpro in einen kurzen Namen speichern
        config = self.config
        postpro = self.postpro

        if not(config.write_to_stdout):
           
                #Abfrage des Namens um das File zu speichern
                self.save_filename = self.Get_Save_File()
                
                
                #Wenn Cancel gedrueckt wurde
                if not self.save_filename:
                    return
                
                (beg, ende) = os.path.split(self.save_filename)
                (fileBaseName, fileExtension) = os.path.splitext(ende) 
        
                pp_file_nr = postpro.output_format.index(fileExtension)
                
                postpro.get_all_vars(pp_file_nr)
        else:
                postpro.get_all_vars(0)
        
               
        #Funktion zum optimieren des Wegs aufrufen
        self.opt_export_route()

        #Initial Status fuer den Export
        status = 1

        #Schreiben der Standardwert am Anfang        
        postpro.write_gcode_be(postpro, self.load_filename)

        #Maschine auf die Anfangshoehe bringen
        postpro.rap_pos_z(config.axis3_retract.get())

        #Bei 1 starten da 0 der Startpunkt ist
        for nr in range(1, len(self.TSP.opt_route)):
            shape = self.shapes_to_write[self.TSP.opt_route[nr]]
            self.textbox.prt((_("\nWriting Shape: %s") % shape), 1)
                


            #Drucken falls die Shape nicht disabled ist
            if not(shape.nr in self.CanvasContent.Disabled):
                #Falls sich die Fr�serkorrektur ver�ndert hat diese in File schreiben
                stat = shape.Write_GCode(config, postpro)
                status = status * stat

        #Maschine auf den Endwert positinieren
        postpro.rap_pos_xy(PointClass(x=config.axis1_st_en.get(), \
                                              y=config.axis2_st_en.get()))

        #Schreiben der Standardwert am Ende        
        string = postpro.write_gcode_en(postpro)

        if status == 1:
            self.textbox.prt(_("\nSuccessfully generated G-Code"))
            self.master.update_idletasks()

        else:
            self.textbox.prt(_("\nError during G-Code Generation"))
            self.master.update_idletasks()

                    
        #Drucken in den Stdout, speziell fuer EMC2 
        if config.write_to_stdout:
            print(string)
            self.ende()     
        else:
            #Exportieren der Daten
                try:
                    #Das File oeffnen und schreiben    
                    f = open(self.save_filename, "w")
                    f.write(string)
                    f.close()       
                except IOError:
                    showwarning(_("Save As"), _("Cannot save the file."))
            
    def Get_Save_File(self):
        """
        Callback Function after the Export Button is pressed. Called by 
        Write_GCode. Only called if the EMC Option is not active
        @return: Returns the string of the choosen path+filename. None if 
        nothing is selected    
        """

        MyFormats = []
        for i in range(len(self.postpro.output_format)):
            name = "%s" % (self.postpro.output_text[i])
            format = "*%s" % (self.postpro.output_format[i])
            MyFormats.append((name, format))
            

        #Cancel if there is no file loaded
        if self.load_filename == None:
            showwarning(_("Export G-Code"), _("Nothing to export!"))
            return
        

        (beg, ende) = os.path.split(self.load_filename)
        (fileBaseName, fileExtension) = os.path.splitext(ende)

        inidir = self.config.save_path
        
        save_filename = asksaveasfilename(initialdir=inidir, \
                               initialfile=fileBaseName, filetypes=MyFormats, defaultextension=self.postpro.output_format[0])
               
        return save_filename


    def opt_export_route(self):
        """
        Optimizes the routes during the export. Function called by Write_GCode
        """
        
        #Errechnen der Iterationen
        iter = min(self.config.max_iterations, len(self.CanvasContent.Shapes) * 20)
        
        #Anfangswerte fuer das Sortieren der Shapes
        self.shapes_to_write = []
        shapes_st_en_points = []
        
        #Alle Shapes die geschrieben werden zusammenfassen
        for shape_nr in range(len(self.CanvasContent.Shapes)):
            shape = self.CanvasContent.Shapes[shape_nr]
            if not(shape.nr in self.CanvasContent.Disabled):
                self.shapes_to_write.append(shape)
                shapes_st_en_points.append(shape.get_st_en_points())
                

        #Hinzufuegen des Start- Endpunkte ausserhalb der Geometrie
        x_st = self.config.axis1_st_en.get()
        y_st = self.config.axis2_st_en.get()
        start = PointClass(x=x_st, y=y_st)
        ende = PointClass(x=x_st, y=y_st)
        shapes_st_en_points.append([start, ende])

        #Optimieren der Reihenfolge
        self.textbox.prt(_("\nTSP Starting"), 1)
                
        self.TSP = TSPoptimize(shapes_st_en_points, self.textbox, self.master, self.config)
        self.textbox.prt(_("\nTSP start values initialised"), 1)
        #self.CanvasContent.path_hdls=[]
        #self.CanvasContent.plot_opt_route(shapes_st_en_points,self.TSP.opt_route)

        for it_nr in range(iter):
            #Jeden 10ten Schrit rausdrucken
            if (it_nr % 10) == 0:
                self.textbox.prt((_("\nTSP Iteration nr: %i") % it_nr), 1)
                for hdl in self.CanvasContent.path_hdls:
                    self.Canvas.canvas.delete(hdl)
                self.CanvasContent.path_hdls = []
                self.CanvasContent.plot_opt_route(shapes_st_en_points, self.TSP.opt_route)
                self.master.update_idletasks()
                
            self.TSP.calc_next_iteration()
            
        self.textbox.prt(_("\nTSP done with result:"), 1)
        self.textbox.prt(("\n%s" % self.TSP), 1)

        self.viewmenu.entryconfig(6, state=NORMAL)        

    def del_route_and_menuentry(self):
        """
        Called from the main menu when the delete optimized route menu entry is 
        pusehd. The menu is only enabled if the route is ploted and therefore if 
        the export was done before. It also disables the menu after that.
        """ 
        try:
            self.viewmenu.entryconfig(6, state=DISABLED)
            self.CanvasContent.delete_opt_path()
        except:
            pass
        
    def Show_About(self):
        """
        Called from the main menu when the About menu entry is pushed. It 
        calles the AboutDialogWindow Class which generated the whole window
        which handels the rest.
        """ 
        AboutDialogWindow(self.master)
  
    def ende(self):
        """
        This function is called if the menu entry close is pushed. It destroys
        the window and quits.
        """ 
        self.master.destroy()
        self.master.quit()

class TextboxClass:
    """
    This class genreated the textbox at the bottom of the frame. The class is 
    called by the MyMainWindow Class and passed to all other classes which 
    have to print in it. 
    G{importgraph modules}
    """

    def __init__(self, frame=None, master=None, DEBUG=0):
        """
        Initialisation of the class
        @param DEBUG: Parameter to define which detail of messages is displayed
        """
      
        self.DEBUG = DEBUG
        self.master = master
        self.text = Text(frame, height=7)
        
        self.textscr = Scrollbar(frame)
        self.text.grid(row=0, column=0, pady=4, sticky=E + W)
        self.textscr.grid(row=0, column=1, pady=4, sticky=N + S)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=0)

        
        #Binding fuer Contextmenu
        self.text.bind("<Button-3>", self.text_contextmenu)
        # Mac OS x has right mouse button mapped to  Button-2
        if platform in ("mac"):
            self.text.bind("<Button-2>", self.text_contextmenu)
            # for single-button macs..
            self.text.bind("<Option-Button-1>", self.text_contextmenu)

        #Anfangstext einfuegen
        self.textscr.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.textscr.set)
        self.prt(_('Program started\n %s %s \nCoded by V. Schulz and C. Kohloeffel' % (VERSION, DATE)))

    def set_debuglevel(self, DEBUG=0):
        """
        Changes the debuglevel. The function should be called from the load
        config file. The debug level can be set in the config file.
        @param DEBUG: Parameter to define which detail of messages is displayed
        """
        self.DEBUG = DEBUG
        if DEBUG:
            self.text.config(height=15)

    def prt(self, txt='', DEBUGLEVEL=0):
        """
        Prints a message in the message window. An additional parameter can be 
        defined which specifies if this is debug message. If Debuglevel is 
        higher then 0, then it is only ploted if DEBUG > DEBUGLEVEL
        @param txt: Text to be displayed
        @param DEBUGLEVEL: At which DEBUGLEVEL the message shall be printed.
        """

        if self.DEBUG >= DEBUGLEVEL:
            self.text.insert(END, txt)
            self.text.yview(END)
            self.master.update_idletasks()
            
    #Contextmenu Text mit Bindings beim Rechtsklick
    def text_contextmenu(self, event):
        """
        Called if the right mouse button is pressed in the message window. It 
        generates a contextmenu. Within the context menu its possible to delete 
        the existing texts.
        """

        #Contextmenu erstellen zu der Geometrie        
        popup = Menu(self.text, tearoff=0)        
        popup.add_command(label='Delete text entries', command=self.text_delete_entries)
        popup.post(event.x_root, event.y_root)
        
    def text_delete_entries(self):
        """
        If in the context menu the delete button is pressed the existing text 
        beginning at line 7 is deleted.
        """

        self.text.delete(7.0, END)
        self.text.yview(END)           

         
#Klasse zum Erstellen des Plots
class CanvasClass:
    def __init__(self, master=None, text=None):
        
        #�bergabe der Funktionswerte
        self.master = master
        self.Content = []

        #Erstellen der Standardwerte
        self.firstevent = []
        self.lastevent = []
        self.sel_rect_hdl = []
        self.dir_var = IntVar()
        self.dx = 0.0
        self.dy = 0.0
        self.scale = 1.0

        #Wird momentan nicht benoetigt, eventuell fuer Beschreibung von Aktionen im Textfeld #self.text=text

        #Erstellen des Labels am Unteren Rand fuer Status Leiste        
        self.label = Label(self.master, text=_("Curser Coordinates: X=0.0, Y=0.0, Scale: 1.00"), bg="white", anchor="w")
        self.label.grid(row=1, column=0, sticky=E + W)

        #Canvas Erstellen und Fenster ausfuellen        
        self.canvas = Canvas(self.master, width=650, height=500, bg="white")
        self.canvas.grid(row=0, column=0, sticky=N + E + S + W)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        #Binding fuer die Bewegung des Mousezeigers
        self.canvas.bind("<Motion>", self.moving)

        #Bindings fuer Selektieren
        self.canvas.bind("<Button-1>", self.select_cont)
        
        #Eventuell mit Abfrage probieren???????????????????????????????????????????
        self.canvas.bind("<Shift-Button-1>", self.multiselect_cont)
        self.canvas.bind("<B1-Motion>", self.select_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.select_release)

        #Binding fuer Contextmenu
        self.canvas.bind("<Button-3>", self.make_contextmenu)

        #Bindings fuer Zoom und Bewegen des Bilds        
        self.canvas.bind("<Control-Button-1>", self.mouse_move)
        self.canvas.bind("<Control-B1-Motion>", self.mouse_move_motion)
        self.canvas.bind("<Control-ButtonRelease-1>", self.mouse_move_release)
        self.canvas.bind("<Control-Button-3>", self.mouse_zoom)
        self.canvas.bind("<Control-B3-Motion>", self.mouse_zoom_motion)
        self.canvas.bind("<Control-ButtonRelease-3>", self.mouse_zoom_release)  

#	if platform in ("mac"):
#            # for macs with three button mice  Button-3  actually is reported as Button-2
#            self.canvas.bind("<Button-2>", self.make_contextmenu)
#            # and if that isnt available, the following does the trick (one-eyed mice)
#            self.canvas.bind("<Option-Button-1>", self.make_contextmenu)
#            self.canvas.bind("<Command-ButtonRelease-1>", self.mouse_zoom_release)   
#            self.canvas.bind("<Command-Button-1>", self.mouse_zoom)
#            self.canvas.bind("<Command-B1-Motion>", self.mouse_zoom_motion)          

    #Callback fuer das Bewegen der Mouse mit Darstellung in untere Leiste
    def moving(self, event):
        x = self.dx + (event.x / self.scale)
        y = self.dy + (self.canvas.winfo_height() - event.y) / self.scale

        if self.scale < 1:
            self.label['text'] = (_("Curser Coordinates: X= %5.0f Y= %5.0f , Scale: %5.3f") \
                                % (x, y, self.scale))
            
        elif (self.scale >= 1)and(self.scale < 10):      
            self.label['text'] = (_("Curser Coordinates: X= %5.1f Y= %5.1f , Scale: %5.2f") \
                                % (x, y, self.scale))
        elif self.scale >= 10:      
            self.label['text'] = (_("Curser Coordinates: X= %5.2f Y= %5.2f , Scale: %5.1f") \
                                % (x, y, self.scale))
        
    #Callback fuer das Ausw�hlen von Elementen
    def select_cont(self, event):
        #Abfrage ob ein Contextfenster offen ist, speziell fuer Linux
        self.close_contextmenu()
        
        self.moving(event)
        self.Content.deselect()
        self.sel_rect_hdl = Rectangle(self.canvas, event.x, event.y, event.x, event.y, outline="grey") 
        self.lastevent = event

    def multiselect_cont(self, event):
        #Abfrage ob ein Contextfenster offen ist, speziell fuer Linux
        self.close_contextmenu()
        
        self.sel_rect_hdl = Rectangle(self.canvas, event.x, event.y, event.x, event.y, outline="grey") 
        self.lastevent = event

    def select_rectangle(self, event):
        self.moving(event)
        self.canvas.coords(self.sel_rect_hdl, self.lastevent.x, self.lastevent.y, \
                           event.x, event.y)

    def select_release(self, event):
 
        dx = self.lastevent.x - event.x
        dy = self.lastevent.y - event.y
        self.canvas.delete(self.sel_rect_hdl)
        
        #Beim Ausw�hlen sollen die Direction Pfeile geloescht werden!!!!!!!!!!!!!!!!!!        
        #self.Content.delete_opt_path()   
        
        #Wenn mehr als 6 Pixel gezogen wurde Enclosed        
        if (abs(dx) + abs(dy)) > 6:
            items = self.canvas.find_overlapping(event.x, event.y, event.x + dx, event.y + dy)
            mode = 'multi'
        else:
            #items=self.canvas.find_closest(event.x, event.y)
            items = self.canvas.find_overlapping(event.x - 3, event.y - 3, event.x + 3, event.y + 3)
            mode = 'single'
            
        shapes = self.Content.get_selected_shapes(items, mode)
        self.Content.change_selection(shapes)

    #Callback fuer Bewegung des Bildes
    def mouse_move(self, event):
        self.master.config(cursor="fleur")
        self.lastevent = event

    def mouse_move_motion(self, event):
        self.moving(event)
        dx = event.x - self.lastevent.x
        dy = event.y - self.lastevent.y
        self.dx = self.dx - dx / self.scale
        self.dy = self.dy + dy / self.scale
        self.canvas.move(ALL, dx, dy)
        self.lastevent = event

    def mouse_move_release(self, event):
        self.master.config(cursor="")      

    #Callback fuer das Zoomen des Bildes     
    def mouse_zoom(self, event):
        self.canvas.focus_set()
        self.master.config(cursor="sizing")
        self.firstevent = event
        self.lastevent = event

    def mouse_zoom_motion(self, event):
        self.moving(event)
        dy = self.lastevent.y - event.y
        sca = (1 + (dy * 3) / float(self.canvas.winfo_height()))
       
        self.dx = (self.firstevent.x + ((-self.dx * self.scale) - self.firstevent.x) * sca) / sca / -self.scale
        eventy = self.canvas.winfo_height() - self.firstevent.y
        self.dy = (eventy + ((-self.dy * self.scale) - eventy) * sca) / sca / -self.scale
        
        self.scale = self.scale * sca
        self.canvas.scale(ALL, self.firstevent.x, self.firstevent.y, sca, sca)
        self.lastevent = event

        self.Content.plot_cut_info() 
        self.Content.plot_wp_zero()

    def mouse_zoom_release(self, event):
        self.master.config(cursor="")
                
    #Contextmenu mit Bindings beim Rechtsklick
    def make_contextmenu(self, event):
        self.lastevent = event

        #Abfrage ob das Contextfenster schon existiert, speziell fuer Linux
        self.close_contextmenu()
            
        #Contextmenu erstellen zu der Geometrie        
        popup = Menu(self.canvas, tearoff=0)
        self.popup = popup
        popup.add_command(label=_('Invert Selection'), command=self.Content.invert_selection)
        popup.add_command(label=_('Disable Selection'), command=self.Content.disable_selection)
        popup.add_command(label=_('Enable Selection'), command=self.Content.enable_selection)

        popup.add_separator()
        popup.add_command(label=_('Switch Direction'), command=self.Content.switch_shape_dir)
        
        #Untermenu fuer die Fr�serkorrektur
        self.dir_var.set(self.Content.calc_dir_var())
        cut_cor_menu = Menu(popup, tearoff=0)
        cut_cor_menu.add_checkbutton(label=_("G40 No correction"), \
                                     variable=self.dir_var, onvalue=0, \
                                     command=lambda:self.Content.set_cut_cor(40))
        cut_cor_menu.add_checkbutton(label=_("G41 Cutting left"), \
                                     variable=self.dir_var, onvalue=1, \
                                     command=lambda:self.Content.set_cut_cor(41))
        cut_cor_menu.add_checkbutton(label=_("G42 Cutting right"), \
                                     variable=self.dir_var, onvalue=2, \
                                     command=lambda:self.Content.set_cut_cor(42))
        popup.add_cascade(label=_('Set Cutter Correction'), menu=cut_cor_menu)

        #Menus Disablen wenn nicht ausgew�hlt wurde        
        if len(self.Content.Selected) == 0:
            popup.entryconfig(0, state=DISABLED)
            popup.entryconfig(1, state=DISABLED)
            popup.entryconfig(2, state=DISABLED)
            popup.entryconfig(4, state=DISABLED)
            popup.entryconfig(5, state=DISABLED)

        popup.post(event.x_root, event.y_root)
        
    #Speziell fuer Linux falls das Contextmenu offen ist dann schliessen
    def close_contextmenu(self):
        """ 
        Additional function to close the popup contextmenu. Was needed in Linux
        since it was not popberly closing.
        """ 
        try:
            self.popup.destroy()
            del(self.popup)
        except:
            pass

    def autoscale(self):
        """ 
        Autoscales the Canvas.
        """ 

        #Rand der um die Extreme des Elemente dargestellt wird        
        rand = 20

        #Alles auf die 0 Koordinaten verschieben, dass sp�ter DX und DY Berechnung richtig erfolgt       
        self.canvas.move(ALL, self.dx * self.scale, -self.canvas.winfo_height() - self.dy * self.scale)
        self.dx = 0;
        self.dy = -self.canvas.winfo_height() / self.scale

        #Umriss aller Elemente
        d = self.canvas.bbox(ALL)
        cx = (d[0] + d[2]) / 2
        cy = (d[1] + d[3]) / 2
        dx = d[2] - d[0]
        dy = d[3] - d[1]

        #Skalierung des Canvas errechnen
        xs = float(dx) / (self.canvas.winfo_width() - rand)
        ys = float(dy) / (self.canvas.winfo_height() - rand)
        scale = 1 / max(xs, ys)
        
        #Skalieren der Elemente        
        self.canvas.scale(ALL, 0, 0, scale, scale)
        self.scale = self.scale * scale

        #Verschieben der Elemente zum Mittelpunkt        
        dx = self.canvas.winfo_width() / 2 - cx * scale
        dy = self.canvas.winfo_height() / 2 - cy * scale
        self.dy = self.dy / scale
        self.dx = self.dx / scale
        self.canvas.move(ALL, dx, dy)
        
        #Mouse Position errechnen
        self.dx = self.dx - dx / self.scale
        self.dy = self.dy + dy / self.scale

        self.Content.plot_cut_info()
        self.Content.plot_wp_zero()
        
    def get_can_coordinates(self, x_st, y_st):
        x_ca = (x_st - self.dx) * self.scale
        y_ca = (y_st - self.dy) * self.scale - self.canvas.winfo_height()
        return x_ca, y_ca
        
#Klasse mit den Inhalten des Canvas & Verbindung zu den Konturen
class CanvasContentClass:
    
    def __init__(self, Canvas, textbox, config, MyNotebook):
        self.Canvas = Canvas
        self.textbox = textbox
        self.config = config
        self.MyNotebook = MyNotebook
        self.Shapes = []
        self.LayerContents = []
        self.EntitiesRoot = EntitieContentClass()
        self.BaseEntities = EntitieContentClass()
        self.EntitieContents = []
        self.Selected = []
        self.Disabled = []
        self.wp_zero_hdls = []
        self.dir_hdls = []
        self.path_hdls = []
        

        #Anfangswert fuer das Ansicht Toggle Menu
        self.toggle_wp_zero = IntVar()
        self.toggle_wp_zero.set(1)

        self.toggle_start_stop = IntVar()
        self.toggle_start_stop.set(0)

        self.toggle_show_disabled = IntVar()
        self.toggle_show_disabled.set(0)  
        
    def __str__(self):
        str = '\nNr. of Shapes -> %str' % len(self.Shapes)
        for lay in self.LayerContents:
            str = str + '\n' + str(lay)
        for ent in self.EntitieContents:
            str = str + '\n' + str(ent)
        str = str + '\nSelected -> %str' % (self.Selected)\
           + '\nDisabled -> %str' % (self.Disabled)
        return str

    def calc_dir_var(self):
        if len(self.Selected) == 0:
            return - 1
        dir = self.Selected[0].cut_cor
        for shape in self.Selected[1:len(self.Selected)]: 
            if not(dir == shape.cut_cor):
                return - 1   
        return dir - 40
                
    #Erstellen des Gesamten Ausdrucks      
    def makeplot(self, values, p0, pb, sca, rot):
        self.values = values

        #Loeschen des Inhalts
        self.Canvas.canvas.delete(ALL)
        
        #Standardwerte fuer scale, dx, dy zuweisen
        self.Canvas.scale = 1
        self.Canvas.dx = 0
        self.Canvas.dy = -self.Canvas.canvas.winfo_height()

        #Zuruecksetzen der Konturen
        self.Shapes = []
        self.CCShapes = []
        self.LayerContents = []
        self.EntitiesRoot = EntitieContentClass(Nr=0, Name='Entities', parent=None, children=[],
                                            p0=p0, pb=pb, sca=sca, rot=rot)
        self.Selected = []
        self.Disabled = []
        self.wp_zero_hdls = []
        self.dir_hdls = []
        self.path_hdls = []

        #Start mit () bedeutet zuweisen der Entities -1 = Standard
        self.makeshapes(parent=self.EntitiesRoot)
        
        self.plot_shapes()
        
        self.makeccshapes(parent=self.EntitiesRoot)
        
        self.plot_ccshapes()
        
        self.LayerContents.sort()     

        #Autoscale des Canvas        
        self.Canvas.autoscale()
        
        self.MyNotebook.CreateLayerContent(self.LayerContents)
           
    def makeshapes(self, parent=None, ent_nr= -1):

        if parent.Name == "Entities":      
            entities = self.values.entities
        else:
            ent_nr = self.values.Get_Block_Nr(parent.Name)
            entities = self.values.blocks.Entities[ent_nr]
            
        #Zuweisen der Geometrien in die Variable geos & Konturen in cont
        ent_geos = entities.geo
               
        #Schleife fuer die Anzahl der Konturen 
        for cont in entities.cont:
            #Abfrage falls es sich bei der Kontur um ein Insert eines Blocks handelt
            if ent_geos[cont.order[0][0]].Typ == "Insert":
                ent_geo = ent_geos[cont.order[0][0]]
                
                #Zuweisen des Basispunkts f�r den Block
                new_ent_nr = self.values.Get_Block_Nr(ent_geo.BlockName)
                new_entities = self.values.blocks.Entities[new_ent_nr]
                pb = new_entities.basep
                
                #Skalierung usw. des Blocks zuweisen
                p0 = ent_geos[cont.order[0][0]].Point
                sca = ent_geos[cont.order[0][0]].Scale
                rot = ent_geos[cont.order[0][0]].rot
                
                #Erstellen des neuen Entitie Contents f�r das Insert
                NewEntitieContent = EntitieContentClass(Nr=0, Name=ent_geo.BlockName,
                                        parent=parent, children=[],
                                        p0=p0,
                                        pb=pb,
                                        sca=sca,
                                        rot=rot)

                parent.addchild(NewEntitieContent)
            
                self.makeshapes(parent=NewEntitieContent, ent_nr=ent_nr)
                
            else:
                #Schleife fuer die Anzahl der Geometrien
                self.Shapes.append(ShapeClass(len(self.Shapes), \
                                                cont.closed, \
                                                40, \
                                                0.0, \
                                                parent, \
                                                [], \
                                                []))
                
                for ent_geo_nr in range(len(cont.order)):
                    ent_geo = ent_geos[cont.order[ent_geo_nr][0]]
                    if cont.order[ent_geo_nr][1]:
                        ent_geo.geo.reverse()
                        for geo in ent_geo.geo:
                            abs_geo = geo.make_abs_geo(parent=parent, reverse=1)
                            abs_geo.calc_bounding_box()
                            self.Shapes[-1].geos.append(abs_geo)
                            self.Shapes[-1].BB = self.Shapes[-1].BB.joinBB(abs_geo.BB)

                        ent_geo.geo.reverse()
                    else:
                        for geo in ent_geo.geo:
                            abs_geo = geo.make_abs_geo(parent=parent, reverse=0)
                            abs_geo.calc_bounding_box()
                            self.Shapes[-1].geos.append(abs_geo)
                            self.Shapes[-1].BB = self.Shapes[-1].BB.joinBB(abs_geo.BB)
                        
                self.addtoLayerContents(self.Shapes[-1], ent_geo.Layer_Nr)
                parent.addchild(self.Shapes[-1])

                self.Shapes[-1].AnalyseAndOptimize(MyConfig=self.config)
                
    def plot_shapes(self):
        for shape in self.Shapes:
            shape.plot2can(self.Canvas.canvas)
           
    def makeccshapes(self, parent=None):
        
        self.CCShapes = []
        self.SOC = ShapeOffsetClass()
        
        for shape in self.Shapes:
            #self.CCShapes.append(self.SOC.do_compensation(shape, 2, 41))
            self.CCShapes.append(self.SOC.do_compensation(shape))
            
    def plot_ccshapes(self):
        """
        Plots the Cutter Compesated shapes to the canvas
        """
        for ccshape in self.CCShapes:
            ccshape.plot2can(self.Canvas.canvas, col='blue')  
  
    #Drucken des Werkstuecknullpunkts
    def plot_wp_zero(self):
        for hdl in self.wp_zero_hdls:
            self.Canvas.canvas.delete(hdl) 
        self.wp_zero_hdls = []
        if self.toggle_wp_zero.get(): 
            x_zero, y_zero = self.Canvas.get_can_coordinates(0, 0)
            xy = x_zero - 8, -y_zero - 8, x_zero + 8, -y_zero + 8
            hdl = Oval(self.Canvas.canvas, xy, outline="gray")
            self.wp_zero_hdls.append(hdl)

            xy = x_zero - 6, -y_zero - 6, x_zero + 6, -y_zero + 6
            hdl = Arc(self.Canvas.canvas, xy, start=0, extent=180, style="pieslice", outline="gray")
            self.wp_zero_hdls.append(hdl)
            hdl = Arc(self.Canvas.canvas, xy, start=90, extent=180, style="pieslice", outline="gray")
            self.wp_zero_hdls.append(hdl)
            hdl = Arc(self.Canvas.canvas, xy, start=270, extent=90, style="pieslice", outline="gray", fill="gray")
            self.wp_zero_hdls.append(hdl)
    def plot_cut_info(self):
        for hdl in self.dir_hdls:
            self.Canvas.canvas.delete(hdl) 
        self.dir_hdls = []

        if not(self.toggle_start_stop.get()):
            draw_list = self.Selected[:]
        else:
            draw_list = range(len(self.Shapes))
               
        for shape in draw_list:
            if not(shape in self.Disabled):
                self.dir_hdls += shape.plot_cut_info(self.Canvas, self.config)


    def plot_opt_route(self, shapes_st_en_points, route):
        #Ausdrucken der optimierten Route
        for en_nr in range(len(route)):
            if en_nr == 0:
                st_nr = -1
                col = 'gray'
            elif en_nr == 1:
                st_nr = en_nr - 1
                col = 'gray'
            else:
                st_nr = en_nr - 1
                col = 'peru'
                
            st = shapes_st_en_points[route[st_nr]][1]
            en = shapes_st_en_points[route[en_nr]][0]

            x_ca_s, y_ca_s = self.Canvas.get_can_coordinates(st.x, st.y)
            x_ca_e, y_ca_e = self.Canvas.get_can_coordinates(en.x, en.y)

            self.path_hdls.append(Line(self.Canvas.canvas, x_ca_s, -y_ca_s, x_ca_e, -y_ca_e, fill=col, arrow='last'))
        self.Canvas.canvas.update()


    #Hinzufuegen der Kontur zum Layer        
    def addtoLayerContents(self, shape_nr, lay_nr):
        #Abfrage of der gesuchte Layer schon existiert
        for LayCon in self.LayerContents:
            if LayCon.LayerNr == lay_nr:
                LayCon.Shapes.append(shape_nr)
                return

        #Falls er nicht gefunden wurde neuen erstellen
        LayerName = self.values.layers[lay_nr].name
        self.LayerContents.append(LayerContentClass(LayerNr=lay_nr,
                                                    LayerName=LayerName,
                                                    Shapes=[shape_nr],
                                                    MyMessages=self.textbox))
        
    #Hinzufuegen der Kontur zu den Entities
    def addtoEntitieContents(self, shape_nr, ent_nr, c_nr):
        
        for EntCon in self.EntitieContents:
            if EntCon.EntNr == ent_nr:
                if c_nr == 0:
                    EntCon.Shapes.append([])
                
                EntCon.Shapes[-1].append(shape_nr)
                return

        #Falls er nicht gefunden wurde neuen erstellen
        if ent_nr == -1:
            EntName = 'Entities'
        else:
            EntName = self.values.blocks.Entities[ent_nr].Name
            
        self.EntitieContents.append(EntitieContentClass(ent_nr, EntName, [[shape_nr]]))

    def delete_opt_path(self):
        for hdl in self.path_hdls:
            self.Canvas.canvas.delete(hdl)
            
        self.path_hdls = []
        
    def deselect(self):
        self.Deselected = self.Selected[:]
        self.Selected = []
        self.set_shapes_color(self.Deselected, 'deselected')
        
        if not(self.toggle_start_stop.get()):
            for hdl in self.dir_hdls:
                self.Canvas.canvas.delete(hdl) 
            self.dir_hdls = []
       
    def get_selected_shapes(self, items, mode):
        shape_nrs = []
        shapes = []
        for item in items:
            try:
                tag = int(self.Canvas.canvas.gettags(item)[-1])
                if not(tag in shape_nrs):
                    shape_nrs.append(tag)
                    if mode == 'single':
                        break
            except:
                pass
            
        for shape_nr in shape_nrs:
            shapes.append(self.Shapes[shape_nr])
            
        return shapes
        
    def change_selection(self, sel_shapes):
        self.Deselected = []
        for shape in sel_shapes:
            if not(shape in self.Selected):
                self.Selected.append(shape)
                self.textbox.prt(_('\n\nAdded shape to selection %s:') % (shape), 3)
            else:
                self.Deselected.append(shape)
                self.Selected.remove(shape)
                self.textbox.prt(_('\n\Removed shape to selection %s:') % (shape), 3)
        
        self.plot_cut_info()
        self.set_shapes_color(self.Selected, 'selected')
        self.set_shapes_color(self.Deselected, 'deselected')
        self.Deselected = []
 
    def invert_selection(self):
        new_sel = []
        for shape in self.Shapes:
            if (not(shape in self.Disabled)) & (not(shape in self.Selected)):
                new_sel.append(shape)

        self.Deselected = self.Selected[:]
        self.Selected = new_sel
        
        self.set_shapes_color(self.Selected, 'selected')
        self.set_shapes_color(self.Deselected, 'deselected')
        self.Deselected = []
        
        self.plot_cut_info()

        self.textbox.prt(_('\nInverting Selection'), 3)
        

    def disable_selection(self):
        for shape in self.Selected:
            if not(shape in self.Disabled):
                self.Disabled.append(shape)
        self.set_shapes_color(self.Selected, 'disabled')
        self.Selected = []
        self.plot_cut_info()

    def enable_selection(self):
        for shape in self.Selected:
            if shape in self.Disabled:
                nr = self.Disabled.index(shape)
                del(self.Disabled[nr])
        self.set_shapes_color(self.Selected, 'deselected')
        self.Selected = []
        self.plot_cut_info()

    def show_disabled(self):
        if (self.toggle_show_disabled.get() == 1):
            self.set_hdls_normal(self.Disabled)
            self.show_dis = 1
        else:
            self.set_hdls_hidden(self.Disabled)
            self.show_dis = 0

    def switch_shape_dir(self):
        for shape in self.Selected:
            shape.reverse()
            self.textbox.prt(_('\n\nSwitched Direction at Shape: %s')\
                             % (shape), 3)
        self.plot_cut_info()
        
    def set_cut_cor(self, correction):
        for shape in self.Selected: 
            shape.cut_cor = correction
            
            self.textbox.prt(_('\n\nChanged Cutter Correction at Shape: %s')\
                             % (shape), 3)
        self.plot_cut_info() 
        
    def set_shapes_color(self, shapes, state):
        s_shapes = []
        d_shapes = []
        for shape in shapes:
            if not(shape in self.Disabled):
                s_shapes.append(shape)
            else:
                d_shapes.append(shape)
        
        s_hdls = self.get_shape_hdls(s_shapes)
        d_hdls = self.get_shape_hdls(d_shapes)

        if state == 'deselected':
            s_color = 'black'
            d_color = 'gray'
        elif state == 'selected':
            s_color = 'red'
            d_color = 'blue'
        elif state == 'disabled':
            s_color = 'gray'
            d_color = 'gray'
            
        self.set_color(s_hdls, s_color)
        self.set_color(d_hdls, d_color)

        if (self.toggle_show_disabled.get() == 0):
            self.set_hdls_hidden(d_shapes)
        
    def set_color(self, hdls, color):
        for hdl in hdls:
            if (self.Canvas.canvas.type(hdl) == "oval") :
                self.Canvas.canvas.itemconfig(hdl, outline=color)
            else:
                self.Canvas.canvas.itemconfig(hdl, fill=color)

    def set_hdls_hidden(self, shapes):
        hdls = self.get_shape_hdls(shapes)
        for hdl in hdls:
            self.Canvas.canvas.itemconfig(hdl, state='hidden')

    def set_hdls_normal(self, shapes):
        hdls = self.get_shape_hdls(shapes)
        for hdl in hdls:
            self.Canvas.canvas.itemconfig(hdl, state='normal')            
        
    def get_shape_hdls(self, shapes):        
        hdls = []
        for shape in shapes:
            if type(shape.geos_hdls[0]) is list:
                for subcont in shape.geos_hdls:
                    hdls = hdls + subcont
            else:
                hdls = hdls + shape.geos_hdls
        return hdls      
                                       

class AboutDialogWindow(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        self.title(_("About DXF2GCODE"))
        self.parent = parent
        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                  parent.winfo_rooty() + 50))

        self.initial_focus.focus_set()
        self.wait_window(self)

    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text=_("OK"), width=10, command=self.ok, default=ACTIVE)
        w.pack(padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()

    def ok(self, event=None):   
        self.withdraw()
        self.update_idletasks()
        self.close()

    def close(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def show_hand_cursor(self, event):
        event.widget.configure(cursor="hand1")
    def show_arrow_cursor(self, event):
        event.widget.configure(cursor="")
        
    def click(self, event):
        w = event.widget
        x, y = event.x, event.y
        tags = w.tag_names("@%d,%d" % (x, y))
        for t in tags:
            if t.startswith("href:"):
                webbrowser.open(t[5:])
                break


    def body(self, master):
        text = Text(master, width=40, height=8)
        text.pack()
        # configure text tag
        text.tag_config("a", foreground="blue", underline=1)
        text.tag_bind("a", "<Enter>", self.show_hand_cursor)
        text.tag_bind("a", "<Leave>", self.show_arrow_cursor)
        text.tag_bind("a", "<Button-1>", self.click)
        text.config(cursor="arrow")

        #add a link with data
        href = "http://christian-kohloeffel.homepage.t-online.de/index.html"
        text.insert(END, _("You are using DXF2GCODE"))
        text.insert(END, ("\nVersion %s (%s)" % (VERSION, DATE)))
        text.insert(END, _("\nFor more information und updates about"))
        text.insert(END, _("\nplease visit my homepage at:"))
        text.insert(END, _("\nwww.christian-kohloeffel.homepage.t-online.de"), ("a", "href:" + href))



class VariableDialogWindow(Toplevel):
    def __init__(self, parent=None, title='Test Dialog', label=('label1', 'label2'), value=(0.0, 0.0)):
        if not(len(label) == len(value)):
            raise Exception, "Number of labels different to number of values"

        #Eingabewerte in self speichern
        self.label = label
        self.value = value
        self.result = False

        Toplevel.__init__(self, parent)
        self.transient(parent)

        self.title(title)
        self.parent = parent

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                  parent.winfo_rooty() + 50))

        self.initial_focus.focus_set()
        self.wait_window(self)

    def buttonbox(self):
        
        box = Frame(self)

        w = Button(box, text=_("OK"), width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text=_("Cancel"), width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def ok(self, event=None):   
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def body(self, master):
        #Die Werte den Tkintervarialben zuweisen
        self.tkintervars = []
        for row_nr in range(len(self.label)):
            self.tkintervars.append(DoubleVar())
            self.tkintervars[-1].set(self.value[row_nr])
            Label(master, text=self.label[row_nr]).grid(row=row_nr, padx=4, sticky=N + W)
            Entry(master, textvariable=self.tkintervars[row_nr], width=10).grid(row=row_nr, column=1, padx=4, sticky=N + W)

    def apply(self):
        self.result = []
        for tkintervar in self.tkintervars:
            self.result.append(tkintervar.get())


#Hauptfunktion zum Aufruf des Fensters und Mainloop     
if __name__ == "__main__":
   
    #sys.stdout = SysOutListener()
    #sys.stderr = SysErrListener()

    master = Tk()
    master.title("%s, Version: %s, Date: %s " % (APPNAME, VERSION, DATE))

    #Falls das Programm mit Parametern von EMC gestartet wurde
    if len(sys.argv) > 1:
        MyMainWindow(sys.argv[1])
    else:
        MyMainWindow()

    master.mainloop()

    
