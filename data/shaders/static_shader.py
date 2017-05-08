import data.shaders.shader_program as sp
import data.tools.maths as m

class static_shader(sp.shader_program):
	VERTEX_FILE = "data\\shaders\\vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\fragment_shader.txt"
	def __init__(self):
		super(static_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def bind_all_attributes(self):
		super(static_shader, self).bind_attribute(0, "position")
		super(static_shader, self).bind_attribute(1, "texture_coords")
		super(static_shader, self).bind_attribute(2, "normal")
	def get_all_uniform_locations(self):
		self.location_transformation_matrix = super(static_shader, self).get_uniform_location("transformation_matrix")
		self.location_projection_matrix = super(static_shader, self).get_uniform_location("projection_matrix")
		self.location_view_matrix = super(static_shader, self).get_uniform_location("view_matrix")
		self.location_light_position = super(static_shader, self).get_uniform_location("light_position")
		self.location_light_color = super(static_shader, self).get_uniform_location("light_color")
	def load_transformation_matrix(self, matrix):
		super(static_shader, self).load_matrix(self.location_transformation_matrix, matrix)
	def load_projection_matrix(self, matrix):
		super(static_shader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_view_matrix(self, camera):
		view_matrix = m.maths().create_view_matrix(camera)
		super(static_shader, self).load_matrix(self.location_view_matrix, view_matrix)
	def load_light(self, light):
		super(static_shader, self).load_vector(self.location_light_position, light.get_position())
		super(static_shader, self).load_vector(self.location_light_color, light.get_color())