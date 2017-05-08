class model_data():
	def __init__(self, vertices, texture_coordinates, normals, indices, furthest_point):
		self.vertices = vertices
		self.texture_coordinates = texture_coordinates
		self.normals = normals
		self.indices = indices
		self.furthest_point = furthest_point
	def get_vertices(self):
		return self.vertices
	def get_texture_coordinates(self):
		return self.texture_coordinates
	def get_normals(self):
		return self.normals
	def get_indices(self):
		return self.indices
	def get_furthest_point(self):
		return self.furthest_point