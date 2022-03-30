"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakke

Class object platform to represent the platforms the players start on and refuel on
"""
# Importing libraries and modules
import pygame
from config import Config
# Defining class object platform to represent the platform 
class Platform(pygame.sprite.Sprite):
    """
    Class object to represent the platform
    """
    def __init__(self, x, y, COLOR):
        # Constructor form parent class
        super().__init__()
        # Defining the size and color of the platform
        self.image = pygame.Surface([Config.platformWIDTH, Config.platformHEIGHT]).convert_alpha()
        # Defining the color of the platform
        self.image.fill(COLOR)
        # Feching a rectangular object from the drawing to represent the platform as a sprite
        self.rect = self.image.get_rect()
        # Defining the position of the platform
        self.rect.x = x
        self.rect.y = y