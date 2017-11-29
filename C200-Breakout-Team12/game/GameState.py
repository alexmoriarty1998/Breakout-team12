# class that holds the game state

from typing import List

from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.Displayable import Displayable
from game.gameClasses.Paddle import Paddle


class GameState:
	bricks: List[Brick]
	paddle: Paddle
	ball: Ball
	displayables: List[Displayable] = []

	level: int
	score: int
	won: bool = 0

	def __init__(self, bricks: List[Brick], ball: Ball, level: int, score: int = 0):
		self.bricks = bricks
		self.ball = ball
		self.level = level
		self.score = score

		self.paddle = Paddle()
