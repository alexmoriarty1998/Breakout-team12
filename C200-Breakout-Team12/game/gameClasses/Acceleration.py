from game.gameClasses.Velocity import Velocity


class Acceleration:
	ddx: float
	ddy: float

	def __init__(self, ddx: float, ddy: float):
		self.ddx = ddx
		self.ddy = ddy

	# apply this acceleration to a velocity
	def apply(self, velocity: Velocity):
		velocity.dx += self.ddx
		velocity.dy += self.ddy
