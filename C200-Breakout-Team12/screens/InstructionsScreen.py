import pygame

import Graphics
import ScreenManager
from Assets import Assets
from screens.Screen import Screen


class InstructionsScreen(Screen):
	def update(self):
		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.blit(Assets.I_INSTRUCTIONS_BACKGROUND, (0, 0))
		Graphics.flip()

		pygame.event.clear()
		if pygame.key.get_pressed()[pygame.K_ESCAPE]:
			# import here to avoid import loop
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
