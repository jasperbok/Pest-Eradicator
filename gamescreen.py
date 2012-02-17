import pygame

import creature
import map
import spells

class GameScreen():
    def __init__(self, map_file_name, screen):
        """Initializes a game screen.

        Keyword arguments:
        map_file_name -- The name of the textfile containing map info.
        screen -- A reference to the screen surface object.

        """
        self.screen_reference = screen
        self.map_file_name = map_file_name
        self.map_name = map_file_name[:-4]
        self.map_ = map.Map(self.map_file_name, self.screen_reference)
        self.creatures = pygame.sprite.RenderUpdates()
        self.active_spells = pygame.sprite.RenderUpdates()
        self.game_hud = GameHUD()

        # This information should come from the map file.
        self.creatures.add(creature.Creature(30, 30, 'female', 'east', self.map_, self))
        self.creatures.add(creature.Creature(840, 30, 'female', 'south', self.map_, self))
        self.creatures.add(creature.Creature(840, 540, 'female', 'west', self.map_, self))
        self.creatures.add(creature.Creature(30, 540, 'female', 'north', self.map_, self))

        self.active_spells.add(spells.Meteor((45, 555), self))

    def update(self):
        self.active_spells.update()
        self.creatures.update()
        self.game_hud.update()

    def draw(self):
        self.map_.draw_tiles()
        self.creatures.draw(self.screen_reference)
        self.active_spells.draw(self.screen_reference)
        #self.game_hud.draw()


class GameHUD():
    def __init__(self):
        self.player = Player()

    def update(self):
        pass

    def draw(self):
        pass


class Player():
    def __init__(self):
        self.mana = 100
        self.selected_spell = 'fireball'
