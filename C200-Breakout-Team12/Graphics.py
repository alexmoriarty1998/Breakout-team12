# Graphics class
# Stores pygame surface, manages windowed/fullscreen and display scaling / abstraction

import sys
from typing import List

from GameConstants import *

DEFAULT_WINDOW_RESOLUTION: Tuple[int, int] = (GC_WORLD_WIDTH // 2, GC_WORLD_HEIGHT // 2)
MODE_WINDOWED: int = 1
MODE_FULLSCREEN: int = 2

GAME_ASPECT_RATIO: float = GC_WORLD_WIDTH / GC_WORLD_HEIGHT

surface: pygame.Surface = pygame.Surface(GC_WORLD_SIZE)  # surface that the game draws on; in world coordinates
windowSurface: pygame.Surface = None  # surface that appears on the screen
currentMode: int = None


def blur() -> None:
	# Importing Assets in this module causes issues with assets being
	# loaded before this Graphics module is fully initialized.
	# However, we know that clear()/blur() will never be called before
	# assets are loaded, so use getattr and sys.modules to load the
	# blur image without actually importing it here.
	img: pygame.Surface = getattr(sys.modules['Assets'], "I_BLUR")
	surface.blit(img, (0, 0))


def hardClear():
	# Clear screen to black
	surface.fill((0, 0, 0))


def clear() -> None:
	# Performs blur() or hardClear() depending on flag in game constants.
	blur() if GC_MOTION_BLUR else hardClear()


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


def isFullscreen():
	return currentMode == MODE_FULLSCREEN


def swapWindowMode():
	goWindowed() if isFullscreen() else goFullscreen()


def unproject(pos):
	x = pos[0]
	y = pos[1]
	xLoc = x / windowSurface.get_width()
	x = xLoc * GC_WORLD_WIDTH
	yLoc = y / windowSurface.get_height()
	y = yLoc * GC_WORLD_HEIGHT
	return x, y
