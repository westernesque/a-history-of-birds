class Word:
    def __init__(self, font_size):
        self.characters = []
        self.width = 0
        self.font_size = font_size

    def add_character(self, character):
        self.characters.append(character)
        self.width += character.get_x_advance() * self.font_size

    def get_characters(self):
        return self.characters

    def get_word_width(self):
        return self.width
