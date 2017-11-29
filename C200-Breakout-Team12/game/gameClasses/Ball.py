import math
import random

from Assets import Assets
from GameConstants import *
from game.gameClasses.Acceleration import Acceleration
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.Velocity import Velocity


class Ball(Blittable):
	circle: PosCircle
	velocity: Velocity
	acceleration: Acceleration

	def __init__(self, circle: PosCircle, velocity: Velocity):
		self.circle = circle
		self.velocity = velocity

		self.acceleration = Acceleration(0, GC_GRAVITY_ACCEL)

		self.image = Assets.I_BALL
