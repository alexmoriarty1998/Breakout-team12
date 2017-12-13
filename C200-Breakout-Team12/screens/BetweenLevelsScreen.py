import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.LevelTools import makeState
from screens.Button import Button
from screens.Screen import Screen


class BetweenLevelsScreen(Screen):
	def __init__(self, level, oldScore, score, numLives):
		super().__init__()

		if GC_GRAB_MOUSE:
			pygame.event.set_grab(False)

		# generate a new game state for the next level
		lifeToAdd = 0
		if level % 2 != 0:
			lifeToAdd = 1
		self.state = makeState(level + 1, oldScore + score, numLives + lifeToAdd)

		self.buttons.append(Button("continue",
								   self.getButtonRect((0.5, 0.5), Assets.I_BTN_BETWEENLEVELS_CONTINUE),
								   Assets.I_BTN_BETWEENLEVELS_CONTINUE, Assets.I_BTN_BETWEENLEVELS_CONTINUE_H))

		self.buttons.append(Button("quit",
								   self.getButtonRect((0.5, 0.75), Assets.I_BTN_QUIT_TO_MENU),
								   Assets.I_BTN_QUIT_TO_MENU,
								   Assets.I_BTN_QUIT_TO_MENU_H))

	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)

		Graphics.clear()
		Graphics.surface.blit(Assets.I_BETWEENLEVELS_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "continue":
			if GC_GRAB_MOUSE:
				pygame.event.set_grab(True)
			from screens.GameScreen import GameScreen
			ScreenManager.setScreen(GameScreen(self.state))
		if buttonName == "quit":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
