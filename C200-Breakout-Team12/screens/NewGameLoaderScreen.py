import math
import random

import ScreenManager
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from game.gameClasses.Ball import Ball
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity
from screens.GameScreen import GameScreen
from screens.Screen import Screen
from game.gameClasses.Brick import Brick



# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen, or 'restart game' button on pause screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()

		# no need to display a loading screen here, this should only take a split second

		# TODO: load the actual bricks
		#######################################################################
		###   init bricks   ###################################################
		#######################################################################
		bricks = [Brick(PosRect(180, 180, GC_BRICK_WIDTH, GC_BRICK_HEIGHT), 80, 1),
				  Brick(PosRect(280, 280, GC_BRICK_WIDTH, GC_BRICK_HEIGHT), 80, 1)]

		#######################################################################
		###   init ball   #####################################################
		#######################################################################
		# generate its position randomly
		posY = random.randint(GC_BRICK_BOTTOM_HEIGHT + 50, GC_PADDLE_TOP_HEIGHT - 50)
		ballCircle = PosCircle(GC_WORLD_WIDTH / 2, posY, GC_BALL_RADIUS)
		# generate its velocity (magnitude and angle) randomly
		initialVelocityMagnitude = random.randint(GC_BALL_INITIAL_VELOCITY_RANGE[0],
												  GC_BALL_INITIAL_VELOCITY_RANGE[1])
		initialVelocityAngle = random.randint(90 - GC_BALL_INITIAL_ANGLE_VARIATION,
											  90 + GC_BALL_INITIAL_ANGLE_VARIATION)
		dx = math.cos(math.radians(initialVelocityAngle)) * initialVelocityMagnitude
		dy = math.sin(math.radians(initialVelocityAngle)) * initialVelocityMagnitude
		ballVelocity = Velocity(dx, dy)
		# make the ball
		ball = Ball(ballCircle, ballVelocity)

		#######################################################################
		###   start the game   ################################################
		#######################################################################
		state = GameState(bricks, ball, 1, 0)
		controller = GameController(state)
		renderer = GameRenderer()

		ScreenManager.setScreen(GameScreen(state, controller, renderer))
