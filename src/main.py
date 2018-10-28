# /usr/bin/env python3
import random
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
	myImage = Texture("../res/jeu.png")
	x1=10
	y1=100
	x2=0
	y2=0

	while True:
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		texture.render(x2, y2)
		myImage.render(x1, y1)
		draw.Text.write("il é bo notr je", 0, 0)


		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
			if e.type==KEYDOWN and e.key==K_DOWN:
				y1=y1+10
			if e.type==KEYDOWN and e.key==K_UP:	
				y1=y1-10
			if e.type==KEYDOWN and e.key==K_RIGHT:
				x1=x1+10
			if e.type==KEYDOWN and e.key==K_LEFT:
				x1=x1-10
			x2=x2+random.randint(0,10)
			y2=y2+random.randint(0,10)

		pygame.display.flip()


if __name__ == "__main__":
	main()