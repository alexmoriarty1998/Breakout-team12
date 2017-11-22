from game.gameClasses.PosPoint import PosPoint


class PosCircle(PosPoint):
	radius: int

	def __init__(self, x: float, y: float, radius: int):
		super().__init__(x, y)
		self.radius = radius

	# clone of HitBox.intersectsCircle()
	# DO NOT type annotate box to be a PosRect
	def intersectsBox(self, box):
		if (self.y > box.y + box.height + self.radius
			or self.x < box.x - self.radius
			or self.x > box.x + box.width + self.radius
			or self.y < box.y - self.radius):
			return False

		nearestX = max(box.x, min(self.x, box.x + box.width))
		nearestY = max(box.y, min(self.y, box.y + box.height))

		deltaX = self.x - nearestX
		deltaY = self.y - nearestY

		return (deltaX ** 2 + deltaY ** 2) < (self.radius ** 2)
