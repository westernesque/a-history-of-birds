class GuiText:
    def __init__(self, text, font_size, font, position, max_line_length, centered):
        self.text_string = text
        self.font_size = font_size
        self.font = font
        self.position = position
        self.max_line_length = max_line_length
        self.centered = centered
        self.color = (0.0, 0.0, 0.0)
        self.number_of_lines = 1
        self.text_mesh_vao = None
        self.vertex_count = 0

    def remove(self):
        pass

    def get_font(self):
        return self.font

    def set_text_color(self, r, g, b):
        self.color = (r, g, b)

    def get_color(self):
        return self.color

    def get_number_of_lines(self):
        return self.number_of_lines

    def get_position(self):
        return self.position

    def get_mesh(self):
        return self.text_mesh_vao

    def set_mesh_info(self, vao, vertex_count):
        self.text_mesh_vao = vao
        self.vertex_count = vertex_count

    def get_vertex_count(self):
        return self.vertex_count

    def get_font_size(self):
        return self.font_size

    def set_number_of_lines(self, number):
        self.number_of_lines = number

    def is_centered(self):
        return self.centered

    def get_max_line_size(self):
        return self.max_line_length

    def get_text_string(self):
        return self.text_string
