import Graphics
from screens.Screen import Screen
import pygame
from GameConstants import *
import Assets

class HighscoreEntryScreen(Screen):
	def __init__(self):
		self.inputStr = ''



	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				self.inputStr += pygame.key.name(e.key)
		Graphics.surface.hardClear()
		Graphics.surface.fill((255,255,255))
		x = 0
		for s in self.inputStr:
			Graphics.surface.blit(getattr(Assets, "I_TXT_" + s), (x, 0))
			x += GC_IMGFONT_SIZE





