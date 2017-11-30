from pygame import Surface

from Assets import Assets
from GameConstants import *
from game.gameClasses.Blittable import Blittable
from game.gameClasses.PosRect import PosRect


class Brick(Blittable):
	rect: PosRect

	score: int
	maxHP: int
	hp: int

	# get the brick image from its max HP and current HP
	@staticmethod
	def getImageFromHP(maxHP: int, currentHP: int) -> Surface:
		if maxHP == -1:
			return Assets.I_BRICK_BOSS
		if maxHP == 1:
			return Assets.I_BRICK_LEVEL1
		if maxHP == 2:
			if currentHP == 2:
				return Assets.I_BRICK_LEVEL2_2
			return Assets.I_BRICK_LEVEL2_1
		if maxHP == 3:
			if currentHP == 1:
				return Assets.I_BRICK_LEVEL3_1
			if currentHP == 2:
				return Assets.I_BRICK_LEVEL3_2
			return Assets.I_BRICK_LEVEL3_3

	def getImage(self, frame: int) -> Surface:
		return self.getImageFromHP(self.maxHP, self.hp)

	def __init__(self, pos: PosRect, score: int, maxHP: int):
		self.rect = PosRect(pos.x, pos.y, GC_BRICK_WIDTH, GC_BRICK_HEIGHT)
		self.image = self.getImageFromHP(maxHP, maxHP)
		self.score = score
		self.maxHP = maxHP
		self.hp = maxHP
