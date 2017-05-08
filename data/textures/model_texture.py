class model_texture():
	def __init__(self, texture):
		self.texture_id = texture[0]
		self.texture_data = texture[1]
		self.shine_damper = 1
		self.reflectivity = 0
	def get_texture_id(self):
		return self.texture_id
	def get_texture_data(self):
		return self.texture_data
	def get_shine_damper(self):
		return self.shine_damper
	def set_shine_damper(self, shine_damper):
		self.shine_damper = shine_damper
	def get_reflectivity(self):
		return self.reflectivity
	def set_reflectivity(self, reflectivity):
		self.reflectivity = reflectivity