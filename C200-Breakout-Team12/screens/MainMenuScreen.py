# Main menu screen

import pygame

import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):
	begin: bool = False

	def update(self):
		super().update()
		# pygame.event.clear()  # polling for keypress instead of getting keydown event, so pump event queue
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				gamePosition = Graphics.unproject(e.pos)
				if gamePosition[0] <= GC_WORLD_WIDTH // 2 and gamePosition[1] >= GC_WORLD_HEIGHT // 2:
					# pressed lower left quarter of screen
					# import here to avoid import loop
					from screens.InstructionsScreen import InstructionsScreen
					ScreenManager.setScreen(InstructionsScreen())
				if gamePosition[0] >= GC_WORLD_WIDTH // 2 and gamePosition[1] >= GC_WORLD_HEIGHT // 2:
					# mouse clicked in bottom right corner of main screen
					from screens.HighscoresDisplayScreen import HighscoresDisplayScreen
					ScreenManager.setScreen(HighscoresDisplayScreen)

		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.blit(Assets.I_MAINMENU_BACKGROUND, (0, 0))
		Graphics.flip()

		if pygame.key.get_pressed()[GC_KEY_BEGIN]:  # may need to change this key, or add a clickable button
			self.begin = True

		if self.begin:
			ScreenManager.setScreen(NewGameLoaderScreen())
