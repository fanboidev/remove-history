# /usr/bin/env python3

from module import draw
from module import setup
from module.images import Texture
from OpenGL.GL import *
import pygame
from pygame.locals import *

pygame.init()


def main():
	dimensions = (1366, 680)
	display = setup.pipigame(dimensions)
	setup.opengl(dimensions)
	texture = Texture("../res/test.png")
	myImage = Texture("../res/test.png")
	x1=0
	y1=0

	while True:
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		texture.render(0, 0)
		myImage.render(x1, y1)
		draw.Text.write("il é bo notr je", 0, 0)


		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
			if e.type==KEYDOWN and e.key==K_DOWN:
				y1=y1-0.5
			if e.type==KEYDOWN and e.key==K_UP:	
				y1=y1+0.5
			if e.type==KEYDOWN and e.key==K_RIGHT:
				x1=x1+0.5
			if e.type==KEYDOWN and e.key==K_LEFT:
				x1=x1-0.5
		pygame.display.flip()


if __name__ == "__main__":
	main()