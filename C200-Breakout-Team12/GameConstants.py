# Various constant values.
# Many modules will have to use many of these values, so
# 'from GameConstants import *' will be a useful statement
# Thus, use the GC_ prefix to avoid namespace conflicts.

# sizes for ball, paddle, bricks, etc. must match up with assets

# debug switches
GC_PRINT_FPS: bool = False
GC_PROFILE: bool = False
GC_MOTION_BLUR: bool = True
GC_BRICK_GENERATION_METHOD: str = "fill"  # possible values: "empty", "random", "fill"

GC_FULLSCREEN = False

import math
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
GC_BALL_INITIAL_ANGLE_VARIATION: int = 20  # degrees to either side of straight down
GC_MAX_BOUNCE_ANGLE: int = 60  # offset from 270 degrees
# do not change ball velocity and gravity strength - these have been specially selected for good gameplay
GC_BALL_INITIAL_VELOCITY: int = 14
GC_GRAVITY_ACCEL: float = 0.1


GC_PADDLE_WIDTH: int = 225
GC_PADDLE_HEIGHT: int = 20
GC_PADDLE_TOP_HEIGHT: int = int(GC_WORLD_HEIGHT - GC_PADDLE_HEIGHT * 2.25)
GC_PADDLE_SPEED: int = 22
GC_PADDLE_UL_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_UL_ANGLE = 360 + GC_PADDLE_UL_ANGLE  # convert negative angle to positive
GC_PADDLE_UR_ANGLE: float = math.degrees(math.atan2(-GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))
GC_PADDLE_UR_ANGLE = 360 + GC_PADDLE_UR_ANGLE
GC_PADDLE_BL_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, -GC_PADDLE_WIDTH / 2))
GC_PADDLE_BR_ANGLE: float = math.degrees(math.atan2(GC_PADDLE_HEIGHT / 2, GC_PADDLE_WIDTH / 2))

GC_BRICK_LAYERS: int = 8
GC_BRICK_COLUMNS: int = 20
GC_BRICK_HEIGHT: int = 50
GC_BRICK_WIDTH: int = (GC_WORLD_WIDTH - 2 * GC_WALL_SIZE) // GC_BRICK_COLUMNS
GC_BRICK_TOP_HEIGHT: int = 150
GC_BRICK_BOTTOM_HEIGHT: int = GC_BRICK_TOP_HEIGHT + GC_BRICK_LAYERS * GC_BRICK_HEIGHT
GC_BRICK_UL_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_UL_ANGLE = 360 + GC_BRICK_UL_ANGLE  # convert negative angle to positive
GC_BRICK_UR_ANGLE: float = math.degrees(math.atan2(-GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
GC_BRICK_UR_ANGLE = 360 + GC_BRICK_UR_ANGLE
GC_BRICK_BL_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, -GC_BRICK_WIDTH / 2))
GC_BRICK_BR_ANGLE: float = math.degrees(math.atan2(GC_BRICK_HEIGHT / 2, GC_BRICK_WIDTH / 2))
