import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.gameClasses.PosRect import PosRect
from screens.Button import Button
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class InstructionsScreen(Screen):

	def __init__(self):
		super().__init__()
		self.buttons.append(
			Button("back",
				   PosRect(GC_WORLD_WIDTH - GC_SMALL_BUTTON_SIZE, 0, GC_SMALL_BUTTON_SIZE, GC_SMALL_BUTTON_SIZE),
				   Assets.I_BTN_BACK, Assets.I_BTN_BACK_H))

	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)
			if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
				ScreenManager.setScreen(NewGameLoaderScreen())

		Graphics.clear()
		Graphics.surface.blit(Assets.I_INSTRUCTIONS_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "back":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
