import LevelElement
import pygame
import Player

class BombBonus(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('bbonus.png')
        
    def get_sprite(self):
        return self.sprite

    def is_solid(self):
        return False

    def interact(self, element):
        if isinstance(element, Player.Player):
            element.bombs += 1
        self.destroy()

    def destroy(self):
        self.alive = False
