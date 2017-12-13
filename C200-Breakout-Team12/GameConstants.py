# Various constant values.
# Many modules will have to use many of these values, so
# 'from GameConstants import *' will be a useful statement
# Thus, use the GC_ prefix to avoid namespace conflicts.

# @formatter:off

import sys

IS_MAC = "darwin" in sys.platform # mac == darwin, enables workarounds to run properly on mac

###############################################################################
###   DEBUG SWITCHES   ########################################################
###############################################################################
GC_PRINT_FPS: bool = False
GC_PROFILE: bool = False  # profile game via cProfile module

GC_BRICK_GEN_MODE: str = "manual"	# "empty", "random", "filled", "manual"
GC_GRAB_MOUSE: bool = True

GC_RESET_HIGHSCORES = False			# reset highscores: enable this, start the game and quit, then disable it

GC_MOTION_BLUR: bool = not IS_MAC
GC_FULLSCREEN: bool = False			# TODO: enable this for final product

###############################################################################
import math
import pygame
from typing import Tuple
from game.Highscores import Highscores

if GC_RESET_HIGHSCORES:
	Highscores.reset()

###############################################################################

###############################################################################
###   SYSTEM SETTINGS   #######################################################
###############################################################################
GC_FPS: int = 60
GC_FRAME_TIME_SECONDS: float = 1 / GC_FPS
GC_FRAME_TIME_MILLISECONDS: float = GC_FRAME_TIME_SECONDS * 1000

GC_WORLD_SIZE: Tuple[int, int] = (1920, 1080)  # size of game screen in world coordinates
GC_WORLD_WIDTH: int = GC_WORLD_SIZE[0]  # dimensions of above must be even
GC_WORLD_HEIGHT: int = GC_WORLD_SIZE[1]

###############################################################################
###   KEYBINDINGS   ###########################################################
###############################################################################
GC_KEY_BEGIN = pygame.K_SPACE  # for various begin functions: begin from main menu, begin a paused ball, continue to next level, etc.

###############################################################################
###   RENDERING   #############################################################
###############################################################################
GC_IMGFONT_SIZE = 75
GC_SMALL_BUTTON_SIZE = 65

###############################################################################
###   GAME CONSTANTS   ########################################################
###############################################################################
###   SCORING   ###############################################################
GC_DEFAULT_LIVES = 3
GC_PAR_TIME = 180
GC_NUM_LEVELS = 1

###   MISC. VALUES   ##########################################################
GC_WALL_SIZE: int = 100  # walls at left/right edges of screen
GC_HIGHSCORES_LEFT_X = 300  # display values for highscore display screen
GC_HIGHSCORE_SPACING = 75
GC_HIGHSCORE_ENTRY_BEGIN_X = int(GC_WORLD_WIDTH // 2 - 1.5 * GC_IMGFONT_SIZE)
GC_HIGHSCORE_ENTRY_HEIGHT = 420

###   BALL   ##################################################################
GC_BALL_RADIUS: int = 13
GC_BALL_INITIAL_ANGLE_VARIATION: int = 20  # degrees to either side of straight down
GC_MAX_BOUNCE_ANGLE: int = 60  # offset from 270 degrees, this is at edge of paddle
GC_BALL_INITIAL_VELOCITY: int = 14  # speed and gravity must be matched together
GC_GRAVITY_ACCEL: float = 0.05

###   PADDLE   ################################################################
GC_PADDLE_WIDTH: int = 225
GC_PADDLE_HEIGHT: int = 20
GC_PADDLE_TOP_HEIGHT: int = int(GC_WORLD_HEIGHT - GC_PADDLE_HEIGHT * 2.25)  # y-coord of top of paddle
GC_PADDLE_SPEED: int = 22

GC_PADDLE_UL_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_UL_ANGLE = 360 + GC_PADDLE_UL_ANGLE  # convert negative angle to positive
GC_PADDLE_UR_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))
GC_PADDLE_UR_ANGLE = 360 + GC_PADDLE_UR_ANGLE
GC_PADDLE_BL_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_BR_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))

###   BRICKS   ################################################################
GC_BRICK_LAYERS: int = 10
GC_BRICK_COLUMNS: int = 20
GC_TOTAL_BRICKS = GC_BRICK_LAYERS * GC_BRICK_COLUMNS

GC_BRICK_HEIGHT: int = 50
GC_BRICK_WIDTH: int = (GC_WORLD_WIDTH - 2 * GC_WALL_SIZE) // GC_BRICK_COLUMNS

GC_BRICK_TOP_HEIGHT: int = 120  # top and bottom height of brick grid
GC_BRICK_BOTTOM_HEIGHT: int = GC_BRICK_TOP_HEIGHT + GC_BRICK_LAYERS * GC_BRICK_HEIGHT

GC_BRICK_UL_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_UL_ANGLE = 360 + GC_BRICK_UL_ANGLE  # convert negative angle to positive
GC_BRICK_UR_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
GC_BRICK_UR_ANGLE = 360 + GC_BRICK_UR_ANGLE
GC_BRICK_BL_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_BR_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
GC_BRICK_SCORES = [100, 200, 300, 0]
