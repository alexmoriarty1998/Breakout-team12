# Alexander Moriarty, Sub Raizada, Kevin Tinsley
# CSCI-C 200
# Final Project: Breakout

# Type hints are used extensively in this project to help write better code faster.
# A few examples of their benefits:
# Code is self-documenting and easier to understand when reading later
# IDE will autocomplete better based on explicitly stated types
# IDE will show types in parameters popup when calling functions
# IDE will often generate warnings on using incorrect type

# This class initializes pygame and graphics, then
# starts the screen manager with the loading screen.

# init pygame before importing/doing anything else
import pygame
pygame.init()

# initialize display
pygame.display.set_caption("Breakout!")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
# done initializing pygame


import Graphics
import ScreenManager
from screens.LoadingScreen import LoadingScreen

Graphics.goWindowed()  # call goFullscreen() instead to start game in fullscreen

# start the game
ScreenManager.currentScreen = LoadingScreen()
ScreenManager.start()
