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
                    obje.faces.append([int(splitedLine[1]), int(splitedLine[2]),int(splitedLine[3]),int(splitedLine[4])])
                    
                elif(definition == 'f'):
                    face = []
                    for i in splitedLine[1:]:
                        face.append(int(i))
                    obje.faces.append(face)
        return obje
        

