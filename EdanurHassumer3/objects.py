# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020


from vec3d import Vec3d
from mat3d import Mat3d
from OpenGL.GL import *
import math
import random

class Objects():
     def __init__(self):
      
        self.vertices =[]
        self.faces = []
        self.divided=[]
       
         
     def levelUp(self,number):
        print("Level-"+str(number))
        for i in range(number):
            self.subdivision()
       

     def subdivision(self):
            
             for face in self.faces:
                 centerpointX=0.0
                 centerpointY=0.0
                 centerpointZ=0.0
                 for i in range(4):
                    
                     centerpointX=centerpointX+ self.vertices[face[i]-1].x
                     centerpointY=centerpointY+self.vertices[face[i]-1].y
                     centerpointZ=centerpointZ+self.vertices[face[i]-1].z
                    
                 centerpointX=centerpointX/4
                 centerpointY=centerpointY/4
                 centerpointZ=centerpointZ/4
                 centerpoint=Vec3d(centerpointX,centerpointY,centerpointZ,0.0)
                 
                 midpoint1=Vec3d(self.vertices[face[0]-1].x-(self.vertices[face[0]-1].x-self.vertices[face[1]-1].x)/2,
                                 self.vertices[face[0]-1].y-(self.vertices[face[0]-1].y-self.vertices[face[1]-1].y)/2,
                                 self.vertices[face[0]-1].z-(self.vertices[face[0]-1].z-self.vertices[face[1]-1].z)/2,0)
                 midpoint2=Vec3d(self.vertices[face[1]-1].x-(self.vertices[face[1]-1].x-self.vertices[face[2]-1].x)/2,
                                 self.vertices[face[1]-1].y-(self.vertices[face[1]-1].y-self.vertices[face[2]-1].y)/2,
                                 self.vertices[face[1]-1].z-(self.vertices[face[1]-1].z-self.vertices[face[2]-1].z)/2,0)
                 midpoint3=Vec3d(self.vertices[face[2]-1].x-(self.vertices[face[2]-1].x-self.vertices[face[3]-1].x)/2,
                                 self.vertices[face[2]-1].y-(self.vertices[face[2]-1].y-self.vertices[face[3]-1].y)/2,
                                 self.vertices[face[2]-1].z-(self.vertices[face[2]-1].z-self.vertices[face[3]-1].z)/2,0)
                 midpoint4=Vec3d(self.vertices[face[3]-1].x-(self.vertices[face[3]-1].x-self.vertices[face[0]-1].x)/2,
                                 self.vertices[face[3]-1].y-(self.vertices[face[3]-1].y-self.vertices[face[0]-1].y)/2,
                                 self.vertices[face[3]-1].z-(self.vertices[face[3]-1].z-self.vertices[face[0]-1].z)/2,0)
                 
                 self.divided.append(Vec3d(self.vertices[face[0]-1].x , self.vertices[face[0]-1].y, self.vertices[face[0]-1].z,0.0))
                 self.divided.append(midpoint1)
                 self.divided.append(centerpoint)
                 self.divided.append(midpoint4)
            
                 self.divided.append(midpoint1)
                 self.divided.append(Vec3d(self.vertices[face[1]-1].x , self.vertices[face[1]-1].y, self.vertices[face[1]-1].z,0.0))
                 self.divided.append(midpoint2)
                 self.divided.append(centerpoint)
                 
                 self.divided.append(midpoint4)
                 self.divided.append(centerpoint)
                 self.divided.append(midpoint3)
                 self.divided.append(Vec3d(self.vertices[face[3]-1].x , self.vertices[face[3]-1].y, self.vertices[face[3]-1].z,0.0))
                 
                 self.divided.append(centerpoint)
                 self.divided.append(midpoint2)
                 self.divided.append(Vec3d(self.vertices[face[2]-1].x , self.vertices[face[2]-1].y, self.vertices[face[2]-1].z,0.0))
                 self.divided.append(midpoint3)
            
             self.vertices=self.divided
             self.divided=[]
             size=(len(self.vertices))/4
             newfaces=[]
             for i in range(int(size)):
                     newfaces.append([(i*4)+1,(i*4)+2,(i*4)+3,(i*4)+4,])  
             self.faces=newfaces
             
             
             
             
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
            
            
            
            
     def draw2(self):
      
         
         
         for face in self.faces:
             
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[0]-1].x , self.vertices[face[0]-1].y, self.vertices[face[0]-1].z)
             glVertex3f(self.vertices[face[1]-1].x , self.vertices[face[1]-1].y, self.vertices[face[1]-1].z)
             glEnd()
             
             glBegin(GL_LINES)          
             glVertex3f(self.vertices[face[1]-1].x , self.vertices[face[1]-1].y, self.vertices[face[1]-1].z)
             glVertex3f(self.vertices[face[2]-1].x , self.vertices[face[2]-1].y, self.vertices[face[2]-1].z)
             glEnd()
             
         
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[2]-1].x , self.vertices[face[2]-1].y, self.vertices[face[2]-1].z)
             glVertex3f(self.vertices[face[3]-1].x , self.vertices[face[3]-1].y, self.vertices[face[3]-1].z)
             glEnd()
         
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[3]-1].x , self.vertices[face[3]-1].y, self.vertices[face[3]-1].z)
             glVertex3f(self.vertices[face[0]-1].x , self.vertices[face[0]-1].y, self.vertices[face[0]-1].z)
             glEnd()
         
    
         
     def render(self,num):
        if(num==1):
            self.draw()
        if(num==2):
            self.draw2()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
       
        
       
        