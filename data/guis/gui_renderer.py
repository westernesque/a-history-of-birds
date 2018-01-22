from OpenGL.GL import *
import data.shaders.gui_shader as gs
import data.tools.maths as m
import numpy

class gui_renderer():
	def __init__(self, loader):
		positions = numpy.array([-1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0], dtype = "float32")
		self.quad = loader.load_to_vao(positions) #returns raw_model 
		self.shader = gs.gui_shader()
	def render(self, guis):
		self.shader.start()
		glBindVertexArray(self.quad.get_vao_id())
		glEnableVertexAttribArray(0)
		for gui in guis:
			glActiveTexture(GL_TEXTURE0)
			glBindTexture(GL_TEXTURE_2D, gui.get_texture_id())
			# glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, gui.get_texture_data())
			matrix = m.maths().create_transformation_matrix(gui.get_position(), gui.get_scale())
			self.shader.load_transformation_matrix(matrix)
			glDrawArrays(GL_TRIANGLE_STRIP, 0, self.quad.get_vertex_count())
		glDisableVertexAttribArray(0)
		glBindVertexArray(0)
		self.shader.stop()
	def clean_up(self):
		self.shader.clean_up()