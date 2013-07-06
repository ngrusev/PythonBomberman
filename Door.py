import LevelElement
import pygame
import Player

class Door(LevelElement.LevelElement):
    def __init__(self, x, y, level):
        super().__init__(x, y)
        self.sprite = pygame.image.load('door.png')
        self.level = level

    def get_sprite(self):
        return self.sprite

    def is_solid(self):
        return False

    def interact(self, element):
        if (isinstance(element, Player.Player) and
            self.level.getDemonCount() == 0):
            self.level.win()

            
