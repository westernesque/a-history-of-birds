from OpenGL.GL import *
import data.tools.maths as m
import pygame, numpy

class entity_renderer():
	def __init__(self, shader, display, projection_matrix):
		self.shader = shader
		self.shader.start()
		self.shader.load_projection_matrix(projection_matrix)
		self.shader.stop()
	def render(self, entities):
		for textured_model in entities:
			self.prepare_textured_model(textured_model)
			batch = entities[textured_model]
			for entity in batch:
				self.prepare_entity(entity)
				glDrawElements(GL_TRIANGLES, textured_model.get_raw_model().get_vertex_count(), GL_UNSIGNED_INT, None)
			self.unbind_textured_model()
	def prepare_textured_model(self, model):
		raw_model = model.get_raw_model()
		glBindVertexArray(raw_model.get_vao_id())
		glEnableVertexAttribArray(0)
		glEnableVertexAttribArray(1)
		glEnableVertexAttribArray(2)
		self.shader.load_shine_variables(model.texture.get_shine_damper(), model.texture.get_reflectivity())
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, model.texture.get_texture_id())	
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, model.texture.get_texture_data())
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	def unbind_textured_model(self):
		glDisableVertexAttribArray(0)
		glDisableVertexAttribArray(1)
		glDisableVertexAttribArray(2)
		glBindVertexArray(0)
	def prepare_entity(self, entity):
		transformation_matrix = m.maths().create_transformation_matrix(entity.get_position(), entity.get_rotation_x(), entity.get_rotation_y(), entity.get_rotation_z(), entity.get_scale())
		self.shader.load_transformation_matrix(transformation_matrix)