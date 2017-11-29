# ScreenManager
# contains main game loop, manages game screens

# in python, modules act like static classes from other languages
# there don't need to be multiple instances of this, so leave it as
# a module instead of making a ScreenManager class

# same concept applies to many other modules in this project

import pygame
import sys

from screens import Screen
from GameConstants import GC_FRAME_TIME_MILLISECONDS, GC_PRINT_FPS

currentScreen: Screen = None


def setScreen(newScreen: Screen):
	global currentScreen
	currentScreen = newScreen


def exit():
	pygame.quit()
	sys.exit()


lastBeginTime = 0

def start():  # start the game - called from C200_Breakout_Team12.py
	while True:
		beginTime = pygame.time.get_ticks()
		currentScreen.update()
		endTime = pygame.time.get_ticks()

		timeConsumed = endTime - beginTime

		# time consumed can be longer than 16.7 ms, for example on the loading screen
		# so don't delay() for a negative value
		if timeConsumed < GC_FRAME_TIME_MILLISECONDS:
			pygame.time.delay(int(GC_FRAME_TIME_MILLISECONDS - timeConsumed))

		if GC_PRINT_FPS:
			global lastBeginTime
			fps = 1000 / (beginTime - lastBeginTime)
			delayTime = int(GC_FRAME_TIME_MILLISECONDS - timeConsumed)
			print("FPS = {0:.1f} frame time = {1} ms; delaying for {2} ms".format(fps, timeConsumed, delayTime))
			lastBeginTime = beginTime
