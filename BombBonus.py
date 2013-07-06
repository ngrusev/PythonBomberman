import LevelElement
import pygame
import Player

class BombBonus(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__sprite = pygame.image.load('bbonus.png')
        
    def getSprite(self):
        return self.__sprite

    def isSolid(self):
        return False

    def interact(self, element):
        if isinstance(element, Player.Player):
            element.increaseBombs()
        self.destroy()

    def destroy(self):
        self._alive = False
