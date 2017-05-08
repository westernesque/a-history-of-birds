class model_texture():
	def __init__(self, texture):
		self.texture_id = texture[0]
		self.texture_data = texture[1]
	def get_texture_id(self):
		return self.texture_id
	def get_texture_data(self):
		return self.texture_data