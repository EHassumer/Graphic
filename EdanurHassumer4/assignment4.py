# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# December 2020


# Note:
# -----
# This Uses PyOpenGL and PyOpenGL_accelerate packages.  It also uses GLUT for UI.
# To get proper GLUT support on linux don't forget to install python-opengl package using apt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import Vec3d
from mat3d import Mat3d
from parserObj import ParserObj
from camera import Camera


import sys
import math

#import time


# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
camera=Camera()
# Number of the glut window.
window = 0

# Shapes
number=0 
num=1
if len(sys.argv)!= 2:
    print("Please enter a file name that format is .obj!\n")
    sys.exit()
    
parser=ParserObj(sys.argv[1])

obje=parser.parse()

print("For increase the division number enter --->  +")   
print("For decrease the division number enter --->  -")    
print("For right enter --->  d or right arrow")
print("For left enter --->  a or left arrow")
print("For up enter --->  w or up arrow")
print("For down enter --->  s or down arrow")
print("For zoom in enter --->  r")
print("For zoom out enter --->  q")
print("For draw with line enter ---> l")
print("For draw with quad enter ---> k")
print("Level-0")
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


    global cube,number, sphere, camera,obje,num

    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()					# Reset The View 
    
    gluLookAt(camera.cameraPos.x,camera.cameraPos.y,camera.cameraPos.z,
              camera.cameraTarget.x,camera.cameraTarget.y,camera.cameraTarget.z,
              camera.cameraUp.x,camera.cameraUp.y,camera.cameraUp.z)
 
    
    glBegin(GL_LINES);

    glVertex3f(-20.0, 0.0, 0.0);
    glVertex3f(20.0, 0.0, 0.0);

    glVertex3f(0.0, -20.0, 0.0);
    glVertex3f(0.0, 20.0, 0.0);

    glVertex3f(0.0, 0.0, -20.0);
    glVertex3f(0.0, 0.0, 20.0);
    glEnd();
    
    obje.render(num)
   

    glutSwapBuffers()



#  since this is double buffered, swap the buffers to display what just got drawn. 
    

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    theta=0
    global number, camera,obje,parser,num, firstvertices, firstquads
    if args[0] == '+'.encode("utf-8"):
        obje=parser.parse()
        number=number+1
        obje.levelUp(number)
        
    if args[0] == '-'.encode("utf-8") and number > 0:
        obje=parser.parse()
        number=number-1
        obje.levelUp(number)
       
    if args[0] == 'w'.encode("utf-8"):
       theta-=10
       camera.updateRight(theta)
    if args[0] == 's'.encode("utf-8"):
       theta+=10
       camera.updateRight(theta)
    if args[0] == 'a'.encode("utf-8"):
        theta-=10
        camera.updateUp(theta)
    if args[0] == 'd'.encode("utf-8"):
        theta+=10
        camera.updateUp(theta)
    if args[0] == 'q'.encode("utf-8"):
        camera.cameraPos.sub(camera.cameraFront)
    if args[0] == 'r'.encode("utf-8"):
        camera.cameraPos.addition(camera.cameraFront)
    if args[0] == 'l'.encode("utf-8"):
        num=2
    if args[0] == 'k'.encode("utf-8"):
        num=1
        
        
    # If escape is pressed, kill everything.
    if args[0] == b'\x1b':
	    sys.exit()
def specialKeyPressed(key, x, y):
    theta=0
    # since i dont want my main scene is dependent to glut, i converted GLUT_KEY_LEFT to LEFT_ARROW and so on.
    global mainScene, obje
    if key == GLUT_KEY_LEFT:
        theta-=10
        camera.updateUp(theta)
    elif key == GLUT_KEY_RIGHT:
        theta+=10
        camera.updateUp(theta)
    elif key == GLUT_KEY_UP:
        theta-=10
        camera.updateRight(theta)
    elif key == GLUT_KEY_DOWN:
        theta+=10
        camera.updateRight(theta)
    

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
	window = glutCreateWindow("CENG487 Assignment3 -Edanur Hassumer")

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
	glutSpecialFunc(specialKeyPressed)
        
	# Initialize our window. 
    

    
	InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print ("Hit ESC key to quit.")
main()
