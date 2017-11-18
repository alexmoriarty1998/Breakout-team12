# Loading Screen
# loads all game assets into asset manager, then switches to MainMenuScreen
# having a progress bar would be nice, but would require asynchronous loading of assets
#  or some nifty tricks to allow for that while fitting neatly into the StateManager framework
import pygame

import Graphics
import ScreenManager
from Screens.MainMenuScreen import MainMenuScreen
from Screens.Screen import Screen


class LoadingScreen(Screen):
	background: pygame.Surface = None

	def __init__(self):
		self.background = pygame.image.load("assets/loadingBackground.png")

	def update(self):
		super().update()

		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		# TODO: stuff goes here
		# all other asset loading calls go here
		# still working out how exactly asset management is going to work

		ScreenManager.setScreen(MainMenuScreen())
