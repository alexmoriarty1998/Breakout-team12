# TODO: allow this to support animations

from pygame import Surface


class Animation:
	image: Surface

	def __init__(self, image):
		self.image = image
