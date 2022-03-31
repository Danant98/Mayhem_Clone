"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
UiT, Institute of Computer Science

Module containing all constants used in the game.
"""
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
    platformY = HEIGHT / 2
    # playerhitbox
    playerHitboxW = 20
    playerHitboxH = 20
    # Player 1 initial position
    player1X = platformX + (platformWIDTH / 2)
    player1Y = platformY - playerHitboxH
    # Obstrcle radius
    obsticleSIZE = 60
