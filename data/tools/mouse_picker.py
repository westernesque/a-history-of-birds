import data.tools.maths as m
import pygame, numpy


class MousePicker:
    current_ray = None
    RAY_RANGE = 600.0
    RECURSION_COUNT = 200

    def __init__(self, camera, projection_matrix, display, terrain):
        self.camera = camera
        self.projection_matrix = projection_matrix
        self.display = display
        self.terrain = terrain
        self.view_matrix = m.Maths().create_view_matrix(camera)
        self.current_terrain_point = None
        self.count = 0

    def get_current_ray(self):
        return self.current_ray

    def update(self):
        self.view_matrix = m.Maths().create_view_matrix(self.camera)
        self.current_ray = self.calculate_mouse_ray()

    def calculate_mouse_ray(self):
        mouse_x, mouse_y = float(pygame.mouse.get_pos()[0]), float(pygame.mouse.get_pos()[1])
        normalized_device_coordinates = self.get_normalized_device_coordinates(mouse_x, mouse_y)
        clip_coordinates = (normalized_device_coordinates[0], normalized_device_coordinates[1], -1.0, 1.0)
        eye_coordinates = self.to_eye_coordinates(clip_coordinates)
        world_ray = self.to_world_coordinates(eye_coordinates)
        return world_ray

    def to_world_coordinates(self, eye_coordinates):
        inverted_view_matrix = numpy.linalg.inv(self.view_matrix)
        ray_world_coordinates = numpy.dot(inverted_view_matrix, eye_coordinates)
        mouse_ray = (-ray_world_coordinates[0], ray_world_coordinates[1], -ray_world_coordinates[2])
        return mouse_ray

    def to_eye_coordinates(self, clip_coordinates):
        inverted_projection_matrix = numpy.linalg.inv(self.projection_matrix)
        eye_coordinates = numpy.dot(inverted_projection_matrix, clip_coordinates)
        return eye_coordinates[0], eye_coordinates[1], -1.0, 0.0

    def get_normalized_device_coordinates(self, mouse_x, mouse_y):
        x = (2.0 * mouse_x) / self.display.get_width() - 1.0
        y = (2.0 * mouse_y) / self.display.get_height() - 1.0
        return (x, y)
        # return (-x, -y)

    def intersect_with_y(self):
        a = self.camera.position[0]
        b = self.camera.position[1]
        c = self.camera.position[2]

        alpha = self.current_ray[0]
        beta = self.current_ray[1]
        gamma = self.current_ray[2]

        x = a - (alpha * b) / beta
        if self.terrain.height is not None:
            y = self.terrain.height
        else:
            y = 0.0
        z = c - (gamma * b) / beta
        # inverted_coordinates = numpy.linalg.inv([x, y, z])
        return (x, y, z)
