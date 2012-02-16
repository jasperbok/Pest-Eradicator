import pygame

import helpers

class Tile(pygame.sprite.Sprite):
    def __init__(self, file_name, passable):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = helpers.load_image(file_name + '.gif')
        self.passable = passable

    def is_passable(self):
        return self.passable
