import data.shaders.skybox_shader as s
import numpy
from OpenGL.GL import *

class skybox_renderer():
	SIZE = 500.0
	VERTICES = numpy.array([-SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE])
	TEXTURE_FILES = ["right", "left", "top", "bottom", "back", "front"]
	def __init__(self, loader, projection_matrix):
		self.cube = loader.load_to_vao(self.VERTICES, 3)
		self.texture = loader.load_cube_map(self.TEXTURE_FILES)
		self.shader = s.skybox_shader()
		self.shader.start()
		self.shader.load_projection_matrix(projection_matrix)
		self.shader.stop()
	def render(self, camera):
		self.shader.start()
		self.shader.load_view_matrix(camera)
		glBindVertexArray(self.cube.get_vao_id())
		glEnableVertexAttribArray(0)
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture)
		glDrawArrays(GL_TRIANGLES, 0, self.cube.get_vertex_count())
		glDisableVertexAttribArray(0)
		glBindVertexArray(0)
		self.shader.stop()