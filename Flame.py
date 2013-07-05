import LevelElement
import pygame

class Flame(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load("flame.png")
        self.alpha = 255
        
    def update(self):
        self.alpha -= LevelElement.FADE_SPEED
        if(self.alpha < LevelElement.FADE_THRESHOLD):
            self.alive = False

    def get_sprite(self):
        self.sprite.set_alpha(self.alpha)
        return self.sprite

    def is_solid(self):
        return False

    def interact(self, element):
        element.destroy()
