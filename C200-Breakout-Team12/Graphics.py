# Graphics class
# Stores pygame surface, manages windowed/fullscreen and display scaling / abstraction

from typing import List, Tuple

import pygame

from GameConstants import *

DEFAULT_WINDOW_RESOLUTION: Tuple[int, int] = (GC_WORLD_WIDTH // 2, GC_WORLD_HEIGHT // 2)
MODE_WINDOWED: int = 1
MODE_FULLSCREEN: int = 2

GAME_ASPECT_RATIO: float = GC_WORLD_WIDTH / GC_WORLD_HEIGHT

font = pygame.font.Font('assets/font.ttf', GC_FONT_SIZE)

surface: pygame.Surface = pygame.Surface(GC_WORLD_SIZE)  # surface that the game draws on; in world coordinates
windowSurface: pygame.Surface = None  # surface that appears on the screen
currentMode: int = None


def blur(blurImg: pygame.Surface) -> None:
	# Importing Assets in this module causes issues with assets being
	# loaded before this Graphics module is fully initialized. The solution
	# is to not init the assets as static variables of the class Assets,
	# but to have them as variables of the class (static or instance)
	# and have a load() method which loads the images. However, this results
	# in either each asset being listed twice (once declared in the class
	# scope, then loaded in load()), or the IDE autocomplete not working well
	# with them (which is important, because assets have long and hard to
	# remember names). So we use unclean code in LoadingScreen.py to avoid
	# this trap there, and here we have the draw code pass in Assets.I_BLUR
	# as the image to blur with, instead of having a reference to it in this
	# module.
	surface.blit(blurImg, (0, 0))


def hardClear():
	surface.fill((0, 0, 0))


def clear(blurImg: pygame.Surface) -> None:
	blur(blurImg) if GC_MOTION_BLUR else hardClear()


def resizeWindow(size) -> None:
	pygame.display.set_mode(size, pygame.RESIZABLE)


def getARScaling() -> List[Tuple]:
	# The window aspect ratio is not always the same as the game's aspect ratio, so
	# calculate the size at which to draw the game onto the screen (leaving black bars
	# at the top/bottom, if necessary). Also calculate the offset (so that there are
	# black bars on both sides, instead of there being one large one at the bottom or
	# right).

	windowWidth = windowSurface.get_width()
	windowHeight = windowSurface.get_height()

	windowAR = windowWidth / windowHeight
	if windowAR > GAME_ASPECT_RATIO:
		# window wider than game
		# limit height to window height, calculate width
		# pos is (widthDiff/2, 0)
		scaledHeight = windowHeight
		scaledWidth = int(windowHeight * GAME_ASPECT_RATIO)  # 16/9 AR; height = 9; width = 9 * 16/9 - math checks out
		widthDiff = windowWidth - scaledWidth
		return [(scaledWidth, scaledHeight), (widthDiff // 2, 0)]
	else:
		# window taller than or == to game
		# limit width, calculate height
		# pos is (0, heightDiff/2)
		scaledWidth = windowWidth
		scaledHeight = int(windowWidth / GAME_ASPECT_RATIO)  # opposite of the code in the if: block
		heightDiff = windowHeight - scaledHeight
		return [(scaledWidth, scaledHeight), (0, heightDiff // 2)]


def flip() -> None:
	# scale the game surface to match the window surface
	# then copy it over and display it on the screen

	windowSurface.fill((0, 0, 0))  # leave black bars on borders in case of aspect ratio mismatch

	arScaling = getARScaling()  # list of two tuples, first is size, 2nd is pos
	windowSurface.blit(pygame.transform.scale(surface, arScaling[0]), arScaling[1])
	pygame.display.flip()


def goFullscreen() -> None:
	global windowSurface, currentMode
	windowSurface = pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)
	currentMode = MODE_FULLSCREEN


def goWindowed() -> None:
	global windowSurface, currentMode
	windowSurface = pygame.display.set_mode(DEFAULT_WINDOW_RESOLUTION, pygame.RESIZABLE)
	currentMode = MODE_WINDOWED


def swapWindowMode():
	goWindowed() if currentMode == MODE_FULLSCREEN else goFullscreen()
