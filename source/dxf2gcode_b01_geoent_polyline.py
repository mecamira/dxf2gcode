#!/usr/bin/python
# -*- coding: cp1252 -*-
#
#dxf2gcode_b01_ent_polyline
#Programmer: Christian Kohl�ffel
#E-mail:     n/A
#
#Copyright 2008 Christian Kohl�ffel
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

from Canvas import Oval, Arc, Line
from math import sqrt, sin, cos, atan2, radians, degrees
from dxf2gcode_b01_point import PointClass, LineGeo, PointsClass, ContourClass


class PolylineClass:
    def __init__(self,Nr=0,caller=None):
        self.Typ='Polyline'
        self.Nr = Nr
        self.Layer_Nr = 0
        self.geo=[]
        self.length= 0

        #Lesen der Geometrie
        self.Read(caller)
        
    def __str__(self):
        # how to print the object
        string=("\nTyp: Polyline")+\
               ("\nNr: %i" %self.Nr)+\
               ("\nLayer Nr: %i" %self.Layer_Nr)+\
               ("\nNr. of Lines: %i" %len(self.geo))+\
               ("\nlength: %0.3f" %self.length)

        
        for geo in self.geo:
            string+=str(geo)
        return string

    def reverse(self):
        self.geo.reverse()
        for geo in self.geo:
            geo.reverse()  

    def App_Cont_or_Calc_IntPts(self, cont, points, i, tol):
        #Hinzuf�gen falls es keine geschlossene Polyline ist
        if self.geo[0].Pa.isintol(self.geo[-1].Pe,tol):
            self.analyse_and_opt()
            cont.append(ContourClass(len(cont),1,[[i,0]],self.length))
        else:            
            points.append(PointsClass(point_nr=len(points),geo_nr=i,\
                                      Layer_Nr=self.Layer_Nr,\
                                      be=self.geo[0].Pa,
                                      en=self.geo[-1].Pe,be_cp=[],en_cp=[]))      

    def analyse_and_opt(self):
        summe=0

        #Richtung in welcher der Anfang liegen soll (unten links)        
        Popt=PointClass(x=-1e3,y=-1e6)
        
        #Berechnung der Fl�ch nach Gau�-Elling Positive Wert bedeutet CW
        #negativer Wert bedeutet CCW geschlossenes Polygon            
        for Line in self.geo:
            summe+=(Line.Pa.x*Line.Pe.y-Line.Pe.x*Line.Pa.y)/2
        
        if summe>0.0:
            self.reverse()

                
        #Suchen des kleinsten Startpunkts von unten Links X zuerst (Muss neue Schleife sein!)
        min_distance=self.geo[0].Pa.distance(Popt)
        min_geo_nr=0
        for geo_nr in range(1,len(self.geo)):
            if (self.geo[geo_nr].Pa.distance(Popt)<min_distance):
                min_distance=self.geo[geo_nr].Pa.distance(Popt)
                min_geo_nr=geo_nr

        #Kontur so anordnen das neuer Startpunkt am Anfang liegt
        self.geo=self.geo[min_geo_nr:len(self.geo)]+self.geo[0:min_geo_nr]
           
    def Read(self, caller):
        #K�rzere Namen zuweisen        
        lp=caller.line_pairs
        e=lp.index_both(0,"SEQEND",caller.start+1)+1

        #Layer zuweisen        
        s=lp.index_code(8,caller.start+1)
        self.Layer_Nr=caller.Get_Layer_Nr(lp.line_pair[s].value)

        #Pa=None f�r den ersten Punkt
        Pa=None
        
        while 1:
            s=lp.index_both(0,"VERTEX",s+1,e)
            if s==None:
                break
            
            #XWert
            s=lp.index_code(10,s+1,e)
            x=float(lp.line_pair[s].value)
            #YWert
            s=lp.index_code(20,s+1,e)
            y=float(lp.line_pair[s].value)
            Pe=PointClass(x=x,y=y)

            #Zuweisen der Geometrien f�r die Polyline
            if not(type(Pa)==type(None)):
                self.geo.append(LineGeo(Pa=Pa,Pe=Pe))
                self.length+=self.geo[-1].length

            Pa=Pe

                   
        #Neuen Startwert f�r die n�chste Geometrie zur�ckgeben        
        caller.start=e

    def plot2can(self,canvas,p0,sca,tag):
        hdl=[]
        for geo in self.geo:
            hdl+=(geo.plot2can(canvas,p0,sca,tag))
        return hdl
    
    def get_start_end_points(self,direction=0):
        if not(direction):
            punkt, angle=self.geo[0].get_start_end_points(direction)
        elif direction:
            punkt, angle=self.geo[-1].get_start_end_points(direction)
        return punkt,angle
    
    def Write_GCode(self,paras,sca,p0,dir,axis1,axis2):
        string=""
        pr_geo=self.geo[:]
        
        #Umdrehen falls Gesamte Geometrie gedreht ist.        
        if dir:
            pr_geo.reverse()
        
        for geo in pr_geo:
            string+=geo.Write_GCode(paras,sca,p0,dir,axis1,axis2)       
        return string  


