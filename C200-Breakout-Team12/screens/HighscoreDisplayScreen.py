import Graphics
import ScreenManager
from Assets import Assets
from GameConstants import *
from game.Highscores import Highscores
from screens.Screen import Screen


class HighscoreDisplayScreen(Screen):
	def update(self):
		super().update()
		pygame.event.clear()
		if pygame.key.get_pressed()[pygame.K_ESCAPE]:
			# import here to avoid import loop
			from screens.MainMenuScreen import MainMenuScreen
			ScreenManager.setScreen(MainMenuScreen())

		Graphics.clear(Assets.I_BLUR)
		Graphics.surface.fill((255, 255, 255))  # font is black, so need white background

		# calculate height to start drawing at
		height = (1080 - 11 * GC_IMGFONT_SIZE - GC_HIGHSCORE_SPACING) // 2

		# draw title
		titleX = GC_WORLD_WIDTH // 2 - GC_IMGFONT_SIZE * 5  # 10 characters in "HIGHSCORES"
		for i in "HIGHSCORES":
			Graphics.surface.blit(getattr(Assets, "I_TXT_" + i), (titleX, height))
			titleX += GC_IMGFONT_SIZE

		height += GC_IMGFONT_SIZE + GC_HIGHSCORE_SPACING

		# draw highscores
		for i in range(10):
			x = 300

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

			height += GC_IMGFONT_SIZE

		Graphics.flip()
