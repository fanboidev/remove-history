class Map:
	def __init__(self):
		self.x=x
		self.y=y
		self.name=name
		self.texture = images.Texture(name)

	def draw(self):
		self.texture.render(self.x, self.y)