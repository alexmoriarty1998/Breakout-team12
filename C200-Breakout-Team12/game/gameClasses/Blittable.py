from pygame import Surface


# This class represents an object that can be blitted.
# Normally a position would also be required, but this
# was not done due to the decision of having hitboxes
# subclass positions.
# This will eventually store animations instead of
# static images, and the getImage() method will
# return the current frame based upon the game tick
# number.

class Blittable:
	image: Surface

	def getImage(self, frame: int) -> Surface:
		return self.image
