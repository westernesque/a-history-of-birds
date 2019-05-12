import pygame, sys, os, time
from OpenGL.GL import *

class display_manager():
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
		glViewport(0, 0, 800, 600)
		self.delta = 0
		self.last_frame_time = self.get_current_time()
	def update_display(self):
		current_frame_time = self.get_current_time()
		self.delta = (current_frame_time - self.last_frame_time) / 1000.0
		self.last_frame_time = current_frame_time
		pygame.display.flip()
	def get_frame_time(self):
		return self.delta
	def close_display(self):
		pygame.quit()
	def get_current_time(self):
		return int(round(time.time() * 1000))