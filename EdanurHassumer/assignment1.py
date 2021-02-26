# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# November 2020


# Note:
# -----
# This Uses PyOpenGL and PyOpenGL_accelerate packages.  It also uses GLUT for UI.
# To get proper GLUT support on linux don't forget to install python-opengl package using apt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import Vec3d
from mat3d import Mat3d
from objects import Objects
import sys

import time


# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Shapes

triangle = Objects()   #Object creation
triangle.addVertices(Vec3d(0.0, 1.0, 0.0, 1.0))		       #Vertices	
triangle.addVertices(Vec3d(1.0, -1.0, 0.0, 1.0))
triangle.addVertices(Vec3d(-1.0, -1.0, 0.0, 1.0))			

triangle.addMatrixs(Mat3d.translationMatrix(0.0, -1.0, 0.0)) #MatrixStack           		
triangle.addMatrixs(Mat3d.rotationByZMatrix(0.003))	                  
triangle.addMatrixs(Mat3d.translationMatrix(0.0, 1.0, 0.0))		           
	               
	                 

square = Objects()     #Object creation
square.addVertices(Vec3d(-1.0, 1.0, 0.0, 1.0))   #Vertices
square.addVertices(Vec3d(1.0, 1.0, 0.0, 1.0))	
square.addVertices(Vec3d(1.0, -1.0, 0.0, 1.0))	
square.addVertices(Vec3d(-1.0, -1.0, 0.0, 1.0))				      
	            
square.addMatrixs(Mat3d.translationMatrix(1.0, -1.0, 0.0))   #MatrixStack
square.addMatrixs(Mat3d.rotationByZMatrix(0.002))
square.addMatrixs( Mat3d.translationMatrix(-1.0, 1.0, 0.0))

	            
# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScene():
   
    update=1.0/60
    first=time.time()
    
    global triangle, square
  
    # update shape positions
    triangle.multiplyMatrixsToVertices()
    square.multiplyMatrixsToVertices()

    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()					# Reset The View 

    # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(-1.5, 0.0, -6.0)



# Since we have smooth color mode on, this will be great for the Phish Heads :-).
# Draw a triangle
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[0].z)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[1].z)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(triangle.vertices[2].x, triangle.vertices[2].y, triangle.vertices[2].z)
    glEnd()


# End of triangle

# Move Right 1.5 units.
    glTranslatef(3.0, 0.0, 0.0)


# Draw a square (quadrilateral)
    glColor3f(0.3, 0.5, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(square.vertices[0].x, square.vertices[0].y, square.vertices[0].z)          
    glVertex3f(square.vertices[1].x, square.vertices[1].y, square.vertices[1].z)
    glVertex3f(square.vertices[2].x, square.vertices[2].y, square.vertices[2].z)
    glVertex3f(square.vertices[3].x, square.vertices[3].y, square.vertices[3].z)
    glEnd()


    second=time.time()
    elapseTime=second-first
    #to update the screen in equal periods
    if(update > elapseTime):
        time.sleep(update - elapseTime)
    else:
       time.sleep(update - (elapseTime % update))
      

#  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()

def main():
	global window
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	glutInitWindowSize(640, 480)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("CENG487 Assignment1 -Edanur Hassumer")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc(DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
	
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)

	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)

	# Initialize our window. 
	InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print ("Hit ESC key to quit.")
main()
