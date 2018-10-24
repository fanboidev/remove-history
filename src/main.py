# /usr/bin/env python3

import module.draw
import module.setup
import OpenGL.GL as gl
import pygame

pygame.init()


def main():
    dimensions = (800, 800)
    display = module.setup.pipigame(dimensions)
    module.setup.opengl(dimensions)

    rect = (
        (0, 0),
        (0, 1),
        (1, 1),
        (1, 0)
    )
    rect2=(
        (15,30),
        (0,0),
        (23,78),
        (2,4)
    )
    while True:
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        module.draw.Text.write("asdf", 0, 0)
        module.draw.Objects.rect((15,30),(0,0),(23,78),(2,4))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        pygame.display.flip()


if __name__ == "__main__":
    main()