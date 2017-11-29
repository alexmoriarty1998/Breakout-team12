# Main menu screen

import pygame

import ScreenManager, Graphics
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen
from Assets import Assets
from GameConstants import GC_KEY_MAINMENU_BEGIN


class MainMenuScreen(Screen):
	background: pygame.Surface = None
	begin: bool = False

	def __init__(self):
		self.background = Assets.I_MAINMENU_BACKGROUND

	def update(self):
		super().update()
		pygame.event.clear()  # polling for keypress instead of getting keydown event, so pump event queue

		Graphics.blur(Assets.I_BLUR)
		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		if pygame.key.get_pressed()[GC_KEY_MAINMENU_BEGIN]:  # may need to change this key, or add a clickable button
			self.begin = True

		if self.begin:
			ScreenManager.setScreen(NewGameLoaderScreen())
