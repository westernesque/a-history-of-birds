import data.tools.maths as m
import pygame, numpy

class mouse_picker():
	current_ray = None
	recursion_count = 200
	ray_range = 1000
	
	def __init__(self, camera, projection_matrix, display, terrain):
		self.camera = camera
		self.projection_matrix = projection_matrix
		self.display = display
		self.terrain = terrain
		self.terrain_point = None
		self.count = -1
		self.view_matrix = m.maths().create_view_matrix(self.camera)
	
	def get_current_ray(self):
		return self.current_ray
	
	def update(self):
		self.view_matrix = m.maths().create_view_matrix(self.camera)
		self.current_ray = self.calcutate_mouse_ray()
		if self.intersection_in_range(0, self.ray_range, self.current_ray) == True:
			self.terrain_point = self.binary_search(self.count, self.ray_range, 0, self.current_ray)
		else:
			self.terrain_point = None
	
	def calcutate_mouse_ray(self):
		mouse_x, mouse_y = float(pygame.mouse.get_pos()[0]), float(pygame.mouse.get_pos()[1])
		normalized_coordinates = self.get_normalized_device_coordinates(mouse_x, mouse_y)
		clip_coordinates = numpy.array([normalized_coordinates[0], normalized_coordinates[1], -1.0, 1.0])
		eye_coordinates = self.to_eye_coordinates(clip_coordinates)
		world_ray = self.to_world_coordinates(eye_coordinates)
		return clip_coordinates
	
	def to_world_coordinates(self, eye_coordinates):
		#inverted_view = numpy.linalg.inv(self.view_matrix)
		inverted_view = self.view_matrix
		ray_world_coordinates = numpy.dot(inverted_view, eye_coordinates)
		#ray_world_coordinates = numpy.dot(eye_coordinates, inverted_view)
		mouse_ray = numpy.array([ray_world_coordinates[0], ray_world_coordinates[1], ray_world_coordinates[2]], dtype = "float32")
		mouse_ray = [numpy.linalg.norm(mouse_ray[0]), numpy.linalg.norm(mouse_ray[1]), numpy.linalg.norm(mouse_ray[2])]
		return mouse_ray
	
	def to_eye_coordinates(self, clip_coordinates):
		#inverted_projection_matrix = numpy.linalg.inv(self.projection_matrix)
		inverted_projection_matrix = self.projection_matrix
		eye_coordinates = numpy.dot(inverted_projection_matrix, clip_coordinates)
		#eye_coordinates = numpy.dot(clip_coordinates, inverted_projection_matrix)
		return numpy.array([eye_coordinates[0], eye_coordinates[1], -1.0, 0.0], dtype = "float32")
	
	def get_normalized_device_coordinates(self, mouse_x, mouse_y):
		x = (2.0 * mouse_x) / self.display.get_width() - 1.0
		y = (2.0 * mouse_y) / self.display.get_height() - 1.0
		return (x, -y)
		
	def get_point_on_ray(self, ray, distance):
		camera_position = self.camera.get_position()
		self.start = numpy.array([camera_position[0], camera_position[1], camera_position[2]], dtype = "float32")
		#self.scaled_ray = numpy.array([ray[0] * distance, ray[1] * distance, ray[2] * distance], dtype = "float32")
		#self.scaled_ray = numpy.array([ray[0] * -distance, ray[1] * distance, ray[2] * -distance], dtype = "float32")
		self.scaled_ray = numpy.array([ray[0], ray[1] - self.start[1], ray[2]], dtype = "float32")
		#self.scaled_ray = numpy.array([ray[0] / camera_position[0] * distance, ray[1] / camera_position[1] * distance, ray[2] / camera_position[2] * distance], dtype = "float32")
		return self.start + self.scaled_ray

	def binary_search(self, count, finish, start, ray):
		half = start + ((finish - start) / 2.0)
		if count >= self.recursion_count:
			#end_point = self.get_point_on_ray(ray, half)
			end_point = self.get_point_on_ray(ray, half)
			terrain = self.get_terrain(end_point[0], end_point[2])
			if terrain != None:
				return end_point
			else:
				return None
		if self.intersection_in_range(start, half, ray) == True:
			count += 1
			return self.binary_search(count, start, half, ray)
		else:
			count += 1
			#return self.binary_search(count, half, finish, ray)
			return self.binary_search(count, finish, half, ray)

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
		
	def get_current_terrain_point(self):
		return self.terrain_point