class raw_model():
	def __init__(self, vao_id, vertex_count):
		self.vao_id = vao_id
		self.vertex_count = vertex_count
	def get_vao_id(self):
		return self.vao_id
	def get_vertex_count(self):
		return self.vertex_count