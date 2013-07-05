import LevelElement
import pygame

PLAYER_WIDTH = 45
PLAYER_HEIGHT = 45
PLAYER_SPEED = 5
PLAYER_BLAST_RADIUS = 2
PLAYER_BOMBS = 1

def modDecrease(value):
    if value > 0:
        value -= 1
    elif value < 0:
        value += 1
    return value

class Player(LevelElement.LevelElement):
    
    def __init__(self):
        super().__init__(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.sprite = pygame.image.load('player.png')
        self.current_level = None
        self.speed = PLAYER_SPEED
        self.blast_radius = PLAYER_BLAST_RADIUS
        self.bombs = PLAYER_BOMBS
        
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
            dx = modDecrease(dx)
            dy = modDecrease(dy)
        self.x += dx
        self.y += dy

    def drop_bomb(self):
        self.current_level.add_bomb()

    def is_solid(self):
        return False

    def destroy(self):
        self.alive = False
