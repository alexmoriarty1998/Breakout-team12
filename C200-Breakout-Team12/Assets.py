# Asset storage class

# images are prepended with I_, sounds with S_, music with M_

import pygame
from pygame import Surface

import Graphics


# shortcut for pygame.image.load; adds assets/ and .png to given path and does convert_alpha()
def li(path: str) -> Surface:
	return pygame.image.load("assets/" + path + ".png").convert_alpha(Graphics.surface)


class Assets:
	###   GENERAL   ###########################################################
	I_BLUR: Surface = li("blur")

	###   SCREEN BACKGROUNDS   ################################################
	I_MAINMENU_BACKGROUND: Surface = li("mainMenu/background")
	I_BETWEEN_LEVELS_BACKGROUND: Surface = li("betweenLevels/background")
	I_INSTRUCTIONS_BACKGROUND: Surface = li("instructions/background")
	I_HIGHSCORE_ENTRY_BACKGROUND: Surface = li("highscoreEntry/background")

	###   GAME SCREEN   #######################################################
	I_BALL: Surface = li("game/ball")
	I_PADDLE: Surface = li("game/paddle")
	I_WALL: Surface = li("game/wall")

	I_BRICK_LEVEL1: Surface = li("game/brick11")  # 1 HP brick
	I_BRICK_LEVEL2_2: Surface = li("game/brick22")  # 2 HP brick at 2 HP
	I_BRICK_LEVEL2_1: Surface = li("game/brick21")  # 2 HP brick at 1 HP
	I_BRICK_LEVEL3_3: Surface = li("game/brick33")  # 3 HP brick at 3 HP
	I_BRICK_LEVEL3_2: Surface = li("game/brick32")  # 3 HP brick at 2 HP
	I_BRICK_LEVEL3_1: Surface = li("game/brick31")  # 3 HP brick at 1 HP
	I_BRICK_BOSS: Surface = li("game/brickBOSS")  # undestroyable brick

	###   IMAGE TEXT   ########################################################
	I_TXT_SCORE: Surface = li("imgFont/score2")  # use any of score1 score2
	I_TXT_LEVEL: Surface = li("imgFont/level3")  # use any of level1 level2 level3
	I_TXT_TIME: Surface = li("imgFont/time2")  # use any of time1 time2
	I_TXT_LIFE: Surface = li("imgFont/life")  # not really text, but still belong with imgFonts


class AssetLoaderHelper:
	# Initializes values in Assets using setattr.
	# setattr cant be used in assets because it would
	# have to be used before the class is fully initialized.
	# This needs to be put in a class so its not run every
	# time this module is imported.

	for i in "0123456789":
		setattr(Assets, "I_TXT_" + i, li("imgFont/" + i))
	# variable names should be caps, image files are lowercase (e.g. a.png -> I_TXT_A)
	for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		setattr(Assets, "I_TXT_" + i, li("imgFont/" + i.lower()))
