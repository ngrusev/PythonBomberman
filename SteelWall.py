import SceneElement
import pygame

WIDTH = 50
HEIGHT = 50

class SteelWall(SceneElement.SceneElement):

    def __init__(self, x, y):
        super().__init__(WIDTH, HEIGHT, x, y)
        self.sprite = pygame.image.load('swall.png')

    def get_sprite(self):
        return self.sprite

    def is_solid(self):
        return True
