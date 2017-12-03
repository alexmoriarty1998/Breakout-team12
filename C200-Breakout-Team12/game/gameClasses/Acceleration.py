from game.gameClasses.Velocity import Velocity


class Acceleration:
	def __init__(self, ddx: float, ddy: float):
		self.ddx: float = ddx
		self.ddy: float = ddy

	# apply this acceleration to a velocity
	def apply(self, velocity: Velocity):
		velocity.dx += self.ddx
		velocity.dy += self.ddy
