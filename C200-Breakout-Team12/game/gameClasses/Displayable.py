import pygame
from pygame.surface import Surface

from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Animation import Animation
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosPoint import PosPoint
from game.gameClasses.Rotator import Rotator
from game.gameClasses.Velocity import Velocity


# holds animations (designed to be used for graphics effects with no impact on the game physics or logic)
class Displayable(Blittable):
	def __init__(self, pos: PosPoint, velocity: Velocity, acceleration: Acceleration, rotator: Rotator,
				 anim: Animation, beginFrame: int, lifespan: int = -1):
		super().__init__(anim)
		self.pos: PosPoint = pos
		self.velocity: Velocity = velocity
		self.acceleration: Acceleration = acceleration
		self.rotator = rotator
		self.beginFrame = beginFrame
		self.image.beginFrame = beginFrame
		self.lifespan = lifespan if lifespan != -1 else anim.frameTime * len(anim.images)

	def getImage(self, frame: int) -> Surface:
		animFrame = super().getImage(frame)
		angle = self.rotator.getAngle(frame)
		if angle == 0:
			return animFrame
		return pygame.transform.rotate(animFrame, angle)
