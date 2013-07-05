import BaseWall
import LevelElement
import pygame

class BrickWall(BaseWall.BaseWall):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = pygame.image.load('bwall.png')
        self.destroyed = False
        self.alpha = 255
        
    def get_sprite(self):
        self.sprite.set_alpha(self.alpha)
        return self.sprite

    def update(self):
        if not self.destroyed:
            return
        self.alpha -= LevelElement.FADE_SPEED
        if(self.alpha < LevelElement.FADE_THRESHOLD):
            self.alive = False

    def destroy(self):
        self.destroyed = True
