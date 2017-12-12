# Main menu screen

import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.gameClasses.PosRect import PosRect
from screens.Button import Button
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):

	def __init__(self):
		super().__init__()

		beginCoords = 0.5, 0.57
		helpCoords = 0.3, 0.8
		highscoresCoords = 0.7, 0.8

		self.begin: bool = False

		self.buttons.append(
			Button("exit",
				   PosRect(GC_WORLD_WIDTH - GC_SMALL_BUTTON_SIZE, 0, GC_SMALL_BUTTON_SIZE, GC_SMALL_BUTTON_SIZE),
				   Assets.I_BTN_EXIT, Assets.I_BTN_EXIT_H))

		fullscreenImg = Assets.I_BTN_UNFULLSCREEN if Graphics.isFullscreen() else Assets.I_BTN_FULLSCREEN
		fullscreenImgH = Assets.I_BTN_UNFULLSCREEN_H if Graphics.isFullscreen() else Assets.I_BTN_FULLSCREEN_H
		self.buttons.append(Button("fullscreen",
								   PosRect(GC_WORLD_WIDTH - GC_SMALL_BUTTON_SIZE,
										   GC_WORLD_HEIGHT - GC_SMALL_BUTTON_SIZE,
										   GC_SMALL_BUTTON_SIZE,
										   GC_SMALL_BUTTON_SIZE),
								   fullscreenImg, fullscreenImgH))
		self.buttons.append(Button("begin",
								   self.getButtonRect(beginCoords, Assets.I_BTN_MAINMENU_BEGIN),
								   Assets.I_BTN_MAINMENU_BEGIN, Assets.I_BTN_MAINMENU_BEGIN_H))
		self.buttons.append(Button("help",
								   self.getButtonRect(helpCoords, Assets.I_BTN_MAINMENU_HELP),
								   Assets.I_BTN_MAINMENU_HELP, Assets.I_BTN_MAINMENU_HELP_H))
		self.buttons.append(Button("highscores",
								   self.getButtonRect(highscoresCoords, Assets.I_BTN_MAINMENU_HIGHSCORES),
								   Assets.I_BTN_MAINMENU_HIGHSCORES, Assets.I_BTN_MAINMENU_HIGHSCORES_H))

	def update(self):
		super().update()
		# pygame.event.clear()  # polling for keypress instead of getting keydown event, so pump event queue
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)

		Graphics.clear()
		Graphics.surface.blit(Assets.I_MAINMENU_BACKGROUND, (0, 0))
		self.drawButtons()
		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "exit":
			ScreenManager.exit()
		if buttonName == "begin":
			ScreenManager.setScreen(NewGameLoaderScreen())
		if buttonName == "highscores":
			from screens.HighscoreDisplayScreen import HighscoreDisplayScreen
			ScreenManager.setScreen(HighscoreDisplayScreen())
		if buttonName == "help":
			from screens.InstructionsScreen import InstructionsScreen
			ScreenManager.setScreen(InstructionsScreen())
		if buttonName == "fullscreen":
			Graphics.swapWindowMode()
			# also need to switch the 'go fullscreen' button to a 'go windowed' button and vice versa
			# get the right image (go fullscreen or go windowed)
			fullscreenImg = Assets.I_BTN_UNFULLSCREEN if Graphics.isFullscreen() else Assets.I_BTN_FULLSCREEN
			fullscreenImgH = Assets.I_BTN_UNFULLSCREEN_H if Graphics.isFullscreen() else Assets.I_BTN_FULLSCREEN_H
			# remove the fullscreen button
			self.buttons = list(filter(lambda b: b.name != "fullscreen", self.buttons))
			# add a fullscreen button with the right image
			self.buttons.append(Button("fullscreen",
									   PosRect(GC_WORLD_WIDTH - GC_SMALL_BUTTON_SIZE,
											   GC_WORLD_HEIGHT - GC_SMALL_BUTTON_SIZE,
											   GC_SMALL_BUTTON_SIZE,
											   GC_SMALL_BUTTON_SIZE),
									   fullscreenImg, fullscreenImgH))
