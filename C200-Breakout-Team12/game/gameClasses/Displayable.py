from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosPoint import PosPoint
from game.gameClasses.Velocity import Velocity


class Displayable(Blittable):
	def __init__(self, pos: PosPoint, velocity: Velocity, acceleration: Acceleration, image,
				 beginFrame: int, lifespan: int = -1):
		super().__init__(image)
		self.pos: PosPoint = pos
		self.velocity: Velocity = velocity
		self.acceleration: Acceleration = acceleration
		self.beginFrame = beginFrame
		self.lifespan: int = lifespan  # -1 means forever
		# there will never be an infinite lifespan static image
		# infinite lifespan will only be set for animations
		# so just change lifespan to length of animations
		if self.lifespan == -1:
			self.lifespan = len(image.images) * image.frameTime
