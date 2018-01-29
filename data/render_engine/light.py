class light():
	def __init__(self, position, color, attenuation = (1.0, 0.0, 0.0)):
		self.position = position
		self.color = color
		self.attenuation = attenuation
	def get_attenuation(self):
		return self.attenuation
	def set_attenuation(self, attenuation):
		self.attenuation = attenuation
	def get_position(self):
		return self.position
	def set_position(self, position):
		self.position = position
	def get_color(self):
		return self.color
	def set_color(self, color):
		self.color = color
		