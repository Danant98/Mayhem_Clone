"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakke

Class object platform to represent the platforms the players start on and refuel on
"""
# Importing libraries and modules
import pygame
from Vector import vector
from config import Config
# Defining class object platform to represent the platform 
class startPlatform(pygame.sprite.Sprite):
    """
    Class object to represent the platform
    """
    def __init__(self, x, y, COLOR, SCREEN):
        # Constructor form parent class
        super().__init__()
        # Defining the background in which the platform is drawn on
        self.SCREEN = SCREEN
        # Defining the size and color of the platform
        self.IMAGE = pygame.Surface([Config.platformWIDTH, Config.platformHEIGHT])
        # Defining teh color of the platform
        self.COLOR = COLOR
        # Feching a rectangular object from the drawing to represent the platform as a sprite
        self.rect = self.draw()
        # Defining the position of the platform
        self.rect.pos = vector(x, y)
        
    def draw(self):
        """
        Method to draw the platform on the screen
        """
        pygame.draw.rect(self.SCREEN, self.COLOR, (self.rect.pos.x, self.rect.pos.y), self.IMAGE)

    def update(self):
        """
        Method to handele updating the object
        """
        self.draw()

