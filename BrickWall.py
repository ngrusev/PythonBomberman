import BaseWall
import pygame

class BrickWall(BaseWall.BaseWall):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('bwall.png')

    def get_sprite(self):
        return self.sprite
