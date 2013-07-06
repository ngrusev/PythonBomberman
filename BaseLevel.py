import LevelElement
import BrickWall
import SteelWall
import Bomb
import random
import Flame
import Demon
import BombBonus
import RadiusBonus
import Door
from Utilities import *

BRICK_WALLS_CHANCE = 0.5
DEMON_SPAWN_CHANCE = 0.1
LEVEL_IN_PROGRESS = 0
LEVEL_OVER = 1
LEVEL_CLEAR = 2
BONUS_CHANCE = 0.05

class BaseLevel:
    def __init__(self, width, height, player):
        self.__player = player
        player.current_level = self
        player.setPosition(0, 0)
        player.setIsPositionValid(lambda element, x, y: self.__isElementPositionValid(element, x, y))
        player.setRegisterBomb(lambda player: self.__addBomb(player))
        self.__height = height
        self.__width = width
        self.__bombCount = 0
        self.__elements = [player]
        self.__demonCount = 0
        self.__occupiedCells = set()
        self.__generateSteelWalls()
        self.__generateBrickWalls()
        self.__createDoor()
        self.__spawnDemons()
        self.__status = LEVEL_IN_PROGRESS
        
    def __isElementPositionValid(self, element, x, y, solidOnly = True):
        return (self.__isPositionValid(element, x, y, solidOnly) and
            self.__isPositionValid(element, x + element.getWidth() - 1, y, solidOnly) and
            self.__isPositionValid(element, x, y  + element.getHeight() - 1, solidOnly) and
            self.__isPositionValid(element, x + element.getWidth() - 1, y + element.getHeight() - 1, solidOnly))

    def __isPositionValid(self, currentElement, x, y, solidOnly):
        if (x < 0 or x >= self.__width or
            y < 0 or y >= self.__height):
            return False

        for elem in self.__elements:
            if (solidOnly and not elem.isSolid() or
                elem == currentElement):
                continue
            elemPos = elem.getPosition()
            if(x >= elemPos[0] and x < elemPos[0] + elem.getWidth() and
               y >= elemPos[1] and y < elemPos[1] + elem.getHeight()):
                return False
        return True
    
    def __generateSteelWalls(self):
        for x in range(0, self.__width // (2 * LevelElement.DEFAULT_WIDTH)):
            for y in range(0, self.__height // (2 * LevelElement.DEFAULT_HEIGHT)):
                self.__elements.append(SteelWall.SteelWall((x * 2 + 1) * LevelElement.DEFAULT_WIDTH, (y * 2 + 1) * LevelElement.DEFAULT_HEIGHT))
                
    def __generateBrickWalls(self):
        for x in range(0, self.__width // LevelElement.DEFAULT_WIDTH):
            for y in range(0, self.__height // LevelElement.DEFAULT_HEIGHT, 1 + x % 2):
                if x < 2 and y < 2:
                    continue
                if random.random() <= BRICK_WALLS_CHANCE:
                    self.__elements.append(BrickWall.BrickWall(x * LevelElement.DEFAULT_WIDTH, y * LevelElement.DEFAULT_HEIGHT, lambda brick: self.__brickDied(brick)))
                    self.__occupiedCells.add((x, y))

    def __createDoor(self):
        brickWallsList = list(self.__occupiedCells)
        i = random.randint(0, len(brickWallsList) - 1)
        doorX = brickWallsList[i][0] * LevelElement.DEFAULT_WIDTH
        doorY = brickWallsList[i][1] * LevelElement.DEFAULT_HEIGHT
        self.__elements.insert(0, Door.Door(doorX, doorY, lambda: self.__registerWin()))

    def __spawnDemons(self):
        for x in range(0, self.__width // LevelElement.DEFAULT_WIDTH):
            for y in range(0, self.__height // LevelElement.DEFAULT_HEIGHT, 1 + x % 2):
                if x < 2 and y < 2 or (x, y) in self.__occupiedCells:
                    continue
                if random.random() <= DEMON_SPAWN_CHANCE:
                    elementPositionValid = lambda element, x, y: self.__isElementPositionValid(element, x, y)
                    registerDemonDeath = lambda: self.__demonDied()
                    self.__elements.append(Demon.Demon(x * LevelElement.DEFAULT_WIDTH, y * LevelElement.DEFAULT_HEIGHT, elementPositionValid, registerDemonDeath))
                    self.__occupiedCells.add((x, y))
                    self.__demonCount += 1
                
    def __isPlayerOnTop(self, element):
        return intersecting(element, self.__player)
                    

    def update(self):
        if self.__status != LEVEL_IN_PROGRESS:
            return
        
        i = 0
        while i < len(self.__elements):
            self.__elements[i].update()
            if not self.__elements[i].isAlive():
                self.__elements.pop(i)
            else:
                i += 1

        for first in self.__elements:
            for second in self.__elements:
                if first != second and not first.isSolid() and not second.isSolid() and intersecting(first, second):
                    first.interact(second)

        i = 0
        while i < len(self.__elements):
            if not self.__elements[i].isAlive():
                self.__elements.pop(i)
            else:
                i += 1

        if not self.__player.isAlive():
            self.__status = LEVEL_OVER

    def __addBomb(self, player):
        if self.__bombCount == player.getBombs():
            return

        col = (player.getX() + player.getWidth() // 2 + player.getWidth() % 2) // LevelElement.DEFAULT_WIDTH
        row = (player.getY() + player.getHeight() // 2 + player.getHeight() % 2) // LevelElement.DEFAULT_HEIGHT
        newX = col * LevelElement.DEFAULT_WIDTH
        newY = row * LevelElement.DEFAULT_HEIGHT

        for elem in self.__elements:
            if (isinstance(elem, Bomb.Bomb) and
                elem.getX() == newX and elem.getY() == newY):
                return
        
        self.__bombCount += 1
        self.__elements.append(Bomb.Bomb(newX, newY, lambda bomb: self.__isPlayerOnTop(bomb), lambda bomb: self.__explodeBomb(bomb)))

    def __explodeBomb(self, bomb):
        self.__bombCount -= 1
        self.__elements.append(Flame.Flame(bomb.getX(), bomb.getY()))
        closest = [self.__player.getRadius() + 1] * 4
        closest_elem = [None] * 4
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        bombPosition = bomb.getPosition()
        elementSizePair = (LevelElement.DEFAULT_WIDTH, LevelElement.DEFAULT_HEIGHT)
        for elem in self.__elements:
            if not elem.isSolid():
                continue
            offset = 0
            if elem.getX() == bomb.getX():
                offset = 1
            elif elem.getY() != bomb.getY():
                continue
            elemPosition = elem.getPosition()
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
                if (newX >= 0 and newX < self.__width and
                    newY >= 0 and newY < self.__height):
                    self.__elements.append(Flame.Flame(newX, newY))

    def __addBombBonus(self, elem):
        self.__elements.append(BombBonus.BombBonus(elem.getX(), elem.getY()))

    def __addRadiusBonus(self, elem):
        self.__elements.append(RadiusBonus.RadiusBonus(elem.getX(), elem.getY()))

    def __registerWin(self):
        if self.__demonCount == 0:
            self.__status = LEVEL_CLEAR

    def __getDemonCount(self):
        return self.__demonCount

    def __demonDied(self):
        self.__demonCount -= 1

    def __brickDied(self, brick):
        if random.random() <= BONUS_CHANCE:
            if random.randint(0, 1) == 0:
                self.__elements.append(BombBonus.BombBonus(brick.getX(), brick.getY()))
            else:
                self.__elements.append(RadiusBonus.RadiusBonus(brick.getX(), brick.getY()))

    def getStatus(self):
        return self.__status

    def getElements(self):
        return self.__elements
