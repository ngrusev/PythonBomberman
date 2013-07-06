import LevelElement
import pygame
from Utilities import *

PLAYER_WIDTH = 45
PLAYER_HEIGHT = 45
PLAYER_SPEED = 5
PLAYER_BLAST_RADIUS = 2
PLAYER_BOMBS = 1

class Player(LevelElement.LevelElement):
    
    def __init__(self):
        super().__init__(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.__sprite = pygame.image.load('player.png')
        self.__speed = PLAYER_SPEED
        self.__radius = PLAYER_BLAST_RADIUS
        self.__bombs = PLAYER_BOMBS
        self.__isPosiotionValid = None
        self.__registerBomb = None
        
    def getSprite(self):
        return self.__sprite

    def moveLeft(self):
        self.__move(-self.__speed, 0)

    def moveUp(self):
        self.__move(0, -self.__speed)

    def moveRight(self):
        self.__move(self.__speed, 0)

    def moveDown(self):
        self.__move(0, self.__speed)

    def __move(self, dx, dy):
        while (not self.__isPosiotionValid(self, self._x + dx, self._y + dy) and
               (dx != 0 or dy != 0)):
            dx = modDecrease(dx)
            dy = modDecrease(dy)
        self._x += dx
        self._y += dy

    def dropBomb(self):
        self.__registerBomb(self)

    def isSolid(self):
        return False

    def destroy(self):
        self._alive = False

    def setPosition(self, x, y):
        self._x = x
        self._y = y

    def increaseBombs(self):
        self.__bombs += 1

    def increaseRadius(self):
        self.__radius += 1

    def setIsPositionValid(self, value):
        self.__isPosiotionValid = value

    def setRegisterBomb(self, value):
        self.__registerBomb = value

    def getBombs(self):
        return self.__bombs

    def getRadius(self):
        return self.__radius
