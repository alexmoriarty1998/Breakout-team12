import random

import ScreenManager
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity
from screens.GameScreen import GameScreen
from screens.Screen import Screen


# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen, or 'restart game' button on pause screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()

		# no need to display a loading screen here, this should only take a split second

		#######################################################################
		###   init bricks   ###################################################
		#######################################################################
		bricks = []

		if GC_BRICK_GENERATION_METHOD == "random":
			maxHP = 1
			for i in range(33):
				brickX = random.randint(GC_WALL_SIZE, GC_WORLD_WIDTH - GC_WALL_SIZE - GC_BRICK_WIDTH)
				brickY = random.randint(GC_BRICK_TOP_HEIGHT,
										GC_BRICK_BOTTOM_HEIGHT - GC_BRICK_HEIGHT)  # top-down coordinates
				bricks.append(Brick(PosRect(brickX, brickY, GC_BRICK_WIDTH, GC_BRICK_HEIGHT), 100, maxHP))
				maxHP += 1
				if maxHP == 4:
					maxHP = -1
				if maxHP == 0:
					maxHP = 1

		if GC_BRICK_GENERATION_METHOD == "fill":
			# TODO: add different chances for different HP blocks
			for i in range(GC_BRICK_COLUMNS):
				for j in range(GC_BRICK_LAYERS):
					brickX = i * GC_BRICK_WIDTH + GC_WALL_SIZE
					brickY = j * GC_BRICK_HEIGHT + GC_BRICK_TOP_HEIGHT
					brickHP = random.randint(1, 4)
					if brickHP == 4:
						brickHP = -1
					bricks.append(Brick(PosRect(brickX, brickY, GC_BRICK_WIDTH, GC_BRICK_HEIGHT), 100, brickHP))

		#######################################################################
		###   init ball   #####################################################
		#######################################################################
		# generate its position randomly
		posY = random.randint(GC_BRICK_BOTTOM_HEIGHT + 50, GC_PADDLE_TOP_HEIGHT - 50)
		ballCircle = PosCircle(GC_WORLD_WIDTH / 2, posY, GC_BALL_RADIUS)
		# generate its velocity (magnitude and angle) randomly
		initialVelocityMagnitude = GC_BALL_INITIAL_VELOCITY
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
		controller = GameController()
		renderer = GameRenderer()

		ScreenManager.setScreen(GameScreen(state, controller, renderer))
