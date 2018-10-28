# /usr/bin/env python3

from module import draw
from module import setup
from module.images import Texture
from OpenGL.GL import *
import pygame

pygame.init()


def main():
	dimensions = (800, 800)
	display = setup.pipigame(dimensions)
	setup.opengl(dimensions)
	texture = Texture("../res/test.png")
	texture2 = Texture("../res/test.png")

	while True:
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		texture2.render(0, 100)
		texture.render(0, 50)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		pygame.display.flip()


if __name__ == "__main__":
	main()