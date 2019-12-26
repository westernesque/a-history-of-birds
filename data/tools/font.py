import pygame


def font_texture(text):
    font = pygame.font.Font("freesansbold.ttf", 80)
    text_surface = font.render(text, True, (255, 255, 255))
    text_surface.set_alpha(0)
    ix, iy = text_surface.get_width(), text_surface.get_height()
    text_rect = pygame.Surface((ix, iy), pygame.SRCALPHA)
    # text_rect.convert_alpha()
    text_rect.fill((0, 255, 255, 0))
    # text_rect.set_alpha(0)
    text_surface.set_alpha(0)
    # text_rect.blit(text_surface, (0, 0))
    text_rect.blit(text_surface, text_surface.get_rect(), special_flags=pygame.BLEND_RGBA_MULT)
    text_rect_image = pygame.image.tostring(text_rect, "RGBA", True)
    return text_rect_image, text_rect.get_width(), text_rect.get_height()