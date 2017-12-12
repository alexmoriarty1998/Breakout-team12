# this module 'runs' a level of the game
# The NewGameLoader screen inits a new game self.state, and makes a
# Game screen for level 0. Each level, the self.stateManager is given
# a between-game-levels screen, and then a new Game screen for
# the next level.
# The GameScreen loads the level and calls this class's update()
# on each GameScreen update. This module updates the game self.state
# (it contains all game logic). Then, the GameScreen uses the
# GameRenderer to display the current game self.state.
# Name derived from the model-view-controller separation that
# is present here.
import sys

import Graphics
import ScreenManager
from GameConstants import *
from game.GameState import GameState
from game.LevelTools import makeBall
from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Ball import Ball
from game.gameClasses.Paddle import Paddle
from game.gameClasses.PosPoint import PosPoint


class GameController:
	def __init__(self, state):
		self.moveDir: int = 0
		self.state: GameState = state
		self.ball: Ball = state.ball  # shortcut to avoid having to type self.state.ball
		self.paddle: Paddle = state.paddle  # shortcut to avoid having to type self.state.paddle

	def update(self):

		# update these in case they changed
		self.ball: Ball = self.state.ball  # shortcut to avoid having to type self.state.ball
		self.paddle: Paddle = self.state.paddle  # shortcut to avoid having to type self.state.paddle

		if self.state.paused:
			# let the paddle move even if the game hasn't started
			self.movePaddle()
			# but don't let it go off the screen
			self.collidePaddleWall()
			# start the game when started
			# cant use pygame.mouse.get_pressed() because the user has to click to begin the game
			#   and so the mouse button will still be held down when the game loads, and it will
			#   immediately begin
			#  would be too complex to put the event loop here
			if pygame.key.get_pressed()[GC_KEY_BEGIN]:
				self.state.paused = False
			return

		self.state.time += GC_FRAME_TIME_SECONDS
		self.updateBall()
		self.movePaddle()
		self.collidePaddleWall()
		self.collideBrickBall()
		self.collidePaddleBall()
		self.score()

	def movePaddle(self):
		for e in pygame.event.get():
			if e.type == pygame.MOUSEMOTION:
				# ignore mouse input if in the embedded main menu game
				# but can't import MainMenuScreen
				if ScreenManager.currentScreen.__class__.__name__ != 'GameScreen':
					break
				x = e.pos[0]
				percent = x / Graphics.windowSurface.get_width()
				x = Graphics.surface.get_width() * percent
				x -= GC_PADDLE_WIDTH / 2
				self.paddle.rect.x = x
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_LEFT:
					self.moveDir = -1
				if e.key == pygame.K_RIGHT:
					self.moveDir = 1
				# The GameScreen class needs to use event-driven input for the pause key
				# and can't poll for it, so post escape key down events back onto the queue.
				if e.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE}))
			if e.type == pygame.KEYUP:
				if e.key == pygame.K_LEFT:
					if self.moveDir == -1:
						self.moveDir = 0
				if e.key == pygame.K_RIGHT:
					if self.moveDir == 1:
						self.moveDir = 0
		self.paddle.velocity.dx = self.moveDir * GC_PADDLE_SPEED
		self.paddle.velocity.apply(self.paddle.rect)

	def updateBall(self):
		# store last position
		self.state.lastPosBall = PosPoint(self.ball.circle.x, self.ball.circle.y)

		# move; update velocity before position
		halfAccel: Acceleration = Acceleration(self.ball.acceleration.ddx / 2, self.ball.acceleration.ddy / 2)
		halfAccel.apply(self.ball.velocity)
		self.ball.velocity.apply(self.ball.circle)
		halfAccel.apply(self.ball.velocity)

		# collide with walls and top/bottom of world
		if self.ball.circle.x - self.ball.circle.radius < GC_WALL_SIZE:
			self.ball.circle.x = GC_WALL_SIZE + self.ball.circle.radius
			self.ball.velocity.dx *= -1
			self.ball.circle.x = GC_WALL_SIZE + self.ball.circle.radius
		elif self.ball.circle.x + self.ball.circle.radius > GC_WORLD_WIDTH - GC_WALL_SIZE:
			self.ball.circle.x = GC_WORLD_WIDTH - self.ball.circle.radius - GC_WALL_SIZE
			self.ball.velocity.dx *= -1
			self.ball.circle.x = GC_WORLD_WIDTH - GC_WALL_SIZE - self.ball.circle.radius

		# set 'won'
		if self.ball.circle.y - self.ball.circle.radius < 0:
			self.state.won = 1
		# decrement lives or set 'lost'
		elif self.ball.circle.y + self.ball.circle.radius > GC_WORLD_HEIGHT:
			if self.state.numLives > 1:
				self.state.numLives -= 1
				self.state.ball = makeBall()  # make sure to set the state's ball, not the local copy of ball
				self.state.paused = True
			else:
				self.state.won = -1

	def collidePaddleWall(self):
		if self.paddle.rect.x < GC_WALL_SIZE:
			self.paddle.rect.x = GC_WALL_SIZE
		elif (self.paddle.rect.x + self.paddle.rect.width) > GC_WORLD_WIDTH - GC_WALL_SIZE:
			self.paddle.rect.x = GC_WORLD_WIDTH - GC_WALL_SIZE - self.paddle.rect.width

	def collidePaddleBall(self):
		# The ball's velocity (per frame) is a large percentage of the paddle height.
		# So find where it actually would have hit the paddle, not where it is
		# relative to the paddle on this frame.

		if self.paddle.rect.intersectsCircle(self.ball.circle):
			# noinspection PyUnusedLocal
			intersectPoint = None
			if self.ball.circle.y == GC_PADDLE_TOP_HEIGHT:
				# avoid divide by zero ??
				# that's why this was added, not sure if it's actually needed
				# TODO: is this if statement needed? does it do anything?
				intersectPoint = self.ball.circle
			else:
				largeY = self.ball.circle.y - self.state.lastPosBall.y
				largeX = self.ball.circle.x - self.state.lastPosBall.x
				smallY = GC_PADDLE_TOP_HEIGHT - self.state.lastPosBall.y
				scale = smallY / largeY
				smallX = scale * largeX
				intersectX = smallX + self.state.lastPosBall.x
				intersectPoint = PosPoint(intersectX, GC_PADDLE_TOP_HEIGHT)

			angle = self.paddle.rect.findAngle(intersectPoint)

			if angle < GC_PADDLE_UL_ANGLE or angle > GC_PADDLE_UR_ANGLE:
				# hit side of paddle
				self.ball.velocity.dx *= -1
			else:
				# hit top of paddle
				velocityMagnitude = (self.ball.velocity.dx ** 2 + self.ball.velocity.dy ** 2) ** 0.5
				xDiff = intersectPoint.x - (self.paddle.rect.x + self.paddle.rect.width // 2)
				xDiff /= self.paddle.rect.width // 2
				reflectAngle = 270 + xDiff * GC_MAX_BOUNCE_ANGLE
				velocityX = math.cos(math.radians(reflectAngle)) * velocityMagnitude
				velocityY = math.sin(math.radians(reflectAngle)) * velocityMagnitude
				self.ball.velocity.dx = velocityX
				self.ball.velocity.dy = velocityY

	def collideBrickBall(self):
		# collision and HP removal
		for brick in self.state.bricks:
			if brick.rect.intersectsCircle(self.ball.circle):
				brick.hp -= 1
				if brick.hp != 0:  # don't bounce the self.ball when it destroys a brick
					angle = brick.rect.findAngle(self.ball.circle)
					if (angle >= GC_BRICK_UR_ANGLE or angle < GC_BRICK_BR_ANGLE or
									GC_BRICK_BL_ANGLE <= angle < GC_BRICK_UL_ANGLE):
						# hit side of brick
						self.ball.velocity.dx *= -1
						if self.ball.circle.x > brick.rect.x + .5 * GC_BRICK_WIDTH:
							self.ball.circle.x = brick.rect.x + GC_BRICK_WIDTH + self.ball.circle.radius
						else:
							self.ball.circle.x = brick.rect.x - self.ball.circle.radius
					else:
						# hit top of brick
						self.ball.velocity.dy *= -1
						if self.ball.circle.y > brick.rect.y + brick.rect.height:
							self.ball.circle.y = brick.rect.y + brick.rect.height + self.ball.circle.radius
						else:
							self.ball.circle.y = brick.rect.y - self.ball.circle.radius

		# add score for dead bricks
		for brick in self.state.bricks:
			if brick.hp == 0:
				self.state.totalBricksDestroyedScore += brick.score

		# noinspection PyShadowingNames
		# remove dead bricks
		self.state.bricks = list(filter(lambda brick: brick.hp != 0, self.state.bricks))

	def score(self):  # the name of this method is a verb, not a noun
		score = GC_PAR_TIME / self.state.time
		percentBricksDestroyed = 0
		if not self.state.totalBrickScore == 0:  # don't divide by zero in case of 'empty' brick generation
			percentBricksDestroyed = self.state.totalBricksDestroyedScore / self.state.totalBrickScore
		score *= (1 - percentBricksDestroyed) + 100
		self.state.score = int(score)
