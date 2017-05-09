class terrain_texture_pack():
	def __init__(self, background_texture, r_texture, g_texture, b_texture):
		self.background_texture = background_texture
		self.r_texture = r_texture
		self.g_texture = g_texture
		self.b_texture = b_texture
	def get_background_texture(self):
		return self.background_texture
	def get_r_texture(self):
		return self.r_texture
	def get_g_texture(self):
		return self.g_texture
	def get_b_texture(self):
		return self.b_texture