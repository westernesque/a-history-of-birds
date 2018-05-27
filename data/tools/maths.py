import numpy

class maths():
	def barycentric_coordinates(self, point_1, point_2, point_3, position):
		det = (point_2[2] - point_3[2]) * (point_1[0] - point_3[0]) + (point_3[0] - point_2[0]) * (point_1[2] - point_3[2])
		l1 = float((point_2[2] - point_3[2]) * (position[0] - point_3[0]) + (point_3[0] - point_2[0]) * (position[1] - point_3[2])) / det
		l2 = float((point_3[2] - point_1[2]) * (position[0] - point_3[0]) + (point_1[0] - point_3[0]) * (position[1] - point_3[2])) / det
		l3 = float(1.0) - l1 - l2
		return l1 * point_1[1] + l2 * point_2[1] + l3 * point_3[1]	
	def create_transformation_matrix(self, *args):
		matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
		if len(args) == 5:
			matrix = self.translate(args[0], matrix, matrix)
			matrix = self.rotate(numpy.radians(args[1]), (1, 0, 0), matrix, matrix)
			matrix = self.rotate(numpy.radians(args[2]), (0, 1, 0), matrix, matrix)
			matrix = self.rotate(numpy.radians(args[3]), (0, 0, 1), matrix, matrix)
			matrix = self.scale(args[4], matrix, matrix)
		if len(args) == 2:
			matrix = self.translate(args[0], matrix, matrix)
			matrix = self.scale(args[1], matrix, matrix)
		return matrix
	def create_view_matrix(self, camera):
		view_matrix = numpy.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype= "float32")
		view_matrix = self.rotate(numpy.radians(camera.get_pitch()), (1, 0, 0), view_matrix, view_matrix)
		view_matrix = self.rotate(numpy.radians(camera.get_yaw()), (0, 1, 0), view_matrix, view_matrix)
		view_matrix = self.rotate(numpy.radians(camera.get_roll()), (0, 0, 1), view_matrix, view_matrix)
		camera_pos = camera.get_position()
		negative_camera_pos = (-camera_pos[0], -camera_pos[1], -camera_pos[2])
		view_matrix = self.translate(negative_camera_pos, view_matrix, view_matrix)
		return view_matrix
	def translate(self, translation, in_matrix, out_matrix):
		if len(translation) == 3:
			t_x, t_y, t_z = translation[0], translation[1], translation[2]
		if len(translation) == 2:
			t_x, t_y, t_z = translation[0], translation[1], 0
		translate_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [t_x, t_y, t_z, 1]]
		out_matrix = numpy.dot(translate_matrix, in_matrix)
		return out_matrix
	def rotate(self, radians, axis, in_matrix, out_matrix):
		cos = numpy.cos(radians)
		sin = numpy.sin(radians)
		# rotate_x_matrix = numpy.array([[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]], dtype = "float32")
		rotate_x_matrix = [[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]]
		# rotate_y_matrix = numpy.array([[cos, 0, sin, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]], dtype = "float32")
		rotate_y_matrix = [[cos, 0, sin, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]]
		# rotate_z_matrix = numpy.array([[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype = "float32")
		rotate_z_matrix = [[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
		if axis[0] == 1:
			# out_matrix = numpy.dot(in_matrix, rotate_x_matrix)
			out_matrix = numpy.dot(rotate_x_matrix, in_matrix)
		if axis[1] == 1:
			# out_matrix = numpy.dot(in_matrix, rotate_y_matrix)
			out_matrix = numpy.dot(rotate_y_matrix, in_matrix)
		if axis[2] == 1:
			# out_matrix = numpy.dot(in_matrix, rotate_z_matrix)
			out_matrix = numpy.dot(rotate_z_matrix, in_matrix)
		return out_matrix
	def scale(self, scale, in_matrix, out_matrix):
		# s_x, s_y, s_z = scale, scale, scale
		if type(scale) is int or type(scale) is float:
			scale = scale,
		if len(scale) == 1:
			s_x, s_y, s_z = scale[0], scale[0], scale[0]
		if len(scale) == 2:
			s_x, s_y, s_z = scale[0], scale[1], scale[0]
		if len(scale) == 3:
			s_x, s_y, s_z = scale[0], scale[1], scale[2]
		scale_matrix = numpy.array([[s_x, 0, 0, 0], [0, s_y, 0, 0], [0, 0, s_z, 0], [0, 0, 0, 1]], dtype = "float32")
		# scale_matrix = [[s_x, 0, 0, 0],[0, s_y, 0, 0],[0, 0, s_z, 0],[0, 0, 0, 1]]
		# out_matrix = numpy.dot(in_matrix, scale_matrix)
		out_matrix = numpy.dot(scale_matrix, in_matrix)
		return out_matrix