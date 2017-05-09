class entity():
	def __init__(self, model, position, rotation_x, rotation_y, rotation_z, scale):
		self.model = model
		self.position = position
		self.rotation_x = rotation_x
		self.rotation_y = rotation_y
		self.rotation_z = rotation_z
		self.scale = scale
	def increase_position(self, increase_x, increase_y, increase_z):
		self.position = list(self.position)
		self.position[0] += increase_x
		self.position[1] += increase_y
		self.position[2] += increase_z
		self.position = tuple(self.position)
	def increase_rotation(self, increase_x, increase_y, increase_z):
		self.rotation_x += increase_x
		self.rotation_y += increase_y
		self.rotation_z += increase_z
	def get_model(self):
		return self.model
	def set_model(self, model):
		self.model = model
	def get_position(self):
		return self.position
	def set_position(self, position):
		self.position = position
	def get_rotation_x(self):
		return self.rotation_x
	def set_rotation_x(self, rotation_x):
		self.rotation_x = rotation_x
	def get_rotation_y(self):
		return self.rotation_y
	def set_rotation_y(self, rotation_y):
		self.rotation_y = rotation_y
	def get_rotation_z(self):
		return self.rotation_z
	def set_rotation_z(self, rotation_z):
		self.rotation_z = rotation_z
	def get_scale(self):
		return self.scale
	def set_scale(self, scale):
		self.scale = scale