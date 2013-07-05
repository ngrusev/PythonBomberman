import LevelElement
import Player
import pygame
import random

DEMON_SPEED = 2

class Demon(LevelElement.LevelElement):
    def __init__(self, x, y, level):
        super().__init__(x, y)
        self.sprite = pygame.image.load('demon.png')
        self.speed = DEMON_SPEED
        self.direction = None
        self.destination = None
        self.level = level

    def get_sprite(self):
        return self.sprite

    def destroy(self):
        self.alive = False

    def is_solid(self):
        return False

    def interact(self, element):
        if isinstance(element, Player.Player):
            element.destroy()

    def update(self):
        if self.direction == None:
            dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            while len(dirs) > 0:
                i = random.randint(0, len(dirs) - 1)
                if self.level.is_element_position_valid(self, self.x + dirs[i][0], self.y + dirs[i][1]):
                    self.direction = (dirs[i][0] * self.speed, dirs[i][1] * self.speed)
                    self.destination = (self.x + dirs[i][0] * LevelElement.DEFAULT_WIDTH, self.y + dirs[i][1] * LevelElement.DEFAULT_HEIGHT)
                    break
                dirs.pop(i)
            if self.direction == None:
                return
        
        dx = self.x - self.destination[0]
        dx = -dx if dx < 0 else dx

        if dx != 0:
            if dx <= self.speed:
                self.x = self.destination[0]
                self.direction = None
                self.destination = None
            else:
                self.x += self.direction[0]
            return

        dy = self.y - self.destination[1]
        dy = -dy if dy < 0 else dy

        if dy != 0:
            if dy <= self.speed:
                self.y = self.destination[1]
                self.direction = None
                self.destination = None
            else:
                self.y += self.direction[1]
