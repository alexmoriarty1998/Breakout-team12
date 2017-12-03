# Main menu screen

import pygame

import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import GC_KEY_BEGIN
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):
	begin: bool = False

	def update(self):
		super().update()
		pygame.event.clear()  # polling for keypress instead of getting keydown event, so pump event queue

		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.blit(Assets.I_MAINMENU_BACKGROUND, (0, 0))
		Graphics.flip()

		if pygame.key.get_pressed()[GC_KEY_BEGIN]:  # may need to change this key, or add a clickable button
			self.begin = True

		if self.begin:
			ScreenManager.setScreen(NewGameLoaderScreen())
