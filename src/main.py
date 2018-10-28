# /usr/bin/env python3

import module.draw
import module.setup
from module.images import Texture
import OpenGL.GL as gl
import pygame
from pygame.locals import *

pygame.init()




def main():
	dimensions = (1366, 680)
	display = module.setup.pipigame(dimensions)
	module.setup.opengl(dimensions)
	texture = Texture("../res/test.png")
	myImage = Texture("../res/jeu.png")
	x1=0
	y1=0
	t1=1
	t2=1
	while True:
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

		texture.render(0, 0, 2, 2)
		myImage.render(x1, y1, t1, t2)
		module.draw.Text.write("il é bo notr je", 0, 0)

		

	

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