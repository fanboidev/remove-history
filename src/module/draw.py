from OpenGL.GL import *
import OpenGL.GLUT as glut
import pygame


class Objects:
	def __init__(self):
		pass

	@staticmethod
	def rect(point1, point2, point3, point4):
		"""

		:param point1: tuple
		:param point2: tuple
		:param point3: tuple
		:param point4: tuple
		:return: void
		"""
		glBegin(GL_QUADS)

		glVertex2f(point1[0], point1[1])
		glVertex2f(point2[0], point2[1])
		glVertex2f(point3[0], point3[1])
		glVertex2f(point4[0], point4[1])

		glEnd()

	@staticmethod
	def tri(point1, point2, point3):
		"""

		:param point1: tuple
		:param point2: tuple
		:param point3: tuple
		:return: void
		"""
		glBegin(GL_TRIANGLES)

		glVertex2i(point1[0], point1[1])
		glVertex2i(point2[0], point2[1])
		glVertex2i(point3[0], point3[1])

		glEnd()


class Text:
	def __init__(self):
		pass

	@staticmethod
	def write(string, posX, posY):
		blending = False
		if glIsEnabled(GL_BLEND):
			blending = True

		# glEnable(GL_BLEND)
		glColor3f(1, 1, 1)
		glRasterPos2f(posX, posY)
		for ch in string:
			glut.glutBitmapCharacter(glut.GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))

		if not blending:
			glDisable(GL_BLEND)