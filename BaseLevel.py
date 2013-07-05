import LevelElement
import BrickWall
import SteelWall
import Bomb
import random
import Flame
import Demon
from Utilities import *

BRICK_WALLS_CHANCE = 0.5
DEMON_SPAWN_CHANCE = 0.1

class BaseLevel:
    def __init__(self, width, height, player):
        self.player = player
        player.current_level = self
        player.x = 0
        player.y = 0
        self.height = height
        self.width = width
        self.bomb_count = 0
        self.elements = [player]
        self.occupied_cells = set()
        self.generate_steel_walls()
        self.generate_brick_walls()
        self.spawn_demons()
        
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
                if x < 2 and y < 2:
                    continue
                if random.random() <= BRICK_WALLS_CHANCE:
                    self.elements.append(BrickWall.BrickWall(x * LevelElement.DEFAULT_WIDTH, y * LevelElement.DEFAULT_HEIGHT))
                    self.occupied_cells.add((x, y))

    def spawn_demons(self):
        for x in range(0, self.width // LevelElement.DEFAULT_WIDTH):
            for y in range(0, self.height // LevelElement.DEFAULT_HEIGHT, 1 + x % 2):
                if x < 2 and y < 2 or (x, y) in self.occupied_cells:
                    continue
                if random.random() <= DEMON_SPAWN_CHANCE:
                    self.elements.append(Demon.Demon(x * LevelElement.DEFAULT_WIDTH, y * LevelElement.DEFAULT_HEIGHT, self))
                    self.occupied_cells.add((x, y))
                
    def has_elements_on_top(self, element):
        for elem in self.elements:
            if elem == element:
                continue
            if intersecting(element, elem):
                return True
        return False

    def update(self):
        i = 0
        while i < len(self.elements):
            self.elements[i].update()
            if not self.elements[i].alive:
                self.elements.pop(i)
            else:
                i += 1

        for first in self.elements:
            for second in self.elements:
                if not first.is_solid() and not second.is_solid() and intersecting(first, second):
                    first.interact(second)

        i = 0
        while i < len(self.elements):
            if not self.elements[i].alive:
                self.elements.pop(i)
            else:
                i += 1

    def add_bomb(self):
        if self.bomb_count == self.player.bombs:
            return

        col = (self.player.x + self.player.width // 2 + self.player.width % 2) // LevelElement.DEFAULT_WIDTH
        row = (self.player.y + self.player.height // 2 + self.player.height % 2) // LevelElement.DEFAULT_HEIGHT
        newX = col * LevelElement.DEFAULT_WIDTH
        newY = row * LevelElement.DEFAULT_HEIGHT

        for elem in self.elements:
            if (isinstance(elem, Bomb.Bomb) and
                elem.x == newX and elem.y == newY):
                return
        
        self.bomb_count += 1
        self.elements.append(Bomb.Bomb(self, newX, newY))

    def explode_bomb(self, bomb):
        self.bomb_count -= 1
        self.elements.append(Flame.Flame(bomb.x, bomb.y))
        closest = [self.player.blast_radius + 1] * 4
        closest_elem = [None] * 4
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        bombPosition = bomb.get_position()
        elementSizePair = (LevelElement.DEFAULT_WIDTH, LevelElement.DEFAULT_HEIGHT)
        for elem in self.elements:
            if not elem.is_solid():
                continue
            offset = 0
            if elem.x == bomb.x:
                offset = 1
            elif elem.y != bomb.y:
                continue
            elemPosition = elem.get_position()
            diff = (elemPosition[offset] - bombPosition[offset]) // elementSizePair[offset]
            if diff < 0:
                diff = -diff
            else:
                offset += 2
            if closest[offset] > diff:
                closest[offset] = diff
                closest_elem[offset] = elem

        for i in range(0, 4):
            if closest_elem[i] != None:
                closest_elem[i].destroy()
            for j in range(1, closest[i]):
                newX = bombPosition[0] + j * directions[i][0] * LevelElement.DEFAULT_WIDTH
                newY = bombPosition[1] + j * directions[i][1] * LevelElement.DEFAULT_HEIGHT
                if (newX >= 0 and newX < self.width and
                    newY >= 0 and newY < self.height):
                    self.elements.append(Flame.Flame(newX, newY))

