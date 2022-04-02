"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

File containg the class object to represent the player
"""
# Importing modules and libraries
import pygame, os
from Vector import vector
from config import Config
# Defining object player class
class Player(pygame.sprite.Sprite):
    """
    Class object to represent the players
    """
    def __init__(self, spaceshipImage, startPos, CONTROLS, SCREEN):
        # Constructor from parent class 
        super().__init__()
        self.SCREEN = SCREEN
        self.CONTROLS = CONTROLS
        self.fuel = Config.maxFuel
        self.GRAVITY = Config.GRAVITY
        self.startPos = startPos
        self.angle = Config.startingAngle
        # Setting 
        self.HIT = False 
        # Loading in image of spaceship
        self.image =pygame.image.load(os.path.join("resources", spaceshipImage)).convert_alpha()
        # Feching rectangular object to represent the spaceship as a sprite
        self.rect = self.image.get_rect()
        # Defining position for the object
        self.rect.x = self.startPos.x - (self.image.get_width() / 2)
        self.rect.y = self.startPos.y - (self.image.get_height() / 2)
        # Defining staring velocity of spaceship
        self.vel = vector(0, 0)
    
    def collWithBoundaries(self):
        """
        Method to determines the motion of the object if it collides with screen walls
        """
        pass 

    def resetSpaceship(self):
        """
        Method to reset the spaceship to start position
        """
        # Setting position back to starting position
        self.rect.x = self.startPos.x - (self.image.get_width() / 2)
        self.rect.y = self.startPos.y - (self.image.get_height() / 2)
        # Setting the velocity back to initial velocity
        self.vel = vector(0, 0)
        # Setting angle bakc to starting angle
        self.angle = Config.startingAngle

