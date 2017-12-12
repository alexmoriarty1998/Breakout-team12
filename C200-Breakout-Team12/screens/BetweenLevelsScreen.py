import GameConstants
import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.LevelTools import makeState
from screens.Screen import Screen


class BetweenLevelsScreen(Screen):
	def __init__(self, level, oldScore, score, numLives):
		lifeToAdd = 0
		if level % 2 != 0:
			lifeToAdd = 1
		self.state = makeState(level + 1, oldScore + score, numLives + lifeToAdd)

	def update(self):
		super().update()
		pygame.event.clear()

		Graphics.clear()
		Graphics.surface.blit(Assets.I_BETWEEN_LEVELS_BACKGROUND, (0, 0))
		Graphics.flip()
