class Line:
    def __init__(self, space_width, font_size, max_length):
        self.space_size = space_width * font_size
        self.max_length = max_length
        self.words = []
        self.current_line_length = 0

    def attempt_to_add_word(self, word):
        additional_length = word.get_word_width()
        if len(self.words) is 0:
            additional_length += 0
        elif len(self.words) > 0:
            additional_length += self.space_size
        if self.current_line_length + additional_length <= self.max_length:
            self.words.append(word)
            self.current_line_length += additional_length
            return True
        else:
            return False

    def get_max_length(self):
        return self.max_length

    def get_current_line_length(self):
        return self.current_line_length

    def get_words(self):
        return self.words
