# /usr/bin/env python3

import module.draw
import module.setup
from module.images import Texture
import OpenGL.GL as gl
import pygame

pygame.init()


def main():
	dimensions = (800, 800)
	display = module.setup.pipigame(dimensions)
	module.setup.opengl(dimensions)
	texture = Texture("../res/test.png")

	while True:
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

		texture.render(0, 0, 2, 2)
		module.draw.Text.write("asdf", 0, 0)
		module.draw.Objects.rect((15, 30), (0, 0), (23, 78), (2, 4), (0, 0, 0))
		module.draw.Objects.tri((23, 78), (2, 4), (0, 0), (255, 0, 0))

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		pygame.display.flip()


if __name__ == "__main__":
	main()