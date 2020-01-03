import data.fonts.character


class MetaFile:
    def __init__(self, file, display):
        self.PAD_TOP = 0
        self.PAD_LEFT = 1
        self.PAD_BOTTOM = 2
        self.PAD_RIGHT = 3

        self.DESIRED_PADDING = 3

        self.SPLITTER = " "
        self.NUMBER_SEPARATOR = ","

        self.aspect_ratio = display.get_width() / display.get_height()

        self.vertical_per_pixel_size = None
        self.horizontal_per_pixel_size = None
        self.space_width = None
        self.padding = 0
        self.padding_width = 0
        self.padding_height = 0

        self.meta_data = {}
        self.values = {}

        self.file = open(file, 'r')
        self.load_padding_data()
        self.load_line_sizes()
        image_width = self.get_value_of_variable("scale_w")
        self.load_character_data(image_width)
        self.file.close()

    def get_space_width(self):
        return self.space_width

    def get_character(self, ascii):
        return self.meta_data.get(ascii)

    def process_next_line(self): # check if this is right
        self.values.clear()
        line = self.file.readline()
        if line is None:
            return False
        for part in line.split(self.SPLITTER):
            value_pairs = part.split("=")
            if len(value_pairs == 2):
                self.values[value_pairs[0]] = value_pairs[1] # may need to make an ordered dict
        return True

    def get_value_of_variable(self, variable):
        return self.values[variable]

    def get_values_of_variable(self, variable):
        numbers = self.values[variable].split(self.NUMBER_SEPARATOR)
        actual_values = len(numbers)
        for i in range(len(actual_values) + 1):
            actual_values[i] = numbers[i]
        return actual_values

    def load_padding_data(self):
        self.process_next_line()
        self.padding = self.get_values_of_variable("padding")
        self.padding_width = self.padding[self.PAD_LEFT] + self.padding[self.PAD_RIGHT]
        self.padding_height = self.padding[self.PAD_TOP] + self.padding[self.PAD_BOTTOM]

    def load_line_sizes(self, text_mesh_creator):
        self.process_next_line()
        line_height_pixels = self.get_values_of_variable("line_height") - self.padding_height
        self.vertical_per_pixel_size = text_mesh_creator.LINE_HEIGHT / line_height_pixels
        self.horizontal_per_pixel_size = self.vertical_per_pixel_size / self.aspect_ratio

    def load_character_data(self, image_width):
        self.process_next_line()
        while self.process_next_line():
            char = self.load_character(image_width)
            if char is None:
                self.meta_data[char.get_id(), char]

    def load_character(self, image_size, text_mesh_creator):
        id = self.get_value_of_variable("id")
        if id == text_mesh_creator.SPACE_ASCII:
            self.space_width = (self.get_value_of_variable("x_advance") - self.padding_width) * \
                               self.horizontal_per_pixel_size
            return None
        x_texture = (self.get_value_of_variable("x") + (self.padding[self.PAD_LEFT] - self.DESIRED_PADDING)) / image_size
        y_texture = (self.get_value_of_variable("y") + (self.padding[self.PAD_TOP] - self.DESIRED_PADDING)) / image_size
        width = self.get_value_of_variable("width") - (self.padding_width - (2 * self.DESIRED_PADDING))
        height = self.get_value_of_variable("height") - (self.padding_height - (2 * self.DESIRED_PADDING))
        quad_width = width * self.horizontal_per_pixel_size
        quad_height = height * self.vertical_per_pixel_size
        x_texture_size = width / image_size
        y_texture_size = height / image_size
        x_offset = (self.get_value_of_variable("x_offset") + self.padding[self.PAD_LEFT] - self.DESIRED_PADDING) * self.horizontal_per_pixel_size
        y_offset = (self.get_value_of_variable("y_offset") + self.padding[self.PAD_TOP] - self.DESIRED_PADDING) * self.vertical_per_pixel_size
        x_advance = (self.get_value_of_variable("x_advance") - self.padding_width) * self.horizontal_per_pixel_size
        return data.fonts.character.Character(id, x_texture, y_texture, x_texture_size, y_texture_size, x_offset, y_offset, quad_width, quad_height, x_advance)
