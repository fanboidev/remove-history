from module import images


class Specie:
	def __init__(self,x,y,name, texturefile):
		self.x=x
		self.y=y
		self.name=name
		self.texture = images.Texture(texturefile)


	def move(self,nouveau_x,nouveau_y):
		self.x=self.x+nouveau_x
		self.y=self.y+nouveau_y


	def draw(self):
		self.texture.render(self.x, self.y)
