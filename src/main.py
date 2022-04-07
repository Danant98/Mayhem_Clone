#!/usr/bin/env python
"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
Uit, Institute of Computer Science, 2022

Clone of the classic Amiga game, Mayhem. Written as an assignment in Inf-1400 Object-oriented programming.
"""
# Importing modules and libratries
import pygame, os, sys, cProfile
from meny import Menu
from config import Config
from Vector import vector
from bullets import Bullet
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
                                  Config.WHITE, 
                                  self.SCREEN)
        self.platform2 = Platform(Config.WIDTH - Config.platformWIDTH - 20, 
                                  Config.platformY, 
                                  Config.RED, 
                                  self.SCREEN)
        # Creating sprite group containng all sprites objects
        self.allSprites = pygame.sprite.Group()
        self.obsticleSprites = pygame.sprite.Group()
        self.platformSprites = pygame.sprite.Group()
        # Add object platform to sprite group
        self.platformList = [self.platform1, self.platform2]
        for platform in self.platformList:
            self.allSprites.add(platform)
            self.platformSprites.add(platform)
        # Calling player object
        self.player1 = Player("spaceship1.png", 
                             vector(Config.player1X, Config.player1Y), 
                              Config.ARROWS, 
                              self.SCREEN)
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
        self.obsticle1 = Obsticle(Config.WIDTH / 2 - Config.obsticleSIZE / 2, 
                             Config.HEIGHT / 2 - Config.obsticleSIZE / 2, 
                             Config.GREEN, 
                             self.SCREEN)
        # Add object obsticle to sprite group
        self.allSprites.add(self.obsticle1)
        self.obsticleSprites.add(self.obsticle1)
        # Calling meny object
        self.menu1 = Menu(self.SCREEN, self.BG)

    def EventHandler(self, time):
        """
        Method to handle event on the game screen
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu1.pause = True
        # Definig actions if player push down 
        keys = pygame.key.get_pressed()
        for spaceship in self.spaceshipList:
            if keys[spaceship.CONTROLS['LEFT']]:
                # Adding on the angle to rotate the player conterclockwise
                spaceship.angle += Config.diffAngle
            if keys[spaceship.CONTROLS['RIGHT']]:
                # Subtracting the angle to rotate the player clockwise
                spaceship.angle -= Config.diffAngle
            if keys[spaceship.CONTROLS['THRUST']] and spaceship.fuel >= 0:
                # Adding accelerating the player if thrust is activated
                spaceship.thrust = Config.acceleration
                # Constant fuel consumption
                spaceship.fuel -= Config.diffFuel * time
                # Setting so the player can not fuel and accelerate at the same time
                spaceship.fueling = False
            if not keys[spaceship.CONTROLS['THRUST']]:
                spaceship.thrust = 0
            if keys[spaceship.CONTROLS['FIRE']]:
                position = spaceship.posOfCockpit()
                spaceship.weapon.add(Bullet(position, spaceship.angle, self.SCREEN))

    
    def collisionHandler(self, time):
        """
        Method to handle all collisions 
        """
        # Collision detection for spaceship and platform
        for spaceship in self.spaceshipList:
            # Using the sprites functions to check for collisions between spaceship and platforms
            spaceshipOnPlatform = pygame.sprite.spritecollide(spaceship, self.platformSprites, False)
            if spaceshipOnPlatform:
                # If spaceship on platform, set velocity equal to zero
                spaceship.vel.x = 0
                spaceship.vel.y = 0
                # Set fueling to true to start fueling if spaceship on platform
                spaceship.fueling = True
                # Setting the angle in degree so the player face up
                spaceship.angle = 90
                # Fueling as long as the spaceship is on platform and fuel is not at max
                if spaceship.fueling and spaceship.fuel < Config.maxFuel:
                    spaceship.fuel += Config.diffFuel * time
                    # Stoping fueling if fuel is at max
                    if spaceship.fuel >= Config.maxFuel:
                        spaceship.fuel = Config.maxFuel
                # Checking if spaceship has left the platform
                for platform in self.platformList:
                    # Stoping fueling if spaceship has left the platform
                    if spaceship.rect.y > platform.rect.y + 2:
                        spaceship.fueling = False
        
        # Collision detection for player - obsticle and bullets - obsticle
        pygame.sprite.spritecollide(self.obsticle1, self.player1.weapon, True)
        pygame.sprite.spritecollide(self.obsticle1, self.player2.weapon, True)
        # Iterating over list of spaceships
        for spaceship in self.spaceshipList:
            # Using sprite collision detection to verify collision
            coll = pygame.sprite.collide_rect(spaceship, self.obsticle1)
            # If collison, reset player to star position and subtract a life
            if coll:
                spaceship.HIT = True
                spaceship.lives -= 1
                spaceship.setToStart()
        
        # Collison detection for player - player, player1 - bullet2 and bullet1 - player2
        player2HitByBullet = pygame.sprite.spritecollide(self.player2, self.player1.weapon, False)
        player1HitByBullet = pygame.sprite.spritecollide(self.player1, self.player2.weapon, False)
        # Increasing score for player with bullets and reseting calling the hit by other player method described in player module
        if player2HitByBullet and not self.player2.fueling:
            # Setting hit equal to True
            self.player2.HIT = True
            self.player2.hitByOtherPlayer()
            # If player2's health is zero, increase player1's score by 1
            if self.player2.decreaseLIFE:
                self.player1.score += 1
        if player1HitByBullet and not self.player1.fueling:
            # Setting hit equal to True
            self.player1.HIT = True
            self.player1.hitByOtherPlayer()
            # If player1's health is zero, increase player2's score by 1
            if self.player1.decreaseLIFE:
                self.player2.score += 1
        
        # Collision detection for platform - bullets
        pygame.sprite.spritecollide(self.platform1, self.player1.weapon, True)
        pygame.sprite.spritecollide(self.platform1, self.player2.weapon, True)
        pygame.sprite.spritecollide(self.platform2, self.player1.weapon, True)
        pygame.sprite.spritecollide(self.platform2, self.player2.weapon, True)
                    
    def Update(self, time):
        """
        Method to update the sprites
        """
        for spaceship in self.spaceshipList:
            spaceship.update(time)
            spaceship.weapon.update(time)
        self.platformSprites.update()
        self.obsticleSprites.update()
        pygame.display.update()
        

    def Main(self):
        """
        Method to represent the main game loop
        """
        while self.runGame:
            self.menu1.startScreen()
            pygame.display.set_caption("Mayhem Game FPS: {0:.0f}".format(self.clock.get_fps()))
            time = self.clock.tick(self.FPS) / 1000 # Get time in sec
            self.SCREEN.blit(self.BG, (0, 0))
            self.menu1.gameScreen(self.player1, self.player2)
            self.menu1.pauseScreen()
            self.EventHandler(time)
            self.collisionHandler(time)
            # Checking if one of the players have a score of 5 or if one of the players are out of lives, which ends the game
            for spaceship in self.spaceshipList:
                if spaceship.score == 5 or spaceship.lives == 0:
                    self.menu1.eScreen = True
            self.menu1.endScreen(self.player1, self.player2)
            self.Update(time)

if __name__ == "__main__":
    Mayhem().Main()
    #cProfile.run('Mayhem().Main()')
