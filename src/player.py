"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

File containg the class object to represent the player
"""
# Importing modules and libraries
import pygame, os
from Vector import vector
from config import Config
import numpy as np
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
        # Defining if spaceship is hit or not
        self.HIT = False 
        # Defining if the thurst is activated 
        self.fueling = False
        self.THRUST = True
        # Setting score for player
        self.score = Config.playerScore
        # Setting starting health 
        self.health = Config.startingHealth
        # Setting number of lives 
        self.lives = 3
        # Loading in image of spaceship
        self.image = pygame.image.load(os.path.join("resources", spaceshipImage)).convert_alpha()
        # Feching rectangular object to represent the spaceship as a sprite
        self.rect = self.image.get_rect()
        # Defining position for the object
        self.rect.x = self.startPos.x - (self.image.get_width() / 2)
        self.rect.y = self.startPos.y - (self.image.get_height() / 2)
        # Defining staring velocity and acceleration of the spaceship
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        # Defining the center of the spaceship
        
    
    def collWithBoundaries(self):
        """
        Method to determines the motion of the object if it collides with screen walls
        """
        if self.rect.x < 0 or self.rect.x + self.image.get_width() > Config.WIDTH:
            self.setToStart()
        if self.rect.y < 0 or self.rect.y + self.image.get_height() > Config.HEIGHT:
            self.setToStart()
    
    def hitByOtherPlayer(self):
        """
        Method to determine action if the player is hit by other player
        """
        # If the player is hit, ther players health bar goes down
        if not self.HIT:
            self.health -= 25
            # If the health bar is zero, the players number of lives goes down and player is reset to the starting position
            if self.health == 0:
                self.lives -= 1
                self.setToStart()


    def setToStart(self):
        """
        Method to reset the spaceship to start position
        """
        # Setting position back to starting position
        self.rect.x = self.startPos.x - (self.image.get_width() / 2)
        self.rect.y = self.startPos.y - (self.image.get_height() / 2)
        # Setting the velocity back to initial velocity
        self.vel = vector(0, 0)
        # Resetting angle 
        self.angle = Config.startingAngle
        # Resetting fuel
        self.fuel = Config.maxFuel
        # Resetting health
        self.health = Config.startingHealth
        # The player's score is reduced by 1 if player collides, but not if player's score is zero
        if self.HIT and self.score != 0:
            self.score -= 1

    def rotate(self):
        center_img = vector(self.rect.x + (self.image.get_width()/2), 
                        self.rect.y + (self.image.get_height()/2))
        rotate_Spaceship = pygame.transform.rotate(self.image, self.angle + Config.diffAngle)
        rotate_Spaceship_rect = rotate_Spaceship.get_rect(center = center_img)
        return rotate_Spaceship, rotate_Spaceship_rect


    def movement(self, time):
    
        # Adding velocity to position  
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
            


    def update(self):
        pass