#/usr/bin/env python3
from entities.species import Specie


class Crabe(Specie):
	def __init__(self, x, y, name):
		Specie.__init__(self, x, y, name, "../res/entities/crabe.png") # Call __init__ of Specie
