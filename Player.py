import LevelElement
import pygame

PLAYER_WIDTH = 45
PLAYER_HEIGHT = 45
PLAYER_SPEED = 5

def decrese(value):
    if value > 0:
        value -= 1
    elif value < 0:
        value += 1
    return value

class Player(LevelElement.LevelElement):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.sprite = pygame.image.load('player.png')
        self.current_level = None
        self.speed = PLAYER_SPEED
        self.bomb_radius = 2
        
    def get_sprite(self):
        return self.sprite

    def move_left(self):
        self.__move(-self.speed, 0)

    def move_up(self):
        self.__move(0, -self.speed)

    def move_right(self):
        self.__move(self.speed, 0)

    def move_down(self):
        self.__move(0, self.speed)

    def __move(self, dx, dy):
        while (not self.current_level.is_element_position_valid(self, self.x + dx, self.y + dy) and
               (dx != 0 or dy != 0)):
            dx = decrese(dx)
            dy = decrese(dy)
        self.x += dx
        self.y += dy

    def is_solid(self):
        return False

    def drop_bomb(self):
        self.current_level.add_bomb()
