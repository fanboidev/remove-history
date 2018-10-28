# /usr/bin/env python3
from OpenGL.GL import *
import OpenGL.GLUT as glut
import pygame


def pipigame(DISPLAY_DIMENSIONS):
	display = pygame.display.set_mode(DISPLAY_DIMENSIONS, pygame.DOUBLEBUF | pygame.OPENGL)
	return display


def opengl(DISPLAY_DIMENSIONS):
	glut.glutInit()
	glTranslatef(0, 0, -5)
	glEnable(GL_TEXTURE_2D)

	glShadeModel(GL_SMOOTH)
	glDisable(GL_DEPTH_TEST)
	glDisable(GL_LIGHTING)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1)

	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glMatrixMode(GL_MODELVIEW)

	glLoadIdentity()
	glMatrixMode(GL_PROJECTION)
	glOrtho(0, DISPLAY_DIMENSIONS[0], DISPLAY_DIMENSIONS[1], 0, 1, -1)
	glMatrixMode(GL_MODELVIEW)
