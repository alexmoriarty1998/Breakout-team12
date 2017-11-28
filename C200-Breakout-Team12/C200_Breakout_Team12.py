# Alexander Moriarty, Sub Raizada, Kevin Tinsley
# CSCI-C 200
# Final Project: Breakout

# Type hints are used extensively in this project
# to help write better code faster.
# A few examples of their benefits:
# Code is self-documenting and easier to understand when reading later
# IDE will autocomplete better based on type
# IDE will show types in parameters popup when calling functions
# IDE will often generate warnings on using incorrect type

# this class initializes pygame and graphics, then
# starts the screen manager with the loading screen

import pygame
from GameConstants import GC_WORLD_SIZE
import Graphics
import ScreenManager

pygame.init()

# initialize display
pygame.display.set_caption("Breakout!")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))

Graphics.surface = pygame.Surface(GC_WORLD_SIZE)  # this is the surface with world coordinates
Graphics.goWindowed()  # call goFullscreen() instead to start game in fullscreen

# start the game
from screens.LoadingScreen import LoadingScreen  # import this after pygame is fully initialized
ScreenManager.currentScreen = LoadingScreen()
ScreenManager.start()
