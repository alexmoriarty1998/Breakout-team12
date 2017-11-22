# TODO: allow this to support animations

from pygame import Surface


# this class will eventually support animations
# animations will be given as a list of images,
# and either a next animation to transition to
# after it ends, or to loop forever

# there will be a method to get the current image
# of the animation

class Image:
	image: Surface

	def __init__(self, image: Surface):
		self.image = image

	def getCurrentImage(self):
		return self.image
