# Main menu screen
import random

import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from game.LevelTools import makeState
from game.gameClasses.PosRect import PosRect
from screens.Button import Button
from screens.NewGameLoaderScreen import NewGameLoaderScreen
from screens.Screen import Screen


class MainMenuScreen(Screen):

	def __init__(self):
		super().__init__()

		# embedded game
		self.gameState: GameState = makeState(99, 0, 1)
		self.gameState.paused = False
		self.gameController: GameController = GameController(self.gameState)
		self.paddleTarget: int = random.randint(GC_WALL_SIZE, GC_WORLD_WIDTH - GC_WALL_SIZE)

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

		# tick the embedded game
		# Paddle needs to not be in the dead center, so the ball does interesting stuff.
		# But generating a random offset each tick results in the paddle jerking around
		# every frame, so limit how fast the offset can change.
		# self.gameState.paddle.rect.x = self.gameState.ball.circle.x - self.gameState.paddle.rect.width // 2
		if self.paddleTarget > self.gameState.paddle.rect.x:
			self.gameState.paddle.rect.x = min(self.gameState.paddle.rect.x + GC_PADDLE_SPEED // 1.4, self.paddleTarget)
		elif self.paddleTarget < self.gameState.paddle.rect.x:
			self.gameState.paddle.rect.x = max(self.gameState.paddle.rect.x - GC_PADDLE_SPEED // 1.4, self.paddleTarget)
		if ((self.gameState.balls[0].circle.x > self.gameState.paddle.rect.x + self.gameState.paddle.rect.width
			 and self.paddleTarget < self.gameState.balls[0].circle.x)
				or (self.gameState.balls[0].circle.x < self.gameState.paddle.rect.x
					and self.paddleTarget > self.gameState.balls[0].circle.x)):
			self.paddleTarget = 0 if self.gameState.balls[0].circle.x < self.gameState.paddle.rect.x else GC_WORLD_WIDTH
		# reset game if it's over
		if self.gameState.won:  # also covers lost
			self.gameState = makeState(99, 0, 1)
			self.gameState.paused = False
			self.gameController = GameController(self.gameState)
		pygame.event.clear()
		self.gameController.update()

		Graphics.clear()
		# draw the embedded game
		GameRenderer.render(self.gameState, self.frame)

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
