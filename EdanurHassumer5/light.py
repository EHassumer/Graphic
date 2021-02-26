# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# January 2021
from vec3d import Vec3d
from OpenGL.GL import *

class SpotLight():
    def __init__(self):
        self.ambient=Vec3d(0.0, 0.0, 0.0, 1.0)
        self.diffuse=Vec3d(1.0, 1.0, 1.0, 1.0)
        self.specular=Vec3d(1.0, 1.0, 1.0, 1.0)
        self.lightName='SpotLight'
        self.position= Vec3d(0.0, 48.8, 0.0, 1.0)
        self.direction=Vec3d(0.0, 0.0, -1.0, 0.0)
        self.cutOff=35.0
        
    def draw(self):
        self.createBox()
        
        glLightfv(GL_LIGHT0, GL_AMBIENT, [self.ambient.x,self.ambient.y,self.ambient.z,self.ambient.w])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [self.diffuse.x,self.diffuse.y,self.diffuse.z,self.diffuse.w])
        glLightfv(GL_LIGHT0, GL_SPECULAR,[ self.specular.x,self.specular.y,self.specular.z,self.specular.w])
        glLightfv(GL_LIGHT0, GL_POSITION,[ self.position.x,self.position.y,self.position.z,self.position.w])
        
        # attenuation related
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1) #2
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0) #1
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0) #0.5        
        # spotlight related
        glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, self.cutOff)
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [self.direction.x,self.direction.y,self.direction.z,self.direction.w])
        glLightfv(GL_LIGHT0, GL_SPOT_EXPONENT, 0.0)
        
        glEnable(GL_LIGHT0)
        
        
        
    def drawMove(self,pos,direc,a):
        self.createBoxMove(a)
        
        glLightfv(GL_LIGHT1, GL_AMBIENT, [self.ambient.x,self.ambient.y,self.ambient.z,self.ambient.w])
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [self.diffuse.x,self.diffuse.y,self.diffuse.z,self.diffuse.w])
        glLightfv(GL_LIGHT1, GL_SPECULAR,[ self.specular.x,self.specular.y,self.specular.z,self.specular.w])
        glLightfv(GL_LIGHT1, GL_POSITION,[ pos.x,pos.y,pos.z,pos.w])
        
        # attenuation related
        glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1) #2
        glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.0) #1
        glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.0) #0.5        
        # spotlight related
        glLightfv(GL_LIGHT1, GL_SPOT_CUTOFF, self.cutOff)
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [direc.x,direc.y,direc.z,direc.w])
        glLightfv(GL_LIGHT1, GL_SPOT_EXPONENT, 0.0)
        
        glEnable(GL_LIGHT1)
        
    def createBoxMove(self,a):
         vertices =[
             Vec3d(-0.2,  a, -0.2, 1.0),#a
             Vec3d( 0.2,  a, -0.2, 1.0),#b
             Vec3d( 0.2, a-0.2, -0.2, 1.0),#c
             Vec3d(-0.2, a-0.2, -0.2, 1.0),#d
             Vec3d(-0.2,  a,  0.2, 1.0),#e
             Vec3d( 0.2,  a,  0.2, 1.0),#f
             Vec3d( 0.2, a-0.2,  0.2, 1.0),#g
             Vec3d(-0.2, a-0.2,  0.2, 1.0)]#h
                                         
         faces = [
            [1, 2, 3, 4],#arka abcd
            [5, 6, 7, 8],#ön  efgh
            [1, 2, 6, 5],#üst abfe
            [2, 6, 7, 3],#sol  bfgc
            [4, 3, 7, 8],#alt dcgh
            [1, 5, 8, 4]]#sağ  aehd
        
         for face in faces:
               glBegin(GL_QUADS)
               glMaterialfv(GL_FRONT, GL_EMISSION,[1.0, 1.0, 1.0, 1.0])
               glColor3f(1.0,1.0,1.0)
              
               for vertexIndex in face:
                   vertex =vertices[vertexIndex-1]
                   glVertex3f(vertex.x, vertex.y, vertex.z)
               glEnd()
        
        
    def createBox(self):
         vertices =[
             Vec3d(-1.0,  22.0, -48.0, 1.0),#a
             Vec3d( 1.0,  22.0, -48.0, 1.0),#b
             Vec3d( 1.0, 20.0, -48.0, 1.0),#c
             Vec3d(-1.0, 20.0, -48.0, 1.0),#d
             Vec3d(-1.0,  22.0,  -47.0, 1.0),#e
             Vec3d( 1.0,  22.0,  -47.0, 1.0),#f
             Vec3d( 1.0, 20.0,  -47.0, 1.0),#g
             Vec3d(-1.0, 20.0,  -47.0, 1.0)]#h
     
                    
         faces = [
            [1, 2, 3, 4],#arka abcd
            [5, 6, 7, 8],#ön  efgh
            [1, 2, 6, 5],#üst abfe
            [2, 6, 7, 3],#sol  bfgc
            [4, 3, 7, 8],#alt dcgh
            [1, 5, 8, 4]]#sağ  aehd
        
        
         for face in faces:
               glBegin(GL_QUADS)
               glMaterialfv(GL_FRONT, GL_EMISSION,[1.0, 1.0, 1.0, 1.0])
               glColor3f(1.0,1.0,1.0)
              
               for vertexIndex in face:
                   vertex =vertices[vertexIndex-1]
                   glVertex3f(vertex.x, vertex.y, vertex.z)
               glEnd()
