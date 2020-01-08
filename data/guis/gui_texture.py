class GuiTexture:
    def __init__(self, texture, position, scale):
        self.texture_id = texture[0]
        self.texture_data = texture[1]
        self.texture_image = texture[2]
        self.texture = texture
        self.position = position
        self.scale = scale

    def get_texture_image(self):
        return self.texture_image

    def get_texture_id(self):
        return self.texture_id

    def get_texture_data(self):
        return self.texture_data

    def get_texture(self):
        return self.texture

    def get_position(self):
        return self.position

    def get_scale(self):
        return self.scale
