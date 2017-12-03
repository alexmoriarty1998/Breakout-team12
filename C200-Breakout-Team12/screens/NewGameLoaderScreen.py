import ScreenManager
from GameConstants import *
from game.LevelTools import makeState
from screens.GameScreen import GameScreen
from screens.Screen import Screen


# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen, or 'restart game' button on pause screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()
		ScreenManager.setScreen(GameScreen(makeState(1, 0, GC_DEFAULT_LIVES)))
