import data.entities.entity as e
import pygame, numpy

class player(e.entity):
	RUN_SPEED = 20
	TURN_SPEED = 160
	current_speed = 0
	current_turn_speed = 0	
	def __init__(self, model, position, rotation_x, rotation_y, rotation_z, scale):
		super(player, self).__init__(model, position, rotation_x, rotation_y, rotation_z, scale)
	def move(self, display):
		self.check_input()
		super(player, self).increase_rotation(0, self.current_turn_speed * display.get_frame_time(), 0)
		distance = self.current_speed * display.get_frame_time()
		distance_x =  float(distance * numpy.cos(numpy.radians(super(player, self).get_rotation_y())))
		distance_z =  float(distance * numpy.sin(numpy.radians(super(player, self).get_rotation_y())))
		super(player, self).increase_position(distance_x, 0, distance_z)
	def check_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] == True:
			self.current_speed = self.RUN_SPEED
		elif keys[pygame.K_s] == True:
			self.current_speed = -self.RUN_SPEED
		else:
			self.current_speed = 0
		if keys[pygame.K_d] == True:
			self.current_turn_speed = -self.TURN_SPEED
		elif keys[pygame.K_a] == True:
			self.current_turn_speed = self.TURN_SPEED
		else:
			self.current_turn_speed = 0