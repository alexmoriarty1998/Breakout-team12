from pygame.surface import Surface

from Assets import Assets
from GameConstants import *
from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.Velocity import Velocity


class Ball(Blittable):
	def __init__(self, circle: PosCircle, velocity: Velocity):
		self.circle: PosCircle = circle
		self.velocity: Velocity = velocity

		self.acceleration: Acceleration = Acceleration(0, GC_GRAVITY_ACCEL)
		self.image: Surface = Assets.I_BALL
