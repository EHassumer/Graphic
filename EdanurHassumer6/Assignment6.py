# CENG 487 Assignment# 
# Edanur Hassumer
# StudentId: 240201003
# February 2021


from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sqrt
import numpy
from camera import *
from scene import *
from program import Program

print("For mouse operation --->  alt + left button mouse ")
print("For zoom operation --->  alt + rigth button mouse ")
print("For exit  --->  ESC ")
scene = Scene()

# create objects
cube1 = Cube("cube", 1.0, 1.0, 1.0, 10, 10, 10)
scene.add(cube1)

cube2 = Cube("cube", 4.0, 1.0, 1.0, 10, 10, 10)
scene.add(cube2)
#mouse attributes
X = -1
Y = -1
Button = -1
State = -1
altPressed = False
mouseX = -1
mouseY = -1
#
# GLOBALS
vertexDim = 4
nVertices = 48
# Global variable to represent the compiled shader program, written in GLSL
programID = None
# Global variables for buffer objects
VBO = None

# create an array to hold positions of our vertices. numpy array is directly transferable to OpenGL
# order: top-right, bottom-right, bottom-left, top-left

vertexPositions = numpy.array(scene.getVertex(),
	dtype='float32'
)

vertexColors = numpy.array(scene.getColor(),
	dtype='float32'
)

# camera globals
#camPosition = numpy.array([0.0, 0.0, 10.0, 1.0], dtype='float32')
#camUpAxis = numpy.array([2.0, 1.0, 5.0, 0.0], dtype='float32')
camNear = 1.0
camFar = 100.0
camAspect = 1.0
camFov = 60.0

camera = Camera()
camera.createView( 	Point3f(0.0, 0.0, 10.0), \
					Point3f(0.0, 0.0, 1.0), \
					Vector3f(0.0, 1.0, 0.0) )
camera.setNear(camNear)
camera.setFar(camFar)
camera.setFov(camFov)

# objectPosition
objectPosition = numpy.array([-1.5, 0, 0, 1.0], dtype='float32')

#
# FUNCTIONS

# vector stuff
def dot(vec1, vec2):
	return 1.0 * numpy.dot(vec2, vec1)

def cross(vec1, vec2):
	result = numpy.cross(vec1[0:3], vec2[0:3], axisa=0, axisb=0, axisc=0)
	return numpy.array([result[0], result[1], result[2], 0.0], dtype='float32')

def normalize(vec):
	vecLen = sqrt(1.0 * numpy.dot(vec, vec))
	return vec / vecLen

# matrix stuff
def getProjMatrix(near, far, aspect, fov):
	f = numpy.reciprocal(numpy.tan(numpy.divide(numpy.deg2rad(fov), 2.0)))
	base = near - far
	term_0_0 = numpy.divide(f, aspect)
	term_2_2 = numpy.divide(far + near, base)
	term_2_3 = numpy.divide(numpy.multiply(numpy.multiply(2, near), far), base)

	# https://en.wikibooks.org/wiki/GLSL_Programming/Vertex_Transformations
	return  numpy.array([	term_0_0, 0.0, 0.0, 0.0,
							0.0, f, 0.0, 0.0,
							0.0, 0.0, term_2_2, -1,
							0.0, 0.0, term_2_3, 0.0], dtype='float32')

def getViewMatrix():
	# THIS HAS A LOT OF HARD CODED STUFF
	# we first calculate camera x, y, z axises and from those we assemble a rotation matrix.
	# Once that is done we add in the translation.
 	# We assume camera always look at the world space origin.
	# Up vector is always in the direction of global yAxis.
	camZAxis = normalize(numpy.array([-camera.getEyePoint().x, -camera.getEyePoint().y, -camera.getEyePoint().z, 0.0], dtype='float32'))
	camXAxis = cross(camZAxis, [camera.getUpVector().x,camera.getUpVector().y,camera.getUpVector().z,0.0])
	camYAxis = cross(camXAxis, camZAxis)

	rotMat = numpy.array([	camXAxis[0], camYAxis[0], -camZAxis[0], 0.0,
							camXAxis[1], camYAxis[1], -camZAxis[1], 0.0,
							camXAxis[2], camYAxis[2], -camZAxis[2], 0.0,
							0.0, 0.0, 0.0, 1.0], dtype='float32').reshape(4,4)

	traMat = numpy.array([	1.0, 0.0, 0.0, 0.0,
							0.0, 1.0, 0.0, 0.0,
							0.0, 0.0, 1.0, 0.0,
							-camera.getEyePoint().x, -camera.getEyePoint().y, -camera.getEyePoint().z, 1.0], dtype='float32').reshape(4,4)

	return traMat.dot(rotMat)

def getModelMatrix():
	return numpy.array([	1.0, 0.0, 0.0, 0.0,
							0.0, 1.0, 0.0, 0.0,
							0.0, 0.0, 1.0, 0.0,
							objectPosition[0], objectPosition[1], objectPosition[2], 1.0], dtype='float32')

# Initialize the OpenGL environment
def init():
	initProgram()
	initVertexBuffer()

# Set up the list of shaders, and call functions to compile them
def initProgram():
	global programID
	program=Program()
	program.createShader("ShapeVertx.glsl",GL_VERTEX_SHADER)
	program.createShader("ShapeFrags.glsl",GL_FRAGMENT_SHADER)
	programID = program.programID
	program.deleteUse()

# Set up the vertex buffer that will store our vertex coordinates for OpenGL's access
def initVertexBuffer():
	global VBO
	VBO = glGenBuffers(1)

	# set array buffer to our ID
	glBindBuffer(GL_ARRAY_BUFFER, VBO)

	# set data
	bufferData = numpy.concatenate((vertexPositions, vertexColors))
	elementSize = numpy.dtype(numpy.float32).itemsize

	# third argument is criptic - in c_types if you multiply a data type with an integer you create an array of that type
	glBufferData(	GL_ARRAY_BUFFER,
					len(bufferData)*elementSize,
					bufferData,
#					(ctypes.c_float * len(bufferData))(*bufferData),
					GL_STATIC_DRAW
	)

	# reset array buffer
	glBindBuffer(GL_ARRAY_BUFFER, 0)

# Called to update the display.
# Because we are using double-buffering, glutSwapBuffers is called at the end
# to write the rendered buffer to the display.
def display():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)

	# use our program
	glUseProgram(programID)

	# get matrices and bind them to vertex shader locations
	modelLocation = glGetUniformLocation( programID, "model" )
	glUniformMatrix4fv(modelLocation, 1, GL_FALSE, getModelMatrix())
	viewLocation = glGetUniformLocation(programID, "view")
	glUniformMatrix4fv(viewLocation, 1, GL_FALSE, getViewMatrix())
	projLocation = glGetUniformLocation(programID, "proj")
	glUniformMatrix4fv(projLocation, 1, GL_FALSE, getProjMatrix(camNear, camFar, camAspect, camFov))

	# reset our vertex buffer
	glBindBuffer(GL_ARRAY_BUFFER, VBO)
	elementSize = numpy.dtype(numpy.float32).itemsize

	# setup vertex attributes
	offset = 0

	# location 0
	glVertexAttribPointer(0, vertexDim, GL_FLOAT, GL_FALSE, elementSize * vertexDim, ctypes.c_void_p(offset))
	glEnableVertexAttribArray(0)

	# define colors which are passed in location 1 - they start after all positions and has four floats consecutively
	offset += elementSize * vertexDim * nVertices
	glVertexAttribPointer(1, vertexDim, GL_FLOAT, GL_FALSE, elementSize * vertexDim, ctypes.c_void_p(offset))
	glEnableVertexAttribArray(1)

	glDrawArrays(GL_QUADS, 0, nVertices)

	# reset to defaults
	glDisableVertexAttribArray(0)
	glDisableVertexAttribArray(1)
	glBindBuffer(GL_ARRAY_BUFFER, 0)
	glUseProgram(0)

	glutSwapBuffers()
#I take this mouse method from view    
def mousePressed(button, state, x, y):
        global X, Y, Button, State, altPressed, mouseX, mouseY 
        X = x
        Y = y
        State = state
        Button = button

		# get status of alt key
        m = glutGetModifiers()
        altPressed = m & GLUT_ACTIVE_ALT

        mouseX = x
        mouseY = y

def mouseMove( x, y):
        global X, Y, Button, State, altPressed, mouseX, mouseY,camera
        if altPressed == False:
            return

        xSpeed = 0.02
        ySpeed = 0.02
        xOffset = (x - mouseX) * xSpeed
        yOffset = (y - mouseY) * ySpeed

        if ( Button == GLUT_RIGHT_BUTTON ):
            camera.zoom(xOffset)
            display()
        elif (Button == GLUT_MIDDLE_BUTTON ):
            camera.dolly(-xOffset, yOffset, 0)
            display()
          
        elif ( Button == GLUT_LEFT_BUTTON ):
            camera.yaw(xOffset)
            camera.pitch(yOffset)
            display()
           
        # store last positions
        mouseX = x
        mouseY = y

		# remember this point
        X = x
        Y = y

# keyboard input handler: exits the program if 'esc' is pressed
def keyboard(key, x, y):
	if ord(key) == 27: # ord() is needed to get the keycode
		glutLeaveMainLoop()
		return
    # If escape is pressed, kill everything.
	elif args[0] == b'\x1b':
	    sys.exit()

# Called whenever the window's size changes (including once when the program starts)
def reshape(w, h):
	glViewport(0, 0, w, h)

# The main function
def main():
    
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    width = 500;
    height = 500;
    glutInitWindowSize (width, height)

    glutInitWindowPosition (300, 200)

    window = glutCreateWindow("CENG487 FinalAssignmet-EdanurHassumer")
   
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    
	
    glutMouseFunc( mousePressed )
    glutMotionFunc( mouseMove )
    

    

    glutMainLoop();

if __name__ == '__main__':
	main()