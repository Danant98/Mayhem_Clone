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
    def __init__(self, x, y, angle):
        # Constructor form parent class 
        super().__init__()
        # Setting the background screen of which we draw the bullets on 
        #self.SCREEN = SCREEN        
        # Defining the position, radius of the bullets and color 
        self.pos = vector(x, y)
        self.R = Config.RADIUS
        self.COLOR = Config.WHITE
        # Defining the velocity of the bullets
        self.speedX = 0
        self.speedY = 0
        self.vel = vector(self.speedX, self.speedY)
        self.maxSpeed = Config.maxSpeed
        # Setting angle the bullet is shoot out in
        self.angle = angle
        #self.rect = self.draw()
    
    def crashWithBoundaries(self):
        """
        Method to determine the action of the bullets with the screen wall
        """
        # If the bullet hits the boundaries of the screen, the bullet is removed from the spritegroup 
        if self.x - self.R < 0:
            self.kill()
        elif self.x + self.R > self.SCREEN.WIDTH:
            self.kill()
        elif self.y - self.R < 0:
            self.kill()
        elif self.y + self.R > self.SCREEN.HEIGHT:
            self.kill()

    def motion(self, time):
        """
        Method to determine the motion of the bullet which is constant
        """
        self.vel += vector(self.maxSpeed * np.cos(np.deg2rad(self.angle)) * time, 
                           self.maxSpeed * -np.sin(np.deg2rad(self.angle)) * time)
        # Updating position using the velocity
        self.pos += self.vel 

    #def draw(self):
    #    pygame.draw.circle(self.SCREEN, self.COLOR, (self.pos.x, self.pos.y), self.R)

    def update(self, time):
        """
        Method to update the motion and methods of the bullet
        """
        self.motion(time)
        self.crashWithBoundaries()
        #self.rect = self.draw()

bullet = Bullet(20, 20, 0)
if __name__ == "__main__":
    bullet.motion(0)
    print(bullet.pos)
    bullet.motion(1)
    print(bullet.pos)
