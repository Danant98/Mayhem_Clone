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
        self.image = pygame.Surface([Config.playerHitboxW, Config.playerHitboxH], pygame.SRCALPHA)

        self.rect = self.image.get_rect()
        self.rect.x = x - (Config.playerHitboxW / 2)
        self.rect.y = y

        self.points = [(0, 0), (100, 50), (0, 100)]
        pygame.draw.polygon(self.image, self.COLOR, self.points)

