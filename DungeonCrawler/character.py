import pygame
import constants

class Character():
    def __init__(self, x, y):
        #coordinates x and Y and width and height of the character
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def draw (self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)