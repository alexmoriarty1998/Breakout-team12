# Main menu screen

import pygame

import ScreenManager, Graphics
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):
	background: pygame.Surface = None
	begin: bool = False

	def __init__(self):
		self.background = pygame.image.load("assets/mainMenuScreen/background.png")

	def update(self):
		super().update()

		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		pygame.event.pump()  # polling for keypress instead of getting keydown event, so pump event queue

		if pygame.key.get_pressed()[pygame.K_SPACE]:  # may need to change this key, or add a clickable button
			self.begin = True

		if self.begin:
			ScreenManager.setScreen(NewGameLoaderScreen())
