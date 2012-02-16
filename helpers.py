import os

import pygame

GRAPHICS_DIR = "graphics"
TILE_DIR = "tiles"

def load_image(name, color_key=None):
    """Loads an image and returns it and its rect."""
    full_name = os.path.join(GRAPHICS_DIR, TILE_DIR, name)
    try:
        image = pygame.image.load(full_name)
    except pygame.error, message:
        print "Cannot load image:", full_name
        raise SystemExit, message
    image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, RLEACCEL)
    return image, image.get_rect()
