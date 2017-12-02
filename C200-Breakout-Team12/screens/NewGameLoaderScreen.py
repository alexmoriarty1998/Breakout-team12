import random

import ScreenManager
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from game.LevelTools import makeState
from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity
from screens.GameScreen import GameScreen
from screens.Screen import Screen


# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen, or 'restart game' button on pause screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()
		ScreenManager.setScreen(GameScreen(makeState(1, 0)))
