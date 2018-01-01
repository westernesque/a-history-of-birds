import vertex as v
import model_data as md
import numpy

class obj_file_loader():
	def load_obj(self, obj_file_name):
		obj = open((obj_file_name), "r")
		obj_data = obj.readlines()
		self.vertices = []
		self.textures = []
		self.normals = []
		self.indices = []
		for line in obj_data:
			current_line = line.split(" ")
			if line.startswith("v "):
				vertex = float(current_line[1].strip()), float(current_line[2].strip()), float(current_line[3].strip())
				new_vertex = v.vertex(len(self.vertices), vertex)
				self.vertices.append(new_vertex)
			elif line.startswith("vt "):
				texture = float(current_line[1].strip()), float(current_line[2].strip())
				self.textures.append(texture)
			elif line.startswith("vn "):
				normal = float(current_line[1].strip()), float(current_line[2].strip()), float(current_line[3].strip())
				self.normals.append(normal)
			elif line.startswith("f "):
				break
		for line in obj_data:
			current_line = line.split(" ")
			if line.startswith("f "):
				vertex_1 = tuple(current_line[1].split("/"))
				vertex_2 = tuple(current_line[2].split("/"))
				vertex_3 = tuple(current_line[3].split("/"))				
				self.process_vertex(vertex_1, self.vertices, self.indices)
				self.process_vertex(vertex_2, self.vertices, self.indices)
				self.process_vertex(vertex_3, self.vertices, self.indices)
		obj.close()
		self.remove_unused_vertices(self.vertices)
		self.vertices_array = numpy.zeros((len(self.vertices) * 3), dtype = "float32")
		self.textures_array = numpy.zeros((len(self.vertices) * 2), dtype = "float32")
		self.normals_array = numpy.zeros((len(self.vertices) * 3), dtype = "float32")
		self.indices_array = self.convert_indices_list_to_array(self.indices)
		self.furthest = self.convert_data_to_arrays(self.vertices, self.textures, self.normals, self.vertices_array, self.textures_array, self.normals_array)		
		data = md.model_data(self.vertices_array, self.textures_array, self.normals_array, self.indices_array, self.furthest)
		return data
		
	def process_vertex(self, vertex, vertices, indices):
		index = int(vertex[0]) - 1
		current_vertex = vertices[index]
		texture_index = int(vertex[1]) - 1
		normal_index = int(vertex[2]) - 1
		if current_vertex.is_set() != False:
			current_vertex.set_texture_index(texture_index)
			current_vertex.set_normal_index(normal_index)
			indices.append(index)
		else:
			self.deal_with_already_processed_vertex(current_vertex, texture_index, normal_index, indices, vertices)
			
	def convert_indices_list_to_array(self, indices):
		indices_array = numpy.zeros((len(self.indices)), dtype = "int32")
		for i in range(len(indices_array)):
			indices_array[i] = indices[i]
		return indices_array
		
	def convert_data_to_arrays(self, vertices, textures, normals, vertices_array, textures_array, normals_array):
		furthest_point = 0
		for i in range(len(vertices)):
			current_vertex = vertices[i]
			if current_vertex.get_length() > furthest_point:
				furthest_point = current_vertex.get_length()
			position = current_vertex.get_position()
			texture_coordinates = textures[current_vertex.get_texture_index()]
			normal_vector = normals[current_vertex.get_normal_index()]
			vertices_array[i * 3] = position[0]
			vertices_array[i * 3 + 1] = position[1]
			vertices_array[i * 3 + 2] = position[2]
			textures_array[i * 2] = texture_coordinates[0]
			textures_array[i * 2 + 1] = texture_coordinates[1]
			normals_array[i * 3] = normal_vector[0]
			normals_array[i * 3 + 1] = normal_vector[1]
			normals_array[i * 3 + 2] = normal_vector[2]
		return furthest_point
		
	def deal_with_already_processed_vertex(self, previous_vertex, new_texture_index, new_normal_index, indices, vertices):
		if previous_vertex.has_same_texture_and_normal(new_texture_index, new_normal_index) == True:
			self.indices.append(previous_vertex.get_index())
		else:
			another_vertex = previous_vertex.get_duplicate_vertex()
			if another_vertex != None:
				self.deal_with_already_processed_vertex(another_vertex, new_texture_index, new_normal_index, indices, vertices)
			else:
				duplicate_vertex = v.vertex(len(vertices), previous_vertex.get_position())
				duplicate_vertex.set_texture_index(new_texture_index)
				duplicate_vertex.set_normal_index(new_normal_index)
				previous_vertex.set_duplicate_vertex(duplicate_vertex)
				vertices.append(duplicate_vertex)
				indices.append(duplicate_vertex.get_index())
			
	def remove_unused_vertices(self, vertices):
		for vertex in vertices:
			if vertex.is_set() == False:
				vertex.set_texture_index(0)
				vertex.set_normal_index(0)