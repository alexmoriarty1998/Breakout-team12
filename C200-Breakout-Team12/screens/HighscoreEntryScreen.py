import Graphics
import ScreenManager
from game.Highscores import Highscores
from screens.HighscoreDisplayScreen import HighscoreDisplayScreen
from screens.Screen import Screen
import pygame
from GameConstants import *
from Assets import Assets

class HighscoreEntryScreen(Screen):
	usableInput = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	def __init__(self, score):
		self.inputStr = ''
		self.score = score



	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				if pygame.K_BACKSPACE == e.key:
					self.inputStr = self.inputStr[:-1]
				if pygame.key.name(e.key) in HighscoreEntryScreen.usableInput:
					if len(self.inputStr) < 3:
						self.inputStr += pygame.key.name(e.key)
				if e.key == pygame.K_RETURN and len(self.inputStr) == 3:
					self.submit()



		Graphics.hardClear()
		Graphics.surface.blit(Assets.I_HIGHSCORE_ENTRY_BACKGROUND, (0,0))
		x = GC_HIGHSCORE_ENTRY_BEGIN_X
		for s in self.inputStr:
			Graphics.surface.blit(getattr(Assets, "I_TXT_" + s.upper()), (x, GC_HIGHSCORE_ENTRY_HEIGHT))
			x += GC_IMGFONT_SIZE
		Graphics.flip()

	def submit(self):
		Highscores.add(self.score, self.inputStr)
		Highscores.flush()
		ScreenManager.setScreen(HighscoreDisplayScreen())




