# class that holds the game state

from typing import List

from GameConstants import GC_PAR_TIME
from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.Displayable import Displayable
from game.gameClasses.Paddle import Paddle
from game.gameClasses.PosPoint import PosPoint


class GameState:
	bricks: List[Brick]
	paddle: Paddle
	ball: Ball
	lastPosBall: PosPoint
	displayables: List[Displayable]

	level: int
	score: int
	won: bool

	time: float
	parTime: float

	def __init__(self, bricks: List[Brick], ball: Ball, level: int, score: int = 0, numLives = 3):
		self.bricks = bricks
		self.ball = ball
		self.level = level
		self.score = score

		self.displayables = []
		self.won = 0

		self.paddle = Paddle()
		self.numLives = numLives
		self.paused = True
		self.time = 0
		self.parTime = GC_PAR_TIME
		sum = 0
		for b in bricks:
			sum += b.score
		self.totalBrickScore = sum
		self.totalBricksDestroyedScore = 0