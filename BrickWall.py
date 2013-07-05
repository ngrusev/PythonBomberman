import BaseWall
import LevelElement
import pygame
import random

BONUS_CHANCE = 0.05

class BrickWall(BaseWall.BaseWall):

    def __init__(self, x, y, level):
        super().__init__(x, y)
        self.sprite = pygame.image.load('bwall.png')
        self.destroyed = False
        self.alpha = 255
        self.level = level
        
    def get_sprite(self):
        self.sprite.set_alpha(self.alpha)
        return self.sprite

    def update(self):
        if not self.destroyed:
            return
        self.alpha -= LevelElement.FADE_SPEED
        if(self.alpha < LevelElement.FADE_THRESHOLD):
            self.alive = False
            if(random.random() <= BONUS_CHANCE):
                if random.randint(0, 1) == 0:
                    self.level.add_bomb_bonus(self)
                else:
                    self.level.add_radius_bonus(self)

    def destroy(self):
        self.destroyed = True
