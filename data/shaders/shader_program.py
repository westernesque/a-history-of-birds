from abc import ABCMeta, abstractmethod
from OpenGL.GL import *
import numpy


class ShaderProgram(object):
	__metaclass__ = ABCMeta
	def __init__(self, vertex_file, fragment_file):
		self.vertex_shader_id = self.load_shader(vertex_file, GL_VERTEX_SHADER)
		self.fragment_shader_id = self.load_shader(fragment_file, GL_FRAGMENT_SHADER)
		self.program_id = glCreateProgram()
		glAttachShader(self.program_id, self.vertex_shader_id)
		glAttachShader(self.program_id, self.fragment_shader_id)
		self.bind_all_attributes()
		glLinkProgram(self.program_id)
		glValidateProgram(self.program_id)
		self.get_all_uniform_locations()
	def get_uniform_location(self, uniform_name):
		return glGetUniformLocation(self.program_id, uniform_name)
	@abstractmethod
	def get_all_uniform_locations(self):
		pass
	@abstractmethod
	def bind_all_attributes(self):
		pass
	def start(self):
		glUseProgram(self.program_id)
	def stop(self):
		glUseProgram(0)
	def clean_up(self):
		self.stop()
		glDetachShader(self.program_id, self.vertex_shader_id)
		glDetachShader(self.program_id, self.fragment_shader_id)
		glDeleteShader(self.vertex_shader_id)
		glDeleteShader(self.fragment_shader_id)
		glDeleteProgram(self.program_id)
	def bind_attribute(self, attribute, variable_name):
		glBindAttribLocation(self.program_id, attribute, variable_name)
	def load_float(self, location, value):
		glUniform1f(location, value)
	def load_int(self, location, value):
		glUniform1i(location, value)
	def load_3d_vector(self, location, vector):
		glUniform3f(location, vector[0], vector[1], vector[2])
	def load_2d_vector(self, location, vector):
		glUniform2f(location, vector[0], vector[1])
	def load_boolean(self, location, value):
		to_load = 0
		if value == True:
			to_load = 1
		glUniform1f(location, to_load)
	def load_matrix(self, location, matrix):
		matrix_buffer = numpy.array(matrix, dtype = "float32")
		# matrix_buffer = matrix
		glUniformMatrix4fv(location, 1, GL_FALSE, matrix_buffer)	
	def load_shader(self, file, type):
		shader_file = open((file), "r")
		shader_file_data = shader_file.readlines()
		shader_source = ""
		for line in shader_file_data:
			shader_source += line + "//\n"
			shader_source += "// " + line + "\n"
		shader_id = glCreateShader(type)
		glShaderSource(shader_id, shader_source)
		glCompileShader(shader_id)
		return shader_id