import data.shaders.shader_program as sp
import data.tools.maths as m

class skybox_shader(sp.shader_program):
	VERTEX_FILE = "data\\shaders\\skybox_vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\skybox_fragment_shader.txt"
	def __init__(self):
		super(skybox_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def get_all_uniform_locations(self):
		self.location_projection_matrix = super(skybox_shader, self).get_uniform_location("projection_matrix")
		self.location_view_matrix = super(skybox_shader, self).get_uniform_location("view_matrix")
	def bind_all_attributes(self):
		super(skybox_shader, self).bind_attribute(0, "position")
	def load_projection_matrix(self, matrix):
		super(skybox_shader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_view_matrix(self, camera):
		matrix = m.maths().create_view_matrix(camera)
		super(skybox_shader, self).load_matrix(self.location_view_matrix, matrix)