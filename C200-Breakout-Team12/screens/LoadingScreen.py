# Loading Screen
# loads all game assets into Assets module, then switches to MainMenuScreen
# having a progress bar would be nice, but would require asynchronous loading of assets
#  or some nifty tricks to allow for that while fitting neatly into the StateManager framework
import pygame
from game.Highscores import Highscores
import Graphics
import ScreenManager
from screens.Screen import Screen


# Abbreviation for pygame.image.load() that also assets/ and .png onto the path and
# also does convert_alpha(). Moved outside of class so 'self.' doesn't have to be typed.
# Will need to make a copy for sound & music, if they are ever implemented.

class LoadingScreen(Screen):
	background: pygame.Surface = None

	def __init__(self):
		self.background = pygame.image.load("assets/loading/background.png")

	def update(self):
		super().update()

		Graphics.hardClear()
		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		# so this is some dirty and hackish trick
		# All the assets are static variables of the class Assets, and
		# they are loaded in their definition. Example
		# class Assets:
		#     First_Asset = pygame.image.load(...)
		#
		# This is used over declaring them all in __init__, because the
		# assets are stored as static variables, and for some reason IDE
		# autocomplete doesn't find static variables created in __init__.
		# Autocomplete is important for assets since they all have long,
		# hard to remember names.
		# The assets will be loaded whenever the Assets class is first
		# imported, so ensure that this doesn't happen until the loading
		# screen has been drawn. Then, you can import MainMenuScreen
		# (which imports Assets). But put a 'from Assets import Assets'
		# just in case MainMenu no longer relies on importing Assets in
		# the future.

		# noinspection PyUnresolvedReferences
		from Assets import Assets
		from screens.MainMenuScreen import MainMenuScreen
		Highscores.load()

		ScreenManager.setScreen(MainMenuScreen())
