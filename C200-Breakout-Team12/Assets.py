# Asset storage class

# images are prepended with I_, sounds with S_, music with M_

import pygame
from pygame import Surface
from os import listdir

import Graphics


# shortcut for pygame.image.load; adds assets/ and .png to given path and does convert_alpha()
from game.gameClasses.Animation import Animation


def li(path: str) -> Surface:
	# noinspection PyUnresolvedReferences
	return pygame.image.load("assets/" + path + ".png").convert_alpha(Graphics.surface)


def la(path: str, name: str, frameTime: int) -> Animation:
	files = listdir("assets/" + path)

	# list is not necessarily alphabetical, so can't just add frames to the list of frames in the for loop
	numFrames = 0
	for f in files:
		if f[0:len(name)] == name:  # if it is a frame of the desired animation
			numFrames += 1

	imagesList = []
	for i in range(numFrames):
		imagesList.append(li(path + "/" + name + str(i)))

	# the beginframe must be set when the animation is created in game
	return Animation(imagesList, frameTime, 0)


class Assets:
	###   GENERAL   ###########################################################
	I_BLUR = li("blur")

	###   SCREEN BACKGROUNDS   ################################################
	I_MAINMENU_BACKGROUND = li("mainMenu/background")
	I_BETWEENLEVELS_BACKGROUND = li("betweenLevels/background")
	I_INSTRUCTIONS_BACKGROUND = li("instructions/background")
	I_HIGHSCORE_DISPLAY_BACKGROUND = li("highscoreDisplay/background")
	I_HIGHSCORE_ENTRY_BACKGROUND = li("highscoreEntry/background")
	I_PAUSE_BACKGROUND = li("pause/background")

	###   GAME SCREEN   #######################################################
	I_BALL = li("game/ball")
	I_PADDLE = li("game/paddle")
	I_WALL = li("game/wall")

	I_BRICK_LEVEL1 = li("game/brick11")  # 1 HP brick
	I_BRICK_LEVEL2_2 = li("game/brick22")  # 2 HP brick at 2 HP
	I_BRICK_LEVEL2_1 = li("game/brick21")  # 2 HP brick at 1 HP
	I_BRICK_LEVEL3_3 = li("game/brick33")  # 3 HP brick at 3 HP
	I_BRICK_LEVEL3_2 = li("game/brick32")  # 3 HP brick at 2 HP
	I_BRICK_LEVEL3_1 = li("game/brick31")  # 3 HP brick at 1 HP
	I_BRICK_BOSS = li("game/brickBOSS")  # undestroyable brick
	I_BRICK_EXTRABALL_2 = li("game/brick_extraBall_2")  # powerup brick at 2 HP
	I_BRICK_EXTRABALL_1 = li("game/brick_extraBall_1")  # powerup brick at 1 HP
	I_BRICK_CLEARROW_2 = li("game/brick_clearRow_2")
	I_BRICK_CLEARROW_1 = li("game/brick_clearRow_1")

	###   IMAGE TEXT   ########################################################
	I_TXT_SCORE = li("imgFont/score")  # use any of score1 score2
	I_TXT_LEVEL = li("imgFont/level1")
	I_TXT_TIME = li("imgFont/time")  # use any of time1 time2
	I_TXT_LIFE = li("imgFont/life")  # not really text, but still belong with imgFonts

	###   BUTTONS   ###########################################################
	# back and exit
	I_BTN_BACK = li("buttons/back")
	I_BTN_BACK_H = li("buttons/back_h")
	I_BTN_EXIT = li("buttons/exit")
	I_BTN_EXIT_H = li("buttons/exit_h")

	# main menu screen
	I_BTN_MAINMENU_EXIT = li("mainMenu/exit")
	I_BTN_MAINMENU_EXIT_H = li("mainMenu/exit_h")
	I_BTN_MAINMENU_BEGIN = li("mainMenu/btn_begin")
	I_BTN_MAINMENU_BEGIN_H = li("mainMenu/btn_begin_h")
	I_BTN_MAINMENU_HELP = li("mainMenu/btn_help")
	I_BTN_MAINMENU_HELP_H = li("mainMenu/btn_help_h")
	I_BTN_MAINMENU_HIGHSCORES = li("mainMenu/btn_highscores")
	I_BTN_MAINMENU_HIGHSCORES_H = li("mainMenu/btn_highscores_h")
	# fullscreen toggling
	I_BTN_FULLSCREEN = li("mainMenu/fullscreen")
	I_BTN_UNFULLSCREEN = li("mainMenu/unfullscreen")
	I_BTN_FULLSCREEN_H = li("mainMenu/fullscreen_h")
	I_BTN_UNFULLSCREEN_H = li("mainMenu/unfullscreen_h")

	# pause screen
	I_BTN_PAUSE_RESUME = li("pause/btn_resume")
	I_BTN_PAUSE_RESUME_H = li("pause/btn_resume_h")

	# between levels screen
	I_BTN_BETWEENLEVELS_CONTINUE = li("betweenLevels/btn_continue")
	I_BTN_BETWEENLEVELS_CONTINUE_H = li("betweenLevels/btn_continue_h")

	# pause & between levels
	I_BTN_QUIT_TO_MENU = li("pause/btn_quit")
	I_BTN_QUIT_TO_MENU_H = li("pause/btn_quit_h")

	# highscore entry
	I_BTN_HIGHSCORES_SUBMIT = li("highscoreEntry/btn_submit")
	I_BTN_HIGHSCORES_SUBMIT_H = li("highscoreEntry/btn_submit_h")
	I_BTN_HIGHSCORES_CANCEL = li("highscoreEntry/btn_cancel")
	I_BTN_HIGHSCORES_CANCEL_H = li("highscoreEntry/btn_cancel_h")

	###   ANIMATIONS   ########################################################
	A_WALL_BOUNCE_S = la("animations", "wallS", 5)


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
