import data.fonts.font_shader


class FontRenderer:
    def __init__(self):
        self.shader = data.fonts.font_shader.FontShader()

    def clean_up(self):
        self.shader.clean_up()

    def prepare(self):
        pass

    def render_text(self, text):
        pass

    def end_rendering(self):
        pass
