import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Dungeon Crawler")

#Creating the player
player = Character(100, 100)

#Main game loop
run = True
while run:

    #Drawing player on the screen
    player.draw(screen)


    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

        pygame.display.update()

pygame.quit()