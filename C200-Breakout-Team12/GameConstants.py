# Various constant values.
# Many modules will have to use many of these values, so
# 'from GameConstants import *' will be a useful statement
# Thus, use the GC_ prefix to avoid namespace conflicts.

# sizes for ball, paddle, bricks, etc. must match up with assets

# debug switches
GC_PRINT_FPS: bool = True
GC_MOTION_BLUR: bool = False

from typing import Tuple
import pygame

# size of game screen in world coordinates
# we want this to be high, even if visual style will be low-res/blocky
# DIMENSIONS MUST BE EVEN
GC_WORLD_SIZE: Tuple[int, int] = (1920, 1080)
GC_WORLD_WIDTH: int = GC_WORLD_SIZE[0]
GC_WORLD_HEIGHT: int = GC_WORLD_SIZE[1]

GC_FPS: int = 60
GC_FRAME_TIME_SECONDS: float = 1 / GC_FPS
GC_FRAME_TIME_MILLISECONDS: float = GC_FRAME_TIME_SECONDS * 1000

# keys, organized by game screen on which they are used
GC_KEY_MAINMENU_BEGIN = pygame.K_SPACE
GC_KEY_GAME_PAUSE = pygame.K_ESCAPE

GC_WALL_SIZE: int = 100  # walls at left/right edges of screen

GC_BALL_RADIUS: int = 13
GC_BALL_INITIAL_ANGLE_VARIATION: int = 60  # degrees to either side of straight down
GC_BALL_INITIAL_VELOCITY_RANGE: Tuple[int, int] = (7, 12)  # initial velocity of ball is within these
GC_GRAVITY_ACCEL = 0.5

GC_PADDLE_WIDTH: int = 225
GC_PADDLE_HEIGHT: int = 20
GC_PADDLE_TOP_HEIGHT: int = int(GC_WORLD_HEIGHT - GC_PADDLE_HEIGHT * 2.25)
GC_PADDLE_SPEED: int = 18

GC_BRICK_LAYERS: int = 12
GC_BRICK_COLUMNS: int = 20
GC_BRICK_HEIGHT: int = 50
GC_BRICK_WIDTH: int = (GC_WORLD_WIDTH - 2 * GC_WALL_SIZE) // GC_BRICK_COLUMNS
GC_BRICK_TOP_HEIGHT: int = 70
GC_BRICK_BOTTOM_HEIGHT: int = GC_BRICK_TOP_HEIGHT + GC_BRICK_LAYERS * GC_BRICK_HEIGHT
