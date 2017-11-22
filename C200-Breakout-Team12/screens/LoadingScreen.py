# Loading Screen
# loads all game assets into Assets module, then switches to MainMenuScreen
# having a progress bar would be nice, but would require asynchronous loading of assets
#  or some nifty tricks to allow for that while fitting neatly into the StateManager framework
import pygame

from Assets import Assets
import Graphics
import ScreenManager
from screens.MainMenuScreen import MainMenuScreen
from screens.Screen import Screen


# abbreviation for pygame.image.load() that also adds assets/ and .png onto the path
# will need to make a copy for sound & music, if they are ever implemented
def li(path: str):
	return pygame.image.load("assets/" + path + ".png").convert_alpha(Graphics.surface)

class LoadingScreen(Screen):
	background: pygame.Surface = None

	def __init__(self):
		self.background = pygame.image.load("assets/loadingScreen/background.png")

	def loadAssets(self):
		# Main Menu
		Assets.I_MAINMENU_BACKGROUND = li("mainMenuScreen/background")

		# ball and paddle
		Assets.I_BALL = li("gameScreen/ball")
		Assets.I_PADDLE = li("gameScreen/paddle")
		# bricks
		Assets.I_BRICK_LEVEL1 = li("gameScreen/brick11")
		Assets.I_BRICK_LEVEL2_2 = li("gameScreen/brick22")
		Assets.I_BRICK_LEVEL2_1 = li("gameScreen/brick21")
		Assets.I_BRICK_LEVEL3_3 = li("gameScreen/brick33")
		Assets.I_BRICK_LEVEL3_2 = li("gameScreen/brick32")
		Assets.I_BRICK_LEVEL3_1 = li("gameScreen/brick31")
		Assets.I_BRICK_BOSS = li("gameScreen/brickBOSS")


	def update(self):
		super().update()

		Graphics.surface.blit(self.background, (0, 0))
		Graphics.flip()

		self.loadAssets()

		ScreenManager.setScreen(MainMenuScreen())
