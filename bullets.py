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
    def __init__(self, x, y, SCREEN, angle):
        # Constructor form parent class 
        super().__init__()
        # Setting the background screen of which we draw the bullets on 
        self.SCREEN = SCREEN        
        # Defining the position, radius of the bullets and color 
        self.pos = vector(x, y)
        self.R = Config.RADIUS
        self.COLOR = Config.WHITE
        # Defining the velocity of the bullets
        self.speedX = 0
        self.speedY = 0
        self.vel = vector(self.speedX, self.speedY)
        self.maxSpeed = Config.maxSpeed
        # 
        self.angle = angle
        self.rect = self.draw()
    
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
        self.speedX += self.maxSpeed * time
        self.speedY += self.maxSpeed * time
        self.vel = vector(self.speedX, self.speedY)
        # Updating position using the velocity
        self.pos.x += self.vel.x 
        self.pos.y += self.vel.y

    def draw(self):
        pygame.draw.circle(self.SCREEN, self.COLOR, (self.pos.x, self.pos.y), self.R)

    def update(self, time):
        """
        Method to update the motion and methods of the bullet
        """
        self.motion(time)
        self.crashWithBoundaries()
        self.rect = self.draw()

