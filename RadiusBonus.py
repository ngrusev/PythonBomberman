import LevelElement
import pygame
import Player

class RadiusBonus(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('rbonus.png')
        
    def get_sprite(self):
        return self.sprite

    def is_solid(self):
        return False

    def interact(self, element):
        if isinstance(element, Player.Player):
            element.blast_radius += 1
        self.destroy()

    def destroy(self):
        self.alive = False
