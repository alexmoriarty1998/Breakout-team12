import math

from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosPoint import PosPoint


class PosRect(PosPoint):
	width: int
	height: int

	def __init__(self, x: float, y: float, width: int, height: int):
		super().__init__(x, y)
		self.width = width
		self.height = height

	# the only collisions here are brick-ball and paddle-ball
	# thus, no need for box-box collision detection
	# hit detection algorithm taken from
	# https://yal.cc/rectangle-circle-intersection-test/
	def intersectsCircle(self, circle: PosCircle) -> bool:
		# cull impossible collisions
		# test in the following order: circle is below, left/right, above box
		# this is what you want for bricks, but backwards for paddle
		# but there are many more bricks than paddles
		if (circle.y > self.y + self.height + circle.radius  # below
			or circle.x < self.x - circle.radius  # left
			or circle.x > self.x + self.width + circle.radius  # right
			or circle.y < self.y - circle.radius):  # above
			return False

		# find point on rectangle closest to circle
		nearestX = max(self.x, min(circle.x, self.x + self.width))
		nearestY = max(self.y, min(circle.y, self.y + self.height))

		# find distance between closest point of rectangle and circle
		deltaX = circle.x - nearestX
		deltaY = circle.y - nearestY

		return (deltaX ** 2 + deltaY ** 2) < (circle.radius ** 2)

	# find the angle of a given point relative to the center of this rectangle
	def findAngle(self, point: PosPoint):
		diffY = point.y - (self.y + self.height // 2)
		diffX = point.x - (self.x + self.width // 2)

		angle = math.degrees(math.atan2(diffY, diffX))

		# convert negative angle to positive
		# noinspection PyRedundantParentheses
		return (angle if angle > 0 else 360 + angle)
