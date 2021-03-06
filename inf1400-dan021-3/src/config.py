"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
UiT, Institute of Computer Science

Module containing all constants used in the game.
"""
# Importing modules and libraries
import pygame
# Defining a class with the constants used in the game
class Config:
    """
    Class containing all constants used in the game
    """
    # Defining height and width of the screen window
    WIDTH = 900
    HEIGHT = 700
    # Set of colors
    RED = "#ff0000"
    WHITE = "#ffffff"
    GREEN = "#00ff00"
    # Defining constants for gravity, startingfuel and constant fueling 
    GRAVITY = 1
    maxFuel = 100
    fueling = 10
    diffFuel = 10
    # Defining radius of bullets
    RADIUS = 4
    # Setting max speed of bullets
    maxSpeed = 40
    # Defing size of platform 
    platformWIDTH = WIDTH // 8
    platformHEIGHT = HEIGHT // 35
    # Platform initial position
    platformX = 20
    platformY = HEIGHT - 200
    # Defining starting angle in degree, staring score and starting health for spaceship objects
    startingAngle = 90
    diffAngle = 5
    acceleration = 3
    playerScore = 0
    startingHealth = 100
    # Player 1 initial position
    player1X = platformX + (platformWIDTH / 2)
    player1Y = platformY - 20
    # Defining controls for the two player objects 
    ARROWS = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 
              'THRUST': pygame.K_UP, 'FIRE': pygame.K_RETURN}
    ASDW = {'LEFT': pygame.K_a, 'RIGHT': pygame.K_d, 
            'THRUST': pygame.K_w, 'FIRE': pygame.K_1}
    # Obstrcle radius
    obsticleSIZE = 150