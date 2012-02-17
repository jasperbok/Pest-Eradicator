import random

import pygame

import helpers
import settings

class Creature(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, gender, direction, map_, gamescreen):
        pygame.sprite.Sprite.__init__(self)
        self.map_reference = map_
        self.gamescreen_reference = gamescreen
        self.gender = gender
        self.speed = 4
        self.hp = 10
        self.direction = direction
        self.image, self.rect = helpers.load_image(gender + '.png')
        self.rect.topleft = (x_pos, y_pos)
        self.current_tile = self.map_reference.get_tile_at_index(self.rect.center)

    def update(self):
        """

        """
        print "Creature.update()"
        print "Current center position:", self.rect.center, "moving towards the", self.direction
        current_tile = self.map_reference.get_tile_at_point(self.rect.center)
        if self.hp <= 0:
            self.die()
        else:
            if not current_tile == self.current_tile:
                self.current_tile = current_tile
                self.pick_new_direction()

            if self.direction is 'north':
                self.rect.top -= self.speed
            if self.direction is 'east':
                self.rect.left += self.speed
            if self.direction is 'south':
                self.rect.top += self.speed
            if self.direction is 'west':
                self.rect.left -= self.speed

    def pick_new_direction(self):
        """Picks a new direction to move in. Discards the opposite of the
        current direction so that the creature won't suddenly turn around.

        """
        opposite_directions = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'}
        choices = self.map_reference.get_available_directions(self.rect.center)
        if opposite_directions[self.direction] in choices:
            choices.remove(opposite_directions[self.direction])
        if len(choices) > 0:
            print "These are my choices:"
            for i in choices:
                print i
            new_direction = random.choice(choices)
        else:
            new_direction = self.direction
        if self.direction is not new_direction:
            self.direction = new_direction
            self.align_self_to_path()

    def align_self_to_path(self):
        current_x, current_y = self.rect.center
        new_x = int(round(current_x / settings.TILE_SIZE)) * settings.TILE_SIZE
        new_y = int(round(current_y / settings.TILE_SIZE)) * settings.TILE_SIZE
        self.rect.topleft = (new_x, new_y)

    def change_hp(self, amount):
        self.hp += amount

    def die(self):
        self.gamescreen_reference.creatures.remove(self)
