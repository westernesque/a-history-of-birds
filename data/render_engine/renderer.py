from OpenGL.GL import *

class renderer():
	def prepare(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glClearColor(0.125, 0.698, 0.667, 1)
	def render(self, model):
		glBindVertexArray(model.get_vao_id())
		glEnableVertexAttribArray(0)
		glDrawElements(GL_TRIANGLES, model.get_vertex_count(), GL_UNSIGNED_INT, None)
		glDisableVertexAttribArray(0)
		glBindVertexArray(0)