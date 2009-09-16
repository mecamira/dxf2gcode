#!/usr/bin/python
# -*- coding: cp1252 -*-
#
#dxf2gcode_b02_geoent_lwpolyline
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

from math import sqrt, sin, cos, atan2, radians, degrees
from dxf2gcode_b02_point import PointClass, LineGeo, ArcGeo, PointsClass, ContourClass


class LWPolylineClass:
    def __init__(self,Nr=0,caller=None):
        self.Typ='LWPolyline'
        self.Nr = Nr
        self.Layer_Nr = 0
        self.geo=[]

        #Lesen der Geometrie
        self.Read(caller)
        
    def __str__(self):
        # how to print the object
        string=("\nTyp: LWPolyline")+\
               ("\nNr: %i" %self.Nr)+\
               ("\nLayer Nr: %i" %self.Layer_Nr)+\
               ("\nNr. of geos: %i" %len(self.geo))
        
        return string

    def reverse(self):
        self.geo.reverse()
        for geo in self.geo:
            geo.reverse()    

    def App_Cont_or_Calc_IntPts(self, cont, points, i, tol,warning):
        if  self.geo[0].Pa.isintol(self.geo[-1].Pe,tol):

            cont.append(ContourClass(len(cont),1,[[i,0]]))
        else:
            points.append(PointsClass(point_nr=len(points),geo_nr=i,\
                                      Layer_Nr=self.Layer_Nr,\
                                      be=self.geo[0].Pa,
                                      en=self.geo[-1].Pe,be_cp=[],en_cp=[]))  
        return warning
                
    def Read(self, caller):
        Old_Point=PointClass(0,0)
        #K�rzere Namen zuweisen
        lp=caller.line_pairs
        e=lp.index_code(0,caller.start+1)
        
        #Layer zuweisen
        s=lp.index_code(8,caller.start+1)
        self.Layer_Nr=caller.Get_Layer_Nr(lp.line_pair[s].value)

        #Pa=None f�r den ersten Punkt
        Pa=None
        
        #Number of vertices
        s=lp.index_code(90,s+1,e)
        NoOfVert=int(lp.line_pair[s].value)
        
        #Polyline flag (bit-coded); default is 0; 1 = Closed; 128 = Plinegen
        s=lp.index_code(70,s+1,e)
        LWPLClosed=int(lp.line_pair[s].value)
        #print LWPLClosed
        
        s=lp.index_code(10,s+1,e)
        while 1:
            #XWert
            if s==None:
                break
            
            x=float(lp.line_pair[s].value)
            #YWert
            s=lp.index_code(20,s+1,e)
            y=float(lp.line_pair[s].value)
            Pe=PointClass(x=x,y=y)
        
            #Bulge
            bulge=0
            
            s_nxt_x=lp.index_code(10,s+1,e)
            e_nxt_b=s_nxt_x
            
            #Wenn am Ende dann Suche bis zum Ende
            if e_nxt_b==None:
                e_nxt_b=e
            
            s_bulge=lp.index_code(42,s+1,e_nxt_b)
            
            #print('stemp: %s, e: %s, next 10: %s' %(s_temp,e,lp.index_code(10,s+1,e)))
            if s_bulge!=None:
                bulge=float(lp.line_pair[s_bulge].value)
                s_nxt_x=s_nxt_x
            
            #�bernehmen des n�chsten X Wert als Startwert
            s=s_nxt_x
                
           #Zuweisen der Geometrien f�r die Polyline
        
            if not(type(Pa)==type(None)):
                if next_bulge==0:
                    self.geo.append(LineGeo(Pa=Pa,Pe=Pe))
                else:
                    #self.geo.append(LineGeo(Pa=Pa,Pe=Pe))
                    #print bulge
                    self.geo.append(self.bulge2arc(Pa,Pe,next_bulge))             
                    
            #Der Bulge wird immer f�r den und den n�chsten Punkt angegeben
            next_bulge=bulge
            Pa=Pe 

                   
        if (LWPLClosed==1):
            #print("sollten �bereinstimmen: %s, %s" %(Pa,Pe))
            if next_bulge:
                self.geo.append(self.bulge2arc(Pa,self.geo[0].Pa,next_bulge))
            else:
                self.geo.append(LineGeo(Pa=Pa,Pe=self.geo[0].Pa))
                       
        #Neuen Startwert f�r die n�chste Geometrie zur�ckgeben        
        caller.start=e

    def get_start_end_points(self,direction=0):
        if not(direction):
            punkt, angle=self.geo[0].get_start_end_points(direction)
        elif direction:
            punkt, angle=self.geo[-1].get_start_end_points(direction)
        return punkt,angle
    
    def bulge2arc(self,Pa,Pe,bulge):
        c=(1/bulge-bulge)/2
        
        #Berechnung des Mittelpunkts (Formel von Mickes!
        O=PointClass(x=(Pa.x+Pe.x-(Pe.y-Pa.y)*c)/2,\
                     y=(Pa.y+Pe.y+(Pe.x-Pa.x)*c)/2)
                    
        #Abstand zwischen dem Mittelpunkt und PA ist der Radius
        r=O.distance(Pa)
        #Kontrolle ob beide gleich sind (passt ...)
        #r=O.distance(Pe)

        #Unterscheidung f�r den �ffnungswinkel.
        if bulge>0:
            return ArcGeo(Pa=Pa,Pe=Pe,O=O,r=r)  
        else:
            arc=ArcGeo(Pa=Pe,Pe=Pa,O=O,r=r)
            arc.reverse()
            return arc