#/usr/bin/env python3
from entities.species import Specie


class Human(Specie):
	def __init__(self, x, y, name):
		Specie.__init__(self, x, y, name, "../res/entities/human.png") # Call __init__ of Specie
