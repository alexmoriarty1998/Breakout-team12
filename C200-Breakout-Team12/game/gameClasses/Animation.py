import sys


class Animation:
	# noinspection PyShadowingBuiltins
	def __init__(self, images: list, frameTime: int, beginFrame: int, next: str = ''):
		self.images = images
		self.frameTime = frameTime
		self.beginFrame = beginFrame
		self.next = next

	def switchTo(self, newAnim, frame: int):
		self.images = newAnim.images
		self.frameTime = newAnim.frameTime
		self.beginFrame = frame
		self.next = newAnim.next

	def getFrame(self, frame: int):
		framesElapsed = (frame - self.beginFrame) % (len(self.images) * self.frameTime)

		# An animation can switch to another animation, specified in the 'next' parameter of the constructor.
		# Each animation will be drawn every frame, so if this is the frame after its last frame, switch to
		# the new animation.
		# This doesn't work with Displayables, since they are deleted by GameController at this frame, before
		# this method is called by GameRenderer. But there's no case in this project where a Displayable needs
		# to chain into another displayable, so it doesn't matter. This is only used for permanent objects, for
		# example, the paddle electric animation transitioning back into the normal paddle image (just a
		# 1-frame animation) after it's over.
		if framesElapsed == 0 and frame > self.beginFrame and self.next != '':  # means animation is complete, just finished last frame
			# switch to the new animation
			# next two lines are same code in Graphics class's blur() method
			assetsClass = getattr(sys.modules['Assets'], 'Assets')
			newAnim: Animation = getattr(assetsClass, self.next)

			# self.images = newAnim.images
			# self.frameTime = newAnim.frameTime
			# self.beginFrame = frame
			# self.next = newAnim.next
			self.switchTo(newAnim, frame)
			return self.images[0]

		return self.images[framesElapsed // self.frameTime]
