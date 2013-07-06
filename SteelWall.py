import BaseWall
import pygame

class SteelWall(BaseWall.BaseWall):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('swall.png')

    def getSprite(self):
        return self.__sprite
    
