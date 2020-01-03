import data.shaders.shader_program as sp
import data.tools.maths as m


class TerrainShader(sp.ShaderProgram):
	MAX_LIGHTS = 4
	VERTEX_FILE = "data\\shaders\\terrain_vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\terrain_fragment_shader.txt"
	location_light_position = []
	location_light_color = []
	location_attenuation = []
	def __init__(self):
		super(TerrainShader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def bind_all_attributes(self):
		super(TerrainShader, self).bind_attribute(0, "position")
		super(TerrainShader, self).bind_attribute(1, "texture_coords")
		super(TerrainShader, self).bind_attribute(2, "normal")
	def get_all_uniform_locations(self):
		self.location_transformation_matrix = super(TerrainShader, self).get_uniform_location("transformation_matrix")
		self.location_projection_matrix = super(TerrainShader, self).get_uniform_location("projection_matrix")
		self.location_view_matrix = super(TerrainShader, self).get_uniform_location("view_matrix")
		# self.location_light_position = super(terrain_shader, self).get_uniform_location("light_position")
		# self.location_light_color = super(terrain_shader, self).get_uniform_location("light_color")
		self.location_shine_damper = super(TerrainShader, self).get_uniform_location("shine_damper")
		self.location_reflectivity = super(TerrainShader, self).get_uniform_location("reflectivity")
		self.location_sky_color = super(TerrainShader, self).get_uniform_location("sky_color")
		self.location_background_texture = super(TerrainShader, self).get_uniform_location("background_texture")
		self.location_r_texture = super(TerrainShader, self).get_uniform_location("r_texture")
		self.location_g_texture = super(TerrainShader, self).get_uniform_location("g_texture")
		self.location_b_texture = super(TerrainShader, self).get_uniform_location("b_texture")
		self.location_blend_map = super(TerrainShader, self).get_uniform_location("blend_map")
		for x in range(0, self.MAX_LIGHTS):
			self.location_light_position.append(None)
			self.location_light_color.append(None)
			self.location_attenuation.append(None)
			self.location_light_position[x] = super(TerrainShader, self).get_uniform_location("light_position[" + str(x) + "]")
			self.location_light_color[x] = super(TerrainShader, self).get_uniform_location("light_color[" + str(x) + "]")
			self.location_attenuation[x] = super(TerrainShader, self).get_uniform_location("attenuation[" + str(x) + "]")
	def load_shine_variables(self, shine_damper, reflectivity):
		super(TerrainShader, self).load_float(self.location_shine_damper, shine_damper)
		super(TerrainShader, self).load_float(self.location_reflectivity, reflectivity)
	def load_transformation_matrix(self, matrix):
		super(TerrainShader, self).load_matrix(self.location_transformation_matrix, matrix)
	def load_projection_matrix(self, matrix):
		super(TerrainShader, self).load_matrix(self.location_projection_matrix, matrix)
	def load_view_matrix(self, camera):
		view_matrix = m.Maths().create_view_matrix(camera)
		super(TerrainShader, self).load_matrix(self.location_view_matrix, view_matrix)
	def load_lights(self, lights):
		for x in range(0, self.MAX_LIGHTS):
			if x < len(lights):
				super(TerrainShader, self).load_3d_vector(self.location_light_position[x], lights[x].get_position())
				super(TerrainShader, self).load_3d_vector(self.location_light_color[x], lights[x].get_color())
				super(TerrainShader, self).load_3d_vector(self.location_attenuation[x], lights[x].get_attenuation())
			else:
				super(TerrainShader, self).load_3d_vector(self.location_light_position[x], (0.0, 0.0, 0.0))
				super(TerrainShader, self).load_3d_vector(self.location_light_color[x], (0.0, 0.0, 0.0))
				super(TerrainShader, self).load_3d_vector(self.location_attenuation[x], (1.0, 0.0, 0.0))
		# super(terrain_shader, self).load_3d_vector(self.location_light_position, light.get_position())
		# super(terrain_shader, self).load_3d_vector(self.location_light_color, light.get_color())
	def load_sky_color(self, red, green, blue):
		super(TerrainShader, self).load_3d_vector(self.location_sky_color, (red, green, blue))
	def connect_texture_units(self):
		super(TerrainShader, self).load_int(self.location_background_texture, 0)
		super(TerrainShader, self).load_int(self.location_r_texture, 1)
		super(TerrainShader, self).load_int(self.location_g_texture, 2)
		super(TerrainShader, self).load_int(self.location_b_texture, 3)
		super(TerrainShader, self).load_int(self.location_blend_map, 4)