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
		self.gameScreen = gameScreen

		self.buttons.append(Button("resume",
								   PosRect(GC_WORLD_WIDTH // 2 - Assets.I_BTN_PAUSE_RESUME.get_width() // 2,
										   GC_WORLD_HEIGHT // 2 - Assets.I_BTN_PAUSE_RESUME.get_height() // 2,
										   Assets.I_BTN_PAUSE_RESUME.get_width(),
										   Assets.I_BTN_PAUSE_RESUME.get_height()),
								   Assets.I_BTN_PAUSE_RESUME,
								   Assets.I_BTN_PAUSE_RESUME_H))

		self.buttons.append(Button("quit",
								   PosRect(GC_WORLD_WIDTH // 2 - Assets.I_BTN_PAUSE_QUIT.get_width() // 2,
										   GC_WORLD_HEIGHT // 2 - Assets.I_BTN_PAUSE_QUIT.get_height() // 2 + 200,
										   Assets.I_BTN_PAUSE_QUIT.get_width(),
										   Assets.I_BTN_PAUSE_QUIT.get_height()),
								   Assets.I_BTN_PAUSE_QUIT,
								   Assets.I_BTN_PAUSE_QUIT_H))

	def update(self):
		super().update()

		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)

		Graphics.clear()
		GameRenderer.render(self.gameScreen.state, self.gameScreen.frame)
		Graphics.surface.blit(Assets.I_PAUSE_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "resume":
			ScreenManager.setScreen(self.gameScreen)
		if buttonName == "quit":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
