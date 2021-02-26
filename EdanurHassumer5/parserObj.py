# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020

#https://github.com/feyil/CENG487/blob/master/parsers/ObjParser.py

from objects import Objects
from vec3d import Vec3d

class ParserObj():
    # Will create a shape object at the end of parse operation
    def __init__(self, fileName):
        self.fileName = fileName
        

    def parse(self):
        # returns shape object
        obje=Objects()
       
        objFile = open(self.fileName)

        for line in objFile:
            splitedLine = line.split()
            
            if(len(splitedLine) != 0 and splitedLine[0] != '#'):
                definition = splitedLine[0]
                
                if(definition == 'v'):
                        obje.vertices.append(Vec3d(float(splitedLine[1]), float(splitedLine[2]), float(splitedLine[3]),0))
                        
                elif(definition == 'f'):

                    index = []
                    for i in splitedLine[1:]:
                        index.append(int(i)-1)
                    obje.quads.append(index)
        return obje
        

    def parseMulti(self):
        objFile = open(self.fileName)

        shapeList = []
        vertexCount = 0

        shape = Objects()
        shape.name=("ShortBox")

        for line in objFile:
            splitedLine = line.split()

            if(len(splitedLine) != 0 and splitedLine[0] != '#'):
                definition = splitedLine[0]

                if(definition == 'g' and splitedLine[1] == 'default'):
                    #Start for an object creation
                    shape = Objects()
                elif(definition == 'v'):
                     shape.vertices.append(Vec3d(float(splitedLine[1]), float(splitedLine[2]), float(splitedLine[3]),0))
                     vertexCount += 1
                elif(definition =='f'):
                    shapeFace = []
                    for i in splitedLine[1:]:
                        shapeFace.append((int(i) - 1) - vertexCount)
                    shape.quads.append(shapeFace)
                elif(definition == 'g' and splitedLine[1] != 'default'):
                    shape.name=(splitedLine[1])
            elif(len(splitedLine) == 0 and shape != None ):
                shapeList.append(shape)
           
        shapeList.append(shape)

        return shapeList
 