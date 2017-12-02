import random

import GameConstants
import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.GameState import GameState
from game.gameClasses.Ball import Ball
from game.gameClasses.Brick import Brick
from game.gameClasses.PosCircle import PosCircle
from game.gameClasses.PosRect import PosRect
from game.gameClasses.Velocity import Velocity
from screens.Screen import Screen


class BetweenLevelsScreen(Screen):
	def __init__(self):
		self.state = makeState(level + 1, score)

	def update(self):
		super().update()
		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.blit(Assets.I_BETWEEN_LEVELS_BACKGROUND, (0, 0))
		Graphics.flip()
		if pygame.key.get_pressed()[GameConstants.GC_KEY_MAINMENU_BEGIN]:
			from screens.GameScreen import GameScreen
			ScreenManager.setScreen(GameScreen(self.state))
