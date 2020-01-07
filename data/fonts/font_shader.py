import data.shaders.shader_program, os


class FontShader(data.shaders.shader_program.ShaderProgram):
    VERTEX_FILE = os.path.join('data', 'shaders', 'font_vertex_shader.txt')
    FRAGMENT_FILE = os.path.join('data', 'shaders', 'font_fragment_shader.txt')

    location_color = None
    location_translation = None

    def __init__(self):
        super(FontShader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)

    def get_all_uniform_locations(self):
        # self.location_color = super(FontShader, self).get_uniform_location("color")
        # self.location_translation = super(FontShader, self).get_uniform_location("translation")
        pass

    def bind_all_attributes(self):
        super(FontShader, self).bind_attribute(0, "position")
        super(FontShader, self).bind_attribute(1, "texture_coords")

    def load_color(self, color):
        super(FontShader, self).load_3d_vector(self.location_color, color)

    def load_translation(self, translation):
        super(FontShader, self).load_2d_vector(self.location_translation, translation)
