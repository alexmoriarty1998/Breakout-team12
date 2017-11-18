# Graphics class
# Stores pygame surface, manages windowed/fullscreen and display scaling / abstraction

import pygame

from GameConstants import WORLD_WIDTH, WORLD_HEIGHT

DEFAULT_WINDOW_RESOLUTION = (WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
MODE_WINDOWED = 1
MODE_FULLSCREEN = 2

surface: pygame.Surface = None  # surface that the game draws on; in world coordinates
windowSurface: pygame.Surface = None  # surface that appears on the screen
currentMode = None


def flip():  # scale the game surface to match the window surface, then copy it over and display it on the screen

	# windowSurface.blit(pygame.transform.scale(gameSurface, (windowSurface.get_width(), windowSurface.get_height())))

	# use destination surface in scale method instead of blitting the scaled surface into windowSurface
	# may or may not work and require reverting to the commented out line above
	pygame.transform.scale(surface, (windowSurface.get_width(), windowSurface.get_height()), windowSurface)
	pygame.display.flip()


def goFullscreen():
	global windowSurface, currentMode
	windowSurface = pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)
	currentMode = MODE_FULLSCREEN


def goWindowed():
	global windowSurface, currentMode
	windowSurface = pygame.display.set_mode(DEFAULT_WINDOW_RESOLUTION, pygame.RESIZABLE)
	currentMode = MODE_WINDOWED


def swapWindowMode():
	if currentMode == MODE_FULLSCREEN:
		goWindowed()
	else:
		goFullscreen()
