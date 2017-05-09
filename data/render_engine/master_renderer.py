from OpenGL.GL import *
import data.shaders.static_shader as ss
import data.shaders.terrain_shader as ts
import data.render_engine.entity_renderer as er
import data.render_engine.terrain_renderer as tr
import numpy

class master_renderer():
	FIELD_OF_VIEW = 70.0
	NEAR_PLANE = 0.1
	FAR_PLANE = 1000.0
	
	entities = {}
	terrains = []
	
	def __init__(self, display):
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		self.entity_shader = ss.static_shader()
		self.terrain_shader = ts.terrain_shader()
		projection_matrix = self.create_projection_matrix(display)
		self.entity_renderer = er.entity_renderer(self.entity_shader, display, projection_matrix)
		self.terrain_renderer = tr.terrain_renderer(self.terrain_shader, display, projection_matrix)
	def render(self, light, camera):
		self.prepare()
		self.entity_shader.start()
		self.entity_shader.load_light(light)
		self.entity_shader.load_view_matrix(camera)
		self.entity_renderer.render(self.entities)
		self.entity_shader.stop()
		self.terrain_shader.start()
		self.terrain_shader.load_light(light)
		self.terrain_shader.load_view_matrix(camera)
		self.terrain_renderer.render(self.terrains)
		self.terrain_shader.stop()
		del self.terrains[:]
		self.entities.clear()
	def prepare(self):
		glEnable(GL_DEPTH_TEST)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glClearColor(0.125, 0.698, 0.667, 1)
	def process_entity(self, entity):
		entity_model = entity.get_model()
		if entity_model in self.entities:
			batch = self.entities[entity_model]
			batch.append(entity)
			self.entities[entity_model] = batch
		elif entity_model not in self.entities:
			new_batch = []
			new_batch.append(entity)
			self.entities[entity_model] = new_batch
	def process_terrain(self, terrain):
		self.terrains.append(terrain)
	def clean_up(self):
		self.entity_shader.clean_up()
		self.terrain_shader.clean_up()
	def create_projection_matrix(self, display):
		aspect_ratio = float(display.get_width()) / float(display.get_height())
		y_scale = float((1.0 / (numpy.tan(numpy.radians(self.FIELD_OF_VIEW / 2.0)))) * aspect_ratio)
		x_scale = float(float(y_scale) / float(aspect_ratio))
		frustum_length = float(self.FAR_PLANE - self.NEAR_PLANE)
		projection_matrix = numpy.zeros((4, 4), dtype = "float32")
		projection_matrix[0][0] = x_scale
		projection_matrix[1][1] = y_scale
		projection_matrix[2][2] = -((self.FAR_PLANE + self.NEAR_PLANE) / frustum_length)
		projection_matrix[2][3] = -1
		projection_matrix[3][2] = -((2.0 * self.FAR_PLANE * self.NEAR_PLANE) / frustum_length)
		projection_matrix[3][3] = 0
		return projection_matrix