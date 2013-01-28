#!/usr/bin/python
# -*- coding: cp1252 -*-
#
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

from Core.Point import Point

import logging
logger=logging.getLogger("Core.EntitieContent")

class EntitieContentClass:
    def __init__(self,type="Entitie",Nr=None,Name='',parent=None,children=[],
                p0=Point(x=0.0,y=0.0),pb=Point(x=0.0,y=0.0),sca=[1,1,1],rot=0.0):
        
        self.type=type
        self.Nr=Nr
        self.Name=Name
        self.children=children
        self.p0=p0
        self.pb=pb
        self.sca=sca
        self.rot=rot
        self.parent=parent
    
    def __cmp__(self, other):
        return cmp(self.EntNr, other.EntNr)
    
    def __str__(self):
        return ('\ntype:        %s' %self.type) +\
               ('\nNr :      %i' %self.Nr) +\
               ('\nName:     %s' %self.Name)+\
               ('\np0:          %s' %self.p0)+\
               ('\npb:          %s' %self.pb)+\
               ('\nsca:         %s' %self.sca)+\
               ('\nrot:         %s' %self.rot)+\
               ('\nchildren:    %s' %self.children)
    
    #Hinzufuegen der Kontur zu den Entities
    #Add the contour of the Entities
    def addchild(self,child):
        self.children.append(child)

