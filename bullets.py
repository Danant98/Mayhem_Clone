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
    def __init__(self, x, y, SCREEN):
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


