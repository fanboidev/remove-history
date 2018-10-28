# /usr/bin/env python3

import module.draw
import module.setup
from module.images import Texture
from OpenGL.GL import *
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import pygame

pygame.init()


def setupPipigame(DISPLAY_DIMENSIONS):
	display = pygame.display.set_mode(DISPLAY_DIMENSIONS, pygame.DOUBLEBUF | pygame.OPENGL)
	return display


def setupOpengl(DISPLAY_DIMENSIONS):
	glu.gluPerspective(45, DISPLAY_DIMENSIONS[0]/DISPLAY_DIMENSIONS[1], 0.1, 50.0)
	glTranslatef(0, 0, -5)
	glDisable(GL_DEPTH_TEST)
	glColor4f(1, 1, 1, 1)
	glEnable(GL_TEXTURE_2D)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE, GL_ONE)
	glut.glutInit()


def main():
	dimensions = (800, 800)
	display = setupPipigame(dimensions)
	setupOpengl(dimensions)
	texture = Texture("../res/test.png")
	texture2 = Texture("../res/test.png")

	while True:
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		texture2.render(0, 0.3, 1, 1)
		texture.render(0, 0, 1, 1)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		pygame.display.flip()


if __name__ == "__main__":
	main()