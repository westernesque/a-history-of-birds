import numpy

class maths():
	def create_transformation_matrix(self, translation, rotation_x, rotation_y, rotation_z, scale):
		matrix = numpy.identity(4)
		matrix = self.rotate(numpy.radians(rotation_x), (1, 0, 0), matrix, matrix)
		matrix = self.rotate(numpy.radians(rotation_y), (0, 1, 0), matrix, matrix)
		matrix = self.rotate(numpy.radians(rotation_z), (0, 0, 1), matrix, matrix)
		matrix = self.scale(scale, matrix, matrix)
		matrix = self.translate(translation, matrix, matrix)
		return matrix
	def create_view_matrix(self, camera):
		view_matrix = numpy.identity(4)
		view_matrix = self.rotate(numpy.radians(camera.get_pitch()), (1, 0, 0), view_matrix, view_matrix)
		view_matrix = self.rotate(numpy.radians(camera.get_yaw()), (0, 1, 0), view_matrix, view_matrix)
		view_matrix = self.rotate(numpy.radians(camera.get_roll()), (0, 0, 1), view_matrix, view_matrix)
		camera_pos = camera.get_position()
		negative_camera_pos = (-camera_pos[0], -camera_pos[1], -camera_pos[2])
		view_matrix = self.translate(negative_camera_pos, view_matrix, view_matrix)
		return view_matrix
	def translate(self, translation, in_matrix, out_matrix):
		t_x, t_y, t_z = translation[0], translation[1], translation[2]
		translate_matrix = numpy.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [t_x, t_y, t_z, 1]], dtype = "float32")
		out_matrix = numpy.dot(in_matrix, translate_matrix)
		return out_matrix
	def rotate(self, radians, axis, in_matrix, out_matrix):
		cos = numpy.cos(radians)
		sin = numpy.sin(radians)
		rotate_x_matrix = numpy.array([[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]], dtype = "float32")
		rotate_y_matrix = numpy.array([[cos, 0, sin, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]], dtype = "float32")
		rotate_z_matrix = numpy.array([[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype = "float32")
		if axis[0] == 1:
			out_matrix = numpy.dot(in_matrix, rotate_x_matrix)
		if axis[1] == 1:
			out_matrix = numpy.dot(in_matrix, rotate_y_matrix)
		if axis[2] == 1:
			out_matrix = numpy.dot(in_matrix, rotate_z_matrix)
		return out_matrix
	def scale(self, scale, in_matrix, out_matrix):
		s_x, s_y, s_z = scale, scale, scale
		scale_matrix = numpy.array([[s_x, 0, 0, 0],[0, s_y, 0, 0],[0, 0, s_z, 0],[0, 0, 0, 1]], dtype = "float32")
		out_matrix = numpy.dot(in_matrix, scale_matrix)
		return out_matrix