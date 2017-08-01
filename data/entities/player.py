import data.entities.entity as e
import pygame, numpy

class player(e.entity):
	RUN_SPEED = 20
	TURN_SPEED = 160
	GRAVITY = -50
	JUMP_POWER = 30
	
	current_speed = 0
	current_turn_speed = 0	
	upward_speed = 0
	
	is_in_air = False
	def __init__(self, model, position, rotation_x, rotation_y, rotation_z, scale):
		super(player, self).__init__(model, position, rotation_x, rotation_y, rotation_z, scale)
	def move(self, display, terrain):
		self.check_input()
		super(player, self).increase_rotation(0, self.current_turn_speed * display.get_frame_time(), 0)
		distance = self.current_speed * display.get_frame_time()
		distance_x =  float(distance * numpy.cos(numpy.radians(super(player, self).get_rotation_y())))
		distance_z =  float(distance * numpy.sin(numpy.radians(super(player, self).get_rotation_y())))
		super(player, self).increase_position(distance_x, 0, distance_z)
		terrain_height = terrain.get_terrain_height(super(player, self).get_position()[0], super(player, self).get_position()[2])
		self.upward_speed += self.GRAVITY * display.get_frame_time()
		super(player, self).increase_position(0, self.upward_speed * display.get_frame_time(), 0)
		if super(player, self).get_position()[1] < terrain_height:
			current_position = list(super(player, self).get_position())
			self.upward_speed = 0
			super(player, self).set_position((current_position[0], terrain_height, current_position[2]))
			self.is_in_air = False
	def jump(self):
		if self.is_in_air == False:
			self.upward_speed = self.JUMP_POWER
			self.is_in_air = True
	def check_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] == True:
			self.current_speed = -self.RUN_SPEED
		elif keys[pygame.K_s] == True:
			self.current_speed = self.RUN_SPEED
		else:
			self.current_speed = 0
		if keys[pygame.K_d] == True:
			self.current_turn_speed = self.TURN_SPEED
		elif keys[pygame.K_a] == True:
			self.current_turn_speed = -self.TURN_SPEED
		else:
			self.current_turn_speed = 0
		if keys[pygame.K_SPACE] == True:
			self.jump()