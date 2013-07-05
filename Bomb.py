import LevelElement
import pygame
from pygame.locals import *

TICKS_PER_STAGE = 60

class Bomb(LevelElement.LevelElement):
    def __init__(self, level, x, y):
        super().__init__(x, y)
        self.level = level
        self.sprite = pygame.image.load('bomb.png')
        self.__armed = False
        self.stage = 0
        self.ticks = 0
        
    def get_sprite(self):
        frame = pygame.Surface((self.width, self.height), flags = SRCALPHA)
        frame.blit(self.sprite, (0, 0), (self.stage * self.width, 0, self.width, self.height))
        return frame

    def is_solid(self):
        return self.__armed

    def update(self):
        if not self.__armed:
            self.__armed = not self.level.has_elements_on_top(self)
            if self.__armed:
                self.stage = 1
            return
            
        self.ticks += 1
        if self.ticks == TICKS_PER_STAGE:
            self.stage += 1
            self.ticks = 0
        if self.stage == 4:
            self.alive = False
            self.level.explode_bomb(self)
        
            
        
