"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

File containg the class object to represent the player
"""
# Importing modules and libraries
import pygame
from Vector import vector
from config import Config
# Defining object player class
class Player(pygame.sprite.Sprite):
    """
    Class object to represent the players
    """
    def __init__(self, x, y, color, SCREEN):
        # Constructor from parent class 
        super().__init__()
        self.pos = vector(x, y)
        self.SCREEN = SCREEN
        self.color = color
        self.fuel = Config.maxFuel
        self.gravity = Config.GRAVITY
        self.image = pygame.Surface([100, 100], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
    

    def draw(self):
        pygame.draw.polygon(self.image, self.color, ([(25,75),(76,125),(250,375)]))
        




