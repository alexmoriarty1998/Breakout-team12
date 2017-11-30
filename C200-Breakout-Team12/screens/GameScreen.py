import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from screens.Screen import Screen


class GameScreen(Screen):
	state: GameState
	controller: GameController
	renderer: GameRenderer
	frame: int = 0  # current game tick, used for animations

	def __init__(self, state: GameState, controller: GameController, renderer: GameRenderer):
		self.state = state
		self.controller = controller
		self.renderer = renderer

	def update(self):
		super().update()

		# update game state
		self.controller.update(self.state)

		# draw current game state
		Graphics.clear(Assets.I_BLUR)
		self.renderer.render(self.state, self.frame)
		if self.state.won == 1:
			Graphics.surface.blit(Assets.I_WON, (0, 0))
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

		# TODO: move to next level if won or lost
		pass
