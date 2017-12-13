from pygame import Surface

from Assets import Assets
from GameConstants import *
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosRect import PosRect


class Brick(Blittable):
	# get the brick image from its max HP and current HP
	@staticmethod
	def getImageFromHP(maxHP: int, currentHP: int, powerUP) -> Surface:
		if powerUP == 'extraBall':
			if currentHP == 1:
				return Assets.I_BRICK_EXTRABALL_1
			return Assets.I_BRICK_EXTRABALL_2

		elif maxHP == -1:
			return Assets.I_BRICK_BOSS
		elif maxHP == 1:
			return Assets.I_BRICK_LEVEL1
		elif maxHP == 2:
			if currentHP == 2:
				return Assets.I_BRICK_LEVEL2_2
			return Assets.I_BRICK_LEVEL2_1
		elif maxHP == 3:
			if currentHP == 1:
				return Assets.I_BRICK_LEVEL3_1
			if currentHP == 2:
				return Assets.I_BRICK_LEVEL3_2
			return Assets.I_BRICK_LEVEL3_3


	def getImage(self, frame: int) -> Surface:
		return self.getImageFromHP(self.maxHP, self.hp, self.powerUp)

	def __init__(self, pos: PosRect, maxHP: int, powerUP):
		self.rect: PosRect = PosRect(pos.x, pos.y, GC_BRICK_WIDTH, GC_BRICK_HEIGHT)
		self.image: Surface = self.getImageFromHP(maxHP, maxHP, powerUP)
		self.maxHP: int = maxHP
		self.hp: int = maxHP
		self.powerUp = powerUP

		# set brick score based on values in GameConstants
		if maxHP == -1:
			self.score: int = GC_BRICK_SCORES[3]
		else:
			self.score: int = GC_BRICK_SCORES[maxHP - 1]
