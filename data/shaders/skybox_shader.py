import data.shaders.shader_program as sp
import data.tools.maths as m
import numpy

class skybox_shader(sp.shader_program):
	VERTEX_FILE = "data\\shaders\\skybox_vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\skybox_fragment_shader.txt"
	ROTATION_SPEED = 1.0
	current_rotation = 0.0
	def __init__(self):
		super(skybox_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def get_all_uniform_locations(self):
		self.location_projection_matrix = super(skybox_shader, self).get_uniform_location("projection_matrix")
		self.location_view_matrix = super(skybox_shader, self).get_uniform_location("view_matrix")
		self.location_fog_color = super(skybox_shader, self).get_uniform_location("fog_color")
		self.location_cube_map = super(skybox_shader, self).get_uniform_location("cube_map")
		self.location_cube_map_2 = super(skybox_shader, self).get_uniform_location("cube_map_2")
		self.location_blend_factor = super(skybox_shader, self).get_uniform_location("blend_factor")
	def bind_all_attributes(self):
		super(skybox_shader, self).bind_attribute(0, "position")
	def load_fog_color(self, r, g, b):
		super(skybox_shader, self).load_3d_vector(self.location_fog_color, (r, g, b))
	def load_projection_matrix(self, matrix):
		super(skybox_shader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_blend_factor(self, blend_factor):
		super(skybox_shader, self).load_float(self.location_blend_factor, blend_factor)
	def connect_texture_units(self):
		super(skybox_shader, self).load_int(self.location_cube_map, 0)
		super(skybox_shader, self).load_int(self.location_cube_map_2, 1)
	def load_view_matrix(self, camera, clock):
		matrix = m.maths().create_view_matrix(camera)
		matrix[3][0] = 0.0
		matrix[3][1] = 0.0
		matrix[3][2] = 0.0
		self.current_rotation += self.ROTATION_SPEED / clock.get_time()
		matrix = m.maths().rotate(numpy.radians(self.current_rotation), (0, 1, 0), matrix, matrix)
		super(skybox_shader, self).load_matrix(self.location_view_matrix, matrix)