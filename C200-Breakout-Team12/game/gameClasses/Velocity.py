class Velocity:
	dx: float
	dy: float

	def __init__(self, dx, dy):
		self.dx = dx
		self.dy = dy

	# apply this velocity to a pos
	def apply(self, pos):
		pos.x += self.dx
		pos.y += self.dy
