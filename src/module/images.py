
from OpenGL.GL import *
from PIL import Image


class Texture:
	def __init__(self, filename):
		self.imgToTexture(filename)

	def imgToTexture(self, filename):
		"""

		:param filename:
		:return: void
		"""
		im = Image.open(filename)
		ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
		self.textureID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glTexImage2D(
			GL_TEXTURE_2D, 0, 3, ix, iy, 0,
			GL_RGBA, GL_UNSIGNED_BYTE, image
		)

	def setupTexture(self):
		glEnable(GL_TEXTURE_2D)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

	def render(self, posX, posY, sizeX, sizeY):
		self.setupTexture()
		glBindTexture(GL_TEXTURE_2D, self.textureID)

		glBegin(GL_QUADS)

		glTexCoord(0, 0)
		glVertex2f(posX, posY)

		glTexCoord(1, 0)
		glVertex2f(posX + sizeX, posY)

		glTexCoord(1, 1)
		glVertex2f(posX + sizeX, posY + sizeY)

		glTexCoord(0, 1)
		glVertex2f(posX, posY + sizeY)

		glEnd()
		glDisable(GL_TEXTURE_2D)
