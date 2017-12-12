from game.gameClasses.PosRect import PosRect
from pygame import Surface


class Button:
	def __init__(self, name: str, rect: PosRect, image: Surface, hoverImage: Surface):
		self.name: str = name
		self.rect: PosRect = rect
		self.image: Surface = image
		self.hoverImage: Surface = hoverImage

	def hovered(self, mouseX: int, mouseY: int):
		return self.rect.intersectsPoint(mouseX, mouseY)
