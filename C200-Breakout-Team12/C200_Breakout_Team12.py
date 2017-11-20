# Alexander Moriarty, Sub Raizada, Kevin Tinsley
# CSCI-C 200
# Final Project: Breakout

# this class initializes pygame and graphics, then
# starts the screen manager with the loading screen

# should this init stuff go here or in LoadingScreen.__init__()?
import pygame

from GameConstants import WORLD_SIZE
import Graphics
import ScreenManager
from screens.LoadingScreen import LoadingScreen

pygame.init()

# initialize display
pygame.display.set_caption("Breakout!")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))

Graphics.surface = pygame.Surface(WORLD_SIZE)  # this is the surface with world coordinates
Graphics.goWindowed()  # call goFullscreen() instead to start game in fullscreen

# start the game
ScreenManager.currentScreen = LoadingScreen()
ScreenManager.start()
