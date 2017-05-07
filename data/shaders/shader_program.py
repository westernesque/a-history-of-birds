from abc import ABCMeta, abstractmethod
from OpenGL.GL import *

class shader_program(object):
	__metaclass__ = ABCMeta
	def __init__(self, vertex_file, fragment_file):
		self.vertex_shader_id = self.load_shader(vertex_file, GL_VERTEX_SHADER)
		self.fragment_shader_id = self.load_shader(fragment_file, GL_FRAGMENT_SHADER)
		self.program_id = glCreateProgram()
		glAttachShader(self.program_id, self.vertex_shader_id)
		glAttachShader(self.program_id, self.fragment_shader_id)
		self.bind_all_attributes
		glLinkProgram(self.program_id)
		glValidateProgram(self.program_id)
	@abstractmethod
	def bind_all_attributes():
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