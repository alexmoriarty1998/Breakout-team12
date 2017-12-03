# Various constant values.
# Many modules will have to use many of these values, so
# 'from GameConstants import *' will be a useful statement
# Thus, use the GC_ prefix to avoid namespace conflicts.

# @formatter:off

###############################################################################
###   DEBUG SWITCHES   ########################################################
###############################################################################
GC_PRINT_FPS: bool        = False
GC_PROFILE: bool          = False	# profile game via cProfile module
GC_PRINT_BALL_SPEED: bool = False
# TODO: remove this once it's shown in the GUI
GC_PRINT_GAME_TIME: bool  = True

GC_BRICK_GEN_MODE: str    = "empty"  # "empty", "random", "fill"

GC_MOTION_BLUR: bool = False               # TODO: enable this for final product
GC_FULLSCREEN: bool  = False               # TODO: enable this for final product

###############################################################################
import math, pygame                                                           #
from typing import Tuple                                                      #
###############################################################################

###############################################################################
###   SYSTEM SETTINGS   #######################################################
###############################################################################
GC_FPS: int = 60
GC_FRAME_TIME_SECONDS: float = 1 / GC_FPS
GC_FRAME_TIME_MILLISECONDS: float = GC_FRAME_TIME_SECONDS * 1000

GC_WORLD_SIZE: Tuple[int, int] = (1920, 1080) # size of game screen in world coordinates
GC_WORLD_WIDTH: int = GC_WORLD_SIZE[0]        # dimensions of above must be even
GC_WORLD_HEIGHT: int = GC_WORLD_SIZE[1]

###############################################################################
###   KEYBINDINGS   ###########################################################
###############################################################################
GC_KEY_BEGIN = pygame.K_SPACE  # for various begin functions: begin from main menu, begin a paused ball, continue to next level, etc.
GC_KEY_PAUSE = pygame.K_ESCAPE

###############################################################################
###   RENDERING   #############################################################
###############################################################################
GC_TEXT_COLOR = (0, 0, 0)
GC_FONT_SIZE = 35

###############################################################################
###   GAME CONSTANTS   ########################################################
###############################################################################
###   SCORING   ###############################################################
GC_DEFAULT_LIVES = 3
GC_PAR_TIME = 60

###   MISC. VALUES   ##########################################################
GC_WALL_SIZE: int = 100  # walls at left/right edges of screen

###   BALL   ##################################################################
GC_BALL_RADIUS: int = 13
GC_BALL_INITIAL_ANGLE_VARIATION: int = 20  # degrees to either side of straight down
GC_MAX_BOUNCE_ANGLE: int = 60              # offset from 270 degrees, this is at edge of paddle
GC_BALL_INITIAL_VELOCITY: int = 14         # speed and gravity must be matched together
GC_GRAVITY_ACCEL: float = 0.1

###   PADDLE   ################################################################
GC_PADDLE_WIDTH: int = 225
GC_PADDLE_HEIGHT: int = 20
GC_PADDLE_TOP_HEIGHT: int = int(GC_WORLD_HEIGHT - GC_PADDLE_HEIGHT * 2.25) # y-coord of top of paddle
GC_PADDLE_SPEED: int = 22

GC_PADDLE_UL_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_UL_ANGLE = 360 + GC_PADDLE_UL_ANGLE  # convert negative angle to positive
GC_PADDLE_UR_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))
GC_PADDLE_UR_ANGLE = 360 + GC_PADDLE_UR_ANGLE
GC_PADDLE_BL_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_BR_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))

###   BRICKS   ################################################################
GC_BRICK_LAYERS: int = 8
GC_BRICK_COLUMNS: int = 20
GC_TOTAL_BRICKS = GC_BRICK_LAYERS * GC_BRICK_COLUMNS

GC_BRICK_HEIGHT: int = 50
GC_BRICK_WIDTH: int = (GC_WORLD_WIDTH - 2 * GC_WALL_SIZE) // GC_BRICK_COLUMNS

GC_BRICK_TOP_HEIGHT: int = 150 # top and bottom height of brick grid
GC_BRICK_BOTTOM_HEIGHT: int = GC_BRICK_TOP_HEIGHT + GC_BRICK_LAYERS * GC_BRICK_HEIGHT

GC_BRICK_UL_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_UL_ANGLE = 360 + GC_BRICK_UL_ANGLE  # convert negative angle to positive
GC_BRICK_UR_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
GC_BRICK_UR_ANGLE = 360 + GC_BRICK_UR_ANGLE
GC_BRICK_BL_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_BR_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
GC_BRICK_SCORES = [100, 200, 300, 0]
