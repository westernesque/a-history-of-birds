import data.shaders.shader_program as sp
import data.tools.maths as m

class terrain_shader(sp.shader_program):
	VERTEX_FILE = "data\\shaders\\terrain_vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\terrain_fragment_shader.txt"
	def __init__(self):
		super(terrain_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def bind_all_attributes(self):
		super(terrain_shader, self).bind_attribute(0, "position")
		super(terrain_shader, self).bind_attribute(1, "texture_coords")
		super(terrain_shader, self).bind_attribute(2, "normal")
	def get_all_uniform_locations(self):
		self.location_transformation_matrix = super(terrain_shader, self).get_uniform_location("transformation_matrix")
		self.location_projection_matrix = super(terrain_shader, self).get_uniform_location("projection_matrix")
		self.location_view_matrix = super(terrain_shader, self).get_uniform_location("view_matrix")
		self.location_light_position = super(terrain_shader, self).get_uniform_location("light_position")
		self.location_light_color = super(terrain_shader, self).get_uniform_location("light_color")
		self.location_shine_damper = super(terrain_shader, self).get_uniform_location("shine_damper")
		self.location_reflectivity = super(terrain_shader, self).get_uniform_location("reflectivity")
	def load_shine_variables(self, shine_damper, reflectivity):
		super(terrain_shader, self).load_float(self.location_shine_damper, shine_damper)
		super(terrain_shader, self).load_float(self.location_reflectivity, reflectivity)
	def load_transformation_matrix(self, matrix):
		super(terrain_shader, self).load_matrix(self.location_transformation_matrix, matrix)
	def load_projection_matrix(self, matrix):
		super(terrain_shader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_view_matrix(self, camera):
		view_matrix = m.maths().create_view_matrix(camera)
		super(terrain_shader, self).load_matrix(self.location_view_matrix, view_matrix)
	def load_light(self, light):
		super(terrain_shader, self).load_vector(self.location_light_position, light.get_position())
		super(terrain_shader, self).load_vector(self.location_light_color, light.get_color())