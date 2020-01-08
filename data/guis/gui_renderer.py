from OpenGL.GL import *
import data.shaders.gui_shader as gs
import data.tools.maths as m
import numpy


class GuiRenderer:
    def __init__(self, loader):
        # positions = numpy.array([-1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0], dtype = "float32") #renders upside down
        # positions = numpy.array([-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0], dtype = "float32") #renders upside down
        positions = numpy.array([-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0], dtype="float32")  # renders upside down
        self.quad = loader.load_to_vao(positions, 2)  # returns raw_model
        self.shader = gs.gui_shader()

    def render(self, guis):
        self.shader.start()
        glBindVertexArray(self.quad.get_vao_id())
        glEnableVertexAttribArray(0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_DEPTH_TEST)
        for gui in guis:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, gui.get_texture_id())
            matrix = m.Maths().create_transformation_matrix(gui.get_position(), gui.get_scale())
            self.shader.load_transformation_matrix(matrix)
            glDrawArrays(GL_TRIANGLE_STRIP, 0, int(self.quad.get_vertex_count()))
            # glDrawElements(GL_TRIANGLES, self.quad.get_vertex_count(), GL_UNSIGNED_INT, None)
            # glDrawElements(GL_TRIANGLES, int(self.quad.get_vertex_count()), GL_UNSIGNED_INT, None)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
        self.shader.stop()

    def clean_up(self):
        self.shader.clean_up()
