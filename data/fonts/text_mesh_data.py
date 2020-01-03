class TestMeshData:
    def __init__(self, vertex_positions, texture_coordinates):
        self.vertex_positions = vertex_positions
        self.texture_coordinates = texture_coordinates

    def get_vertex_positions(self):
        return self.vertex_positions

    def get_texture_coordinates(self):
        return self.texture_coordinates

    def get_vertex_count(self):
        return len(self.vertex_positions) / 2
