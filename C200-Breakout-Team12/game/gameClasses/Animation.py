class Animation:
	def __init__(self, images: list, frameTime: int, beginFrame: int):
		self.images = images
		self.frameTime = frameTime
		self.beginFrame = beginFrame

	def getImage(self, frame):
		framesElapsed = (frame - self.beginFrame) % (len(self.images) * self.frameTime)
		return self.images[framesElapsed // self.frameTime]
