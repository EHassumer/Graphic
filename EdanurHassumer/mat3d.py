# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# November 2020

from vec3d import Vec3d
import math

class Mat3d():

    def __init__(self, matrix):
        self.matrix = matrix
        
    def translationMatrix(x, y, z):
        return Mat3d([Vec3d(1, 0, 0, x),
                      Vec3d(0, 1, 0, y),
                      Vec3d(0, 0, 1, z),
                      Vec3d(0, 0, 0, 1)])
 
    def rotationByXMatrix(rad):
        return Mat3d([Vec3d(1, 0, 0, 0),
                      Vec3d(0, math.cos(rad), -math.sin(rad), 0),
                      Vec3d(0, math.sin(rad), math.cos(rad),  0),
                      Vec3d(0, 0, 0, 1)])

    def rotationByYMatrix(rad):
        return Mat3d([Vec3d(math.cos(rad),  0, math.sin(rad), 0),
                      Vec3d(0, 1, 0, 0),
                      Vec3d(-math.sin(rad), 0, math.cos(rad), 0),
                      Vec3d(0, 0, 0, 1)])

    def rotationByZMatrix(rad):
        return Mat3d([Vec3d(math.cos(rad), -math.sin(rad), 0, 0),
                      Vec3d(math.sin(rad), math.cos(rad),  0, 0),
                      Vec3d(0, 0, 1, 0),
                      Vec3d(0, 0, 0, 1)])

    def scalingMatrix(x, y, z):
        return Mat3d([Vec3d(x, 0, 0, 0),
                      Vec3d(0, y, 0, 0),
                      Vec3d(0, 0, z, 0),
                      Vec3d(0, 0, 0, 1)])
    
    def multiplicationMatrixAndVector(self, vector3d):
        return Vec3d(self.matrix[0].dotProduct(vector3d),
                     self.matrix[1].dotProduct(vector3d),
                     self.matrix[2].dotProduct(vector3d),
                     self.matrix[3].dotProduct(vector3d))
    
    def transposeMatrix(self):
        return Mat3d([Vec3d(self.matrix[0].x, self.matrix[1].x, self.matrix[2].x, self.matrix[3].x),
                      Vec3d(self.matrix[0].y, self.matrix[1].y, self.matrix[2].y, self.matrix[3].y),
                      Vec3d(self.matrix[0].z, self.matrix[1].z, self.matrix[2].z, self.matrix[3].z),
                      Vec3d(self.matrix[0].w, self.matrix[1].w, self.matrix[2].w, self.matrix[3].w)])
    
    def getVec3d(self, num):
        return self.matrix[num]
        
        
        
        
        