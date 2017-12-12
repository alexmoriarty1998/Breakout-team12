import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from screens.BetweenLevelsScreen import BetweenLevelsScreen
from screens.HighscoreDisplayScreen import HighscoreDisplayScreen
from screens.HighscoreEntryScreen import HighscoreEntryScreen
from screens.PauseScreen import PauseScreen
from screens.Screen import Screen
from game.Highscores import Highscores


class GameScreen(Screen):
	state: GameState
	frame: int = 0  # current game tick, used for animations

	def __init__(self, state: GameState):
		super().__init__()
		self.state = state
		self.controller = GameController(self.state)

	def update(self):
		super().update()

		###   UPDATE GAME STATE   #############################################
		self.controller.update()

		###   DRAW GAME STATE   ###############################################
		Graphics.clear()
		GameRenderer.render(self.state, self.frame)
		Graphics.flip()

		###   GO TO WIN/LOSS SCREENS   ########################################
		if self.state.won == 1:
			if self.state.level == 5:
				if Highscores.isHighScore(self.state.oldScore + self.state.score):
					ScreenManager.setScreen(HighscoreEntryScreen(self.state.oldScore + self.state.score))
				ScreenManager.setScreen(HighscoreDisplayScreen())
			else:
				ScreenManager.setScreen(
					BetweenLevelsScreen(self.state.level, self.state.oldScore, self.state.score, self.state.numLives))

		elif self.state.won == -1:
			if Highscores.isHighScore(self.state.oldScore):
				ScreenManager.setScreen(HighscoreEntryScreen(self.state.oldScore))
			else:
				ScreenManager.setScreen(HighscoreDisplayScreen())

		###   GO TO PAUSE SCREEN   ############################################
		# need to use event loop so it doesn't get repaused if user presses
		# escape to exit from the pause menu
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
				ScreenManager.setScreen(PauseScreen(self))

		# debug print
		if GC_PRINT_BALL_SPEED:
			print("{0:.2f}".format((self.state.ball.velocity.dx ** 2 + self.state.ball.velocity.dy ** 2) ** 0.5))
		# debug print
		if GC_PRINT_GAME_TIME:
			print("{0:.2f}".format(self.state.time))
