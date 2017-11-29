# Asset storage class

# images are prepended with I_, sounds with S_, music with M_

import Graphics
import pygame
from pygame import Surface


# shortcut for pygame.image.load; adds assets/ and .png to given path and does convert_alpha()
def li(path: str) -> Surface:
	return pygame.image.load("assets/" + path + ".png").convert_alpha(Graphics.surface)


class Assets:
	# Testing confirms that these are initialized only once, not every time the class is imported
	# They are static variables to avoid having to pass around an instance of this class everywhere.

	# temporary/testing assets
	I_WON: Surface = li('testing/won')
	I_LOST: Surface = li('testing/lost')


	I_BLUR: Surface = li("blur")

	I_MAINMENU_BACKGROUND: Surface = li("mainMenu/background")

	I_BALL: Surface = li("game/ball")
	I_PADDLE: Surface = li("game/paddle")

	I_BRICK_LEVEL1: Surface = li("game/brick11")  # 1 HP brick
	I_BRICK_LEVEL2_2: Surface = li("game/brick22")  # 2 HP brick at 2 HP
	I_BRICK_LEVEL2_1: Surface = li("game/brick21")  # 2 HP brick at 1 HP
	I_BRICK_LEVEL3_3: Surface = li("game/brick33")  # 3 HP brick at 3 HP
	I_BRICK_LEVEL3_2: Surface = li("game/brick32")  # 3 HP brick at 2 HP
	I_BRICK_LEVEL3_1: Surface = li("game/brick31")  # 3 HP brick at 1 HP
	I_BRICK_BOSS: Surface = li("game/brickBOSS")  # undestroyable brick
	I_WALL: Surface = li("game/wall")
