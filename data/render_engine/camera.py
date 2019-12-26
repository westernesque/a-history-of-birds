import pygame

class camera():
	def __init__(self):
		self.position = (0.0, 10.0, 0.0)
		self.pitch = 0
		self.yaw = 0
		self.roll = 0
	def move(self):
		self.position = list(self.position)
		keys = pygame.key.get_pressed()
		mod_keys = pygame.key.get_mods()
		if keys[pygame.K_w] == True and keys[pygame.K_LSHIFT] == False:
			self.position[2] -= 0.2
		if keys[pygame.K_s] == True and keys[pygame.K_LSHIFT] == False:
			self.position[2] += 0.2
		if keys[pygame.K_s] == True and keys[pygame.K_SPACE] == True:
			self.position[2] += 1.0
		if keys[pygame.K_a] == True and keys[pygame.K_LSHIFT] == False:
			self.position[0] -= 0.2
		if keys[pygame.K_d] == True and keys[pygame.K_LSHIFT] == False:
			self.position[0] += 0.2
		if keys[pygame.K_w] == True and keys[pygame.K_LSHIFT] == True:
			self.position[1] += 0.2
		if keys[pygame.K_s] == True and keys[pygame.K_LSHIFT] == True:
			self.position[1] -= 0.2
		if keys[pygame.K_j] == True and keys[pygame.K_RSHIFT] == False:
			self.yaw -= 0.2
		if keys[pygame.K_k] == True and keys[pygame.K_RSHIFT] == False:
			self.yaw += 0.2
		if keys[pygame.K_j] == True and keys[pygame.K_RSHIFT] == True:
			self.pitch += 0.2
		if keys[pygame.K_k] == True and keys[pygame.K_RSHIFT] == True:
			self.pitch -= 0.2
		if keys[pygame.K_h] == True and keys[pygame.K_LSHIFT] == False:
			self.roll -= 0.2
		if keys[pygame.K_l] == True and keys[pygame.K_LSHIFT] == False:
			self.roll += 0.2
		self.position = tuple(self.position)
#		print self.position
		pass
	def get_position(self):
		return self.position
	def get_pitch(self):
		return self.pitch
	def get_yaw(self):
		return self.yaw
	def get_roll(self):
		return self.roll