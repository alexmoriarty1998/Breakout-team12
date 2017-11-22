from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Blittable import Blittable
from game.gameClasses.Image import Image
from game.gameClasses.PosPoint import PosPoint
from game.gameClasses.Velocity import Velocity


class Displayable(Blittable):
	pos: PosPoint
	velocity: Velocity
	acceleration: Acceleration
	lifespan: int

	def __init__(self, pos: PosPoint, velocity: Velocity, acceleration: Acceleration, image: Image, lifespan: int = -1):
		self.pos = pos
		self.velocity = velocity
		self.acceleration = acceleration
		self.image = image
		self.lifespan = lifespan
