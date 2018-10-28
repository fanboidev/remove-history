class Specie:
	def __init__(self,x,y,name):
		self.x=x
		self.y=y
		self.name=name
	def move(self,nouveau_x,nouveau_y):
		self.x=self.x+nouveau_x
		self.y=self.y+nouveau_y
	def draw():
		print("drawing...")