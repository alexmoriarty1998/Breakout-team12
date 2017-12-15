from Assets import Assets
from GameConstants import *
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity


class Paddle(Blittable):
	def __init__(self):
		super().__init__(Assets.A_PADDLE)
		self.velocity: Velocity = Velocity(0, 0)

		x = GC_WORLD_WIDTH / 2 - GC_PADDLE_WIDTH // 2
		self.rect: PosRect = PosRect(x, GC_PADDLE_TOP_HEIGHT, GC_PADDLE_WIDTH, GC_PADDLE_HEIGHT)
