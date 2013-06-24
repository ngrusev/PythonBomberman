import pygame, sys
import Player, BaseLevel
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Bomberman')

player = Player.Player(50, 50, 50, 50)
level = BaseLevel.BaseLevel(400, 300, player)
direction = None

while True:
    DISPLAYSURF.fill((255, 255, 255))
    DISPLAYSURF.blit(player.get_sprite(), player.get_position())
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            direction = event.key
        elif event.type == KEYUP and event.key == direction:
            direction = None

    if direction == K_LEFT:
        player.move_left()
    elif direction == K_RIGHT:
        player.move_right()
    elif direction == K_UP:
        player.move_up()
    elif direction == K_DOWN:
        player.move_down()
    
    pygame.display.update()
    fpsClock.tick(FPS)
