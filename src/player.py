"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

File containg the class object to represent the player
"""
# Importing modules and libraries
from re import I
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
        # Setting a spritelist containg the bullets of the spaceship
        self.weapon = pygame.sprite.Group()
        
    
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


    def posOfCockpit(self):
        """
        Method to get the coordinates of the spaceship's cockpit
        """
        # Defining the rotational matrix as a numpy array 
        rotationalMatrix = np.array([np.cos(np.deg2rad(self.angle)), -np.sin(np.deg2rad(self.angle)), 
                                     np.sin(np.deg2rad(self.angle)), np.cos(np.deg2rad(self.angle))])
        # Defining the position of the cockpit as a numpy array
        position = np.array([self.rect.get_widht() / 2, 0])
        # Multiplying the position with the rotation matrix
        rotPos = np.matmul(position, rotationalMatrix)
        # Setting the center of the player object
        center = (self.rect.x + self.rect.get_widht() / 2, self.rect.y + self.rect.get_widht() / 2)
        # Returning the position of the cockpit as a list
        return (np.array(center) + rotPos).tolist()


    def rotateDraw(self):
        """
        Method to rotate the player object round the center of image and blit to screen
        """
        # Dividing the angle by 360 degree to make the angle stay between 0 and 360 degree
        self.angle %= 360
        # Rotate the image by a given angle
        self.rotIm = pygame.transform.rotate(self.image, (self.angle - np.rad2deg(np.pi / 2)))
        # Updating a new rect object round the rotated image with center in the original image
        self.rect = self.rotIm.get_rect(center=self.rect.center)
        # Blit the rotated image on the screen
        self.SCREEN.blit(self.rotIm, self.rect)

    def movement(self, time):
        """
        Method to determine the movement of the player
        """
        # Updating the velocity of the player object 
        self.vel.x += np.cos(np.deg2rad(self.angle)) * self.thrust * time
        self.vel.y += ((-np.sin(np.deg2rad(self.angle))) * self.thrust + Config.GRAVITY) * time
        # Updating the position of the player object using the updated velocity 
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
    
    def update(self, time):
        """
        Method to update the motion of player
        """
        self.collWithBoundaries()
        self.rotateDraw()
        self.movement(time)