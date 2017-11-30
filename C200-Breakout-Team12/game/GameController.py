# this module 'runs' a level of the game
# The NewGameLoader screen inits a new game state, and makes a
# Game screen for level 0. Each level, the StateManager is given
# a between-game-levels screen, and then a new Game screen for
# the next level.
# The GameScreen loads the level and calls this class's update()
# on each GameScreen update. This module updates the game state
# (it contains all game logic). Then, the GameScreen uses the
# GameRenderer to display the current game state.
# Name derived from the model-view-controller separation that
# is present here.

from GameConstants import *
from game.GameState import GameState
from game.gameClasses.PosPoint import PosPoint


class GameController:
	@staticmethod
	def update(state: GameState):
		# shortcuts for brevity
		paddle = state.paddle
		ball = state.ball

		#######################################################################
		###   paddle input   ##################################################
		#######################################################################
		for e in pygame.event.get():
			# TODO
			pass

		#######################################################################
		###   paddle movement   ###############################################
		#######################################################################
		# TODO

		#######################################################################
		###   input & paddle movement   #######################################
		#######################################################################
		# TODO: fix this; complete above two todos
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			state.paddle.velocity.dx = - GC_PADDLE_SPEED
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			state.paddle.velocity.dx = GC_PADDLE_SPEED
		else:
			state.paddle.velocity.dx = 0
		paddle.velocity.apply(paddle.rect)
		if paddle.rect.x < GC_WALL_SIZE:
			paddle.rect.x = GC_WALL_SIZE
		elif (paddle.rect.x + paddle.rect.width) > GC_WORLD_WIDTH - GC_WALL_SIZE:
			paddle.rect.x = GC_WORLD_WIDTH - GC_WALL_SIZE - paddle.rect.width

		#######################################################################
		###   ball movement   #################################################
		#######################################################################
		state.lastPosBall = PosPoint(ball.circle.x, ball.circle.y)
		ball.acceleration.apply(ball.velocity)
		ball.velocity.apply(ball.circle)
		if ball.circle.x - ball.circle.radius < GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.x + ball.circle.radius > GC_WORLD_WIDTH - GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.y - ball.circle.radius < 0:
			state.won = 1
		elif ball.circle.y + ball.circle.radius > GC_WORLD_HEIGHT:
			state.won = -1

		#######################################################################
		###   paddle collision   ##############################################
		#######################################################################
		if paddle.rect.intersectsCircle(ball.circle):
			# noinspection PyUnusedLocal
			intersectPoint = None
			if ball.circle.y == GC_PADDLE_TOP_HEIGHT:
				intersectPoint = ball.circle
			else:
				largeY = ball.circle.y - state.lastPosBall.y
				largeX = ball.circle.x - state.lastPosBall.x
				smallY = GC_PADDLE_TOP_HEIGHT - state.lastPosBall.y
				scale = smallY / largeY
				smallX = scale * largeX
				intersectX = smallX + state.lastPosBall.x
				intersectPoint = PosPoint(intersectX, GC_PADDLE_TOP_HEIGHT)
			angle = paddle.rect.findAngle(intersectPoint)
			if angle < GC_PADDLE_UL_ANGLE or angle > GC_PADDLE_UR_ANGLE:
				ball.velocity.dx *= -1  # hit side of paddle
			else:
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
		for brick in state.bricks:
			if brick.rect.intersectsCircle(ball.circle):
				if brick.hp > 0:
					brick.hp -= 1
				if brick.hp != 0:
					angle = brick.rect.findAngle(ball.circle)
					if (GC_BRICK_UR_ANGLE <= angle < GC_BRICK_BR_ANGLE) or (
									GC_BRICK_BL_ANGLE <= angle < GC_BRICK_UL_ANGLE):
						# hit side of brick
						ball.velocity.dx *= -1
					else:  # hit top of brick
						ball.velocity.dy *= -1
		# remove dead bricks
		state.bricks = list(filter(lambda b: b.hp != 0, state.bricks))
