from game.gameClasses.Position import Position
from game.gameClasses.HitBox import HitBox


class HitCircle(Position):
	radius: int

	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self.radius = radius

	# clone of HitBox.intersectsCircle()
	def intersectsBox(self, box: HitBox):
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
