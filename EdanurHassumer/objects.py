# CENG 487 Assignment#
# Edanur Hassumer
# StudentId: 240201003
# November 2020
class Objects():
    
    def __init__(self):
        self.vertices=[]
        self.matrixStack=[]
        self.currentvertices=[] #orginal vertices
        
    
    def multiplyMatrixsToVertices(self):
        for matrix in self.matrixStack:
            for i in range(len(self.vertices)):
                 self.vertices[i] = matrix.multiplicationMatrixAndVector(self.vertices[i])
        

    def addVertices(self, vector):
        self.currentvertices.append(vector)
        self.vertices.append(vector)
    
    def addMatrixs(self, matrix):
        self.matrixStack.append(matrix)
        
    
