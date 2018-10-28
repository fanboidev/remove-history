# /usr/bin/env python3
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import pygame


def opengl(DISPLAY_DIMENSIONS):
	glu.gluPerspective(45, DISPLAY_DIMENSIONS[0]/DISPLAY_DIMENSIONS[1], 0.1, 50.0)
	gl.glEnable(gl.GL_BLEND)
	gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
	gl.glClearColor(0.0, 0.0, 0.0, 0.0)
	gl.glTranslatef(0, 0, -5)
	glut.glutInit()


def pipigame(DISPLAY_DIMENSIONS):
	display = pygame.display.set_mode(DISPLAY_DIMENSIONS, pygame.DOUBLEBUF | pygame.OPENGL)
	return display
