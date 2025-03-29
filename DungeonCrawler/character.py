import math
import pygame
import constants

class Character:
    def __init__(self, x, y):
        #coordinates x and Y and width and height of the character
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):

        #Controlling diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def draw (self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)