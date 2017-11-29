# testing :).
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
from game.GameState import GameState
from GameConstants import *
import pygame


class GameController:
	state: GameState

	def __init__(self, state: GameState):
		self.state = state

	def update(self):
		paddle = self.state.paddle
		ball = self.state.ball
		for e in pygame.event.get():
			pass

		# paddle movement
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

		# ball movement
		self.state.lastPosBall = ball.circle
		ball.velocity.apply(ball.circle)
		if ball.circle.x - ball.circle.radius < GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.x + ball.circle.radius > GC_WORLD_WIDTH - GC_WALL_SIZE:
			ball.velocity.dx *= -1
		elif ball.circle.y - ball.circle.radius < 0:
			self.state.won = 1
		elif ball.circle.y + ball.circle.radius > GC_WORLD_HEIGHT:
			self.state.won = -1

		# ball paddle collision
		if paddle.rect.intersectsCircle(ball.circle):
			angle = paddle.rect.findAngle(ball.circle)
			if angle < 0:
				angle = (-360 - angle) * -1

			if angle < GC_PADDLE_ULANGLE or angle > GC_PADDLE_URANGLE:
				ball.velocity.dx *= -1
			else:
				ball.velocity.dy *= -1


		# brick ball collision
		brickHit = False
		for brick in self.state.bricks:
			if brick.rect.intersectsCircle(ball.circle):
				brickHit = True
				if brick.hp > 0:
					brick.hp -= 1
		if brickHit:
			ball.velocity.dy *= -1
			ball.velocity.dx *= -1
		
		self.state.bricks = list(filter(lambda b: b.hp != 0, self.state.bricks))