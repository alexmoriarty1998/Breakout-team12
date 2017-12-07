from game.gameClasses.PosPoint import PosPoint


class PosCircle(PosPoint):
	def __init__(self, x: float, y: float, radius: int):
		super().__init__(x, y)
		self.radius: int = radius
