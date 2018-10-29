#/usr/bin/env python3
from entities.species import Specie


class Goblin(Specie):
	def __init__(self, x, y, name):
		Specie.__init__(self, x, y, name, "../res/entities/goblin.png") # Call __init__ of Specie
