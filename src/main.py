#!/usr/bin/env python
"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
Uit, Institute of Computer Science, 2022

Clone of the classic Amiga game, Mayhem. Written as an assignment in Inf-1400 Object-oriented programming.
"""
# Importing modules and libratries
import pygame, os
from meny import Menu
from config import Config
from Vector import vector
from startPlatform import Platform
from player import Player
from obsticle import Obsticle
# Defining main game class 
class Mayhem:
    """
    Class object to represent the main game loop
    """
    def __init__(self):
        pygame.init()
        # Defining screen display 
        self.SCREEN = pygame.display.set_mode([Config.WIDTH, Config.HEIGHT])
        self.BG = pygame.image.load(os.path.join("resources", "futuristic_city.jpg")).convert_alpha()
        # Rescaling the background image
        self.BG = pygame.transform.smoothscale(self.BG, (Config.WIDTH, Config.HEIGHT))
        # Setting the cloks
        self.clock = pygame.time.Clock()
        self.runGame = True
        # Setting FPS
        self.FPS = 60
        # Calling platform object
        self.platform1 = Platform(Config.platformX, 
                                  Config.platformY, 
                                  Config.WHITE)
        self.platform2 = Platform(Config.WIDTH - Config.platformWIDTH - 20, 
                                  Config.platformY, 
                                  Config.RED)
        # Creating sprite group containng all sprites objects
        self.allSprites = pygame.sprite.Group()
        # Add object platform to sprite group
        self.allSprites.add(self.platform1)
        self.allSprites.add(self.platform2)
        # Calling player object
        self.player1 = Player("spaceship1.png", 
                             vector(Config.player1X, Config.player1Y), 
                              Config.ARROWS, 
                              self.SCREEN)
        self.player1.score = 5
        self.player2 = Player("spaceship2.png", 
                               vector(Config.WIDTH - Config.platformWIDTH / 2 - 20, 
                                      Config.player1Y),
                                      Config.ASDW, 
                                      self.SCREEN)
        # Defining list containing all players                      
        self.spaceshipList = [self.player1, self.player2]
        # Add object player to sprite group
        for spaceship in self.spaceshipList:
            self.allSprites.add(spaceship)
        # Calling obsticle object 
        obsticle1 = Obsticle(Config.WIDTH / 2, 
                             Config.HEIGHT / 2, 
                             Config.GREEN)
        # Add object obsticle to sprite group
        self.allSprites.add(obsticle1)
        # Calling meny object
        self.meny1 = Menu(self.SCREEN, self.BG)

    def EventHandler(self):
        """
        Method to handle event on the game screen
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.meny1.pause = True
                # Definig actions if player push down 
                for spaceship in self.spaceshipList:
                    if event.key == spaceship.CONTROLS['LEFT']:
                        spaceship.angle += Config.diffAngle
                        spaceship.rotate()
                    if event.key == spaceship.CONTROLS['RIGHT']:
                        spaceship.angle -= Config.diffAngle
                        spaceship.rotate()
                        

    
    
    def collisionHandler(self):
        """
        Method to handle all collisions 
        """
        pass


                    
    def Update(self):
        self.allSprites.draw(self.SCREEN)
        pygame.display.update()
        

    def Main(self):
        while self.runGame:
            pygame.display.set_caption("Mayhem Game FPS: {0:.0f}".format(self.clock.get_fps()))
            time = self.clock.tick(self.FPS) / 1000 # Get time in sec
            self.SCREEN.blit(self.BG, (0, 0))
            self.meny1.gameScreen(self.player1, self.player2)
            #self.meny1.pauseScreen()
            self.EventHandler()
            self.collisionHandler()
            # Checking if one of the players have a score of 5 which ends the game
            for spaceship in self.spaceshipList:
                if spaceship.score == 5:
                    self.meny1.eScreen = True
            self.meny1.endScreen(self.player1, self.player2)
            self.Update()

if __name__ == "__main__":
    Mayhem().Main()