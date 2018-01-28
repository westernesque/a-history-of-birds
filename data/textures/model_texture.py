class model_texture():
	def __init__(self, texture):
		self.texture_id = texture[0]
		self.texture_data = texture[1]
		self.texture_image = texture[2]
		self.shine_damper = 0.5
		self.reflectivity = 0.1
		self.has_transparency = False
		self.use_fake_lighting = False
		self.number_of_rows = 1
	def get_use_fake_lighting(self):
		return self.use_fake_lighting
	def set_use_fake_lighting(self, value):
		self.use_fake_lighting = value
	def get_has_transparency(self):
		return self.has_transparency
	def set_has_transparency(self, value):
		self.has_transparency = value
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
	def get_number_of_rows(self):
		return self.number_of_rows
	def set_number_of_rows(self, value):
		self.number_of_rows = value