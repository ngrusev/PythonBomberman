import pygame, sys
import Player, BaseLevel
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((450, 350))
pygame.display.set_caption('Bomberman')

player = Player.Player(0, 0)
level = BaseLevel.BaseLevel(450, 350, player)
direction_mask = 0

direction_map = { K_LEFT : 1, K_UP : 2, K_RIGHT : 4, K_DOWN : 8 }

while True:
    DISPLAYSURF.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key in direction_map:
            direction_mask |= direction_map[event.key]
        elif event.type == KEYUP and event.key in direction_map:
            direction_mask &= ~direction_map[event.key]
            
    if direction_mask & direction_map[K_LEFT] != 0:
        player.move_left()
    if direction_mask & direction_map[K_RIGHT] != 0:
        player.move_right()
    if direction_mask & direction_map[K_UP] != 0:
        player.move_up()
    if direction_mask & direction_map[K_DOWN] != 0:
        player.move_down()

    for elem in level.elements:
        DISPLAYSURF.blit(elem.get_sprite(), elem.get_position())
    
    
    pygame.display.update()
    fpsClock.tick(FPS)
