import pygame, sys, os
from OpenGL.GL import *

class display_manager():
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
		glViewport(0, 0, 800, 600)
	def update_display(self):
		pygame.display.flip()
	def close_display(self):
		pygame.quit()
		sys.exit()