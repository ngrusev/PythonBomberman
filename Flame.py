import LevelElement
import pygame

class Flame(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__sprite = pygame.image.load("flame.png")
        self.__alpha = 255
        
    def update(self):
        self.__alpha -= LevelElement.FADE_SPEED
        if(self.__alpha < LevelElement.FADE_THRESHOLD):
            self._alive = False

    def getSprite(self):
        self.__sprite.set_alpha(self.__alpha)
        return self.__sprite

    def isSolid(self):
        return False

    def interact(self, element):
        element.destroy()
