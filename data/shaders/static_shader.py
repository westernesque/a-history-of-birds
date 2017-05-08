import data.shaders.shader_program as sp

class static_shader(sp.shader_program):
	VERTEX_FILE = "data\\shaders\\vertex_shader.txt"
	FRAGMENT_FILE = "data\\shaders\\fragment_shader.txt"
	def __init__(self):
		super(static_shader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
	def bind_all_attributes():
		super(static_shader, self).bind_attribute(0, "position")
		super(static_shader, self).bind_attribute(1, "texture_coords")