import pygame
import math

import constants


class Weapon:
    def __init__(self, image, arrow_image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.arrow_image = arrow_image
        self.rect = self.image.get_rect()
        self.fired = False
        self.last_shot = pygame.time.get_ticks()

    def update(self, player):
        shot_cooldown = 300
        arrow = None

        self.rect.center = player.rect.center

        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        y_dist = -(pos[1] - self.rect.centery) #It's negative because pygame y coordinates increase down the screen
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        #Getting mouse clicks
        if pygame.mouse.get_pressed()[0] and self.fired == False and (pygame.time.get_ticks() - self.last_shot) >= shot_cooldown:
            arrow = Arrow(self.arrow_image, self.rect.centerx, self.rect.centery, self.angle)
            self.fired = True
            self.last_shot = pygame.time.get_ticks()

        #Reseting the mouse click
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

        return arrow

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width()/2)), self.rect.centery - int(self.image.get_height() / 2)))

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #Calculating horizontal and vertical speed based on the angle
        self.dx = math.cos(math.radians(self.angle)) * constants.ARROW_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * constants.ARROW_SPEED)

    def update(self):

        #Reposition based on speed
        self.rect.x += self.dx
        self.rect.y += self.dy

        #Checking if the arrow has gone off the screen
        if self.rect.right < 0 or self.rect.left > constants.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > constants.SCREEN_HEIGHT:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, ((self.rect.centerx - int(self.image.get_width() / 2)), self.rect.centery - int(self.image.get_height() / 2)))