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
    def __init__(self, SCREEN, runGame):
        # Defining the background 
        self.SCREEN = SCREEN
        # Setting the fonts for the outlay of each background
        self.bigScreenFont = pygame.font.SysFont("Verdana", 60)
        self.mediumScreenFont = pygame.font.SysFont("Helvetica", 30)
        self.smallScreenFont = pygame.font.SysFont("Helvetica", 20)
        # Defining a variable to determine if the game is pause or not
        self.pause = False
        # 
        self.runGame = runGame

    def mainMeny(self):
        pass


    def gameScreen(self, player1, player2):
        """
        Module to represent the game screen outlay
        """
        ## Render text for outlay of each player's score, lives, fuel and health
        # Start by rendering for player 1
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
        """
        Method to represent the pause screen
        """
        while self.pause:
            # Feching the mouse position
            mouseX, mouseY = pygame.mouse.get_pos()
            # Render pause text
            textPAUSE = self.bigScreenFont.render("PAUSE", False, Config.WHITE)
            button1 = pygame.Rect(Config.WIDTH / 2 - 20, Config.HEIGHT / 2 - 50, 200, 60)
            button2 = pygame.Rect(Config.WIDTH / 2 -20 , Config.HEIGHT / 2 + 50, 200, 60)
            if button1.collidepoint((mouseX, mouseY)):
                self.pause = False
                self.runGame = True
            if button2.collidepoint((mouseX, mouseY)):
                self.pause = False
                self.runGame = False
            pygame.draw.rect(self.SCREEN, Config.WHITE, button1)
            pygame.draw.rect(self.SCREEN, Config.WHITE, button2)
            self.SCREEN.blit(textPAUSE, ((Config.WIDTH / 2) - textPAUSE.get_width(), 30))
            

    def endScreen(self):
        pass 


