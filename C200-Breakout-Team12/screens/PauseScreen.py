import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameRenderer import GameRenderer
from screens.Button import Button
from screens.Screen import Screen


class PauseScreen(Screen):
	def __init__(self, gameScreen):
		super().__init__()

		if GC_GRAB_MOUSE:
			pygame.event.set_grab(False)

		self.gameScreen = gameScreen

		self.buttons.append(Button("resume",
								   self.getButtonRect((0.5, 0.5), Assets.I_BTN_PAUSE_RESUME),
								   Assets.I_BTN_PAUSE_RESUME,
								   Assets.I_BTN_PAUSE_RESUME_H))

		self.buttons.append(Button("quit",
								   self.getButtonRect((0.5, 0.75), Assets.I_BTN_QUIT_TO_MENU_PAUSESCREEN),
								   Assets.I_BTN_QUIT_TO_MENU_PAUSESCREEN,
								   Assets.I_BTN_QUIT_TO_MENU_PAUSESCREEN_H))

	def update(self):
		super().update()

		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)
			# Don't allow pressing escape to resume if on mac system; look at bottom of GameScreen class for info.
			if e.type == pygame.KEYDOWN and not IS_MAC:
				if e.key == pygame.K_ESCAPE:
					self.buttonClicked("resume")  # pressing escape is same as pressing resume button...

		Graphics.clear()
		GameRenderer.render(self.gameScreen.state, self.gameScreen.frame)
		Graphics.surface.blit(Assets.I_PAUSE_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "resume":
			if GC_GRAB_MOUSE:
				pygame.event.set_grab(True)
			ScreenManager.setScreen(self.gameScreen)
		if buttonName == "quit":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
