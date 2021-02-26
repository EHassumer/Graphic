# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020


from vec3d import Vec3d
from mat3d import Mat3d
from OpenGL.GL import *
import math
import random

class Cube():
     def __init__(self):
      
        self.vertices =[
             Vec3d(-1.0,  1.0, -1.0, 1.0),#a
             Vec3d( 1.0,  1.0, -1.0, 1.0),#b
             Vec3d( 1.0, -1.0, -1.0, 1.0),#c
             Vec3d(-1.0, -1.0, -1.0, 1.0),#d
             Vec3d(-1.0,  1.0,  1.0, 1.0),#e
             Vec3d( 1.0,  1.0,  1.0, 1.0),#f
             Vec3d( 1.0, -1.0,  1.0, 1.0),#g
             Vec3d(-1.0, -1.0,  1.0, 1.0)]#h
                         
                         
                         
                         
        self.faces = [
            [1, 2, 3, 4],#arka abcd
            [5, 6, 7, 8],#ön  efgh
            [1, 2, 6, 5],#üst abfe
            [2, 6, 7, 3],#sol  bfgc
            [4, 3, 7, 8],#alt dcgh
            [1, 5, 8, 4]]#sağ  aehd
      
        


     def draw(self):
           i=0
           faceColors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0]]
           for face in self.faces:
            glBegin(GL_QUADS)
            color = faceColors[i]
            glColor3f(color[0], color[1], color[2])
            i=(i+1)%6
            for vertexIndex in face:
                vertex = self.vertices[vertexIndex-1]
                glVertex3f(vertex.x, vertex.y, vertex.z)
            glEnd()
          
     def subdivision(self, number):
         faceColors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0]]
         lenght=math.sqrt((self.vertices[1].x - self.vertices[0].x)**2 + (self.vertices[1].y - self.vertices[0].y)**2)
         lenght=lenght/number
         #arka
         firstX=self.vertices[self.faces[0][0]-1].x
         firstY=self.vertices[self.faces[0][0]-1].y
         
         for j in range(number):
             
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(firstX , firstY, -1)
                 glVertex3f(firstX + lenght, firstY,-1)
                 glVertex3f(firstX + lenght, firstY - lenght,-1)
                 glVertex3f(firstX , firstY - lenght,-1)
                 
                 glEnd()
                 
                 firstX=firstX+lenght
             
             firstX=self.vertices[self.faces[0][0]-1].x
             firstY=firstY-lenght
             
         #ön
         firstX=self.vertices[self.faces[1][0]-1].x
         firstY=self.vertices[self.faces[1][0]-1].y
    
         for j in range(number):
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(firstX , firstY,1)
                 glVertex3f(firstX + lenght, firstY,1)
                 glVertex3f(firstX + lenght, firstY - lenght,1)
                 glVertex3f(firstX , firstY - lenght,1)
                 glEnd()
                 
                 firstX=firstX+lenght
             firstX=self.vertices[self.faces[1][0]-1].x
             firstY=firstY-lenght
         #üst   
         firstX=self.vertices[self.faces[2][0]-1].x
         firstZ=self.vertices[self.faces[2][0]-1].z
         
         for j in range(number):
             
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(firstX , 1, firstZ)
                 glVertex3f(firstX + lenght, 1,firstZ)
                 glVertex3f(firstX + lenght, 1,firstZ+lenght)
                 glVertex3f(firstX , 1,firstZ+lenght)
                 
                 glEnd()
                 
                 firstX=firstX+lenght
             
             firstX=self.vertices[self.faces[4][0]-1].x
             firstZ=firstZ+lenght
         #alt
         firstX=self.vertices[self.faces[4][0]-1].x
         firstZ=self.vertices[self.faces[4][0]-1].z
         
         for j in range(number):
             
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(firstX , -1, firstZ)
                 glVertex3f(firstX + lenght, -1,firstZ)
                 glVertex3f(firstX + lenght, -1,firstZ+lenght)
                 glVertex3f(firstX , -1,firstZ+lenght)
                 
                 glEnd()
                 
                 firstX=firstX+lenght
             
             firstX=self.vertices[self.faces[4][0]-1].x
             firstZ=firstZ+lenght
             
         #sağ
         firstY=self.vertices[self.faces[5][0]-1].y
         firstZ=self.vertices[self.faces[5][0]-1].z
         
         for j in range(number):
             
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(1 , firstY, firstZ)
                 glVertex3f(1, firstY-lenght,firstZ)
                 glVertex3f(1, firstY-lenght,firstZ+lenght)
                 glVertex3f(1, firstY,firstZ+lenght)
                 
                 glEnd()
                 
                 firstY=firstY-lenght
             
             firstY=self.vertices[self.faces[5][0]-1].y
             firstZ=firstZ+lenght
                
        
         #sol
         firstY=self.vertices[self.faces[3][0]-1].y
         firstZ=self.vertices[self.faces[3][0]-1].z
         
         for j in range(number):
             
             for i in range(number):
                 k=random.randint(0, 6)
                 glBegin(GL_QUADS)
                 color = faceColors[k]
                 glColor3f(color[0], color[1], color[2])
                 glVertex3f(-1 , firstY, firstZ)
                 glVertex3f(-1, firstY-lenght,firstZ)
                 glVertex3f(-1, firstY-lenght,firstZ+lenght)
                 glVertex3f(-1, firstY,firstZ+lenght)
                 
                 glEnd()
                 
                 firstY=firstY-lenght
             
             firstY=self.vertices[self.faces[3][0]-1].y
             firstZ=firstZ+lenght
      
    	    
         
         
         
         
         
         
         
         
         
         
         