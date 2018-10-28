import pygame
from OpenGL.GL import *

class Texture:
	def __init__(self, filename):
		self.loadImage(filename)


	def loadImage(self, filename):
		textureSurface = pygame.image.load(filename)

		textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

		self.width = textureSurface.get_width()
		self.height = textureSurface.get_height()

		self.textureID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)


	def render(self, posX, posY):
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glBegin(GL_QUADS)

		glTexCoord(0, 1)
		glVertex2f(posX, posY)

		glTexCoord(1, 1)
		glVertex2f(posX + self.width, posY)

		glTexCoord(1, 0)
		glVertex2f(posX + self.width, posY + self.height)

		glTexCoord(0, 0)
		glVertex2f(posX, posY + self.height)

		glEnd()


	def setSize(self, width, height):
		self.width = width
		self.height = height


