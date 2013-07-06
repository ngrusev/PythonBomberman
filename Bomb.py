import LevelElement
import pygame
from pygame.locals import *

TICKS_PER_STAGE = 60

class Bomb(LevelElement.LevelElement):
    def __init__(self, x, y, hasElementsOnTop, registerExplosion):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('bomb.png')
        self.__armed = False
        self.__stage = 0
        self.__ticks = 0
        self.__hasElementsOnTop = hasElementsOnTop
        self.__registerExplosion = registerExplosion
        
    def getSprite(self):
        frame = pygame.Surface((self._width, self._height), flags = SRCALPHA)
        frame.blit(self.__sprite, (0, 0), (self.__stage * self._width, 0, self._width, self._height))
        return frame

    def isSolid(self):
        return self.__armed and self._alive

    def update(self):
        if not self.__armed:
            self.__armed = not self.__hasElementsOnTop(self)
            if self.__armed:
                self.__stage = 1
            return
            
        self.__ticks += 1
        if self.__ticks == TICKS_PER_STAGE:
            self.__stage += 1
            self.__ticks = 0
        if self.__stage == 4:
            self.__explode()

    def __explode(self):
        if self._alive:
            self._alive = False
            self.__registerExplosion(self)
        
    def destroy(self):
        self.__explode()
        
