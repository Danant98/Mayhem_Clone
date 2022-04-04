"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

Module to represent the meny screen and render game text on screen
"""
# Importing modules and libraries
import pygame
# Class object
class Meny:
    """
    Object to handle text on screen and menys the players is able to open
    """
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.bigScreenFont = pygame.font.Sysfont("Verdana", 60)
        self.smallScreenFont = pygame.font.Sysfont("Helvetica", 20)

    def startScreen(self):
        pass 


    def gameScreen(self):
        pass


    def pauseScreen(self):
        pass


    def endScreen(self):
        pass 


