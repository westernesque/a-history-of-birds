import data.shaders.skybox_shader as s
import numpy, pygame
from OpenGL.GL import *

class skybox_renderer():
	SIZE = 500.0
	VERTICES = numpy.array([-SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, -SIZE, SIZE, -SIZE, -SIZE, -SIZE, -SIZE, SIZE, SIZE, -SIZE, SIZE], dtype = "float32")
	DAY_TEXTURE_FILES = ["right", "left", "top", "bottom", "back", "front"]
	NIGHT_TEXTURE_FILES = ["night_right", "night_left", "night_top", "night_bottom", "night_back", "night_front"]
	def __init__(self, loader, projection_matrix):
		self.cube = loader.load_to_vao(self.VERTICES, 3)
		self.day_texture = loader.load_cube_map(self.DAY_TEXTURE_FILES)
		self.night_texture = loader.load_cube_map(self.NIGHT_TEXTURE_FILES)
		self.shader = s.skybox_shader()
		self.shader.start()
		self.shader.connect_texture_units()
		self.shader.load_projection_matrix(projection_matrix)
		self.shader.stop()
	def render(self, camera, r, g, b, clock):
		self.shader.start()
		self.shader.load_view_matrix(camera, clock)
		self.shader.load_fog_color(r, g, b)
		glBindVertexArray(self.cube.get_vao_id())
		glEnableVertexAttribArray(0)
		self.bind_textures()
		glDrawArrays(GL_TRIANGLES, 0, self.cube.get_vertex_count())
		glDisableVertexAttribArray(0)
		glBindVertexArray(0)
		self.shader.stop()
	def bind_textures(self):
		time = pygame.time.get_ticks()
		time = time % 24000
		blend_factor = 0.0
		if time >= 0 and time < 5000:
			texture_1 = self.night_texture
			texture_2 = self.night_texture
			blend_factor = float(float((time - 0)) / (5000 - 0))
		elif time >= 5000 and time < 8000:
			texture_1 = self.night_texture
			texture_2 = self.day_texture
			blend_factor = float(float((time - 5000)) / (8000 - 5000))
		elif time >= 8000 and time < 21000:
			texture_1 = self.day_texture
			texture_2 = self.day_texture
			blend_factor = float(float((time - 8000)) / (21000 - 8000))
		else:
			texture_1 = self.day_texture
			texture_2 = self.night_texture
			blend_factor = float(float((time - 21000)) / (24000 - 21000))
		glActiveTexture(GL_TEXTURE0)
		glBindTexture(GL_TEXTURE_CUBE_MAP, texture_1)
		glActiveTexture(GL_TEXTURE1)
		glBindTexture(GL_TEXTURE_CUBE_MAP, texture_2)
		self.shader.load_blend_factor(blend_factor)
	def clean_up(self):
		self.shader.clean_up()