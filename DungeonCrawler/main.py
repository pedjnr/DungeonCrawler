import pygame
from pygame.examples.aliens import Player

import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Dungeon Crawler")

#Crating clock for maintaining framerate
clock = pygame.time.Clock()

#Defining player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#Helper function to scale images
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

#Loading character images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]

for mob in mob_types:
    #Loading the images
    animation_list = []
    for animation in animation_types:
        #Reseting temporary list of images
        temp_list = []
        for i in range(4):
            #Loading the player image into the game
            img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            #Scaling the player according to the scale constant
            img = scale_img(img, constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

#Creating the player
player = Character(100, 100, mob_animations, 0)

#Main game loop
run = True
while run:

    #Controlling the FrameRate
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    #Calculating player movement
    dx = 0
    dy = 0

    #If the player is moving to the right the number is positive, but if its moving to the other direction, the number is negative, same with down and up commands
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED

    #Moving the player
    player.move(dx, dy)

    #updating the player
    player.update()

    #Drawing player on the screen
    player.draw(screen)


    #Event handler
    for event in pygame.event.get():
        #Enabling the game to close manually
        if event.type == pygame.QUIT:
            run = False

        #Enabling fullscreen mode
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

        #Taking keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

        #Keyboard Button Release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()