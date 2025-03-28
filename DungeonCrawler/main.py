import pygame
import constants
from pygame._sdl2 import Window

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Dungeon Crawler")

#Main game loop
run = True
while run:

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

pygame.quit()