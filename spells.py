import pygame

import helpers

class Spell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Meteor(Spell):
    def __init__(self, target_point, game_instance):
        Spell.__init__(self)
        self.image, self.rect = helpers.load_image('fireball.png')
        self.target_x, self.target_y = target_point
        start_x, start_y = target_point
        start_x += 30
        start_y -= 300
        self.target_reached = False
        self.game_instance_reference = game_instance
        self.rect.center = (start_x, start_y)
        self.target_tile = self.game_instance_reference.map_.get_tile_at_point(target_point)

    def update(self):
        if not self.target_reached:
            current_x, current_y = self.rect.center
            if self.target_x < current_x:
                print "Fireball is at", current_x, current_y
                self.rect.center = (current_x - 2, current_y + 20)
            else:
                self.target_reached = True
        else:
            for creature in self.game_instance_reference.creatures:
                if creature.current_tile == self.target_tile:
                    creature.change_hp(-10)
