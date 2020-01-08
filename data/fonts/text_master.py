import data.fonts.font_renderer


class TextMaster:
    def __init__(self, loader):
        self.renderer = data.fonts.font_renderer.FontRenderer()
        self.loader = loader
        self.texts = {}

    def render(self):
        self.renderer.render(self.texts)

    def load_text(self, text):
        font = text.get_font()
        print(font)
        data = font.load_text(text)
        print(data)
        vao = self.loader.load_to_vao(data.get_vertex_positions(), data.get_texture_coordinates())
        text.set_mesh_info(vao, data.get_vertex_count())
        text_batch = self.texts.get(font)
        print(text_batch)
        # text_batch = list(self.texts.get(font))
        if text_batch is None:
        # if len(text_batch) is 0:
            text_batch = []
            self.texts[font] = text_batch
        text_batch.append(text)

    def remove_text(self, text):
        text_batch = list(self.texts.get(text.get_font()))
        text_batch.remove(text)
        if len(text_batch) is 0:
            del self.texts[text.get_font()]

    def clean_up(self):
        self.renderer.clean_up()
