# Main menu screen

import pygame

import ScreenManager, Graphics
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):
	background: pygame.Surface = None

	def __init__(self):
		self.background = pygame.image.load("assets/mainMenuScreen/background.png")

	def update(self):
		super().update()

		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		# TODO: implement below code
		user_started_game = False
		if user_started_game:
			ScreenManager.setScreen(NewGameLoaderScreen())
