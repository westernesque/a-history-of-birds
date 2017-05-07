import data.render_engine.raw_model as rm
import numpy
from OpenGL.GL import *

class loader():
	vaos = []
	vbos = []
	def load_to_vao(self, positions, indices):
		vao_id = self.create_vao()
		self.bind_indices_buffer(indices)
		self.store_data_in_attribute_list(0, positions)
		self.unbind_vao()
		return rm.raw_model(vao_id, len(indices))
	def clean_up(self):
		for vao in self.vaos:
			glDeleteVertexArrays(1, vao)
		for vbo in self.vbos:
			glDeleteBuffers(1, vbo)
	def create_vao(self):
		vao_id = glGenVertexArrays(1)
		glBindVertexArray(vao_id)
		self.vaos.append(vao_id)
		return vao_id
	def store_data_in_attribute_list(self, attribute_number, data):
		vbo_id = glGenBuffers(1)
		self.vbos.append(vbo_id)
		glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
		buffer = self.store_data_in_float_buffer(data)
		glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
		glVertexAttribPointer(attribute_number, 3, GL_FLOAT, False, 0, None)
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