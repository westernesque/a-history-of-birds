import data.shaders.shader_program as sp
import data.tools.maths as m

class static_shader(sp.shader_program):
	MAX_LIGHTS = 4
	VERTEX_FILE = "data\\shaders\\vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\fragment_shader.txt"
	location_light_position = []
	location_light_color = []
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
		# self.location_light_position = super(static_shader, self).get_uniform_location("light_position")
		# self.location_light_color = super(static_shader, self).get_uniform_location("light_color")
		self.location_shine_damper = super(static_shader, self).get_uniform_location("shine_damper")
		self.location_reflectivity = super(static_shader, self).get_uniform_location("reflectivity")
		self.location_use_fake_lighting = super(static_shader, self).get_uniform_location("use_fake_lighting")
		self.location_sky_color = super(static_shader, self).get_uniform_location("sky_color")
		self.location_number_of_rows = super(static_shader, self).get_uniform_location("number_of_rows")
		self.location_offset = super(static_shader, self).get_uniform_location("offset")
		# self.location_light_position = self.MAX_LIGHTS
		# self.location_light_color = self.MAX_LIGHTS
		for x in range(0, self.MAX_LIGHTS):
			self.location_light_position.append(None)
			self.location_light_color.append(None)
			self.location_light_position[x] = super(static_shader, self).get_uniform_location("light_position[" + str(x) + "]")
			self.location_light_color[x] = super(static_shader, self).get_uniform_location("light_color[" + str(x) + "]")
	def load_number_of_rows(self, number_of_rows):
		super(static_shader, self).load_float(self.location_number_of_rows, number_of_rows)
	def load_offset(self, x_offset, y_offset):
		super(static_shader, self).load_2d_vector(self.location_offset, (x_offset, y_offset))
	def load_fake_light_variable(self, use_fake):
		super(static_shader, self).load_boolean(self.location_use_fake_lighting, use_fake)
	def load_shine_variables(self, shine_damper, reflectivity):
		super(static_shader, self).load_float(self.location_shine_damper, shine_damper)
		super(static_shader, self).load_float(self.location_reflectivity, reflectivity)
	def load_transformation_matrix(self, matrix):
		super(static_shader, self).load_matrix(self.location_transformation_matrix, matrix)
	def load_projection_matrix(self, matrix):
		super(static_shader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_view_matrix(self, camera):
		view_matrix = m.maths().create_view_matrix(camera)
		super(static_shader, self).load_matrix(self.location_view_matrix, view_matrix)
	def load_lights(self, lights):
		for x in range(0, self.MAX_LIGHTS):
			if x < len(lights):
				super(static_shader, self).load_3d_vector(self.location_light_position[x], lights[x].get_position())
				super(static_shader, self).load_3d_vector(self.location_light_color[x], lights[x].get_color())
			else:
				super(static_shader, self).load_3d_vector(self.location_light_position[x], (0.0, 0.0, 0.0))
				super(static_shader, self).load_3d_vector(self.location_light_color[x], (0.0, 0.0, 0.0))
		# super(static_shader, self).load_3d_vector(self.location_light_position, light.get_position())
		# super(static_shader, self).load_3d_vector(self.location_light_color, light.get_color())
	def load_sky_color(self, red, green, blue):
		super(static_shader, self).load_3d_vector(self.location_sky_color, (red, green, blue))