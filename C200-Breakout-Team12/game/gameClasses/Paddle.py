from Assets import Assets
from GameConstants import *
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity


class Paddle(Blittable):
	rect: PosRect
	velocity: Velocity

	def __init__(self):
		self.velocity = Velocity(0, 0)

		x = GC_WORLD_WIDTH / 2 - GC_PADDLE_WIDTH // 2
		self.rect = PosRect(x, GC_PADDLE_TOP_HEIGHT, GC_PADDLE_WIDTH, GC_PADDLE_HEIGHT)

		self.image = Assets.I_PADDLE

	'''def updateVelocity(self):
		self.velocity = Velocity(0, 0)
		for event in pygame.event.get():'''

