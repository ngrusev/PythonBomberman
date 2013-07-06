import BaseWall
import LevelElement
import pygame
import random

class BrickWall(BaseWall.BaseWall):

    def __init__(self, x, y, registerDeath):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('bwall.png')
        self.__destroyed = False
        self.__alpha = 255
        self.__registerDeath = registerDeath
        
    def getSprite(self):
        self.__sprite.set_alpha(self.__alpha)
        return self.__sprite

    def update(self):
        if not self.__destroyed:
            return
        self.__alpha -= LevelElement.FADE_SPEED
        if(self.__alpha < LevelElement.FADE_THRESHOLD):
            self._alive = False
            self.__registerDeath(self)
            
    def destroy(self):
        self.__destroyed = True
