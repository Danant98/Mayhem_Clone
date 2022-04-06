"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

Module to represent the bullets fired by the players
"""
# Importing the module and libraries
import pygame
import numpy as np
from config import Config
from Vector import vector
# Class object 
class Bullet(pygame.sprite.Sprite):
    """
    Class object to represent the bullets
    """
    def __init__(self, x, y, angle, SCREEN):
        # Constructor form parent class 
        super().__init__()
        # Setting background where the bullet is drawn on
        self.SCREEN = SCREEN
        # Defining a surface to draw the bullet on and drawing it as a circle
        self.image = pygame.Surface([Config.RADIUS, Config.RADIUS]).convert_alpha()
        pygame.draw.circle(self.image, 
                           Config.WHITE, 
                           (self.image.get_widht() / 2, 
                           self.image.get_height() / 2), 
                           Config.RADIUS / 2)
        # Defining the rectangular shape to represent the object as sprites
        self.rect = self.image.get_rect()
        # Defining the position of the sprite object
        self.rect.x = x
        self.rect.y = y
        # Defining the velocity of the bullets
        self.vel = vector(0, 0)
        self.maxSpeed = Config.maxSpeed
        # Setting angle the bullet is shoot out in
        self.angle = angle
    
    def draw(self):
        """
        Method to draw the object 
        """
        self.SCREEN.blit(self.image, self.rect)

    def crashWithBoundaries(self):
        """
        Method to determine the action of the bullets with the screen wall
        """
        # If the bullet hits the boundaries of the screen, the bullet is removed from the spritegroup using kill method from sprites 
        if self.rect.x < 0 or self.rect.x + self.image.get_width() > Config.WIDTH:
            self.kill()
        if self.rect.y < 0 or self.rect.y + self.image.get_height() > Config.HEIGHT:
            self.kill()

    def motion(self, time):
        """
        Method to determine the motion of the bullet which is constant in x-direction and affected by gravity in the y-direction
        """
        self.vel.x += self.maxSpeed * np.cos(np.deg2rad(self.angle)) * time
        self.vel.y += self.maxSpeed * (-np.sin(np.deg2rad(self.angle))) * time
        # Updating position using the velocity
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

    def update(self, time):
        """
        Method to update the motion and methods of the bullet
        """
        self.motion(time)
        self.crashWithBoundaries()
        self.draw()

if __name__ == "__main__":
    bullet = Bullet(20, 20, 0)
    bullet.motion(0)
    print(bullet.rect.x, bullet.rect.y)
    bullet.motion(1)
    print(bullet.rect.x, bullet.rect.y)
