# asteroid png from https://pngtree.com/so/asteroid
import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('asteroid_attack/data/asteroid.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += (self.settings.asteroid_speed)
        self.rect.y = self.y