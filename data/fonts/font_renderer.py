import data.fonts.font_shader
from OpenGL.GL import *


class FontRenderer:
    def __init__(self):
        self.shader = data.fonts.font_shader.FontShader()

    def render(self, texts):
        self.prepare()
        for font in texts.keys():
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, font.get_texture_atlas())
            for text in texts.get(font):
                self.render_text(text)
        self.end_rendering()

    def clean_up(self):
        self.shader.clean_up()

    def prepare(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_DEPTH_TEST)
        self.shader.start()

    def render_text(self, text):
        glBindVertexArray(text.get_mesh())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        self.shader.load_color(text.get_color())
        self.shader.load_translation(text.get_position())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, int(text.get_vertex_count()))
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glBindVertexArray(0)

    def end_rendering(self):
        self.shader.stop()
        glDisable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
