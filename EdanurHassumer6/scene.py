class Scene:
	def __init__(self):
		self.nodes = []

	def add(self, node):
		self.nodes.append(node)

	def getVertex(self):
		totalList=[]
		for i in self.nodes:
				vertexlist=i.vertices
				facelist=i.faces
				for face in facelist:
						for k in face:
								totalList.append(vertexlist[k].x)
								totalList.append(vertexlist[k].y)
								totalList.append(vertexlist[k].z)
								totalList.append(1.0)                                
                                 
		result=totalList
		totalList=[]                                    
		return result
    
    
	def getColor(self):
		totalList=[]
		for i in self.nodes:
				facelist=i.faces
				for face in facelist:
						for k in face:
								totalList.append(0.0)
								totalList.append(0.5)                                
								totalList.append(0.5)                                
								totalList.append(1.0)                               
		                                   
		result=totalList
		totalList=[]                                    
		return result