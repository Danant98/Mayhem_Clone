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
    def __init__(self, x, y, COLOR, SCREEN):
        # Constructor from parent class 
        super().__init__()
        self.SCREEN = SCREEN
        self.COLOR = COLOR
        self.fuel = Config.maxFuel
        self.GRAVITY = Config.GRAVITY
        self.image = pygame.Surface([100, 100], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.polygon(self.image, self.COLOR, ([(self.rect.x + 50, self.rect.y),
                                                    (self.rect.x, self.rect.y + 100),
                                                    (self.rect.x + 100, self.rect.y + 100)]))

    #def draw(self):
     #   pygame.draw.polygon(self.image, self.color, ([(self.rect.x + 50, self.rect.y),(self.rect.x, self.rect.y + 100), (self.rect.x + 100, self.rect.y + 100)]))
        




