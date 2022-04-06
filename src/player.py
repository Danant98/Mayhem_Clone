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
        # Setting the screen the image is loaded to
        self.SCREEN = SCREEN
        # Defining controls 
        self.CONTROLS = CONTROLS
        # Defining starting amount of fuel
        self.fuel = Config.maxFuel
        # Setting the gravity
        self.GRAVITY = Config.GRAVITY
        # Defining the starting position of the player
        self.startPos = startPos
        # Defining the starting angle of the player
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
        self.rotIm = self.image
        #cen = (self.rect.x -self.image.get_width() / 2, self.rect.y - self.image.get_height() / 2)
        # Feching rectangular object to represent the spaceship as a sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
        # Defining position for the object
        self.rect.x = self.startPos.x - (self.image.get_width() / 2)
        self.rect.y = self.startPos.y - (self.image.get_height() / 2)
        # Defining staring velocity and acceleration of the spaceship
        self.vel = vector(0, 0)
        self.thrust = 0
        
    
    def collWithBoundaries(self):
        """
        Method to determines the motion of the object if it collides with screen walls
        """
        if self.rect.x < 0 or self.rect.x + self.image.get_width() > Config.WIDTH:
            self.setToStart()
            self.lives -= 1
        if self.rect.y < 0 or self.rect.y + self.image.get_height() > Config.HEIGHT:
            self.setToStart()
            self.lives -= 1
    
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


    def rotateDraw(self):
        """
        Method to rotate the player object round the center of image and blit to screen
        """
        self.angle %= 360
        self.rotIm = pygame.transform.rotate(self.image, (self.angle - np.rad2deg(np.pi / 2)))
        self.rect = self.rotIm.get_rect(center=self.rect.center)
        self.SCREEN.blit(self.rotIm, self.rect)

    def movement(self, time):
        self.vel.x += np.cos(np.deg2rad(self.angle)) * self.thrust * time
        self.vel.y += ((-np.sin(np.deg2rad(self.angle))) * self.thrust + Config.GRAVITY) * time

        # Adding velocity to position  
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
    
    def update(self, time):
        self.collWithBoundaries()
        self.rotateDraw()
        self.movement(time)