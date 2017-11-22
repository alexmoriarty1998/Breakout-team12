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
import pygame


class GameController:
	state: GameState

	def __init__(self, state: GameState):
		self.state = state

	def update(self):
		keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
			self.state.paddle.rectangle = -7
		if keystate[pygame.K_RIGHT]:
			self.state.paddle.rectangle = 7


		pass
