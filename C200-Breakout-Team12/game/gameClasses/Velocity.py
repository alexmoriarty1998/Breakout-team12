from game.gameClasses.PosPoint import PosPoint
import math

class Velocity:
	dx: float
	dy: float

	def __init__(self, dx: float, dy: float):
		self.dx = dx
		self.dy = dy

	# apply this velocity to a pos
	def apply(self, pos: PosPoint):
		pos.x += self.dx
		pos.y += self.dy

	# Apply an instantaneous acceleration at angle 'angle'
	# with strength 'boost'.
	# If 'angle' is same as the current velocity angle, then
	# the velocity will increase by 'boost'.
	def impulse(self, angle: float, boost: float):
		xBoost = math.cos(math.radians(angle)) * boost
		yBoost = math.sin(math.radians(angle)) * boost
		self.dx += xBoost
		self.dy += yBoost
