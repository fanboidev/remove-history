# /usr/bin/env python3
import OpenGL.GL as gl
import OpenGL.GLU as glu
import pygame


def opengl(DISPLAY_DIMENSIONS):
	glu.gluPerspective(45, DISPLAY_DIMENSIONS[0]/DISPLAY_DIMENSIONS[1], 0.1, 50.0)
	gl.glTranslatef(0, 0, -5)


def pipigame(DISPLAY_DIMENSIONS):
	display = pygame.display.set_mode(DISPLAY_DIMENSIONS, pygame.DOUBLEBUF | pygame.OPENGL)
	return display
