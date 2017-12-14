import Graphics
import ScreenManager
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from game.Highscores import Highscores
from screens.BetweenLevelsScreen import BetweenLevelsScreen
from screens.HighscoreDisplayScreen import HighscoreDisplayScreen
from screens.HighscoreEntryScreen import HighscoreEntryScreen
from screens.PauseScreen import PauseScreen
from screens.Screen import Screen


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
			if self.state.level == GC_NUM_LEVELS:
				if Highscores.isHighScore(self.state.oldScore + self.state.score):
					ScreenManager.setScreen(HighscoreEntryScreen(self.state.oldScore + self.state.score))
				else:
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
		# This is to avoid a bug with mac systems.
		# Normally, the user can press escape to enter the pause menu. He can click the button to resume the game, but
		# should also be able to resume by pressing escape again. Can't use polling to enter the pause screen, because
		# if the user presses escape to exit the pause screen, polling will return that pause is pressed, and will
		# immediately go back to the pause screen. So use an event loop to get only the keydown event for the escape
		# key. However, gameController has its own event loop for paddle movement. The solution is to have it post
		# escape key down events back onto the event queue, so this second event loop picks up the event. However, for
		# some reason, this breaks paddle movement (mouse and keyboard) on macs. So for macs, use polling to enter the
		# pause menu, and disable the ability to exit the pause menu by pressing escape again.
		if IS_MAC:
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				ScreenManager.setScreen(PauseScreen(self))
		else:
			for e in pygame.event.get():
				if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
					ScreenManager.setScreen(PauseScreen(self))
				else:
					# this will gobble up some left/right key events if they aren't posted back
					pygame.event.post(e)
