#!/usr/bin/env python
"""
@authors: Daniel Elisabethsønn Antonsen and Håkon Alfred Bakker
Uit, Institute of Computer Science, 2022

Clone of the classic Amiga game, Mayhem. Written as an assignment in Inf-1400 Object-oriented programming.
"""
# Importing modules and libratries
import pygame
import sys
from config import HEIGHT, WIDHT, BLACK
#
class Mayhem:
    def __init__(self, *argv):
        pygame.init()
        self.SCREEN = pygame.display.set_mode([WIDHT, HEIGHT])
        self.clock = pygame.time.Clock()
        self.runGame = True
        self.FPS = 30

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runGame = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runGame = False
                    sys.exit()

    def Update(self):
        pass

    def Draw(self):
        pygame.display.update()

    def Main(self):
        while self.runGame:
            pygame.display.set_caption("Mayhem Game FPS: {0:.0f}".format(self.clock.get_fps()))
            self.clock.tick(self.FPS)
            self.SCREEN.fill(BLACK)
            self.EventHandler()
            self.Draw()

if __name__ == "__main__":
    game = Mayhem()
    game.Main()