class Character:
    def __init__(self, id, x_texture_coordinate, y_texture_coordinate, x_texture_size, y_texture_size, x_offset,
                 y_offset,x_size, y_size, x_advance):
        self.id = id
        self.x_texture_coordinate = x_texture_coordinate
        self.y_texture_coordinate = y_texture_coordinate
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x_size = x_size
        self.y_size = y_size
        self.x_max_texture_coordinate = x_texture_size + y_texture_coordinate
        self.y_max_texture_coordinate = y_texture_size + y_texture_coordinate
        self.x_advance = x_advance

    def get_id(self):
        return self.id

    def get_x_texture_coordinate(self):
        return self.x_texture_coordinate

    def get_y_texture_coordinate(self):
        return self.y_texture_coordinate

    def get_x_max_texture_coordinate(self):
        return self.x_max_texture_coordinate

    def get_y_max_texture_coordinate(self):
        return self.y_max_texture_coordinate

    def get_x_offset(self):
        return self.x_offset

    def get_y_offset(self):
        return self.y_offset

    def get_x_size(self):
        return self.x_size

    def get_y_size(self):
        return self.y_size

    def get_x_advance(self):
        return self.x_advance
