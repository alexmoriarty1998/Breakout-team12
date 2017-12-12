import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.gameClasses.PosRect import PosRect
from screens.Button import Button
from game.GameRenderer import GameRenderer
from screens.Screen import Screen


class PauseScreen(Screen):
	def __init__(self, gameScreen):
		super().__init__()

		pygame.event.set_grab(False)

		self.gameScreen = gameScreen

		self.buttons.append(Button("resume",
								   self.getButtonRect((0.5, 0.5), Assets.I_BTN_PAUSE_RESUME),
								   Assets.I_BTN_PAUSE_RESUME,
								   Assets.I_BTN_PAUSE_RESUME_H))

		self.buttons.append(Button("quit",
								   self.getButtonRect((0.5, 0.75), Assets.I_BTN_QUIT_TO_MENU),
								   Assets.I_BTN_QUIT_TO_MENU,
								   Assets.I_BTN_QUIT_TO_MENU_H))

	def update(self):
		super().update()

		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE and not IS_MAC:
					self.buttonClicked("resume")  # pressing escape is same as pressing resume button...

		Graphics.clear()
		GameRenderer.render(self.gameScreen.state, self.gameScreen.frame)
		Graphics.surface.blit(Assets.I_PAUSE_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "resume":
			pygame.event.set_grab(True)
			ScreenManager.setScreen(self.gameScreen)
		if buttonName == "quit":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
