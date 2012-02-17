import sys

import pygame
from pygame.locals import *

import gamescreen
import settings


class Game():
    def __init__(self):
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.window_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption('Pest Eradicator')
        self.load_screen('test.txt')
        self.game_loop()

    def load_screen(self, screen_name):
        if screen_name.endswith('.txt'):
            self.screen = gamescreen.GameScreen(screen_name, self.window_surface)

    def update(self):
        self.screen.update()

    def draw(self):
        self.screen.draw()
        pygame.display.update()

    def game_loop(self):
        while 1:
            # Handle the player's input.
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            self.fps_clock.tick(settings.FPS)


if __name__ == "__main__":
    game = Game()
