from game.gameClasses.PosPoint import PosPoint


class PosCircle(PosPoint):
	radius: int

	def __init__(self, x: float, y: float, radius: int):
		super().__init__(x, y)
		self.radius = radius
