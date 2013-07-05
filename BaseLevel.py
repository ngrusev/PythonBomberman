import LevelElement
import BrickWall
import SteelWall
import Bomb
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
        
    def is_element_position_valid(self, element, x, y, solid_only = True):
        return (self.is_position_valid(element, x, y, solid_only) and
            self.is_position_valid(element, x + element.width - 1, y, solid_only) and
            self.is_position_valid(element, x, y  + element.height - 1, solid_only) and
            self.is_position_valid(element, x + element.width - 1, y + element.height - 1, solid_only))

    def is_position_valid(self, current_element, x, y, solid_only):
        if (x < 0 or x >= self.width or
            y < 0 or y >= self.height):
            return False

        for elem in self.elements:
            if (solid_only and not elem.is_solid() or
                elem == current_element):
                continue
            elem_pos = elem.get_position()
            if(x >= elem_pos[0] and x < elem_pos[0] + elem.width and
               y >= elem_pos[1] and y < elem_pos[1] + elem.height):
                return False
        return True
    
    def generate_steel_walls(self):
        for x in range(0, self.width // (2 * LevelElement.DEFAULT_WIDTH)):
            for y in range(0, self.height // (2 * LevelElement.DEFAULT_HEIGHT)):
                self.elements.append(SteelWall.SteelWall((x * 2 + 1) * LevelElement.DEFAULT_WIDTH, (y * 2 + 1) * LevelElement.DEFAULT_HEIGHT))
                
    def generate_brick_walls(self):
        for x in range(0, self.width // LevelElement.DEFAULT_WIDTH):
            for y in range(0, self.height // LevelElement.DEFAULT_HEIGHT, 1 + x % 2):
                if(x < 2 and y < 2):
                    continue
                if(random.random() <= BRICK_WALLS_CHANCE):
                    self.elements.append(BrickWall.BrickWall(x * LevelElement.DEFAULT_WIDTH, y * LevelElement.DEFAULT_HEIGHT))
                    
    def has_elements_on_top(self, element):
        pos = element.get_position()
        return not self.is_element_position_valid(element, pos[0], pos[1], False)

    def explode_bomb(self, bomb):
        return

    def update(self):
        i = 0
        while i < len(self.elements):
            self.elements[i].update()
            if not self.elements[i].alive:
                self.elements.pop(i)
            else:
                i += 1

    def add_bomb(self):
        col = (self.player.x + self.player.width // 2 + self.player.width % 2) // LevelElement.DEFAULT_WIDTH
        row = (self.player.y + self.player.height // 2 + self.player.height % 2) // LevelElement.DEFAULT_HEIGHT
        self.elements.append(Bomb.Bomb(self, col * LevelElement.DEFAULT_WIDTH, row * LevelElement.DEFAULT_HEIGHT))
