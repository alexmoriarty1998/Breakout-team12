# renders a GameState
import pygame

import Graphics
from Assets import Assets
from GameConstants import GC_TEXT_COLOR, GC_WALL_SIZE, GC_WORLD_WIDTH
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
		scoreSurface = Graphics.font.render(str(state.score), True, GC_TEXT_COLOR)
		Graphics.surface.blit(scoreSurface, (10, 10))

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
