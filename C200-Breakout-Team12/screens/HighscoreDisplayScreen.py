import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.Highscores import Highscores
from game.gameClasses.PosRect import PosRect
from screens.Button import Button
from screens.Screen import Screen


class HighscoreDisplayScreen(Screen):
	VERTICAL_SPACING = 25

	def __init__(self):
		super().__init__()
		if GC_GRAB_MOUSE:
			pygame.event.set_grab(False)
		self.buttons.append(
			Button("back",
				   PosRect(GC_WORLD_WIDTH - GC_SMALL_BUTTON_SIZE, 0, GC_SMALL_BUTTON_SIZE, GC_SMALL_BUTTON_SIZE),
				   Assets.I_BTN_BACK, Assets.I_BTN_BACK_H))

	def update(self):
		super().update()
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				self.clickButtons(e.pos)

		Graphics.clear()
		Graphics.surface.blit(Assets.I_HIGHSCORE_DISPLAY_BACKGROUND, (0, 0))

		# calculate height to start drawing at
		height = (GC_WORLD_HEIGHT - 10 * (GC_IMGFONT_SIZE + HighscoreDisplayScreen.VERTICAL_SPACING)) // 2 + 5

		# draw highscores
		for i in range(10):
			x = 375

			# draw highscore number (1-10)
			if i == 9:
				Graphics.surface.blit(Assets.I_TXT_1, (x, height))
				x += GC_IMGFONT_SIZE
				Graphics.surface.blit(Assets.I_TXT_0, (x, height))
				x += GC_IMGFONT_SIZE
			else:
				Graphics.surface.blit(Assets.I_TXT_0, (x, height))
				x += GC_IMGFONT_SIZE
				image: pygame.Surface = getattr(Assets, "I_TXT_" + str(i + 1))
				Graphics.surface.blit(image, (x, height))
				x += GC_IMGFONT_SIZE

			x += GC_HIGHSCORE_SPACING

			# draw name
			for j in Highscores.names[i]:
				image: pygame.Surface = getattr(Assets, "I_TXT_" + j.upper())
				Graphics.surface.blit(image, (x, height))
				x += GC_IMGFONT_SIZE

			x += GC_HIGHSCORE_SPACING
			for j in str(Highscores.scores[i]):
				image: pygame.Surface = getattr(Assets, "I_TXT_" + str(j))
				Graphics.surface.blit(image, (x, height))
				x += GC_IMGFONT_SIZE

			height += GC_IMGFONT_SIZE + HighscoreDisplayScreen.VERTICAL_SPACING

		self.drawButtons()

		Graphics.flip()

	def buttonClicked(self, buttonName):
		if buttonName == "back":
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())
