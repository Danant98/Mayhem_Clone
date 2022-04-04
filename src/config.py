"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
UiT, Institute of Computer Science

Module containing all constants used in the game.
"""
# Importing modules and libraries
import pygame
import numpy as np
# Defining a class with the constants used in the game
class Config:
    """
    Class containing all constants used in the game
    """
    # Defining height and width of the screen window
    WIDTH = 900
    HEIGHT = 700
    # Color for the background of the screen
    BLACK = "#000000"
    # Set of colors
    RED = "#ff0000"
    WHITE = "#ffffff"
    GREEN = "#00ff00"
    BLUE = "#0000ff"
    # Defining constants for gravity and startingfuel
    GRAVITY = 10
    maxFuel = 100
    # Defining radius of bullets
    RADIUS = 5
    # Setting max speed of bullets
    maxSpeed = 500
    # Defing size of platform 
    platformWIDTH = WIDTH // 8
    platformHEIGHT = HEIGHT // 35
    # Platform initial position
    platformX = 20
    platformY = HEIGHT - 100
    # Defining starting angle, staring score and starting health for spaceship objects
    startingAngle = (3/2)*np.pi
    playerScore = 0
    startingHealth = 100
    # Player 1 initial position
    player1X = platformX + (platformWIDTH / 2)
    player1Y = platformY - 20
    # Defining controls for the two player objects 
    ARROWS = {'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT, 
                    'THRUST': pygame.K_UP, 'BOOST': pygame.K_DOWN, 'FIRE': pygame.K_RETURN}
    ASDW = {'LEFT': pygame.K_a, 'RIGHT': pygame.K_d, 'THRUST': pygame.K_w, 
                    'BOOST': pygame.K_s, 'FIRE': pygame.K_1}
    # Obstrcle radius
    obsticleSIZE = 100



