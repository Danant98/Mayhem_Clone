#!/usr/bin/env python
"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
Uit, Institute of Computer Science, 2022

Clone of the classic Amiga game, Mayhem. Written as an assignment in Inf-1400 Object-oriented programming.
"""
# Importing modules and libratries
import pygame , sys, os
from config import Config
from startPlatform import Platform
from player import Player
# Defining main game class 
class Mayhem:
    """
    Class object to represent the main game loop
    """
    def __init__(self, *argv):
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
        self.platform1 = Platform(Config.platformX, Config.platformY, Config.WHITE)
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.platform1)
        # Calling player object
        self.player1 = Player(Config.player1X, Config.player1Y, Config.WHITE, self.SCREEN)
        self.allSprites.add(self.player1)

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runGame = False
                    

    def Update(self):
        self.allSprites.draw(self.SCREEN)
        pygame.display.update()
        

    def Main(self):
        while self.runGame:
            pygame.display.set_caption("Mayhem Game FPS: {0:.0f}".format(self.clock.get_fps()))
            time = self.clock.tick(self.FPS) / 1000 # Get time in sec
            self.SCREEN.blit(self.BG, (0, 0))
            self.EventHandler()
            self.Update()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Mayhem()
    game.Main()