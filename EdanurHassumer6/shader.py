# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# February 2021

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


class Shader():
    def __init__(self,file,type):
        self.shaderID= glCreateShader(type)
        code =open(file,"r").read()
        glShaderSource(self.shaderID,code)
        glCompileShader(self.shaderID)
        status = None
        glGetShaderiv(self.shaderID, GL_COMPILE_STATUS, status)
        if status == GL_FALSE:
            # Note that getting the error log is much simpler in Python than in C/C++
            # and does not require explicit handling of the string buffer
            strInfoLog = glGetShaderInforLog(shaderID)
            strShaderType = ""
            if shaderType is GL_VERTEX_SHADER:
                strShaderType = "vertex"
            elif shaderType is GL_GEOMETRY_SHADER:
                strShaderType = "geometry"
            elif shaderType is GL_FRAGMENT_SHADER:
                strShaderType = "fragment"

            print(b"Compilation failure for " + strShaderType + b" shader:\n" + strInfoLog)
        

        