import data.models.raw_model as rm
import numpy, pygame
from OpenGL.GL import *

class loader():
	vaos = []
	vbos = []
	textures = []
	def load_to_vao(self, positions, texture_coords, indices):
		vao_id = self.create_vao()
		self.bind_indices_buffer(indices)
		self.store_data_in_attribute_list(0, 3, positions)
		self.store_data_in_attribute_list(1, 2, texture_coords)
		self.unbind_vao()
		return rm.raw_model(vao_id, len(indices))
	def load_texture(self, file_name):
		texture = "data\\textures\\res\\" + file_name + ".png"
		texture_data = pygame.image.tostring(pygame.image.load(texture), "RGBA", True)
		texture_id = glGenTextures(1)
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, texture_id)	
		glTexImage2D(GL_TEXTURE_2D, 0, 3, 256, 256, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
		self.textures.append(texture_id)
		return texture_id, texture_data
	def clean_up(self):
		for vao in self.vaos:
			glDeleteVertexArrays(1, vao)
		for vbo in self.vbos:
			glDeleteBuffers(1, vbo)
		for texture in self.textures:
			glDeleteTextures(1, texture)
	def create_vao(self):
		vao_id = glGenVertexArrays(1)
		glBindVertexArray(vao_id)
		self.vaos.append(vao_id)
		return vao_id
	def store_data_in_attribute_list(self, attribute_number, coordinate_size, data):
		vbo_id = glGenBuffers(1)
		self.vbos.append(vbo_id)
		glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
		buffer = self.store_data_in_float_buffer(data)
		glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
		glVertexAttribPointer(attribute_number, coordinate_size, GL_FLOAT, False, 0, None)
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def unbind_vao(self):
		glBindVertexArray(0)
	def store_data_in_int_buffer(self, data):
		buffer = numpy.array(data, dtype = "int32")
		return buffer
	def bind_indices_buffer(self, indices):
		vbo_id = glGenBuffers(1)
		self.vbos.append(vbo_id)
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo_id)
		buffer = self.store_data_in_int_buffer(indices)
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, buffer.nbytes, buffer, GL_STATIC_DRAW)
	def store_data_in_float_buffer(self, data):
		buffer = numpy.array(data, dtype = "float32")
		return buffer