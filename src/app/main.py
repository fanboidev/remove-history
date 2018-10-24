# /usr/bin/env python3

import sys
sys.path.append("../")

import module.draw
import module.setup
import OpenGL.GL as gl
import pygame

pygame.init()

def main():
	dimensions = (800, 800)
	module.setup.pipigame(dimensions)
	module.setup.opengl(dimensions)

	rect = (
		(0, 0),
		(0, 1),
		(1, 1),
		(1, 0)
	)

	while True:
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
		module.draw.Objects.quad(rect[0], rect[1], rect[2], rect[3])

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		pygame.display.flip()



if __name__ == "__main__":
	main()
