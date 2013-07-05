import BaseWall
import BrickWall
import SteelWall
import random

BRICK_WALLS_CHANCE = 0.5

class BaseLevel:
    def __init__(self, width, height, player):
        self.player = player
        player.current_level = self
        self.height = height
        self.width = width
        self.elements = [player]
        self.generate_steel_walls()
        self.generate_brick_walls()
        
    def is_element_position_valid(self, element, x, y):
        return (self.is_position_valid(element, x, y) and
            self.is_position_valid(element, x + element.width - 1, y) and
            self.is_position_valid(element, x, y  + element.height - 1) and
            self.is_position_valid(element, x + element.width - 1, y + element.height - 1))

    def is_position_valid(self, current_element, x, y):
        if (x < 0 or x >= self.width or
            y < 0 or y >= self.height):
            return False

        for elem in self.elements:
            if not elem.is_solid() or elem == current_element:
                continue
            elem_pos = elem.get_position()
            if(x >= elem_pos[0] and x < elem_pos[0] + elem.width and
               y >= elem_pos[1] and y < elem_pos[1] + elem.height):
                return False
        return True
    
    def generate_steel_walls(self):
        for x in range(0, self.width // (2 * BaseWall.WIDTH)):
            for y in range(0, self.height // (2 * BaseWall.HEIGHT)):
                self.elements.append(SteelWall.SteelWall((x * 2 + 1) * BaseWall.WIDTH, (y * 2 + 1) * BaseWall.HEIGHT))
                
    def generate_brick_walls(self):
        for x in range(0, self.width // BaseWall.WIDTH):
            for y in range(0, self.height // BaseWall.HEIGHT, 1 + x % 2):
                if(x < 2 and y < 2):
                    continue
                if(random.random() <= BRICK_WALLS_CHANCE):
                    self.elements.append(BrickWall.BrickWall(x * BaseWall.WIDTH, y * BaseWall.HEIGHT))
