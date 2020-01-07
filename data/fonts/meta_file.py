import data.fonts.character


class MetaFile:
    def __init__(self, file, text_mesh_creator):
        self.PAD_TOP = 0
        self.PAD_LEFT = 1
        self.PAD_BOTTOM = 2
        self.PAD_RIGHT = 3

        self.DESIRED_PADDING = 3

        self.SPLITTER = " "
        self.NUMBER_SEPARATOR = ","

        self.aspect_ratio = 800 / 600
        # self.aspect_ratio = display.get_width() / display.get_height()

        self.vertical_per_pixel_size = None
        self.horizontal_per_pixel_size = None
        self.space_width = None
        self.padding = 0
        self.padding_width = 0
        self.padding_height = 0

        self.meta_data = {}
        self.values = {}
        self.value_pairs = {}

        self.file = open(file, 'r')
        self.load_padding_data()
        self.load_line_sizes(text_mesh_creator)
        image_width = self.get_value_of_variable("scale_w")
        self.load_character_data(image_width, text_mesh_creator)
        self.file.close()

    def get_space_width(self):
        return self.space_width

    def get_character(self, ascii):
        return self.meta_data.get(ascii)

    def process_next_line(self): # check if this is right
        self.values.clear()
        line = self.file.readline().strip()
        # print("line:\n" + line + "-- test")
        if len(line) is 0:
            return False
        if line is not None:
            for part in line.split(self.SPLITTER):
                value_pairs = part.split("=")
                if len(value_pairs) == 2:
                    self.values[value_pairs[0]] = value_pairs[1]
            return True

    def get_value_of_variable(self, variable):
        # print("values: \n" + str(self.values))
        return self.values[variable]

    def get_values_of_variable(self, variable):
        numbers = self.values[variable].split(self.NUMBER_SEPARATOR)
        actual_values = numbers
        for i in range(len(actual_values)):
        # for i in range(len(actual_values) + 1):
            actual_values[i] = numbers[i]
        return actual_values

    def load_padding_data(self):
        self.process_next_line()
        self.padding = self.get_values_of_variable("padding")
        self.padding_width = self.padding[self.PAD_LEFT] + self.padding[self.PAD_RIGHT]
        self.padding_height = self.padding[self.PAD_TOP] + self.padding[self.PAD_BOTTOM]

    def load_line_sizes(self, text_mesh_creator):
        self.process_next_line()
        line_height_pixels = int(self.get_values_of_variable("line_height")[0]) - int(self.padding_height)
        self.vertical_per_pixel_size = text_mesh_creator.LINE_HEIGHT / line_height_pixels
        self.horizontal_per_pixel_size = self.vertical_per_pixel_size / self.aspect_ratio

    def load_character_data(self, image_width, text_mesh_creator):
        self.process_next_line()
        self.process_next_line()
        while self.process_next_line():
            char = self.load_character(image_width, text_mesh_creator)
            if char is not None:
                self.meta_data[char.get_id()] = char

    def load_character(self, image_size, text_mesh_creator):
        id = int(self.get_value_of_variable("id"))
        if id == text_mesh_creator.SPACE_ASCII:
            self.space_width = (int(self.get_value_of_variable("xadvance")) - int(self.padding_width)) * \
                               self.horizontal_per_pixel_size
            return None
        x_texture = (int(self.get_value_of_variable("x")) + (int(self.padding[self.PAD_LEFT]) - self.DESIRED_PADDING)) / int(image_size)
        y_texture = (int(self.get_value_of_variable("y")) + (int(self.padding[self.PAD_TOP]) - self.DESIRED_PADDING)) / int(image_size)
        width = int(self.get_value_of_variable("width")) - (int(self.padding_width) - (2 * self.DESIRED_PADDING))
        height = int(self.get_value_of_variable("height")) - (int(self.padding_height) - (2 * self.DESIRED_PADDING))
        quad_width = width * self.horizontal_per_pixel_size
        quad_height = height * self.vertical_per_pixel_size
        x_texture_size = width / int(image_size)
        y_texture_size = height / int(image_size)
        x_offset = (int(self.get_value_of_variable("xoffset")) + int(self.padding[self.PAD_LEFT]) - self.DESIRED_PADDING) * self.horizontal_per_pixel_size
        y_offset = (int(self.get_value_of_variable("yoffset")) + int(self.padding[self.PAD_TOP]) - self.DESIRED_PADDING) * self.vertical_per_pixel_size
        x_advance = (int(self.get_value_of_variable("xadvance")) - int(self.padding_width)) * self.horizontal_per_pixel_size
        return data.fonts.character.Character(id, x_texture, y_texture, x_texture_size, y_texture_size, x_offset, y_offset, quad_width, quad_height, x_advance)
