# class that holds the game state

# TODO: complete everything listed below

# init function should generate:
# paddle pos (based off of constants in GameConstants)
# ball initial x/y:
#   x is center of screen, y is random
# ball initial dx/dy (random)

from typing import List
from game.gameClasses.Brick import Brick
from game.gameClasses.Paddle import Paddle
from game.gameClasses.Ball import Ball
from game.gameClasses.Displayable import Displayable


class GameState:
	bricks: List[Brick]
	paddle: Paddle
	ball: Ball
	displayables: List[Displayable]

	level: int
	score: int
	won: bool = False

	def __init__(self, bricks, score=0):
		self.bricks = bricks
		self.score = score

		# TODO: calculate paddle/ball pos and ball velocity
		self.paddle = Paddle()
		self.ball = Ball()

# each game object class (brick, paddle, ball) contains some of the component classes
# for example, the Brick class will have a Position and Animation component

# the hitbox stores the top-left corner and width/height
# the hitcircle stores the center of the circle and the radius

# game class definitions (also go in gameClasses):
# Ball:
#  HitCircle, Velocity, Animation
# Paddle:
#  HitBox, Velocity, Animation
#    should paddles be able to move vertically?
# Brick:
#  HitBox, Animation
#    bricks don't have velocity
# Displayable:
#  Position, Velocity, Animation, lifespan: int
#    used for various graphical effects
#    e.g. bricks shattering and falling after being destroyed
#    lifespan counts down to 0, then object is removed
#      or set it to -1 for permanent lifespan
