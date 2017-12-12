import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.Highscores import Highscores
from screens.Button import Button
from screens.HighscoreDisplayScreen import HighscoreDisplayScreen
from screens.Screen import Screen


class HighscoreEntryScreen(Screen):
	usableInput = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
				   "u", "v", "w", "x", "y", "z"]

	def __init__(self, score):
		super().__init__()

		pygame.event.set_grab(False)
		self.inputStr = ''
		self.score = score

		self.buttons.append(Button("submit",
								   self.getButtonRect((0.5, 0.67), Assets.I_BTN_HIGHSCORES_SUBMIT),
								   Assets.I_BTN_HIGHSCORES_SUBMIT, Assets.I_BTN_HIGHSCORES_SUBMIT_H))

		self.buttons.append(Button("cancel",
								   self.getButtonRect((0.5, 0.84), Assets.I_BTN_HIGHSCORES_CANCEL),
								   Assets.I_BTN_HIGHSCORES_CANCEL, Assets.I_BTN_HIGHSCORES_CANCEL_H))

	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)
			if e.type == pygame.KEYDOWN:
				if pygame.K_BACKSPACE == e.key:
					self.inputStr = self.inputStr[:-1]
				if pygame.key.name(e.key) in HighscoreEntryScreen.usableInput:
					if len(self.inputStr) < 3:
						self.inputStr += pygame.key.name(e.key)
				if e.key == pygame.K_RETURN:
					self.submit()

		Graphics.hardClear()
		Graphics.surface.blit(Assets.I_HIGHSCORE_ENTRY_BACKGROUND, (0, 0))
		x = GC_HIGHSCORE_ENTRY_BEGIN_X
		for s in self.inputStr:
			Graphics.surface.blit(getattr(Assets, "I_TXT_" + s.upper()), (x, GC_HIGHSCORE_ENTRY_HEIGHT))
			x += GC_IMGFONT_SIZE
		self.drawButtons()
		Graphics.flip()

	def submit(self):
		if len(self.inputStr) != 3:
			return
		Highscores.add(self.score, self.inputStr)
		Highscores.flush()
		ScreenManager.setScreen(HighscoreDisplayScreen())

	def buttonClicked(self, buttonName):
		if buttonName == "submit":
			self.submit()
		if buttonName == "cancel":
			ScreenManager.setScreen(HighscoreDisplayScreen())
