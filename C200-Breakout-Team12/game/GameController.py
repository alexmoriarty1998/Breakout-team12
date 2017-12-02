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
		self.state = state

	def update(self):
		if self.state.paused:
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.state.paused = False
			else:
				return
		# shortcuts for brevity
		paddle = self.state.paddle
		ball = self.state.ball

		for e in pygame.event.get():
			if e.type == pygame.MOUSEMOTION:
				x = e.pos[0]
				percent = x/Graphics.windowSurface.get_width()
				x = Graphics.surface.get_width()*percent
				x -= GC_PADDLE_WIDTH / 2
				paddle.rect.x = x

		#######################################################################
		###   input & paddle movement   #######################################
		#######################################################################
		# TODO: fix this; complete above two todos
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.state.paddle.velocity.dx = - GC_PADDLE_SPEED
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.state.paddle.velocity.dx = GC_PADDLE_SPEED
		else:
			self.state.paddle.velocity.dx = 0
		paddle.velocity.apply(paddle.rect)
		if paddle.rect.x < GC_WALL_SIZE:
			paddle.rect.x = GC_WALL_SIZE
		elif (paddle.rect.x + paddle.rect.width) > GC_WORLD_WIDTH - GC_WALL_SIZE:
			paddle.rect.x = GC_WORLD_WIDTH - GC_WALL_SIZE - paddle.rect.width

		#######################################################################
		###   ball movement   #################################################
		#######################################################################
		self.state.lastPosBall = PosPoint(ball.circle.x, ball.circle.y)
		ball.acceleration.apply(ball.velocity)
		ball.velocity.apply(ball.circle)
		if ball.circle.x - ball.circle.radius < GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.x + ball.circle.radius > GC_WORLD_WIDTH - GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.y - ball.circle.radius < 0:
			self.state.won = 1
		elif ball.circle.y + ball.circle.radius > GC_WORLD_HEIGHT:
			if self.state.numLives > 1:
				self.state.numLives -= 1
				self.state.ball = makeBall()
				self.state.paused = True
			else:
				self.state.won = -1


		#######################################################################
		###   paddle collision   ##############################################
		#######################################################################
		if paddle.rect.intersectsCircle(ball.circle):
			# noinspection PyUnusedLocal
			intersectPoint = None
			if ball.circle.y == GC_PADDLE_TOP_HEIGHT:
				# avoid divide by zero ??
				# that's why this was added, not sure if it's actually needed
				intersectPoint = ball.circle
			else:
				largeY = ball.circle.y - self.state.lastPosBall.y
				largeX = ball.circle.x - self.state.lastPosBall.x
				smallY = GC_PADDLE_TOP_HEIGHT - self.state.lastPosBall.y
				scale = smallY / largeY
				smallX = scale * largeX
				intersectX = smallX + self.state.lastPosBall.x
				intersectPoint = PosPoint(intersectX, GC_PADDLE_TOP_HEIGHT)

			angle = paddle.rect.findAngle(intersectPoint)

			if angle < GC_PADDLE_UL_ANGLE or angle > GC_PADDLE_UR_ANGLE:
				# hit side of paddle
				ball.velocity.dx *= -1
			else:
				# hit top of paddle
				velocityMagnitude = (ball.velocity.dx ** 2 + ball.velocity.dy ** 2) ** 0.5
				xDiff = intersectPoint.x - (paddle.rect.x + paddle.rect.width // 2)
				xDiff /= paddle.rect.width // 2
				reflectAngle = 270 + xDiff * GC_MAX_BOUNCE_ANGLE
				velocityX = math.cos(math.radians(reflectAngle)) * velocityMagnitude
				velocityY = math.sin(math.radians(reflectAngle)) * velocityMagnitude
				ball.velocity.dx = velocityX
				ball.velocity.dy = velocityY

		#######################################################################
		###   brick collision   ###############################################
		#######################################################################
		for brick in self.state.bricks:
			if brick.rect.intersectsCircle(ball.circle):
				brick.hp -= 1
				if brick.hp != 0:  # don't bounce the ball when it destroys a brick
					angle = brick.rect.findAngle(ball.circle)
					if (angle >= GC_BRICK_UR_ANGLE or angle < GC_BRICK_BR_ANGLE or
									GC_BRICK_BL_ANGLE <= angle < GC_BRICK_UL_ANGLE):
						# hit side of brick
						ball.velocity.dx *= -1
						if ball.circle.x > brick.rect.x + .5*GC_BRICK_WIDTH:
							ball.circle.x = brick.rect.x + GC_BRICK_WIDTH + ball.circle.radius
						else:
							ball.circle.x = brick.rect.x - ball.circle.radius
					else:
						# hit top of brick
						ball.velocity.dy *= -1
						if ball.circle.y > brick.rect.y + brick.rect.height:
							ball.circle.y = brick.rect.y + brick.rect.height + ball.circle.radius
						else:
							ball.circle.y = brick.rect.y - ball.circle.radius




		# remove dead bricks
		self.state.bricks = list(filter(lambda b: b.hp != 0, self.state.bricks))
