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
	oldScore: int
	score: int
	won: bool

	time: float
	parTime: float

	def __init__(self, bricks: List[Brick], ball: Ball, level: int, oldScore: int = 0, numLives: int = 3):
		self.bricks = bricks
		self.ball = ball
		self.level = level
		self.oldScore = oldScore
		self.score = 0

		self.displayables = []
		self.won = 0

		self.paddle = Paddle()
		self.numLives = numLives
		self.paused = True
		self.time = 0
		self.parTime = GC_PAR_TIME
		self.totalBrickScore = 0
		for brick in bricks:
			self.totalBrickScore += brick.score
		self.totalBricksDestroyedScore = 0
