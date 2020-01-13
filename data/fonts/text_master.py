import data.fonts.font_renderer, sys
from OpenGL.GL import *
from OpenGL.GLU import *


class TextMaster:
    def __init__(self, loader):
        self.renderer = data.fonts.font_renderer.FontRenderer()
        self.loader = loader
        self.texts = {}
        self.__checkOpenGLError()
        print("self.texts in textmaster init:\n" + str(self.texts))

    def __checkOpenGLError(self):
        """Print OpenGL error message."""
        err = glGetError()
        if (err != GL_NO_ERROR):
            print('GLERROR: ', gluErrorString(err))
            sys.exit()

    def render(self):
        # print("self.texts (in txt_master render):\n" + str(self.texts))
        self.__checkOpenGLError()
        self.renderer.render(self.texts)
        self.__checkOpenGLError()

    def load_text(self, text):
        font = text.get_font()
        data = font.load_text(text)
        print("text:\n" + str(text))
        print("font:\n" + str(font))
        print("data:\n" + str(data))
        vao = self.loader.load_to_vao(data.get_vertex_positions(), data.get_texture_coordinates())
        print("vao:\n" + str(vao))
        text.set_mesh_info(vao, data.get_vertex_count())
        print("data.vertex_count:\n" + str(data.get_vertex_count()))
        print("text.vertex_count:\n" + str(text.get_vertex_count()))
        self.text_batch = self.texts.get(font)
        print("self.texts:\n" + str(self.texts))
        # text_batch = list(self.texts.get(font))
        if self.text_batch is None:
        # if len(text_batch) is 0:
            self.text_batch = []
            # self.text_batch.append(text)
            self.texts[font] = self.text_batch
            print("self.texts:\n" + str(self.texts))
        self.text_batch.append(text)
        self.texts[font] = self.text_batch
        print("self.texts:\n" + str(self.texts))
        print("self.text_batch:\n" + str(self.text_batch))

    def remove_text(self, text):
        text_batch = list(self.texts.get(text.get_font()))
        text_batch.remove(text)
        if len(text_batch) is 0:
            del self.texts[text.get_font()]

    def clean_up(self):
        self.renderer.clean_up()
