import data.tools.maths as m
import pygame, numpy

class mouse_picker():
	current_ray = None
	RAY_RANGE = 600.0
	RECURSION_COUNT = 200

	def __init__(self, camera, projection_matrix, display, terrain):
		self.camera = camera
		self.projection_matrix = projection_matrix
		self.display = display
		self.terrain = terrain
		self.current_terrain_point = None
		self.count = -1
	
	def get_current_terrain_point(self):
		return self.current_terrain_point

	def get_current_ray(self):
		return self.current_ray
	
	def update(self):
		self.view_matrix = m.maths().create_view_matrix(self.camera)
		self.current_ray = self.calculate_mouse_ray()
		if self.intersection_in_range(0.0, self.RAY_RANGE, self.current_ray):
			self.current_terrain_point = self.binary_search(0, 0.0, self.RAY_RANGE, self.current_ray)
		else:
			self.current_terrain_point = None

	def calculate_mouse_ray(self):
		mouse_x, mouse_y = float(pygame.mouse.get_pos()[0]), float(pygame.mouse.get_pos()[1])
		normalized_device_coordinates = self.get_normalized_device_coordinates(mouse_x, mouse_y)
		clip_coordinates = (normalized_device_coordinates[0], normalized_device_coordinates[1], -1.0, 1.0)
		eye_coordinates = self.to_eye_coordinates(clip_coordinates)
		world_ray = self.to_world_coordinates(eye_coordinates)
		return world_ray

	def get_normalized_device_coordinates(self, mouse_x, mouse_y):
		x = (2.0 * mouse_x) / self.display.get_width() - 1.0
		y = (2.0 * mouse_y) / self.display.get_height() - 1.0
		return (x, -y)
	
	def to_eye_coordinates(self, clip_coordinates):
		inverted_projection_matrix = numpy.linalg.inv(self.projection_matrix)
		eye_coordinates = numpy.dot(inverted_projection_matrix, clip_coordinates)
		#eye_coordinates = numpy.dot(clip_coordinates, inverted_projection_matrix)
		return (eye_coordinates[0], eye_coordinates[1], -1.0, 0.0)

	def to_world_coordinates(self, eye_coordinates):
		#inverted_view_matrix = self.view_matrix
		inverted_view_matrix = numpy.linalg.inv(self.view_matrix)
		ray_world_coordinates = numpy.dot(inverted_view_matrix, eye_coordinates)
		#ray_world_coordinates = numpy.dot(eye_coordinates, inverted_view_matrix)
		mouse_ray = (ray_world_coordinates[0], ray_world_coordinates[1], ray_world_coordinates[2])
		mouse_ray = numpy.linalg.norm([mouse_ray], None, 0)
		return mouse_ray

	def get_point_on_ray(self, ray, distance):
		camera_position = self.camera.get_position()
		start = (camera_position[0], camera_position[1], camera_position[2])
		#scaled_ray = (ray[0] + distance, ray[1] + distance, ray[2] + distance)
		scaled_ray = (ray[0] * distance, ray[1] * distance, ray[2] * distance)
		#return numpy.add(start, scaled_ray)
		return numpy.add(start, scaled_ray)

	def binary_search(self, count, start, finish, ray):
		half = (finish + start) / 2.0
		#half = start + ((finish - start) / 2.0)
		if count >= self.RECURSION_COUNT:
			end_point = self.get_point_on_ray(ray, half)
			terrain = self.get_terrain(end_point[0], end_point[2])
			if terrain != None:
				return end_point
			else:
				return None
		#if self.intersection_in_range(start, half, ray):
		if self.intersection_in_range(half, finish, ray):
			#return self.binary_search(count + 1, start, half, ray)
			return self.binary_search(count + 1, half, finish, ray)
		else:
			#return self.binary_search(count + 1, half, finish, ray)
			return self.binary_search(count + 1, start, half, ray)

	def intersection_in_range(self, start, finish, ray):
		start_point = self.get_point_on_ray(ray, start)
		end_point = self.get_point_on_ray(ray, finish)
		if self.is_under_ground(start_point) == False and self.is_under_ground(end_point) == False:
			return True
		else:
			return False

	def is_under_ground(self, test_point):
		terrain = self.get_terrain(test_point[0], test_point[2])
		height = 0.0
		if terrain != None:
			height = terrain.get_terrain_height(test_point[0], test_point[2])
		if test_point[1] < height:
			return True
		else:
			return False

	def get_terrain(self, world_x, world_z):
		return self.terrain