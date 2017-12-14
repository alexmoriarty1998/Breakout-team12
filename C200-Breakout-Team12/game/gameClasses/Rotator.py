from GameConstants import GC_FRAME_TIME_SECONDS


class Rotator:
	def __init__(self, a: float, da: float, dda: float):
		self.a: float = a
		self.da: float = da
		self.dda: float = dda

	def getAngle(self, frame: int) -> float:
		# angle = initial + da * t
		# da = initial da + dda*t
		# angle = initial_angle + (initial_da + dda*t) * t
		# angle = initial_angle + initial_da * t + dda*t^2
		time = GC_FRAME_TIME_SECONDS * frame
		return self.a + self.da * time + self.dda * time * time
