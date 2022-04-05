"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker

Module to represent the meny screen and render game text on screen
"""
# Importing modules and libraries
import pygame, sys
from config import Config
# Class object
class Menu:
    """
    Object to handle text on screen and menys the players is able to open
    """
    def __init__(self, SCREEN, BG):
        # Defining the background and screen
        self.SCREEN = SCREEN
        self.BG = BG
        # Setting the fonts for the outlay of each background
        self.bigScreenFont = pygame.font.SysFont("Verdana", 60)
        self.mediumScreenFont = pygame.font.SysFont("Helvetica", 30)
        self.smallScreenFont = pygame.font.SysFont("Helvetica", 20)
        # Defining a variable to determine if the game is pause or not
        self.pause = False
        # Define a variable to determine if the end screen is open
        self.eScreen = False

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
            pygame.display.set_caption("Mayhem Game")
            # Setting background for pause screen
            self.SCREEN.blit(self.BG, (0, 0))
            # Render pause text
            textPAUSE = self.bigScreenFont.render("PAUSE", False, Config.WHITE)
            textCON = self.mediumScreenFont.render("Press SPACEBAR to continue", False, Config.WHITE)
            textQUIT = self.mediumScreenFont.render("Press ESCAPE to exit game", False, Config.WHITE)
            # Checking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            # Print pause menu text on screen
            self.SCREEN.blit(textPAUSE, ((Config.WIDTH / 2) - textPAUSE.get_width() / 2, 30))
            self.SCREEN.blit(textCON, ((Config.WIDTH / 2) - textCON.get_width() / 2, (Config.HEIGHT / 2) - 100))
            self.SCREEN.blit(textQUIT, ((Config.WIDTH / 2) - textQUIT.get_width() / 2, (Config.HEIGHT / 2) + 100))
            # Updating screen and setting fps
            pygame.display.update()
            
            

    def endScreen(self, player1, player2):
        """
        Method to determine the end screen showing the winner
        """
        while self.eScreen:
            # Setting background for end screen
            self.SCREEN.blit(self.BG, (0, 0))
            # Writing the winner depending on the score of each player
            if player1.score > player2.score:
                # Rendering end screen text
                textWINNER = self.mediumScreenFont.render("PLAYER 1 IS THE WINNER!!", 
                                                        False, Config.WHITE)
                textWINNER2 = self.mediumScreenFont.render("SCORE: " + str(player1.score), False, Config.WHITE)
                textCON = self.mediumScreenFont.render("Press SPACEBAR to restart the game", False, Config.WHITE)
                textQUIT = self.mediumScreenFont.render("Press ESCAPE to quit", False, Config.WHITE)
            elif player1.score == player2.score:
                # Rendering end screen text
                textWINNER = self.mediumScreenFont.render("THE SCORE ENDED EVEN!!!", 
                                                        False, Config.WHITE)
                textWINNER2 = self.mediumScreenFont.render("SCORE: " + str(player1.score), False, Config.WHITE)
                textCON = self.mediumScreenFont.render("Press SPACEBAR to restart the game", False, Config.WHITE)
                textQUIT = self.mediumScreenFont.render("Press ESCAPE to quit", False, Config.WHITE)    
            else:
                # Rendering end screen text
                textWINNER = self.mediumScreenFont.render("PLAYER 2 IS THE WINNER!!", 
                                                        False, Config.WHITE)
                textWINNER2 = self.mediumScreenFont.render("SCORE: " + str(player1.score), False, Config.WHITE)
                textCON = self.mediumScreenFont.render("Press SPACEBAR to restart the game", False, Config.WHITE)
                textQUIT = self.mediumScreenFont.render("Press ESCAPE to quit", False, Config.WHITE)    
            # Checking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.eScreen = False
                        # Game is restarted with spaceships in the starting pos, reset score and lives
                        for player in [player1, player2]:
                            player.setToStart()
                            player.score = 0
                            player.lives = 3
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            # Blitting text on the screen
            self.SCREEN.blit(textWINNER, ((Config.WIDTH / 2) - textWINNER.get_width() + 110, (Config.HEIGHT / 2) - 180))
            self.SCREEN.blit(textWINNER2, ((Config.WIDTH / 2) - textWINNER.get_width() + 110, (Config.HEIGHT / 2) - 100))
            self.SCREEN.blit(textCON, ((Config.WIDTH / 2) - textCON.get_width() + 200, (Config.HEIGHT / 2) + 150))
            self.SCREEN.blit(textQUIT, ((Config.WIDTH / 2) - textQUIT.get_width() + 100, (Config.HEIGHT / 2) + 300))
            # Updating screen
            pygame.display.update()
            


