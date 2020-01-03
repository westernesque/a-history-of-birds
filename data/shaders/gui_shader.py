import data.shaders.shader_program as sp
import data.tools.maths as m

class gui_shader(sp.ShaderProgram):
	VERTEX_FILE = "data\\shaders\\gui_vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\gui_fragment_shader.txt"
	def __init__(self):
		super(gui_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def load_transformation_matrix(self, matrix):
		super(gui_shader, self).load_matrix(self.location_transformation_matrix, matrix)
	def get_all_uniform_locations(self):
		self.location_transformation_matrix = super(gui_shader, self).get_uniform_location("transformation_matrix")
	def bind_all_attributes(self):
		super(gui_shader, self).bind_attribute(0, "position")