import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from screens.BetweenLevelsScreen import BetweenLevelsScreen
from screens.Screen import Screen


class GameScreen(Screen):
	state: GameState
	frame: int = 0  # current game tick, used for animations

	def __init__(self, state: GameState):
		self.state = state
		self.controller = GameController(self.state)

	def update(self):
		super().update()

		###   UPDATE GAME STATE   #############################################
		self.controller.update()

		###   DRAW GAME STATE   ###############################################
		Graphics.clear(Assets.I_BLUR)
		GameRenderer.render(self.state, self.frame)
		Graphics.flip()

		###   GO TO WIN/LOSS SCREENS   ########################################
		if self.state.won == 1:
			ScreenManager.setScreen(BetweenLevelsScreen(self.state.level, self.state.score, self.state.numLives))
		elif self.state.won == -1:
			# TODO: transition to highscore display/entry as appropriate
			pass

		###   GO TO PAUSE SCREEN   ############################################
		if pygame.key.get_pressed()[GC_KEY_PAUSE]:
			# TODO: transition to pause screen
			pass

		# TODO: remove this debug feature
		if pygame.key.get_pressed()[pygame.K_r]:
			from screens.NewGameLoaderScreen import NewGameLoaderScreen
			ScreenManager.setScreen(NewGameLoaderScreen())

		# debug print
		if GC_PRINT_BALL_SPEED:
			print("{0:.2f}".format((self.state.ball.velocity.dx ** 2 + self.state.ball.velocity.dy ** 2) ** 0.5))
		# debug print
		if GC_PRINT_GAME_TIME:
			print("{0:.2f}".format(self.state.time))
