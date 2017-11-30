import random

import GameConstants
import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameState import GameState
from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity
from screens.Screen import Screen


class BetweenLevelsScreen(Screen):
	def __init__(self, level, score):
		self.level = level
		self.score = score
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
		state = GameState(bricks, ball, self.level + 1, self.score)
		self.state = state

	def update(self):
		super().update()
		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.blit(Assets.I_BETWEEN_LEVELS_BACKGROUND, (0, 0))
		Graphics.flip()
		if pygame.key.get_pressed()[GameConstants.GC_KEY_MAINMENU_BEGIN]:
			from screens.GameScreen import GameScreen
			ScreenManager.setScreen(GameScreen(self.state))
