# /usr/bin/env python3

from module import draw
from module import setup
from OpenGL.GL import *
import pygame
from entities.Human import Human
from entities.crabe import Crabe
from entities.goblin import Goblin



pygame.init()


def main():
	dimensions = (1366, 680)
	display = setup.pipigame(dimensions)
	setup.opengl(dimensions)

	john = Human(10, 10, "John Cena")
	animal = Crabe(20,20,"c'est lui")
	monstre = Goblin(50,10,"c'est l'autre")

	while True:
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		john.draw()
		animal.draw()
		monstre.draw()
		draw.Text.write("il é bo notr je", 0, 0)


		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return

		pygame.display.flip()


if __name__ == "__main__":
	main()