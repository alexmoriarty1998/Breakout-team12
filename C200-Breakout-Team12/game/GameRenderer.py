# renders a GameState
from game.GameState import GameState
import Graphics
import pygame
from Assets import Assets
from GameConstants import GC_WORLD_WIDTH, GC_WALL_SIZE


class GameRenderer:
	@staticmethod
	def render(state: GameState, frame: int) -> None:
		surface: pygame.Surface = Graphics.surface

		# always render displayables first

		###   DISPLAYABLES   ##################################################
		for d in state.displayables:
			image: pygame.Surface = d.getImage(frame)
			surface.blit(image, (d.pos.x - d.image.get_width() // 2, d.pos.y - d.image.get_height() // 2))

		###   BRICKS   ########################################################
		for b in state.bricks:
			surface.blit(b.getImage(frame), (b.rect.x, b.rect.y))

		###   PADDLE   ########################################################
		surface.blit(state.paddle.getImage(frame), (state.paddle.rect.x, state.paddle.rect.y))

		###   BALL   ##########################################################
		ballPos = state.ball.circle
		surface.blit(state.ball.getImage(frame), (ballPos.x - ballPos.radius, ballPos.y - ballPos.radius))

		###   WALL   ##########################################################
		surface.blit(Assets.I_WALL, (0,0))
		surface.blit(Assets.I_WALL,(GC_WORLD_WIDTH - GC_WALL_SIZE, 0))
