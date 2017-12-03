# renders a GameState

import Graphics
from Assets import Assets
from GameConstants import *
from game.GameState import GameState


class GameRenderer:
	@staticmethod
	def render(state: GameState, frame: int) -> None:
		surface: pygame.Surface = Graphics.surface

		# don't change this render order

		###   WALL   ##########################################################
		surface.blit(Assets.I_WALL, (0, 0))
		surface.blit(Assets.I_WALL, (GC_WORLD_WIDTH - GC_WALL_SIZE, 0))

		### STATS  ############################################################
		# scoreSurface = Graphics.font.render(str(state.score), True, GC_TEXT_COLOR)
		# Graphics.surface.blit(scoreSurface, (10, 10))

		# the size of text assets is the same as wall size

		# score
		Graphics.surface.blit(Assets.I_TXT_SCORE, (0, 0))
		height = Assets.I_TXT_SCORE.get_height()
		for i in str(state.score):
			# get image (stored as I_TXT_N, where N is an integer 0-9) from the number in the string
			image: pygame.Surface = getattr(Assets, "I_TXT_" + str(i))
			Graphics.surface.blit(image, (0, height))
			height += GC_WALL_SIZE

		# level
		Graphics.surface.blit(Assets.I_TXT_LEVEL, (GC_WORLD_WIDTH - GC_WALL_SIZE, 0))
		height = Assets.I_TXT_LEVEL.get_height()
		# draw levels as '01' '02' etc. instead of just '1' '2'
		if state.level < 10:
			Graphics.surface.blit(Assets.I_TXT_0, (GC_WORLD_WIDTH - GC_WALL_SIZE, height))
			height += GC_WALL_SIZE
		for i in str(state.level):
			image: pygame.Surface = getattr(Assets, "I_TXT_" + str(i))
			Graphics.surface.blit(image, (GC_WORLD_WIDTH - GC_WALL_SIZE, height))
			height += GC_WALL_SIZE

		# lives
		height = GC_WORLD_HEIGHT - GC_WALL_SIZE
		for i in range(state.numLives):
			Graphics.surface.blit(Assets.I_TXT_LIFE, (GC_WORLD_WIDTH - GC_WALL_SIZE, height))
			height -= GC_WALL_SIZE

		# time
		height = GC_WORLD_HEIGHT - Assets.I_TXT_TIME.get_height()
		Graphics.surface.blit(Assets.I_TXT_TIME, (0, height))
		height -= GC_WALL_SIZE
		for i in reversed(str(int(state.time))):
			image: pygame.Surface = getattr(Assets, "I_TXT_" + str(i))
			Graphics.surface.blit(image, (0, height))
			height -= GC_WALL_SIZE
		# like level, draw leading zeroes (trailing in this case)
		if int(state.time) < 100:
			Graphics.surface.blit(Assets.I_TXT_0, (0, height))
			height -= GC_WALL_SIZE
		if int(state.time) < 10:
			Graphics.surface.blit(Assets.I_TXT_0, (0, height))

		###   PADDLE   ########################################################
		surface.blit(state.paddle.getImage(frame), (state.paddle.rect.x, state.paddle.rect.y))

		###   BRICKS   ########################################################
		for b in state.bricks:
			surface.blit(b.getImage(frame), (b.rect.x, b.rect.y))

		###   BALL   ##########################################################
		ballPos = state.ball.circle
		surface.blit(state.ball.getImage(frame), (ballPos.x - ballPos.radius, ballPos.y - ballPos.radius))

		###   DISPLAYABLES   ##################################################
		for d in state.displayables:
			image: pygame.Surface = d.getImage(frame)
			surface.blit(image, (d.pos.x - d.image.get_width() // 2, d.pos.y - d.image.get_height() // 2))
