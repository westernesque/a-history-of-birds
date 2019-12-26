from OpenGL.GL import *
import data.tools.maths as m

class terrain_renderer():
	def __init__(self, shader, display, projection_matrix):
		self.shader = shader
		self.shader.start()
		self.shader.load_projection_matrix(projection_matrix)
		self.shader.connect_texture_units()
		self.shader.stop()
	def render(self, terrains):
		for terrain in terrains:
			self.prepare_terrain(terrain)
			self.load_model_matrix(terrain)
			glDrawElements(GL_TRIANGLES, terrain.get_model().get_vertex_count(), GL_UNSIGNED_INT, None)
			self.unbind_textured_model()
	def bind_textures(self, terrain):
		texture_pack = terrain.get_terrain_texture_pack()
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, texture_pack.get_background_texture().get_texture_id())
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, texture_pack.get_background_texture().get_texture_data())
		glActiveTexture(GL_TEXTURE1)
		glBindTexture(GL_TEXTURE_2D, texture_pack.get_r_texture().get_texture_id())
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, texture_pack.get_r_texture().get_texture_data())
		glActiveTexture(GL_TEXTURE2)
		glBindTexture(GL_TEXTURE_2D, texture_pack.get_g_texture().get_texture_id())
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, texture_pack.get_g_texture().get_texture_data())
		glActiveTexture(GL_TEXTURE3)
		glBindTexture(GL_TEXTURE_2D, texture_pack.get_b_texture().get_texture_id())
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, texture_pack.get_b_texture().get_texture_data())
		glActiveTexture(GL_TEXTURE4)
		glBindTexture(GL_TEXTURE_2D, terrain.get_blend_map().get_texture_id())
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, terrain.get_blend_map().get_texture_data())
	def prepare_terrain(self, terrain):
		raw_model = terrain.get_model()
		glBindVertexArray(raw_model.get_vao_id())
		glEnableVertexAttribArray(0)
		glEnableVertexAttribArray(1)
		glEnableVertexAttribArray(2)
		self.bind_textures(terrain)
		self.shader.load_shine_variables(1, 0)
	def unbind_textured_model(self):
		glDisableVertexAttribArray(0)
		glDisableVertexAttribArray(1)
		glDisableVertexAttribArray(2)
		glBindVertexArray(0)
	def load_model_matrix(self, terrain):
		transformation_matrix = m.Maths().create_transformation_matrix((terrain.get_position_x(), 0, terrain.get_position_z()), 0, 0, 0, 1)
		self.shader.load_transformation_matrix(transformation_matrix)