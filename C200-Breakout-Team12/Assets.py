# Asset storage class

# images are prepended with I_, sounds with S_, music with M_

import Graphics
import pygame
from pygame import Surface

from GameConstants import GC_FONT_SIZE


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
	I_TXT_LIFE: Surface = li("imgFont/life")
	I_TXT_0: Surface = li("imgFont/0")
	I_TXT_1: Surface = li("imgFont/1")
	I_TXT_2: Surface = li("imgFont/2")
	I_TXT_3: Surface = li("imgFont/3")
	I_TXT_4: Surface = li("imgFont/4")
	I_TXT_5: Surface = li("imgFont/5")
	I_TXT_6: Surface = li("imgFont/6")
	I_TXT_7: Surface = li("imgFont/7")
	I_TXT_8: Surface = li("imgFont/8")
	I_TXT_9: Surface = li("imgFont/9")

	###   FONTS   #############################################################
	# TODO: do we need this?
	F_DJ_CONDENSED = pygame.font.Font('assets/fonts/dejavu_sans_condensed.ttf', GC_FONT_SIZE)
