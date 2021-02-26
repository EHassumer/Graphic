# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020


#https://stackoverflow.com/questions/7687148/drawing-sphere-in-opengl-without-using-glusphere

import math
from vec3d import Vec3d
from OpenGL.GL import *
import random
class Sphere():
    
    def create(self):
        for i in range(self.y_segment+1):
            angle_y=(math.pi*i) / self.y_segment
            angle_y=(angle_y*math.pi) /180
            y=math.cos(angle_y)
            xz=math.sin(angle_y)
            
            for j in range(self.x_segment+1):
                angle_x=(2*math.pi*j) / self.x_segment
                angle_x=(angle_x*math.pi) /180
                x=xz*math.cos(angle_x)
                z=xz*math.sin(angle_x)
                vector=Vec3d(x,y,z,0)
                self.vertices[i*(self.x_segment+1)+j]=vector
                self.vertices.insert(i*(self.x_segment+1)+j,vector)
    def draw(self):
        
            for vertex in self.vertices:
                glBegin(GL_POINTS)
                glColor3f(1.0, 1.0, 0.0)
                glVertex3f(vertex.x, vertex.y, vertex.z)
            glEnd()
    def subdivision(self,number):
        faceColors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0]]
        stackCount = number*4
        sectorCount = number*4
        r = 1
        for i in range(stackCount+1):
            lat0 = math.pi * (-0.5 + (i - 1) / stackCount)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)
            lat1 = math.pi * (-0.5 + i / stackCount)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)
            
            glBegin(GL_QUAD_STRIP)
            k=random.randint(0, 6)
            color = faceColors[k]
            glColor3f(color[0], color[1], color[2])
            for j in range(sectorCount+1):
                lng = 2* math.pi * (j-1) / sectorCount
                x = math.cos(lng)
                y = math.sin(lng)
                
                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(r * x * zr0, r * y * zr0, r * z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(r * x * zr1, r * y * zr1, r * z1)
            glEnd()