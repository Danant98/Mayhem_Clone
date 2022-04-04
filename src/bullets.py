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
        # Setting the background screen of which we draw the bullets on 
        self.SCREEN = SCREEN        
        # Defining the position, radius of the bullets and color 
        self.pos = vector(x, y)
        self.R = Config.RADIUS
        self.COLOR = Config.WHITE
        # Defining the velocity of the bullets
        self.vel = vector(0, 0)
        self.maxSpeed = Config.maxSpeed
        # Setting angle the bullet is shoot out in
        self.angle = angle
        # Defining the rect
        self.rect = self.draw()
    
    def crashWithBoundaries(self):
        """
        Method to determine the action of the bullets with the screen wall
        """
        # If the bullet hits the boundaries of the screen, the bullet is removed from the spritegroup using kill method from sprites 
        if self.pos.x - self.R < 0:
            self.kill()
        if self.pos.x + self.R > self.SCREEN.WIDTH:
            self.kill()
        if self.pos.y - self.R < 0:
            self.kill()
        if self.pos.y + self.R > self.SCREEN.HEIGHT:
            self.kill()

    def motion(self, time):
        """
        Method to determine the motion of the bullet which is constant in x-direction and affected by gravity in the y-direction
        """
        self.vel += vector(self.maxSpeed * np.cos(np.deg2rad(self.angle)) * time, 
                           self.maxSpeed * -np.sin(np.deg2rad(self.angle)) * time * Config.GRAVITY)
        # Updating position using the velocity
        self.pos += self.vel 

    def draw(self):
        """
        Method to draw the object on the screen
        """
        pygame.draw.circle(self.SCREEN, self.COLOR, (self.pos.x, self.pos.y), self.R)

    def update(self, time):
        """
        Method to update the motion and methods of the bullet
        """
        self.motion(time)
        self.crashWithBoundaries()
        self.rect = self.draw()

if __name__ == "__main__":
    bullet = Bullet(20, 20, 0)
    bullet.motion(0)
    print(bullet.pos)
    bullet.motion(1)
    print(bullet.pos)
