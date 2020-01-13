import data.fonts.text_mesh_creator


class FontType:
    def __init__(self, texture_atlas, font_file):
        self.texture_atlas = texture_atlas
        print("FONTTYPE TEST")
        print("texture_atlas = " + str(self.texture_atlas))
        self.loader = data.fonts.text_mesh_creator.TextMeshCreator(font_file)

    def get_texture_atlas(self):
        return self.texture_atlas

    def load_text(self, text):
        return self.loader.create_text_mesh(text)
