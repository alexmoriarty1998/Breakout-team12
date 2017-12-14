# camera class, used to implement screenshake

# Can get a (x, y) for current camera offset (from center of screen),
# this is used by Graphics' flip() to move the final render.
import random

from GameConstants import *


class Camera:

	def __init__(self):
		self.enabled: bool = False
		self.radius: float = 0
		self.offset: Tuple[float] = (0, 0)
		self.angle: int = -1  # -1 means no shake yet

	def reset(self):
		self.radius = 0
		self.offset = 0, 0
		self.angle = -1

	def enable(self):
		self.enabled = True

	def disable(self):
		self.enabled = False
		self.reset()

	def kick(self, amount: float):  # 'kick' the camera - increases shake
		self.radius += amount

	def update(self):
		# generate new angle
		if self.angle == -1:
			newAngle = random.randint(0, 360)
		else:
			newAngle = random.randint(self.angle - GC_SCREENSHAKE_ANGLE_VARIATION,
									  self.angle + GC_SCREENSHAKE_ANGLE_VARIATION)

		# generate new distance
		newRadius = random.uniform(self.radius * GC_SCREENSHAKE_MAX_DISTANCE_REDUCTION,
								   self.radius * GC_SCREENSHAKE_MIN_DISTANCE_REDUCTION)

		# find x, y
		x = newRadius * math.cos(math.radians(newAngle))
		y = newRadius * math.sin(math.radians(newAngle))

		# store new values
		self.radius = newRadius
		self.angle = newAngle
		self.offset = (x, y)

		# stop screenshake once radius is low
		if self.radius <= GC_SCREENSHAKE_MIN_RADIUS:
			self.reset()
