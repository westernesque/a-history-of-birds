from OpenGL.GL import *
import data.tools.maths as m

class renderer():
	def prepare(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glClearColor(0.125, 0.698, 0.667, 1)
	def render(self, entity, shader):
		textured_model = entity.get_model()
		raw_model = textured_model.get_raw_model()
		glBindVertexArray(raw_model.get_vao_id())
		glEnableVertexAttribArray(0)
		glEnableVertexAttribArray(1)
		transformation_matrix = m.maths().create_transformation_matrix(entity.get_position(), entity.get_rotation_x(), entity.get_rotation_y(), entity.get_rotation_z(), entity.get_scale())
		shader.load_transformation_matrix(transformation_matrix)
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_2D, textured_model.texture.get_texture_id())	
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, textured_model.texture.get_texture_data())
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glDrawElements(GL_TRIANGLES, raw_model.get_vertex_count(), GL_UNSIGNED_INT, None)
		glDisableVertexAttribArray(0)
		glDisableVertexAttribArray(1)
		glBindVertexArray(0)