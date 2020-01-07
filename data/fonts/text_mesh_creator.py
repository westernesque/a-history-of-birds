import data.fonts.meta_file, data.fonts.line, data.fonts.word, data.fonts.text_mesh_data


class TextMeshCreator:
    def __init__(self, meta_file):
        self.LINE_HEIGHT = 0.03
        self.SPACE_ASCII = 32
        self.meta_data = data.fonts.meta_file.MetaFile(meta_file, self)
        print(self.meta_data)

    def create_text_mesh(self, text):
        lines = self.create_structure(text)
        data = self.create_quad_vertices(text, lines)
        return data

    def create_structure(self, text):
        chars = list(text.get_text_string())
        lines = []
        current_line = data.fonts.line.Line(self.meta_data.get_space_width(), text.get_font_size(), text.get_max_line_size())
        current_word = data.fonts.word.Word(text.get_font_size())
        # chars.append(text.get_text_string())
        for char in chars:
            ascii = ord(char)
            if ascii == self.SPACE_ASCII:
                added = current_line.attempt_to_add_word(current_word)
                if not added:
                    lines.append(current_line)
                    current_line = data.fonts.line.Line(self.meta_data.get_space_width(), text.get_font_size(), text.get_max_line_size())
                    current_line.attempt_to_add_word(current_word)
                current_word = data.fonts.word.Word(text.get_font_size())
                continue
            character = self.meta_data.get_character(ascii)
            # print(character)
            current_word.add_character(character)
        self.complete_structure(lines, current_line, current_word, text)
        return lines

    def complete_structure(self, lines, current_line, current_word, text):
        added = current_line.attempt_to_add_word(current_word)
        if not added:
            lines.append(current_line)
            current_line = data.fonts.line.Line(self.meta_data.get_space_width(), text.get_font_size(), text.get_max_line_size())
            current_line.attempt_to_add_word(current_word)
        lines.append(current_line)

    def create_quad_vertices(self, text, lines):
        text.set_number_of_lines(len(lines))
        # text.set_number_of_lines(len(lines.size))
        cursor_x = 0
        cursor_y = 0
        vertices = []
        texture_coordinates = []
        for line in lines:
            if text.is_centered():
                cursor_x = (line.get_max_length() - line.get_current_line_length()) / 2
            for word in line.get_words():
                for letter in word.get_characters():
                    self.add_vertices_for_character(cursor_x, cursor_y, letter, text.get_font_size(), vertices)
                    self.add_texture_coordinates(texture_coordinates, letter.get_x_texture_coordinate(), letter.get_y_texture_coordinate(), letter.get_x_max_texture_coordinate(), letter.get_y_max_texture_coordinate())
                    cursor_x += letter.get_x_advance() * text.get_font_size()
                cursor_x += self.meta_data.get_space_width() * text.get_font_size()
            cursor_x = 0
            cursor_y += self.LINE_HEIGHT * text.get_font_size()
        return data.fonts.text_mesh_data.TextMeshData(vertices, texture_coordinates)

    def add_vertices_for_character(self, cursor_x, cursor_y, character, font_size, vertices):
        x = cursor_x + (character.get_x_offset() * font_size)
        y = cursor_y + (character.get_y_offset() * font_size)
        max_x = x + (character.get_x_size() * font_size)
        max_y = y + (character.get_y_size() * font_size)
        proper_x = (2 * x) - 1
        proper_y = (-2 * y) + 1
        proper_max_x = (2 * max_x) - 1
        proper_max_y = (-2 * max_y) + 1
        self.add_vertices(vertices, proper_x, proper_y, proper_max_x, proper_max_y)

    def add_vertices(self, vertices, x, y, max_x, max_y):
        vertices.append(x)
        vertices.append(y)
        vertices.append(x)
        vertices.append(max_y)
        vertices.append(max_x)
        vertices.append(max_y)
        vertices.append(max_x)
        vertices.append(max_y)
        vertices.append(max_x)
        vertices.append(y)
        vertices.append(x)
        vertices.append(y)

    def add_texture_coordinates(self, texture_coordinates, x, y, max_x, max_y):
        texture_coordinates.append(x)
        texture_coordinates.append(y)
        texture_coordinates.append(x)
        texture_coordinates.append(max_y)
        texture_coordinates.append(max_x)
        texture_coordinates.append(max_y)
        texture_coordinates.append(max_x)
        texture_coordinates.append(max_y)
        texture_coordinates.append(max_x)
        texture_coordinates.append(y)
        texture_coordinates.append(x)
        texture_coordinates.append(y)
