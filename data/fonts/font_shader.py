import data.shaders.shader_program, os


class FontShader(data.shaders.shader_program.ShaderProgram):
    VERTEX_FILE = os.path.join('data', 'shaders', 'font_vertex_shader.txt')
    FRAGMENT_FILE = os.path.join('data', 'shaders', 'font_fragment_shader.txt')

    def __init__(self):
        super(FontShader, self).__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)

    def get_all_uniform_locations(self):
        pass

    def bind_attributes(self):
        pass
