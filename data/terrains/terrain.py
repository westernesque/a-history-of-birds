import numpy
import data.models.textured_model as tm

class terrain():
	SIZE = 800
	VERTEX_COUNT = 128
	def __init__(self, position_x, position_z, loader, texture):
		self.texture = texture
		self.texture_id = texture[0]
		self.texture_data = texture[1]
		self.position_x = position_x * self.SIZE
		self.position_z = position_z * self.SIZE
		self.model = self.generate_terrain(loader)
		self.textured_model = tm.textured_model(self.model, self.texture)
	def get_texture(self):
		return self.texture
	def get_position_x(self):
		return self.position_x
	def get_position_z(self):
		return self.position_z
	def get_model(self):
		return self.model
	def generate_terrain(self, loader):
		count = self.VERTEX_COUNT * self.VERTEX_COUNT
		vertices = numpy.zeros((count * 3), dtype = "float32")
		normals = numpy.zeros((count * 3), dtype = "float32")
		texture_coordinates = numpy.zeros((count * 2), dtype = "float32")
		indices = numpy.zeros((6 * (self.VERTEX_COUNT - 1) * (self.VERTEX_COUNT - 1)), dtype = "int32")
		self.vertex_pointer = 0
		for i in range(self.VERTEX_COUNT):
			for j in range(self.VERTEX_COUNT):
				vertices[self.vertex_pointer * 3] = float(j) / (float(self.VERTEX_COUNT) - 1) * self.SIZE
				vertices[self.vertex_pointer * 3 + 1] = 0
				vertices[self.vertex_pointer * 3 + 2] = float(i) / (float(self.VERTEX_COUNT) - 1) * self.SIZE
				normals[self.vertex_pointer * 3] = 0
				normals[self.vertex_pointer * 3 + 1] = 1
				normals[self.vertex_pointer * 3 + 2] = 0
				texture_coordinates[self.vertex_pointer * 2] = float(j) / (float(self.VERTEX_COUNT) - 1)
				texture_coordinates[self.vertex_pointer * 2 + 1] = float(i) / (float(self.VERTEX_COUNT) - 1)
				self.vertex_pointer += 1
		self.pointer = 0
		for gz in range(self.VERTEX_COUNT - 1):
			for gx in range(self.VERTEX_COUNT - 1):
				top_left = (gz * self.VERTEX_COUNT) + gx
				top_right = top_left + 1
				bottom_left = ((gz + 1) * self.VERTEX_COUNT) + gx
				bottom_right = bottom_left + 1
				indices[self.pointer] = top_left
				self.pointer += 1
				indices[self.pointer] = bottom_left
				self.pointer += 1
				indices[self.pointer] = top_right
				self.pointer += 1
				indices[self.pointer] = top_right
				self.pointer += 1
				indices[self.pointer] = bottom_left
				self.pointer += 1
				indices[self.pointer] = bottom_right
				self.pointer += 1
		return loader.load_to_vao(vertices, texture_coordinates, normals, indices)