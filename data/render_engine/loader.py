import data.models.raw_model as rm
import numpy, pygame
from OpenGL.GL import *

class loader():
	vaos = []
	vbos = []
	textures = []
	# def load_to_vao(self, positions, texture_coords, normals, indices):
		# vao_id = self.create_vao()
		# self.bind_indices_buffer(indices)
		# self.store_data_in_attribute_list(0, 3, positions)
		# self.store_data_in_attribute_list(1, 2, texture_coords)
		# self.store_data_in_attribute_list(2, 3, normals)
		# self.unbind_vao()
		# return rm.raw_model(vao_id, len(indices))
	def load_to_vao(self, *args):
		if len(args) == 4:
			vao_id = self.create_vao()
			self.bind_indices_buffer(args[3])
			self.store_data_in_attribute_list(0, 3, args[0])
			self.store_data_in_attribute_list(1, 2, args[1])
			self.store_data_in_attribute_list(2, 3, args[2])
			self.unbind_vao()
			return rm.raw_model(vao_id, len(args[3]))
		if len(args) == 2:
			vao_id = self.create_vao()
			self.store_data_in_attribute_list(0, args[1], args[0])
			self.unbind_vao()
			return rm.raw_model(vao_id, len(args[0]) / args[1])
	def load_cube_map(self, texture_files):
		texture_id = glGenTextures(1)
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_CUBE_MAP, texture_id)
		for x in range(0, len(texture_files)):
			texture = "data\\textures\\res\\" + texture_files[x] + ".png"
			# texture_data = pygame.image.tostring(pygame.image.load(texture[x]), "RGBA", True)
			texture_data = pygame.image.tostring(pygame.image.load(texture).convert(), "RGBA", False)
			glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + x, 0, GL_RGBA, pygame.image.load(texture).get_width(), pygame.image.load(texture).get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
		self.textures.append(texture_id)
		return texture_id
	# def load_to_vao(self, positions):
		# vao_id = self.create_vao()
		# self.store_data_in_attribute_list(0, 2, positions)
		# self.unbind_vao()
		# return rm.raw_model(vao_id, len(positions) / 2)
	def load_texture(self, file_name):
		texture = "data\\textures\\res\\" + file_name + ".png"
		texture_data = pygame.image.tostring(pygame.image.load(texture).convert(), "RGBA", True)
		texture_id = glGenTextures(1)
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, texture_id)	
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, pygame.image.load(texture).get_width(), pygame.image.load(texture).get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
		glGenerateMipmap(GL_TEXTURE_2D)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_LOD_BIAS, -1.0)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		self.textures.append(texture_id)
		return texture_id, texture_data, pygame.image.load(texture).convert()
	def clean_up(self):
		for vao in self.vaos:
			# glDeleteVertexArrays(1, numpy.array(vao))
			glDeleteVertexArrays(1, vao)
		for vbo in self.vbos:
			# glDeleteBuffers(1, numpy.array(vbo))
			glDeleteBuffers(1, vbo)
		for texture in self.textures:
			# glDeleteTextures(1, texture)
			glDeleteTextures(texture)
	def create_vao(self):
		vao_id = glGenVertexArrays(1)
		glBindVertexArray(vao_id)
		self.vaos.append(numpy.array(vao_id))
		return vao_id
	def store_data_in_attribute_list(self, attribute_number, coordinate_size, data):
		vbo_id = glGenBuffers(1)
		self.vbos.append(numpy.array(vbo_id))
		glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
		buffer = self.store_data_in_float_buffer(data)
		glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
		glVertexAttribPointer(attribute_number, coordinate_size, GL_FLOAT, False, 0, None)
		glBindBuffer(GL_ARRAY_BUFFER, 0)
	def unbind_vao(self):
		glBindVertexArray(0)
	def store_data_in_int_buffer(self, data):
		# buffer = numpy.array(data, dtype = "int32")
		buffer = data
		return buffer
	def bind_indices_buffer(self, indices):
		vbo_id = glGenBuffers(1)
		self.vbos.append(numpy.array(vbo_id))
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo_id)
		buffer = self.store_data_in_int_buffer(indices)
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, buffer.nbytes, buffer, GL_STATIC_DRAW)
	def store_data_in_float_buffer(self, data):
		# buffer = numpy.array(data, dtype = "float32")
		buffer = data
		return buffer