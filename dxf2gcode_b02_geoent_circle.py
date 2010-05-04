#!/usr/bin/python
# -*- coding: cp1252 -*-
#
#dxf2gcode_b02_geoent_circle
#Programmers:   Christian Kohl�ffel
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

from Canvas import Oval, Arc, Line
from math import sqrt, sin, cos, atan2, radians, degrees, pi
from dxf2gcode_b02_point import PointClass, PointsClass, ArcGeo, ContourClass

class CircleClass:
    def __init__(self,Nr=0,caller=None):
        self.Typ='Circle'
        self.Nr = Nr
        self.Layer_Nr = 0
        self.length= 0.0
        self.geo=[]

        #Lesen der Geometrie
        self.Read(caller)
        
    def __str__(self):
        # how to print the object
        return("\nTyp: Circle ")+\
              ("\nNr: %i" %self.Nr)+\
              ("\nLayer Nr:%i" %self.Layer_Nr)+\
              str(self.geo[-1])

    def App_Cont_or_Calc_IntPts(self, cont, points, i, tol,warning):
        cont.append(ContourClass(len(cont),1,[[i,0]],self.length))
        return warning
        
        
    def Read(self, caller):

        #K�rzere Namen zuweisen
        lp=caller.line_pairs

        #Layer zuweisen        
        s=lp.index_code(8,caller.start+1)
        self.Layer_Nr=caller.Get_Layer_Nr(lp.line_pair[s].value)
        #XWert
        s=lp.index_code(10,s+1)
        x0=float(lp.line_pair[s].value)
        #YWert
        s=lp.index_code(20,s+1)
        y0=float(lp.line_pair[s].value)
        O=PointClass(x0,y0)
        #Radius
        s=lp.index_code(40,s+1)
        r= float(lp.line_pair[s].value)
                                
        #Berechnen der Start und Endwerte des Kreises ohne �berschneidung              
        s_ang = -3 * pi / 4
        m_ang = s_ang -pi
        e_ang = -3 * pi / 4

        #Berechnen der Start und Endwerte des Arcs
        Pa = PointClass(x=cos(s_ang) * r, y=sin(s_ang) * r) + O
        Pm = PointClass(x=cos(m_ang) * r, y=sin(m_ang) * r) + O
        Pe = PointClass(x=cos(e_ang) * r, y=sin(e_ang) * r) + O

        #Anh�ngen der ArcGeo Klasse f�r die Geometrie
        self.geo.append(ArcGeo(Pa=Pa,Pe=Pm,O=O,r=r,s_ang=s_ang,e_ang=m_ang,dir=-1))
        self.geo.append(ArcGeo(Pa=Pm,Pe=Pe,O=O,r=r,s_ang=m_ang,e_ang=e_ang,dir=-1))
 

        #L�nge entspricht der L�nge des Kreises
        self.length=self.geo[-1].length+self.geo[-2].length
       
        #Neuen Startwert f�r die n�chste Geometrie zur�ckgeben        
        caller.start=s             

    def get_start_end_points(self, direction=0):
        if not(direction):
            punkt, angle = self.geo[0].get_start_end_points(direction)
        elif direction:
            punkt, angle = self.geo[-1].get_start_end_points(direction)
        return punkt, angle