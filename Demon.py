import LevelElement
import Player
import pygame
import random

DEMON_SPEED = 2

class Demon(LevelElement.LevelElement):
    def __init__(self, x, y, isPositionValid, registerDeath):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('demon.png')
        self.__speed = DEMON_SPEED
        self.__direction = None
        self.__destination = None
        self.__isPositionValid = isPositionValid
        self.__registerDeath = registerDeath

    def getSprite(self):
        return self.__sprite

    def destroy(self):
        if self._alive:
            self._alive = False
            self.__registerDeath()

    def isSolid(self):
        return False

    def interact(self, element):
        if isinstance(element, Player.Player):
            element.destroy()

    def update(self):
        if self.__direction == None:
            dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            while len(dirs) > 0:
                i = random.randint(0, len(dirs) - 1)
                if self.__isPositionValid(self, self._x + dirs[i][0], self._y + dirs[i][1]):
                    self.__direction = (dirs[i][0] * self.__speed, dirs[i][1] * self.__speed)
                    self.__destination = (self._x + dirs[i][0] * LevelElement.DEFAULT_WIDTH, self._y + dirs[i][1] * LevelElement.DEFAULT_HEIGHT)
                    break
                dirs.pop(i)
            if self.__direction == None:
                return
        
        dx = self._x - self.__destination[0]
        dx = -dx if dx < 0 else dx

        if dx != 0:
            if dx <= self.__speed:
                self._x = self.__destination[0]
                self.__direction = None
                self.__destination = None
            else:
                self._x += self.__direction[0]
            return

        dy = self._y - self.__destination[1]
        dy = -dy if dy < 0 else dy

        if dy != 0:
            if dy <= self.__speed:
                self._y = self.__destination[1]
                self.__direction = None
                self.__destination = None
            else:
                self._y += self.__direction[1]
