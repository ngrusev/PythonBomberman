import LevelElement
import pygame
import Player

class Door(LevelElement.LevelElement):
    def __init__(self, x, y, registerWin):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('door.png')
        self.__registerWin = registerWin

    def getSprite(self):
        return self.__sprite

    def isSolid(self):
        return False

    def interact(self, element):
        if (isinstance(element, Player.Player)):
            self.__registerWin()

            
