# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020


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
        

