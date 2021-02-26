# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# February 2021

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from shader import Shader

class Program:
    def __init__(self): 
        self.vertexShader=None
        self.fragmentShader=None
        self.isLinkProgram=False
        self.programID=glCreateProgram()
        
        
    def createShader(self,fileName,type):
        shader=Shader(fileName,type)
        glAttachShader(self.programID,shader.shaderID)
        if(type== GL_VERTEX_SHADER):
            self.vertexShader=shader
        else:
            self.fragmentShader=shader
            
    def deleteUse(self):
        if not self.isLinkProgram:
            glLinkProgram(self.programID)
            self.isLinkProgram=True
            glDeleteShader(self.vertexShader.shaderID)
            glDeleteShader(self.fragmentShader.shaderID)
            
            
        