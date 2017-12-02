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

		# update game state
		self.controller.update()

		# draw current game state
		Graphics.clear(Assets.I_BLUR)
		GameRenderer.render(self.state, self.frame)
		if self.state.won == 1:
			Graphics.surface.blit(Assets.I_WON, (0, 0))
			score = GC_PAR_TIME / self.state.time
			percentBricksDestroyed = self.state.totalBricksDestroyedScore / self.state.totalBrickScore
			score *= (1 - percentBricksDestroyed) + 100
			score = int(score)
			print(score)

		elif self.state.won == -1:
			Graphics.surface.blit(Assets.I_LOST, (0, 0))
		Graphics.flip()

		# TODO: remove this debug feature
		if pygame.key.get_pressed()[pygame.K_r]:
			from screens.NewGameLoaderScreen import NewGameLoaderScreen
			ScreenManager.setScreen(NewGameLoaderScreen())

		# transition to next screens on win/loss/pause
		if pygame.key.get_pressed()[GC_KEY_GAME_PAUSE]:
			pass  # TODO: pause

		if self.state.won == 1:
			ScreenManager.setScreen(BetweenLevelsScreen(self.state.level, self.state.score, self.state.numLives))
		pass
