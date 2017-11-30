from game.gameClasses.PosPoint import PosPoint


class Velocity:
	dx: float
	dy: float

	def __init__(self, dx: float, dy: float):
		self.dx = dx
		self.dy = dy

	# apply this velocity to a pos
	def apply(self, pos: PosPoint) -> None:
		pos.x += self.dx
		pos.y += self.dy
