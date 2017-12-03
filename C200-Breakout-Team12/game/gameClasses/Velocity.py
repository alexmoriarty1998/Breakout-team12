from game.gameClasses.PosPoint import PosPoint


class Velocity:
	def __init__(self, dx: float, dy: float):
		self.dx: float = dx
		self.dy: float = dy

	# apply this velocity to a pos
	def apply(self, pos: PosPoint) -> None:
		pos.x += self.dx
		pos.y += self.dy
