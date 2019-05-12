import pygame, numpy, OpenGL
from OpenGL.GL import *


class third_person_camera():
	def __init__(self, player):
		self.player = player
		self.angle_around_player = 0.0
		self.distance_from_player = 100.0
		self.position = (0.0, 0.0, 0.0)
		self.pitch = -90.0
		self.yaw = 0
		self.roll = 0
	def move(self):
		mouse_keys = pygame.mouse.get_pressed()
		rel_mouse_pos = pygame.mouse.get_rel()
		self.calculate_zoom(mouse_keys, rel_mouse_pos)
		self.calculate_pitch(mouse_keys, rel_mouse_pos)
		self.calculate_rotation(mouse_keys, rel_mouse_pos)
		horizontal_distance = self.calculate_horizontal_distance()
		vertical_distance = self.calculate_vertical_distance()
		self.calculate_camera_position(horizontal_distance, vertical_distance)
		self.yaw = 360 - (self.player.get_rotation_y() - self.angle_around_player)
	def calculate_zoom(self, mouse_keys, rel_mouse_pos):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z] == True:
			# zoom_level = 1.0
			zoom_level = 5.0
			self.distance_from_player -= zoom_level
		elif keys[pygame.K_x] == True:
			# zoom_level = 1.0
			zoom_level = 5.0
			self.distance_from_player += zoom_level
	def calculate_pitch(self, mouse_keys, rel_mouse_pos):
		if mouse_keys[2] == True:
			if rel_mouse_pos[1] > 0:
				pitch_change = rel_mouse_pos[1] * 0.1
				self.pitch += pitch_change
			elif rel_mouse_pos[1] < 0:
				pitch_change = rel_mouse_pos[1] * 0.1
				self.pitch += pitch_change
	def calculate_rotation(self, mouse_keys, rel_mouse_pos):
		# if mouse_keys[0] == True:
		if mouse_keys[0] == True and 0 == 1:
			if rel_mouse_pos[0] > 0:
				angle_change = rel_mouse_pos[0] * 0.3
				self.angle_around_player -= angle_change
			elif rel_mouse_pos[0] < 0:
				angle_change = rel_mouse_pos[0] * 0.3
				self.angle_around_player -= angle_change
	def calculate_horizontal_distance(self):
		return self.distance_from_player * numpy.cos(numpy.radians(self.pitch))
	def calculate_vertical_distance(self):
		return self.distance_from_player * numpy.sin(numpy.radians(self.pitch))
	def calculate_camera_position(self, horizontal_distance, vertical_distance):
		self.position = list(self.position)
		theta = 360 - (self.player.get_rotation_y() - self.angle_around_player)
		offset_x = float(horizontal_distance * numpy.sin(numpy.radians(theta)))
		offset_z = float(horizontal_distance * numpy.cos(numpy.radians(theta)))
		self.position[0] = list(self.player.get_position())[0] + offset_x
		self.position[1] = list(self.player.get_position())[1] - vertical_distance
		self.position[2] = list(self.player.get_position())[2] + offset_z
		self.position = tuple(self.position)
	def get_position(self):
		return self.position
	def get_pitch(self):
		return self.pitch
	def get_yaw(self):
		return self.yaw
	def get_roll(self):
		return self.roll