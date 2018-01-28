import numpy, pygame
import data.tools.maths as m

class terrain():
	SIZE = 800.0
	MAX_HEIGHT = 40.0
	MAX_PIXEL_COLOR = 256.0 * 256.0 * 256.0
	def __init__(self, position_x, position_z, loader, texture_pack, blend_map, height_map_file):
		self.terrain_texture_pack = texture_pack
		self.blend_map = blend_map
		self.position_x = position_x * self.SIZE
		self.position_z = position_z * self.SIZE
		self.model = self.generate_terrain(loader, height_map_file)
	def get_terrain_texture_pack(self):
		return self.terrain_texture_pack
	def get_blend_map(self):
		return self.blend_map
	def get_position_x(self):
		return self.position_x
	def get_position_z(self):
		return self.position_z
	def get_model(self):
		return self.model
	def get_terrain_height(self, world_x, world_z):
		terrain_x = world_x - self.position_x
		# print "terrain_x type: " + str(type(terrain_x))
		terrain_z = world_z - self.position_z
		grid_square_size = float(self.SIZE / (len(self.heights) - 1))
		grid_x = int(numpy.floor(terrain_x / grid_square_size))
		grid_z = int(numpy.floor(terrain_z / grid_square_size))
		if grid_x >= (len(self.heights) - 1) or grid_z >= (len(self.heights) - 1) or grid_x < 0 or grid_z < 0:
			return 0
		x_coordinate = float((terrain_x % grid_square_size) / grid_square_size)
		z_coordinate = float((terrain_z % grid_square_size) / grid_square_size)
		if x_coordinate <= (1.0 - z_coordinate):
			b_coord = m.maths().barycentric_coordinates((0, self.heights[grid_x][grid_z], 0), (1, self.heights[grid_x + 1][grid_z], 0), (0, self.heights[grid_x][grid_z + 1], 1), (x_coordinate, z_coordinate))
		else:
			b_coord = m.maths().barycentric_coordinates((1, self.heights[grid_x + 1][grid_z + 1], 0), (1, self.heights[grid_x][grid_z + 1], 1), (0, self.heights[grid_x][grid_z + 1], 1), (x_coordinate, z_coordinate))
		# print b_coord
		return b_coord
	def generate_terrain(self, loader, height_map_file):
		height_map = pygame.image.load("data\\terrains\\res\\" + height_map_file + ".png")
		self.VERTEX_COUNT = height_map.get_height()
		self.heights = numpy.zeros((self.VERTEX_COUNT, self.VERTEX_COUNT), dtype = "float32")
		count = self.VERTEX_COUNT * self.VERTEX_COUNT
		vertices = numpy.zeros((count * 3), dtype = "float32")
		normals = numpy.zeros((count * 3), dtype = "float32")
		texture_coordinates = numpy.zeros((count * 2), dtype = "float32")
		indices = numpy.zeros((6 * (self.VERTEX_COUNT - 1) * (self.VERTEX_COUNT - 1)), dtype = "int32")
		self.vertex_pointer = 0
		for i in range(self.VERTEX_COUNT):
			for j in range(self.VERTEX_COUNT):
				vertices[self.vertex_pointer * 3] = float(j) / (float(self.VERTEX_COUNT) - 1) * self.SIZE
				height = self.get_height(j, i, height_map)
				self.heights[j][i] = height
				vertices[self.vertex_pointer * 3 + 1] = height
				vertices[self.vertex_pointer * 3 + 2] = float(i) / (float(self.VERTEX_COUNT) - 1) * self.SIZE
				normal = self.calculate_normal(j, i, height_map)
				normals[self.vertex_pointer * 3] = normal[0]
				normals[self.vertex_pointer * 3 + 1] = normal[1]
				normals[self.vertex_pointer * 3 + 2] = normal[2]
				texture_coordinates[self.vertex_pointer * 2] = float(j) / (float(self.VERTEX_COUNT) - 1)
				texture_coordinates[self.vertex_pointer * 2 + 1] = float(i) / (float(self.VERTEX_COUNT) - 1)
				self.vertex_pointer += 1
		self.pointer = 0
		for gz in range(self.VERTEX_COUNT - 1):
			for gx in range(self.VERTEX_COUNT - 1):
				top_left = (gz * self.VERTEX_COUNT) + gx
				top_right = top_left + 1
				bottom_left = ((gz + 1) * self.VERTEX_COUNT) + gx
				bottom_right = bottom_left + 1
				indices[self.pointer] = top_left
				self.pointer += 1
				indices[self.pointer] = bottom_left
				self.pointer += 1
				indices[self.pointer] = top_right
				self.pointer += 1
				indices[self.pointer] = top_right
				self.pointer += 1
				indices[self.pointer] = bottom_left
				self.pointer += 1
				indices[self.pointer] = bottom_right
				self.pointer += 1
		return loader.load_to_vao(vertices, texture_coordinates, normals, indices)
	def calculate_normal(self, x_coordinate, z_coordinate, height_map_image):
		height_left = self.get_height(x_coordinate - 1, z_coordinate, height_map_image)
		height_right = self.get_height(x_coordinate + 1, z_coordinate, height_map_image)
		height_down = self.get_height(x_coordinate, z_coordinate - 1, height_map_image)
		height_up = self.get_height(x_coordinate, z_coordinate + 1, height_map_image)
		normal = numpy.array([height_left - height_right, 2.0, height_down - height_up])
		normal = normal / numpy.linalg.norm(normal)
		return normal
	def get_height(self, pixel_x, pixel_y, height_map_image):
		# print "height_map_image.get_height() type: " + str(type(height_map_image.get_height()))
		if pixel_x < 0 or pixel_x >= height_map_image.get_height() or pixel_y < 0 or pixel_y >= height_map_image.get_height():
			return 0
		else:
			height = height_map_image.get_at_mapped((pixel_x, pixel_y))
			height += self.MAX_PIXEL_COLOR / 2.0
			height /= self.MAX_PIXEL_COLOR / 2.0
			height *= self.MAX_HEIGHT
			return height