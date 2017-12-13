from pygame.surface import Surface

from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosPoint import PosPoint
from game.gameClasses.Velocity import Velocity


class Displayable(Blittable):
	def __init__(self, pos: PosPoint, velocity: Velocity, acceleration: Acceleration, image,
				 lifespan: int = -1):
		super().__init__(image)
		self.pos: PosPoint = pos
		self.velocity: Velocity = velocity
		self.acceleration: Acceleration = acceleration
		self.lifespan: int = lifespan  # -1 means forever
