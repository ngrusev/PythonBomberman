import BaseWall
import pygame

class SteelWall(BaseWall.BaseWall):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('swall.png')

    def get_sprite(self):
        return self.sprite
    
