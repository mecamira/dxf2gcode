#!/usr/bin/python
# -*- coding: cp1252 -*-
#
#dxf2gcode_b02_point
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


from math import sqrt, sin, cos, atan2, radians, degrees, pi, floor, ceil
from wx.lib.floatcanvas import FloatCanvas
import wx
from wx.lib.expando import ExpandoTextCtrl

class PointClass:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return ('X ->%6.3f  Y ->%6.3f' %(self.x,self.y))
        #return ('CPoints.append(PointClass(x=%6.5f, y=%6.5f))' %(self.x,self.y))
    def __cmp__(self, other) : 
      return (self.x == other.x) and (self.y == other.y)
    def __neg__(self):
        return -1.0*self
    def __add__(self, other): # add to another point
        return PointClass(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return self + -other
    def __rmul__(self, other):
        return PointClass(other * self.x,  other * self.y)
    def __mul__(self, other):
        if type(other)==list:
            #Skalieren des Punkts
            return PointClass(x=self.x*other[0],y=self.y*other[1])
        else:
            #Skalarprodukt errechnen
            return self.x*other.x + self.y*other.y

    def unit_vector(self,Pto=None):
        diffVec=Pto-self
        l=diffVec.distance()
        return PointClass(diffVec.x/l,diffVec.y/l)
    def distance(self,other=None):
        if type(other)==type(None):
            other=PointClass(x=0.0,y=0.0)
        return sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2))
    def norm_angle(self,other=None):
        if type(other)==type(None):
            other=PointClass(x=0.0,y=0.0)
        return atan2(other.y-self.y,other.x-self.x)
    def isintol(self,other,tol):
        return (abs(self.x-other.x)<=tol) & (abs(self.y-other.y)<tol)
    def transform_to_Norm_Coord(self,other,alpha):
        xt=other.x+self.x*cos(alpha)+self.y*sin(alpha)
        yt=other.y+self.x*sin(alpha)+self.y*cos(alpha)
        return PointClass(x=xt,y=yt)
    def get_arc_point(self,ang=0,r=1):
        return PointClass(x=self.x+cos(radians(ang))*r,\
                          y=self.y+sin(radians(ang))*r)

    def Write_GCode(self,parent=None,postpro=None):
        point=self.rot_sca_abs(parent=parent)
        return postpro.rap_pos_xy(point)
    
    def plot2can(self,EntitieContent):
        pass
    
    def triangle_height(self,other1,other2):
        #Die 3 L�ngen des Dreiecks ausrechnen
        a=self.distance(other1)
        b=other1.distance(other2)
        c=self.distance(other2)
        return sqrt(pow(b,2)-pow((pow(c,2)+pow(b,2)-pow(a,2))/(2*c),2))  
      
    def rot_sca_abs(self,sca=None,p0=None,pb=None,rot=None,parent=None):
        if type(sca)==type(None) and type(parent)!=type(None):
            p0=parent.p0
            pb=parent.pb
            sca=parent.sca
            rot=parent.rot
            
            pc=self-pb
            rotx=(pc.x*cos(rot)+pc.y*-sin(rot))*sca[0]
            roty=(pc.x*sin(rot)+pc.y*cos(rot))*sca[1]
            p1= PointClass(x=rotx,y=roty)+p0
            
            #Rekursive Schleife falls selbst eingef�gt
            if type(parent.parent)!=type(None):
                p1=p1.rot_sca_abs(parent=parent.parent)
            
        elif type(parent)==type(None) and type(sca)==type(None):
            p0=PointClass(0,0)
            pb=PointClass(0,0)
            sca=[0,0,0]
            rot=0
            
            pc=self-pb
            rot=rot
            rotx=(pc.x*cos(rot)+pc.y*-sin(rot))*sca[0]
            roty=(pc.x*sin(rot)+pc.y*cos(rot))*sca[1]
            p1= PointClass(x=rotx,y=roty)+p0
        else:
            pc=self-pb
            rot=rot
            rotx=(pc.x*cos(rot)+pc.y*-sin(rot))*sca[0]
            roty=(pc.x*sin(rot)+pc.y*cos(rot))*sca[1]
            p1= PointClass(x=rotx,y=roty)+p0
        
        
#        print(("Self:    %s\n" %self)+\
#                ("P0:      %s\n" %p0)+\
#                ("Pb:      %s\n" %pb)+\
#                ("Pc:      %s\n" %pc)+\
#                ("rot:     %0.1f\n" %degrees(rot))+\
#                ("sca:     %s\n" %sca)+\
#                ("P1:      %s\n\n" %p1))
        
        return p1
      
class PointsClass:
    #Initialisieren der Klasse
    def __init__(self,point_nr=0, geo_nr=0,Layer_Nr=None,be=[],en=[],be_cp=[],en_cp=[]):
        self.point_nr=point_nr
        self.geo_nr=geo_nr
        self.Layer_Nr=Layer_Nr
        self.be=be
        self.en=en
        self.be_cp=be_cp
        self.en_cp=en_cp
        
    
    #Wie die Klasse ausgegeben wird.
    def __str__(self):
        # how to print the object
        return '\npoint_nr ->'+str(self.point_nr)+'\ngeo_nr ->'+str(self.geo_nr) \
               +'\nLayer_Nr ->'+str(self.Layer_Nr)\
               +'\nbe ->'+str(self.be)+'\nen ->'+str(self.en)\
               +'\nbe_cp ->'+str(self.be_cp)+'\nen_cp ->'+str(self.en_cp)

class ContourClass:
    #Initialisieren der Klasse
    def __init__(self,cont_nr=0,closed=0,order=[],length=0):
        self.cont_nr=cont_nr
        self.closed=closed
        self.order=order
        self.length=length
        

    #Komplettes umdrehen der Kontur
    def reverse(self):
        self.order.reverse()
        for i in range(len(self.order)):
            if self.order[i][1]==0:
                self.order[i][1]=1
            else:
                self.order[i][1]=0
        return

    #Ist die klasse geschlossen wenn ja dann 1 zur�ck geben
    def is_contour_closed(self):

        #Immer nur die Letzte �berpr�fen da diese neu ist        
        for j in range(len(self.order)-1):
            if self.order[-1][0]==self.order[j][0]:
                if j==0:
                    self.closed=1
                    return self.closed
                else:
                    self.closed=2
                    return self.closed
        return self.closed


    #Ist die klasse geschlossen wenn ja dann 1 zur�ck geben
    def remove_other_closed_contour(self):
        for i in range(len(self.order)):
            for j in range(i+1,len(self.order)):
                #print '\ni: '+str(i)+'j: '+str(j)
                if self.order[i][0]==self.order[j][0]:
                   self.order=self.order[0:i]
                   break
        return 
    #Berechnen der Zusammengesetzen Kontur L�nge
    def calc_length(self,geos=None):        
        #Falls die beste geschlossen ist und erste Geo == Letze dann entfernen
        if (self.closed==1) & (len(self.order)>1):
            if self.order[0]==self.order[-1]:
                del(self.order[-1])

        self.length=0
        for i in range(len(self.order)):
            self.length+=geos[self.order[i][0]].length
        return


    
    def analyse_and_opt(self,geos=None):
        #Errechnen der L�nge
        self.calc_length(geos)
        
        #Optimierung f�r geschlossene Konturen
        if self.closed==1:
            summe=0
            #Berechnung der Fl�ch nach Gau�-Elling Positive Wert bedeutet CW
            #negativer Wert bedeutet CCW geschlossenes Polygon
            geo_point_l, dummy=geos[self.order[-1][0]].get_start_end_points(self.order[-1][1])            
            for geo_order_nr in range(len(self.order)):
                geo_point, dummy=geos[self.order[geo_order_nr][0]].get_start_end_points(self.order[geo_order_nr][1])
                summe+=(geo_point_l.x*geo_point.y-geo_point.x*geo_point_l.y)/2
                geo_point_l=geo_point
            if summe>0.0:
                self.reverse()

            #Suchen des kleinsten Startpunkts von unten Links X zuerst (Muss neue Schleife sein!)
            min_point=geo_point_l
            min_point_nr=None
            for geo_order_nr in range(len(self.order)):
                geo_point, dummy=geos[self.order[geo_order_nr][0]].get_start_end_points(self.order[geo_order_nr][1])
                #Geringster Abstand nach unten Unten Links
                if (min_point.x+min_point.y)>=(geo_point.x+geo_point.y):
                    min_point=geo_point
                    min_point_nr=geo_order_nr
            #Kontur so anordnen das neuer Startpunkt am Anfang liegt
            self.set_new_startpoint(min_point_nr)
            
        #Optimierung f�r offene Konturen
        else:
            geo_spoint, dummy=geos[self.order[0][0]].get_start_end_points(self.order[0][1])
            geo_epoint, dummy=geos[self.order[0][0]].get_start_end_points(not(self.order[0][1]))
            if (geo_spoint.x+geo_spoint.y)>=(geo_epoint.x+geo_epoint.y):
                self.reverse()


    #Neuen Startpunkt an den Anfang stellen
    def set_new_startpoint(self,st_p):
        self.order=self.order[st_p:len(self.order)]+self.order[0:st_p]
        
    #Wie die Klasse ausgegeben wird.
    def __str__(self):
        # how to print the object
        return '\ncont_nr ->'+str(self.cont_nr)+'\nclosed ->'+str(self.closed) \
               +'\norder ->'+str(self.order)+'\nlength ->'+str(self.length)

class ArcGeo:
    def __init__(self,Pa=None,Pe=None,O=None,r=1,s_ang=None,e_ang=None,dir=1):
        self.type="ArcGeo"
        self.Pa=Pa
        self.Pe=Pe
        self.O=O
        self.r=abs(r)
        self.col='Black'
        self.nva=PointClass(0.0,0.0)	
        self.nve=PointClass(0.0,0.0)	
        
       
        # Kreismittelpunkt bestimmen wenn Pa,Pe,r,und dir bekannt
        if type(O)==type(None):
           
            if (type(Pa)!=type(None)) and (type(Pe)!=type(None)) and (type(dir)!=type(None)):
               
                arc=self.Pe.norm_angle(Pa)-pi/2
                Ve=Pe-Pa
                m=(sqrt(pow(Ve.x, 2)+pow(Ve.y, 2)))/2
                lo=sqrt(pow(r, 2)-pow(m, 2))
                if dir<0:
                    d=-1
                else:
                    d=1
                O=Pa+0.5*Ve
                O.y+=lo*sin(arc)*d
                O.x+=lo*cos(arc)*d
                self.O=O
              
        # Falls nicht �bergeben Mittelpunkt ausrechnen  
            elif (type(s_ang)!=type(None)) and (type(e_ang)!=type(None)):
                O.x=Pa.x-r*cos(s_ang)
                O.y=Pa.y-r*sin(s_ang)
                self.O=O
            else:
                print('Fehlende Angabe f�r Kreis')
                self.O=O
        #Falls nicht �bergeben dann Anfangs- und Endwinkel ausrechen            
        if type(s_ang)==type(None):
            s_ang=O.norm_angle(Pa)
        if type(e_ang)==type(None):
            e_ang=O.norm_angle(Pe)
        
        self.nva.x=sin(s_ang)
        self.nva.y=cos(s_ang)
        self.nva.x=sin(e_ang)
        self.nva.y=cos(e_ang)
        #Falls nicht �bergeben dann Anfangs- und Endwinkel ausrechen            
        if type(s_ang)==type(None):
            s_ang=O.norm_angle(Pa)
        if type(e_ang)==type(None):
            e_ang=O.norm_angle(Pe)

        #Aus dem Vorzeichen von dir den extend ausrechnen
        self.ext=e_ang-s_ang
        if dir>0.0:
            self.ext=self.ext%(-2*pi)
            self.ext-=floor(self.ext/(2*pi))*(2*pi)
        else:
            self.ext=self.ext%(-2*pi)
            self.ext+=ceil(self.ext/(2*pi))*(2*pi)

        #Falls es ein Kreis ist Umfang 2pi einsetzen        
        if self.ext==0.0:
            self.ext=2*pi
                   
        self.s_ang=s_ang
        self.e_ang=e_ang
        self.length=self.r*abs(self.ext)

    def __str__(self):
        return ("\nArcGeo")+\
               ("\nPa : %s; s_ang: %0.5f" %(self.Pa,self.s_ang))+\
               ("\nPe : %s; e_ang: %0.5f" %(self.Pe,self.e_ang))+\
               ("\nO  : %s; r: %0.3f" %(self.O,self.r))+\
               ("\next  : %0.5f; length: %0.5f" %(self.ext,self.length))

    def dif_ang(self, P1, P2, dir):
        sa=self.O.norm_angle(P1)
       
        if(sa<0):
            sa+=2*pi
        
        ea=self.O.norm_angle(P2)
        if(ea<0):
            ea+=2*pi
        
        if(dir>0):     # GU
            if(sa>ea):
                ang=(2*pi-sa+ea)
            else:
                ang=(ea-sa)
        else:
            if(ea>sa):
                ang=(sa+2*pi-ea)
            else:
                ang=(sa-ea)
        
        return(ang)        
        
    def reverse(self):
        Pa=self.Pa
        Pe=self.Pe
        ext=self.ext
        s_ang=self.e_ang
        e_ang=self.s_ang
        
        self.Pa=Pe
        self.Pe=Pa
        self.ext=ext*-1
        self.s_ang=s_ang
        self.e_ang=e_ang
           
    def plot2can(self,EntitieContent):  
                        
        points=[]; hdl=[]
        #Alle 3 Grad ein Segment => 120 Segmente f�r einen Kreis !!
        segments=int((abs(degrees(self.ext))//3)+1)
        
        for i in range(segments+1):    
            ang=self.s_ang+i*self.ext/segments
            p_cur=PointClass(x=(self.O.x+cos(ang)*abs(self.r)),\
                       y=(self.O.y+sin(ang)*abs(self.r)))
                    
            p_cur_rot=p_cur.rot_sca_abs(parent=EntitieContent)

            points.append((p_cur_rot.x,p_cur_rot.y))

        return points

    def get_start_end_points(self,direction,parent=None):
        if not(direction):
            punkt=self.Pa.rot_sca_abs(parent=parent)
            angle=self.rot_angle(degrees(self.s_ang)+90*self.ext/abs(self.ext),parent)
        elif direction:
            punkt=self.Pe.rot_sca_abs(parent=parent)
            angle=self.rot_angle(degrees(self.e_ang)-90*self.ext/abs(self.ext),parent)
        return punkt,angle
    
   
    def rot_angle(self,angle,parent):

        #Rekursive Schleife falls mehrfach verschachtelt.
        if type(parent)!=type(None):
            angle=angle+degrees(parent.rot)
            angle=self.rot_angle(angle,parent.parent)
                
        return angle
    
    def scaleR(self,sR,parent):
        
        #Rekursive Schleife falls mehrfach verschachtelt.
        if type(parent)!=type(None):
            sR=sR*parent.sca[0]
            sR=self.scaleR(sR,parent.parent)
                
        return sR

    def Write_GCode(self,parent=None,postpro=None):
        anf, anf_ang=self.get_start_end_points(0,parent)
        O=self.O.rot_sca_abs(parent=parent)
        IJ=(O-anf)
        ende, en_ang=self.get_start_end_points(1,parent)
        
        s_ang=self.rot_angle(self.s_ang,parent)
        e_ang=self.rot_angle(self.e_ang,parent)
        
        sR=self.scaleR(self.r,parent)

        #Vorsicht geht nicht f�r Ovale
        if (self.ext>0):
            #string=("G3 %s%0.3f %s%0.3f I%0.3f J%0.3f\n" %(axis1,ende.x,axis2,ende.y,IJ.x,IJ.y))
            string=postpro.lin_pol_arc("ccw",anf,ende,s_ang,e_ang,sR,O,IJ)
        elif (self.ext<0) and not(postpro.export_ccw_arcs_only):
            string=postpro.lin_pol_arc("ccw",ende,anf,e_ang,s_ang,sR,O,(O-ende))
        elif postpro.export_ccw_arcs_only:
            #string=("G2 %s%0.3f %s%0.3f I%0.3f J%0.3f\n" %(axis1,ende.x,axis2,ende.y,IJ.x,IJ.y))
            string=postpro.lin_pol_arc("cw",anf,ende,s_ang,e_ang,sR,O,IJ)
        return string  

    
    def MakeTreeText(self,parent):
        
        font1 = wx.Font(8,wx.SWISS, wx.NORMAL, wx.NORMAL)
        textctrl = ExpandoTextCtrl(parent, -1, "", 
                            size=wx.Size(160,55))
                            
        
        textctrl.SetFont(font1)
                                
        #dastyle = wx.TextAttr()
        #dastyle.SetTabs([100, 120])
        #textctrl.SetDefaultStyle(dastyle)
        textctrl.AppendText('Center: X:%0.2f Y%0.2f\n' %(self.O.x, self.O.y))
        textctrl.AppendText('Radius: %0.2f \n' %self.r)
        textctrl.AppendText('Start: %0.1fdeg End: %0.1fdeg' %(degrees(self.s_ang), degrees(self.e_ang)))
        return textctrl

    def makeSelectionStr(self):
    
        return MySelectionStrClass(Name=('Arc'),\
                                    Type=self.type,\
                                    Pa=self.Pa,\
                                    Pe=self.Pe,\
                                    r=self.r)
    
class LineGeo:
    def __init__(self,Pa,Pe):
        self.type="LineGeo"
        self.Pa=Pa
        self.Pe=Pe
        self.col='Black'
        self.length=self.Pa.distance(self.Pe)
        Va=PointClass(0.0,0.0)
         
        Ve=self.Pe-self.Pa            # Richtungsabh�ngiger Normalenvektor
        if (abs(Ve.x)>abs(Ve.y)):
            if(Ve.x>0):
                Va.y=-1
            else:
                Va.y=1
            if(Ve.y!=0):
                Va.x=-Ve.y*Va.y/Ve.x
            else:
                Va.x=0;
        else:
            if(Ve.y>0):
                Va.x=1
            else:
                Va.x=-1
            if(Ve.y!=0):
                Va.y=-Ve.x*Va.x/Ve.y
            else:
                Va.y=0
            
        betrag=Va.distance()
               
        self.nve=1/betrag*Va
        self.nva=self.nve
       
        
    def __str__(self):
        return ("\nLineGeo")+\
               ("\nPa : %s" %self.Pa)+\
               ("\nPe : %s" %self.Pe)+\
               ("\nlength: %0.5f" %self.length)        

    def reverse(self):
        Pa=self.Pa
        Pe=self.Pe
        
        self.Pa=Pe
        self.Pe=Pa

    def reverse_copy(self):
        Pa=self.Pe
        Pe=self.Pa
        return LineGeo(Pa=Pa,Pe=Pe)
        
    def plot2can(self,parent):
        
        anf=self.Pa.rot_sca_abs(parent=parent)
        ende=self.Pe.rot_sca_abs(parent=parent)
        
        return [(anf.x,anf.y),(ende.x,ende.y)]


    def get_start_end_points(self,direction,parent=None):
        if not(direction):
            punkt=self.Pa.rot_sca_abs(parent=parent)
            punkt_e=self.Pe.rot_sca_abs(parent=parent)
            angle=degrees(punkt.norm_angle(punkt_e))
        elif direction:
            punkt_a=self.Pa.rot_sca_abs(parent=parent)
            punkt=self.Pe.rot_sca_abs(parent=parent)
            angle=degrees(punkt.norm_angle(punkt_a))
        return punkt, angle
    
    def Write_GCode(self,parent=None,postpro=None):
        anf, anf_ang=self.get_start_end_points(0,parent)
        ende, end_ang=self.get_start_end_points(1,parent)

        return postpro.lin_pol_xy(anf,ende)
    
    def MakeTreeText(self,parent):
        textctrl = wx.TextCtrl(parent, -1, "", 
                            size=wx.Size(160,60),
                            style=wx.TE_MULTILINE)
                                
        dastyle = wx.TextAttr()
        dastyle.SetTabs([60,80])
        textctrl.SetDefaultStyle(dastyle)
        textctrl.AppendText('Point \tX:\tY:')
        return textctrl
    
    def makeSelectionStr(self):
    
        return MySelectionStrClass(Name=('Line'),\
                                    Type=self.type,\
                                    Pa=self.Pa,\
                                    Pe=self.Pe)
    
    def distance2point(self,point):
        try:
            AE=self.Pa.distance(self.Pe)
            AP=self.Pa.distance(point)
            EP=self.Pe.distance(point)
            AEPA=(AE+AP+EP)/2
            return abs(2*sqrt(abs(AEPA*(AEPA-AE)*(AEPA-AP)*(AEPA-EP)))/AE)
        except:
            return 1e10
            

class BiarcClass:
    def __init__(self,Pa=[],tan_a=[],Pb=[],tan_b=[],min_r=5e-4):
        min_len=1e-9        #Min Abstand f�r doppelten Punkt
        min_alpha=1e-4      #Winkel ab welchem Gerade angenommen wird inr rad
        max_r=5e3           #Max Radius ab welchem Gerade angenommen wird (10m)
        min_r=min_r         #Min Radius ab welchem nichts gemacht wird
        
        self.Pa=Pa
        self.tan_a=tan_a
        self.Pb=Pb
        self.tan_b=tan_b
        self.l=0.0
        self.shape=None
        self.geos=[]
        self.k=0.0

        #Errechnen der Winkel, L�nge und Shape
        norm_angle,self.l=self.calc_normal(self.Pa,self.Pb)

        alpha,beta,self.teta,self.shape=self.calc_diff_angles(norm_angle,\
                                                              self.tan_a,\
                                                              self.tan_b,\
                                                              min_alpha)
        
        if(self.l<min_len):
            self.shape="Zero"
            pass
        
            
        elif(self.shape=="LineGeo"):
            #Erstellen der Geometrie
            self.shape="LineGeo"
            self.geos.append(LineGeo(self.Pa,self.Pb))
        else:
            #Berechnen der Radien, Mittelpunkte, Zwichenpunkt            
            r1, r2=self.calc_r1_r2(self.l,alpha,beta,self.teta)
            
            if (abs(r1)>max_r)or(abs(r2)>max_r):
                #Erstellen der Geometrie
                self.shape="LineGeo"
                self.geos.append(LineGeo(self.Pa,self.Pb))
                return
            
            elif (abs(r1)<min_r)or(abs(r2)<min_r):
                self.shape="Zero"
                return
          
            O1, O2, k =self.calc_O1_O2_k(r1,r2,self.tan_a,self.teta)
            
            #Berechnen der Start und End- Angles f�r das drucken
            s_ang1,e_ang1=self.calc_s_e_ang(self.Pa,O1,k)
            s_ang2,e_ang2=self.calc_s_e_ang(k,O2,self.Pb)

            #Berechnen der Richtung und der Extend
            dir_ang1=(tan_a-s_ang1)%(-2*pi)
            dir_ang1-=ceil(dir_ang1/(pi))*(2*pi)

            dir_ang2=(tan_b-e_ang2)%(-2*pi)
            dir_ang2-=ceil(dir_ang2/(pi))*(2*pi)
            
            
            #Erstellen der Geometrien          
            self.geos.append(ArcGeo(Pa=self.Pa,Pe=k,O=O1,r=r1,\
                                    s_ang=s_ang1,e_ang=e_ang1,dir=dir_ang1))
            self.geos.append(ArcGeo(Pa=k,Pe=self.Pb,O=O2,r=r2,\
                                    s_ang=s_ang2,e_ang=e_ang2,dir=dir_ang2)) 

    def calc_O1_O2_k(self,r1,r2,tan_a,teta):
        #print("r1: %0.3f, r2: %0.3f, tan_a: %0.3f, teta: %0.3f" %(r1,r2,tan_a,teta))
        #print("N1: x: %0.3f, y: %0.3f" %(-sin(tan_a), cos(tan_a)))
        #print("V: x: %0.3f, y: %0.3f" %(-sin(teta+tan_a),cos(teta+tan_a)))

        O1=PointClass(x=self.Pa.x-r1*sin(tan_a),\
                      y=self.Pa.y+r1*cos(tan_a))
        k=PointClass(x=self.Pa.x+r1*(-sin(tan_a)+sin(teta+tan_a)),\
                     y=self.Pa.y+r1*(cos(tan_a)-cos(tan_a+teta)))
        O2=PointClass(x=k.x+r2*(-sin(teta+tan_a)),\
                      y=k.y+r2*(cos(teta+tan_a)))
        return O1, O2, k

    def calc_normal(self,Pa,Pb):
        norm_angle=Pa.norm_angle(Pb)
        l=Pa.distance(Pb)
        return norm_angle, l        

    def calc_diff_angles(self,norm_angle,tan_a,tan_b,min_alpha):
        #print("Norm angle: %0.3f, tan_a: %0.3f, tan_b %0.3f" %(norm_angle,tan_a,tan_b))
        alpha=(norm_angle-tan_a)   
        beta=(tan_b-norm_angle)
        alpha,beta= self.limit_angles(alpha,beta)

        if alpha*beta>0.0:
            shape="C-shaped"
            teta=alpha
        elif abs(alpha-beta)<min_alpha:
            shape="LineGeo"
            teta=alpha
        else:
            shape="S-shaped"
            teta=(3*alpha-beta)/2
            
        return alpha, beta, teta, shape    

    def limit_angles(self,alpha,beta):
        #print("limit_angles: alpha: %s, beta: %s" %(alpha,beta))
        if (alpha<-pi):
           alpha += 2*pi
        if (alpha>pi):
           alpha -= 2*pi
        if (beta<-pi):
           beta += 2*pi
        if (beta>pi):
           beta -= 2*pi
        while (alpha-beta)>pi:
            alpha=alpha-2*pi
        while (alpha-beta)<-pi:
            alpha=alpha+2*pi
        #print("   -->>       alpha: %s, beta: %s" %(alpha,beta))         
        return alpha,beta
            
    def calc_r1_r2(self,l,alpha,beta,teta):
        #print("alpha: %s, beta: %s, teta: %s" %(alpha,beta,teta))
        r1=(l/(2*sin((alpha+beta)/2))*sin((beta-alpha+teta)/2)/sin(teta/2))
        r2=(l/(2*sin((alpha+beta)/2))*sin((2*alpha-teta)/2)/sin((alpha+beta-teta)/2))
        return r1, r2
    
    def calc_s_e_ang(self,P1,O,P2):
        s_ang=O.norm_angle(P1)
        e_ang=O.norm_angle(P2)
        return s_ang, e_ang
    
    def get_biarc_fitting_error(self,Pt):
        #Abfrage in welchem Kreissegment der Punkt liegt:
        w1=self.geos[0].O.norm_angle(Pt)
        if (w1>=min([self.geos[0].s_ang,self.geos[0].e_ang]))and\
           (w1<=max([self.geos[0].s_ang,self.geos[0].e_ang])):
            diff=self.geos[0].O.distance(Pt)-abs(self.geos[0].r)
        else:
            diff=self.geos[1].O.distance(Pt)-abs(self.geos[1].r)
        return abs(diff)
            
    def __str__(self):
        s= ("\nBiarc Shape: %s" %(self.shape))+\
           ("\nPa : %s; Tangent: %0.3f" %(self.Pa,self.tan_a))+\
           ("\nPb : %s; Tangent: %0.3f" %(self.Pb,self.tan_b))+\
           ("\nteta: %0.3f, l: %0.3f" %(self.teta,self.l))
        for geo in self.geos:
            s+=str(geo)
        return s

class MySelectionStrClass:
    def __init__(self,Name=0,Type='',Closed='',Pa='',Pe='',r=''):
        self.Name=Name
        self.Type=Type
        self.Closed=Closed
        self.Pa=Pa
        self.Pe=Pe
        self.r=r
        
    def __str__(self):
        s= ("\nName: %s" %(self.Name))+\
           ("\nType : %s" %(self.Type))+\
           ("\nPa : %s" %(self.Pa))+\
           ("\nPe: %s" %(self.Pe))+\
           ("\nr: %s" %(self.r))
        return s