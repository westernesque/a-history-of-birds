class textured_model():
	def __init__(self, model, texture):
		self.raw_model = model
		self.texture = texture
	def get_raw_model(self):
		return self.raw_model
	def get_texture(self):
		return self.texture