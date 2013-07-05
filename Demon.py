import LevelElement
import pygame

DEMON_SPEED = 3

class Demon(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('demon.png')

    def get_sprite(self):
        return self.sprite

    def destroy(self):
        self.alive = False

    def is_solid(self):
        return False
