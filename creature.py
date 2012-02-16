import random

import pygame

import helpers

class Creature(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, gender, direction, map_reference):
        pygame.sprite.Sprite.__init__(self)
        self.map_reference = map_reference
        self.gender = gender
        self.speed = 3
        self.direction = direction
        self.image, self.rect = helpers.load_image(gender + '.gif')
        self.rect.topleft = (x_pos, y_pos)
        self.current_tile = self.map_reference.get_tile_at_index(self.rect.center)

    def update(self):
        """

        """
        current_tile = self.map_reference.get_tile_at_point(self.rect.center)
        if not current_tile == self.current_tile:
            self.current_tile = current_tile
            self.pick_new_direction()
        tile_x_offset, tile_y_offset = self.map_reference.get_tile_index_at_point(self.rect.center)

        tile = self.map_reference.get_tile_at_index((tile_x_offset, tile_y_offset))
        if self.direction is 'north':
            self.rect.top -= self.speed
            next_tile = self.map_reference.get_tile_at_index((tile_x_offset, tile_y_offset - 1))
        if self.direction is 'east':
            self.rect.left += self.speed
            next_tile = self.map_reference.get_tile_at_index((tile_x_offset + 1, tile_y_offset))
        if self.direction is 'south':
            self.rect.top += self.speed
            next_tile = self.map_reference.get_tile_at_index((tile_x_offset, tile_y_offset + 1))
        if self.direction is 'west':
            self.rect.left -= self.speed
            next_tile = self.map_reference.get_tile_at_index((tile_x_offset - 1, tile_y_offset))

        if not next_tile.is_passable():
            self.pick_new_direction(tile_x_offset, tile_y_offset)

    def pick_new_direction(self):
        """Picks a new direction to move in. Discards the opposite of the
        current direction.

        Keyword arguments:
        tile_x --
        tile_y --

        """
        opposite_directions = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'}
        choices = self.map_reference.get_available_directions(self.rect.center)
        if opposite_directions[self.direction] in choices:
            choices.remove(opposite_directions[self.direction])
        if len(choices) > 0:
            print "These are my choices:"
            for i in choices:
                print i
            self.direction = random.choice(choices)
        self.align_self_to_path()

    def align_self_to_path(self):
        current_x, current_y = self.rect.center
        new_x = int(round(current_x / 20)) * 20
        new_y = int(round(current_y / 20)) * 20
        self.rect.topleft = (new_x, new_y)
