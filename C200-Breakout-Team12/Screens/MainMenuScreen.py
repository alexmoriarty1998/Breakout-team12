# Main menu screen

import pygame

import ScreenManager, Graphics
from Screens.NewGameLoaderScreen import NewGameLoaderScreen
from Screens.Screen import Screen


class MainMenuScreen(Screen):
	background: pygame.Surface = None

	def __init__(self):
		self.background = pygame.image.load("assets/mainMenuBackground.png")

	def update(self):
		super().update()

		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		# TODO: implement below code
		user_started_game = False
		if user_started_game:
			ScreenManager.setScreen(NewGameLoaderScreen())
