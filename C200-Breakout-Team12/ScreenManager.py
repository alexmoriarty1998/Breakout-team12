# ScreenManager
# contains main game loop, manages game screens

# in python, modules act like static classes from other languages
# there don't need to be multiple instances of this, so leave it as
# a module instead of making a ScreenManager class

# same concept applies to many other modules in this project

import pygame
import sys

from screens import Screen
from GameConstants import FRAME_TIME

currentScreen: Screen = None


def setScreen(newScreen: Screen):
	global currentScreen
	currentScreen = newScreen


def exit():
	sys.exit()


def start():  # start the game - called from C200_Breakout_Team12.py
	while True:
		beginTime = pygame.time.get_ticks()
		currentScreen.update()
		endTime = pygame.time.get_ticks()

		timeConsumed = endTime - beginTime

		# time consumed can be longer than 16.7 ms, for example on the loading screen
		# so don't delay() for a negative value
		if timeConsumed < FRAME_TIME:
			pygame.time.delay(int(FRAME_TIME - timeConsumed))
