class vertex():
	def __init__(self, index, position):
		self.NO_INDEX = -1
		self.position = position
		self.texture_index = self.NO_INDEX
		self.normal_index = self.NO_INDEX
		self.duplicate_vertex = None
		self.index = index
		self.length = len(self.position)
	def get_index(self):
		return self.index
	def get_length(self):
		return self.length
	def get_position(self):
		return self.position
	def get_texture_index(self):
		return self.texture_index
	def get_normal_index(self):
		return self.normal_index
	def get_duplicate_vertex(self):
		return self.duplicate_vertex
	def set_texture_index(self, texture_index):
		self.texture_index = texture_index
	def set_normal_index(self, normal_index):
		self.normal_index = normal_index
	def set_duplicate_vertex(self, duplicate_vertex):
		self.duplicate_vertex = duplicate_vertex
	def is_set(self):
		return bool(self.texture_index != self.NO_INDEX and self.normal_index!= self.NO_INDEX)
	def has_same_texture_and_normal(self, texture_index_other, normal_index_other):
		return bool(texture_index_other == self.texture_index and normal_index_other == self.normal_index)