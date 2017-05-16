import pygame, numpy

class camera():
	distance_from_player = 100.0
	angle_around_player = 0
	def __init__(self, player):
		self.player = player
		self.position = (0, 10.0, 0)
		self.pitch = 0
		self.yaw = 0
		self.roll = 0
	def move(self):
		# self.calculate_rotation()
		self.calculate_pitch()
		self.calculate_zoom()
		horizontal_distance = self.calculate_horizontal_distance()
		print horizontal_distance
		vertical_distance = self.calculate_vertical_distance()
		print vertical_distance
		self.calculate_camera_position(horizontal_distance, vertical_distance)
		self.yaw = (self.player.get_rotation_y() + self.angle_around_player)
		# print self.angle_around_player
		# self.position = list(self.position)
		# keys = pygame.key.get_pressed()
		# mod_keys = pygame.key.get_mods()
		# if keys[pygame.K_w] == True and keys[pygame.K_LSHIFT] == False:
			# self.position[2] -= 0.2
		# if keys[pygame.K_s] == True and keys[pygame.K_LSHIFT] == False:
			# self.position[2] += 0.2
		# if keys[pygame.K_s] == True and keys[pygame.K_SPACE] == True:
			# self.position[2] += 1.0
		# if keys[pygame.K_a] == True and keys[pygame.K_LSHIFT] == False:
			# self.position[0] -= 0.2
		# if keys[pygame.K_d] == True and keys[pygame.K_LSHIFT] == False:
			# self.position[0] += 0.2
		# if keys[pygame.K_w] == True and keys[pygame.K_LSHIFT] == True:
			# self.position[1] += 0.2
		# if keys[pygame.K_s] == True and keys[pygame.K_LSHIFT] == True:
			# self.position[1] -= 0.2
		# if keys[pygame.K_j] == True and keys[pygame.K_RSHIFT] == False:
			# self.yaw -= 0.2
		# if keys[pygame.K_k] == True and keys[pygame.K_RSHIFT] == False:
			# self.yaw += 0.2
		# if keys[pygame.K_j] == True and keys[pygame.K_RSHIFT] == True:
			# self.pitch += 0.2
		# if keys[pygame.K_k] == True and keys[pygame.K_RSHIFT] == True:
			# self.pitch -= 0.2
		# if keys[pygame.K_h] == True and keys[pygame.K_LSHIFT] == False:
			# self.roll -= 0.2
		# if keys[pygame.K_l] == True and keys[pygame.K_LSHIFT] == False:
			# self.roll += 0.2
		# self.position = tuple(self.position)
		pass
	def calculate_zoom(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z] == True:
			zoom_level = 0.1
			self.distance_from_player -= zoom_level
		elif keys[pygame.K_x] == True:
			zoom_level = 0.1
			self.distance_from_player += zoom_level
	def calculate_pitch(self):
		mouse_keys = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		rel_mouse_pos = pygame.mouse.get_rel()
		if mouse_keys[2] == True:
			if rel_mouse_pos[1] > 0:
				pitch_change = rel_mouse_pos[1] * 0.1
				self.pitch += pitch_change
			elif rel_mouse_pos[1] < 0:
				pitch_change = rel_mouse_pos[1] * 0.1
				self.pitch += pitch_change
	def calculate_rotation(self):
		mouse_keys = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		rel_mouse_pos = pygame.mouse.get_rel()
		if mouse_keys[0] == True:
			if rel_mouse_pos[0] > 0:
				print "test2"
				angle_change = rel_mouse_pos[0] * 0.3
				self.angle_around_player -= angle_change
				print angle_change
			elif rel_mouse_pos[0] < 0:
				angle_change = rel_mouse_pos[0] * 0.3
				self.angle_around_player -= angle_change
	def calculate_horizontal_distance(self):
		return self.distance_from_player * numpy.sin(numpy.radians(self.pitch))
	def calculate_vertical_distance(self):
		return self.distance_from_player * numpy.cos(numpy.radians(self.pitch))
	def calculate_camera_position(self, horizontal_distance, vertical_distance):
		self.position = list(self.position)
		theta = self.player.get_rotation_y()
		offset_x = float(horizontal_distance * numpy.sin(numpy.radians(theta)))
		offset_z = float(horizontal_distance * numpy.cos(numpy.radians(theta)))
		self.position[0] = list(self.player.get_position())[0] - offset_x
		self.position[1] = list(self.player.get_position())[1] + vertical_distance
		self.position[2] = list(self.player.get_position())[2] - offset_z
		self.position = tuple(self.position)
	def get_position(self):
		return self.position
	def get_pitch(self):
		return self.pitch
	def get_yaw(self):
		return self.yaw
	def get_roll(self):
		return self.roll