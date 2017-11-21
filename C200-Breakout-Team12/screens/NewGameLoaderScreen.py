import ScreenManager
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from screens.GameScreen import GameScreen
from screens.Screen import Screen


# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen, or 'restart game' button on pause screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()

		# no need to display loading screen here, this should only take a split second

		# TODO: need to load bricks for first level
		state = GameState([], 0)
		controller = GameController(state)
		renderer = GameRenderer()

		ScreenManager.setScreen(GameScreen(state, controller, renderer))

		pass
