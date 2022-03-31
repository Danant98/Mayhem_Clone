"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred

Obsticle module describing the obsticle objects randomly generated on the screen
"""
# Importing libraries and modules
from config import Config
import pygame
# Creating class object obsticle
class Obsticle(pygame.sprite.Sprite):
    """
    Class representing the obsticle object
    """
    def __init__(self, x, y, COLOR):
        # Constructor form parent class
        super().__init__()
        # Creating image of object as a pygame surface with a set size and color 
        self.image = pygame.Surface([Config.obsticleSIZE, Config.obsticleSIZE], pygame.SRCALPHA)
        self.COLOR = COLOR   
        pygame.draw.circle(self.image, self.COLOR,
                            (Config.obsticleSIZE / 2, Config.obsticleSIZE / 2), 
                             Config.obsticleSIZE / 2)     
        # Fetching a rectangular object to represent the object
        self.rect = self.image.get_rect()
        # Definig position of the object
        self.rect.x = x
        self.rect.y = y