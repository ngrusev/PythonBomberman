import pygame, sys
import Player, BaseLevel
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((850, 650))
pygame.display.set_caption('Bomberman')

player = Player.Player()
level = BaseLevel.BaseLevel(850, 650, player)
directionMask = 0

directionMap = { K_LEFT : 1, K_UP : 2, K_RIGHT : 4, K_DOWN : 8 }

while True:
    DISPLAYSURF.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key in directionMap:
            directionMask |= directionMap[event.key]
        elif event.type == KEYUP and event.key in directionMap:
            directionMask &= ~directionMap[event.key]
        elif event.type == KEYDOWN and event.key == K_SPACE:
            player.dropBomb()
            
    if directionMask & directionMap[K_LEFT] != 0:
        player.moveLeft()
    if directionMask & directionMap[K_RIGHT] != 0:
        player.moveRight()
    if directionMask & directionMap[K_UP] != 0:
        player.moveUp()
    if directionMask & directionMap[K_DOWN] != 0:
        player.moveDown()

    level.update()

    if level.getStatus() != BaseLevel.LEVEL_IN_PROGRESS:
        if level.getStatus() == BaseLevel.LEVEL_OVER:
            player = Player.Player()
        level = BaseLevel.BaseLevel(850, 650, player)
    
    for elem in level.getElements():
        DISPLAYSURF.blit(elem.getSprite(), elem.getPosition())

    pygame.display.flip()
    
    pygame.display.update()
    fpsClock.tick(FPS)
