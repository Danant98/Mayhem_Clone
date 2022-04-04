"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

Module to represent the meny screen and render game text on screen
"""
# Importing modules and libraries
import pygame
from config import Config
# Class object
class Meny:
    """
    Object to handle text on screen and menys the players is able to open
    """
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.bigScreenFont = pygame.font.SysFont("Verdana", 60)
        self.mediumScreenFont = pygame.font.SysFont("Helvetica", 30)
        self.smallScreenFont = pygame.font.SysFont("Helvetica", 20)

    def startScreen(self):
        pass


    def gameScreen(self, player1, player2):
        """
        Module to represent the game screen outlay
        """
        # Render text for outlay of each player's score, lives, fuel and health
        # Star by rendering for player 1
        player_1 = self.mediumScreenFont.render("Player 1", False, Config.WHITE)
        # Render text 
        healthBar = self.smallScreenFont.render("Health: " + str(player1.health) + "%", 1, Config.WHITE)
        numberOfLives = self.smallScreenFont.render("Lives: " + str(player1.lives), 1, Config.WHITE)
        fuelBar = self.smallScreenFont.render("Fuel: " + str(player1.fuel) + "%", 1, Config.WHITE)
        score = self.smallScreenFont.render("Score: " + str(player1.score), 1, Config.WHITE)
        # Bliting on the screen
        self.SCREEN.blit(player_1, (20, Config.HEIGHT - 110))
        self.SCREEN.blit(healthBar, (20, Config.HEIGHT - 70))
        self.SCREEN.blit(numberOfLives, (20, Config.HEIGHT - 50))
        self.SCREEN.blit(fuelBar, (20, Config.HEIGHT - 30))
        self.SCREEN.blit(score, (20, 30))
        # Then do the same for player 2
        player_2 = self.mediumScreenFont.render("Player 2", False, Config.RED)
        # Render text
        healthBar2 = self.smallScreenFont.render("Health: " + str(player2.health) + "%", 1, Config.RED)
        numberOfLives2 = self.smallScreenFont.render("Lives: " + str(player2.lives), 1, Config.RED)
        fuelBar2 = self.smallScreenFont.render("Fuel: " + str(player2.fuel) + "%", 1, Config.RED)
        score2 = self.smallScreenFont.render("Score: " + str(player2.score), 1, Config.RED)
        # Bliting on the screen
        self.SCREEN.blit(player_2, (Config.WIDTH - 120, Config.HEIGHT - 110))
        self.SCREEN.blit(healthBar2, (Config.WIDTH - 120, Config.HEIGHT - 70))
        self.SCREEN.blit(numberOfLives2, (Config.WIDTH - 120, Config.HEIGHT - 50))
        self.SCREEN.blit(fuelBar2, (Config.WIDTH - 120, Config.HEIGHT - 30))
        self.SCREEN.blit(score2, (Config.WIDTH - 120, 30))



    def pauseScreen(self):
        pass


    def endScreen(self):
        pass 


