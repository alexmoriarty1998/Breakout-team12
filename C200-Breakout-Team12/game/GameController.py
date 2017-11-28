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
		for event in pygame.event.get():
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				self.state.paddle.velocity.dx = - GC_PADDLE_SPEED
			elif pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.state.paddle.velocity.dx = GC_PADDLE_SPEED
			else:
				self.state.paddle.velocity.dx = 0



		self.state.paddle.velocity.apply(self.state.paddle.rect)
		if self.state.paddle.rect.x < GC_WALL_SIZE:
			self.state.paddle.rect.x = GC_WALL_SIZE
		elif (self.state.paddle.rect.x + self.state.paddle.rect.width) > GC_WORLD_WIDTH - GC_WALL_SIZE:
			self.state.paddle.rect.x = GC_WORLD_WIDTH - GC_WALL_SIZE - self.state.paddle.rect.width



		pass
