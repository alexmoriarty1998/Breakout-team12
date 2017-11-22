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

	def __init__(self):
		initialVelocityMagnitude = random.randint(GC_BALL_INITIAL_VELOCITY_RANGE[0],
												  GC_BALL_INITIAL_VELOCITY_RANGE[1])
		initialVelocityAngle = random.randint(270 - GC_BALL_INITIAL_ANGLE_VARIATION,
											  270 + GC_BALL_INITIAL_ANGLE_VARIATION)
		dx = math.cos(math.radians(initialVelocityAngle)) * initialVelocityMagnitude
		dy = math.sin(math.radians(initialVelocityAngle)) * initialVelocityMagnitude
		self.velocity = Velocity(dx, dy)

		self.acceleration = Acceleration(0, GC_GRAVITY_ACCEL)

		posY = random.randint(GC_BRICK_BOTTOM_HEIGHT + 50, GC_PADDLE_TOP_HEIGHT - 50)
		self.pos = PosCircle(GC_WORLD_WIDTH / 2, posY, GC_BALL_RADIUS)

		self.image = Assets.I_BALL
