# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# November 2020

import math

class Vec3d():
    
     def __init__(self, x, y, z, w):
         self.x = x
         self.y = y
         self.z = z
         self.w = w
        
     def dotProduct(self,vector3d):
         return self.x * vector3d.x + self.y * vector3d.y + self.z * vector3d.z + self.w * vector3d.w
         
     def crossProduct(self, vector3d):
         return Vec3d(self.y * vector3d.z - self.z * vector3d.y, 
                      self.z * vector3d.x - self.x * vector3d.z, 
                      self.x * vector3d.y - self.y * vector3d.x, 0)
          
    
     def projection(self,basisVector):
         result=self.lengthOfVector()* math.cos(self.angleRadyan(basisVector)) 
         basisVector.scalarMulti(result/ basisVector.lengthOfVector())
         return  basisVector
    
     def angleDegree(self, vector3d):
         return (180/math.pi) * math.acos(self.dotProduct(vector3d) / (self.lengthOfVector() * vector3d.lengthOfVector()))
     
     def angleRadyan(self, vector3d):
         return  math.acos(self.dotProduct(vector3d) / (self.lengthOfVector() * vector3d.lengthOfVector()))
    
     def addition(self, vector3d):
         self.x += vector3d.x
         self.y += vector3d.y
         self.z += vector3d.z
        
     def scalarMulti(self, k):
         self.x *=k
         self.y *=k
         self.z *=k
        
     def lengthOfVector(self):
         return math.sqrt(self.x**2 + self.y**2 + self.z**2)
           

    


