# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020

#https://github.com/cgibson/python-subdiv/blob/master/mesh.py     
from vec3d import Vec3d
from mat3d import Mat3d
from OpenGL.GL import *
import math
import random
import numpy as np

class Objects():
     def __init__(self):
      
        self.vertices =[]
        self.quads =[]
        self.index =[]
        self.faces = []
        self.divided=[]
        
        
             
     def levelUp(self,number):
        print("Level-"+str(number))
     
        for i in range(number):
            self.subdivide()
            
     def render(self,num):
        if(num==1):
            self.draw()
        if(num==2):
            self.draw2()       
         
                  
     def draw(self):
           i=0
           faceColors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0]]
           
           for face in self.quads:
               glBegin(GL_QUADS)
               color = faceColors[i]
               glColor3f(color[0], color[1], color[2])
               i=(i+1)%6
               for vertexIndex in face:
                   vertex = self.vertices[vertexIndex]
                   glVertex3f(vertex.x, vertex.y, vertex.z)
               glEnd()
              
            
            
            
     def draw2(self):
      
         
         
         for face in self.quads:
             
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[0]].x , self.vertices[face[0]].y, self.vertices[face[0]].z)
             glVertex3f(self.vertices[face[1]].x , self.vertices[face[1]].y, self.vertices[face[1]].z)
             glEnd()
             
             glBegin(GL_LINES)          
             glVertex3f(self.vertices[face[1]].x , self.vertices[face[1]].y, self.vertices[face[1]].z)
             glVertex3f(self.vertices[face[2]].x , self.vertices[face[2]].y, self.vertices[face[2]].z)
             glEnd()
             
         
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[2]].x , self.vertices[face[2]].y, self.vertices[face[2]].z)
             glVertex3f(self.vertices[face[3]].x , self.vertices[face[3]].y, self.vertices[face[3]].z)
             glEnd()
         
             glBegin(GL_LINES)
             glVertex3f(self.vertices[face[3]].x , self.vertices[face[3]].y, self.vertices[face[3]].z)
             glVertex3f(self.vertices[face[0]].x , self.vertices[face[0]].y, self.vertices[face[0]].z)
             glEnd()
         
    
        
            
        
     """mesh"""
     def addVertex(self, v):
        self.vertices.append(v)
        return len(self.vertices) - 1

     # Add a quad to the mesh
     def addQuad(self, v1, v2, v3, v4):

        for idx in [v1,v2,v3,v4]:
            if idx > len(self.vertices):
                raise ValueError("idx %s is out-of-bounds (> %s)" % (idx,len(self.vertices)))

        self.quads.append([v1, v2, v3, v4])
        return len(self.quads) - 1
     # Return the average of the given indices
     def midpoint(self, *indices):
        mpoint = Vec3d(0, 0, 0, 0)
        for idx in indices:
            mpoint = mpoint.add(self.vertices[idx])

        return mpoint.div_f(len(indices))

     # Find all faces that contain the given indices
     def quadsContain(self, *indices):
        connected = []

        # For every quad
        for curQuad, quadVerts in enumerate(self.quads, 0):

            # If every indice exists in the quad, add it to our list
            for idx in indices:
                if not idx in quadVerts:
                    break
            else:
                connected.append(curQuad)

        return connected

     # Return any vertices that are connected via edge to the given vertId
     def connectedVerts(self, vertIdx):
        connectedVertIndices = []

        # For every quad in the mesh
        for quadVerts in self.quads:
            polySize = len(quadVerts)

            # If the vertexId exists in the quad
            if vertIdx in quadVerts:

                # Find those in the quad loop on each side
                quadIdx = quadVerts.index(vertIdx)
                connectedVertIndices.append(quadVerts[(quadIdx-1) % polySize])
                connectedVertIndices.append(quadVerts[(quadIdx+1) % polySize])

        # Return only unique results (we don't care about order)
        return list(set(connectedVertIndices))

     # Subdivide the current mesh by one level
     def subdivide(self):

        # A list of the new quads we will be creating. We will replace the old quads
        # with these when we're done
        newQuads = []

        # These data-structures will hold the intermediary vertices for edge midpoints
        # and face centers. We will need ready access to these after we generate them
        edgeMids = {}
        quadCtrList = []

        oldVertexCount = len(self.vertices)

        # STEP ONE: Generate face points
        # -----------------------------------------------------------
        for quadVerts in self.quads:
            polyCount = len(quadVerts)
            # create the center point
            ctr = Vec3d(0, 0, 0 ,0)
            for idx in quadVerts:
                ctr = ctr.add(self.vertices[idx])
            ctr = ctr.div_f(polyCount)

            centerIdx = self.addVertex(ctr)

            quadCtrList.append(centerIdx)

        # STEP TWO: Generate edge points
        # -----------------------------------------------------------
        for curQuad, quadVerts in enumerate(self.quads, 0):
            polyCount = len(quadVerts)

            # create center points for every edge
            for quadIdx in range(polyCount):

                idx = quadVerts[quadIdx]
                idx2 = quadVerts[(quadIdx+1) % polyCount]

                # For sanity/indexing sake, we always want idx < idx2
                if idx > idx2:
                    tmp = idx
                    idx = idx2
                    idx2 = tmp

                # if we don't have an entry, add one
                if not idx in edgeMids.keys():
                    edgeMids[idx] = {}

                # if we haven't already created this edge midpoint while working
                # on another quad, then build it
                if not idx2 in edgeMids[idx]:

                    # The new edge midpoints will be an average of the terminal vertices as well
                    # as the new face points in the quads this edge straddles

                    # First, find those quads
                    connectedQuads = self.quadsContain(idx, idx2)
                    assert len(connectedQuads) == 2

                    avg = self.midpoint(idx, idx2, quadCtrList[connectedQuads[0]], quadCtrList[connectedQuads[1]])

                    edgeMids[idx][idx2] = self.addVertex(avg)

        # STEP THREE: Modify the existing vertices
        # -----------------------------------------------------------
        for idx in range(oldVertexCount):

                # Modify original edge point according to complex system. Mark it as done
                connectedQuads = self.quadsContain(idx)
                n = float(len(connectedQuads))

                # M1: Generate old coord weight
                m1 = self.vertices[idx]

                # M2: Generate average face points weight
                m2 = self.midpoint(*[quadCtrList[quadIdx] for quadIdx in connectedQuads])

                # M3: Generate average edge points weight
                connectedVertIndices = self.connectedVerts(idx)
                connectedEdgeMids = []

                # Given all vertices that have edges connecting to this current vertex,
                # find and average all of the midpoints
                for connectedVertIdx in connectedVertIndices:

                    # Again, index using the smaller vert index value first
                    if idx < connectedVertIdx:
                        cIdx1 = idx
                        cIdx2 = connectedVertIdx
                    else:
                        cIdx1 = connectedVertIdx
                        cIdx2 = idx

                    connectedEdgeMids.append(edgeMids[cIdx1][cIdx2])

                m3 = self.midpoint(*connectedEdgeMids)

                # Weights (for easy modification)
                # There are many methods of weighing the various elements

                # Technique 1
                w1 = (n - 3.0) / n
                w2 = 1.0 / n
                w3 = 2.0 / n

                # Technique 2
                #w1 = (n - 2.5) / n
                #w2 = 1.0 / n
                #w3 = 1.5 / n

                # Technique 3
                #w1 = ((4.0 * n) - 7.0) / (4.0 * n)
                #w2 = 1.0 / (4.0 * (n * n))
                #w3 = 1.0 / (2.0 * (n * n))

                m1 = m1.mul_f(w1)
                m2 = m2.mul_f(w2)
                m3 = m3.mul_f(w3)

                self.vertices[idx] = m1.add(m2).add(m3)

        # STEP FOUR: Create new quads
        # -----------------------------------------------------------
        for curQuad, quadVerts in enumerate(self.quads, 0):
            polyCount = len(quadVerts)

            # create four new quads in the new quad data-structure
            for quadIdx in range(len(quadVerts)):
                idx0 = quadVerts[(quadIdx-1) % polyCount]
                idx1 = quadVerts[quadIdx]
                idx2 = quadVerts[(quadIdx+1) % polyCount]

                if idx0 < idx1:
                    mpoint1 = edgeMids[idx0][idx1]
                else:
                    mpoint1 = edgeMids[idx1][idx0]

                if idx1 < idx2:
                    mpoint2 = edgeMids[idx1][idx2]
                else:
                    mpoint2 = edgeMids[idx2][idx1]

                centerIdx = quadCtrList[curQuad]

                newQuads.append([centerIdx, mpoint1, idx1, mpoint2])

        # STEP FIVE: Rebuild quads
        # -----------------------------------------------------------
        self.quads = []

        for quad in newQuads:
            self.addQuad(*quad)
   
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
       
        
       
        