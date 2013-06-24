import SceneElement
import pygame

class Player(SceneElement.SceneElement):

    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.sprite = pygame.image.load('player.png')
        self.current_level = None
        self.speed = 5
        
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
        if self.current_level.is_element_position_valid(self, self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
