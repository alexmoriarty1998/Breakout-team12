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
import Graphics
from GameConstants import *
from game.GameState import GameState
from game.LevelTools import makeBall
from game.gameClasses.PosPoint import PosPoint


class GameController:

	def __init__(self, state):
		self.moveDir = 0
		self.state = state

	def update(self):
		if self.state.paused:
			self.movePaddle()
			self.collidePaddleWall()
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.state.paused = False
			else:
				return
		self.state.time += GC_FRAME_TIME_SECONDS

		self.moveBall()
		self.movePaddle()
		self.collidePaddleWall()
		self.collideBallBrick()
		self.collidePaddleBall()
		# shortcuts for brevity

	def movePaddle(self):
		for e in pygame.event.get():
			if e.type == pygame.MOUSEMOTION:
				x = e.pos[0]
				percent = x/Graphics.windowSurface.get_width()
				x = Graphics.surface.get_width()*percent
				x -= GC_PADDLE_WIDTH / 2
				self.state.paddle.rect.x = x
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_LEFT:
					self.moveDir = -1

				if e.key == pygame.K_RIGHT:
					self.moveDir = 1
			if e.type == pygame.KEYUP:
				if e.key == pygame.K_LEFT:
					if self.moveDir == -1:
						self.moveDir = 0
				if e.key == pygame.K_RIGHT:
					if self.moveDir == 1:
						self.moveDir = 0
		self.state.paddle.velocity.dx = self.moveDir * GC_PADDLE_SPEED
		self.state.paddle.velocity.apply(self.state.paddle.rect)


		#######################################################################
		###   input & self.state.paddle movement   #######################################
		#######################################################################
		# TODO: fix this; complete above two todos
	def collidePaddleWall(self):
		if self.state.paddle.rect.x < GC_WALL_SIZE:
			self.state.paddle.rect.x = GC_WALL_SIZE
		elif (self.state.paddle.rect.x + self.state.paddle.rect.width) > GC_WORLD_WIDTH - GC_WALL_SIZE:
			self.state.paddle.rect.x = GC_WORLD_WIDTH - GC_WALL_SIZE - self.state.paddle.rect.width
	def moveBall(self):
		#######################################################################
		###   self.state.ball movement   #################################################
		#######################################################################
		self.state.lastPosBall = PosPoint(self.state.ball.circle.x, self.state.ball.circle.y)
		self.state.ball.acceleration.apply(self.state.ball.velocity)
		self.state.ball.velocity.apply(self.state.ball.circle)
		if self.state.ball.circle.x - self.state.ball.circle.radius < GC_WALL_SIZE:
			self.state.ball.velocity.dx *= -1
		elif self.state.ball.circle.x + self.state.ball.circle.radius > GC_WORLD_WIDTH - GC_WALL_SIZE:
			self.state.ball.velocity.dx *= -1
		elif self.state.ball.circle.y - self.state.ball.circle.radius < 0:
			self.state.won = 1
		elif self.state.ball.circle.y + self.state.ball.circle.radius > GC_WORLD_HEIGHT:
			if self.state.numLives > 1:
				self.state.numLives -= 1
				self.state.ball = makeBall()
				self.state.paused = True
			else:
				self.state.won = -1

	def collidePaddleBall(self):
		#######################################################################
		###   self.state.paddle collision   ##############################################
		#######################################################################
		if self.state.paddle.rect.intersectsCircle(self.state.ball.circle):
			# noinspection PyUnusedLocal
			intersectPoint = None
			if self.state.ball.circle.y == GC_PADDLE_TOP_HEIGHT:
				# avoid divide by zero ??
				# that's why this was added, not sure if it's actually needed
				intersectPoint = self.state.ball.circle
			else:
				largeY = self.state.ball.circle.y - self.state.lastPosBall.y
				largeX = self.state.ball.circle.x - self.state.lastPosBall.x
				smallY = GC_PADDLE_TOP_HEIGHT - self.state.lastPosBall.y
				scale = smallY / largeY
				smallX = scale * largeX
				intersectX = smallX + self.state.lastPosBall.x
				intersectPoint = PosPoint(intersectX, GC_PADDLE_TOP_HEIGHT)

			angle = self.state.paddle.rect.findAngle(intersectPoint)

			if angle < GC_PADDLE_UL_ANGLE or angle > GC_PADDLE_UR_ANGLE:
				# hit side of self.state.paddle
				self.state.ball.velocity.dx *= -1
			else:
				# hit top of self.state.paddle
				velocityMagnitude = (self.state.ball.velocity.dx ** 2 + self.state.ball.velocity.dy ** 2) ** 0.5
				xDiff = intersectPoint.x - (self.state.paddle.rect.x + self.state.paddle.rect.width // 2)
				xDiff /= self.state.paddle.rect.width // 2
				reflectAngle = 270 + xDiff * GC_MAX_BOUNCE_ANGLE
				velocityX = math.cos(math.radians(reflectAngle)) * velocityMagnitude
				velocityY = math.sin(math.radians(reflectAngle)) * velocityMagnitude
				self.state.ball.velocity.dx = velocityX
				self.state.ball.velocity.dy = velocityY

	def collideBallBrick(self):
		#######################################################################
		###   brick collision   ###############################################
		#######################################################################
		for brick in self.state.bricks:
			if brick.rect.intersectsCircle(self.state.ball.circle):
				brick.hp -= 1
				if brick.hp != 0:  # don't bounce the self.state.ball when it destroys a brick
					angle = brick.rect.findAngle(self.state.ball.circle)
					if (angle >= GC_BRICK_UR_ANGLE or angle < GC_BRICK_BR_ANGLE or
									GC_BRICK_BL_ANGLE <= angle < GC_BRICK_UL_ANGLE):
						# hit side of brick
						self.state.ball.velocity.dx *= -1
						if self.state.ball.circle.x > brick.rect.x + .5*GC_BRICK_WIDTH:
							self.state.ball.circle.x = brick.rect.x + GC_BRICK_WIDTH + self.state.ball.circle.radius
						else:
							self.state.ball.circle.x = brick.rect.x - self.state.ball.circle.radius
					else:
						# hit top of brick
						self.state.ball.velocity.dy *= -1
						if self.state.ball.circle.y > brick.rect.y + brick.rect.height:
							self.state.ball.circle.y = brick.rect.y + brick.rect.height + self.state.ball.circle.radius
						else:
							self.state.ball.circle.y = brick.rect.y - self.state.ball.circle.radius



		for b in self.state.bricks:
			if b.hp == 0:
				self.state.totalBricksDestroyedScore += b.score
		# remove dead bricks
		self.state.bricks = list(filter(lambda b: b.hp != 0, self.state.bricks))
		print(self.state.totalBricksDestroyedScore, '/', self.state.totalBrickScore)

		def calculateScore(self):
			score = GC_PAR_TIME / self.state.time
			percentBricksDestroyed = self.state.totalBricksDestroyedScore / self.state.totalBrickScore
			score *= (1 - percentBricksDestroyed) + 100
			self.state.score = int(score)
