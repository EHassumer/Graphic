# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020

from vec3d import Vec3d
from mat3d import Mat3d
import math
class Camera():
    
    def __init__(self):
        self.cameraPos=Vec3d(0.0,0.0,12.0,0.0)
        self.cameraTarget=Vec3d(0.0,0.0,0.0,0.0)
        self.up=Vec3d(0.0,1.0,0.0,1.0)
        self.cameraFront=Vec3d(0.0,0.0,-1.0,0.0)
        self.cameraDirection=self.cameraPos.subtraction(self.cameraTarget).normalize()
        self.cameraRight=self.up.crossProduct(self.cameraDirection).normalize()
        self.cameraUp=self.cameraDirection.crossProduct(self.cameraRight)
        
              
    
        
    def updateUp(self,angle):
        rotation=self.rotationMatrix(angle, self.cameraUp)
        self.cameraPos=rotation.multiplicationMatrixAndVector(self.cameraPos)
        self.cameraFront=rotation.multiplicationMatrixAndVector(self.cameraFront)
        self.cameraTarget=self.cameraFront.add(self.cameraPos)
        self.cameraDirection=self.cameraPos.subtraction(self.cameraTarget).normalize()
        self.cameraRight=self.cameraUp.crossProduct(self.cameraDirection).normalize()
        self.cameraUp=self.cameraDirection.crossProduct(self.cameraRight)
    def updateRight(self,angle):
        rotation=self.rotationMatrix(angle, self.cameraRight)
        self.cameraPos=rotation.multiplicationMatrixAndVector(self.cameraPos)
        self.cameraFront=rotation.multiplicationMatrixAndVector(self.cameraFront)
        self.cameraTarget=self.cameraFront.add(self.cameraPos)
        self.cameraDirection=self.cameraPos.subtraction(self.cameraTarget).normalize()
        self.cameraRight=self.cameraUp.crossProduct(self.cameraDirection).normalize()
        self.cameraUp=self.cameraDirection.crossProduct(self.cameraRight)
    
    def rotationMatrix(self,angle,translateVector):
        rad=angle*math.pi/180
        cosinus = math.cos(rad)
        sinus = math.sin(rad)
        translateVector = translateVector.normalize()
        x2 = translateVector.x * translateVector.x
        y2 = translateVector.y * translateVector.y
        z2 = translateVector.z * translateVector.z
        xy = translateVector.x * translateVector.y
        yz = translateVector.y * translateVector.z
        xz = translateVector.x * translateVector.z
        
        return Mat3d([Vec3d(cosinus + x2*(1-cosinus), xy*(1-cosinus) - translateVector.z*sinus, xz*(1-cosinus) + translateVector.y*sinus, 0),
                      Vec3d(xy*(1-cosinus) + translateVector.z*sinus, cosinus + y2*(1-cosinus), yz*(1-cosinus)- translateVector.x*sinus, 0),
                      Vec3d(xz*(1-cosinus) - translateVector.y*sinus, yz*(1-cosinus) + translateVector.x*sinus, cosinus + z2*(1-cosinus), 0),
                      Vec3d(0, 0, 0, 0)])
    
    
    
    
    
    
    
    
    
    
    
    