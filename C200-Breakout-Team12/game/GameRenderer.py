# renders a GameState
from game.GameState import GameState
import Graphics
import pygame


class GameRenderer:
	def render(self, state: GameState, frame: int):
		surface: pygame.Surface = Graphics.surface
		# things to draw: bricks, paddle, ball, displayables
		# ball should be drawn last

		for b in state.bricks:
			surface.blit(b.getImage(), (b.rect.x, b.rect.y))

		surface.blit(state.paddle.getImage(frame), (state.paddle.rect.x, state.paddle.rect.y))

		for d in state.displayables:
			image: pygame.Surface = d.getImage(frame)
			surface.blit(image, (d.pos.x - d.image.get_width() // 2, d.pos.y - d.image.get_height() // 2))

		###   BALL   ##########################################################
		ballPosition = state.ball.pos
		ballULX = ballPosition.x - ballPosition.radius  # ball upper left x
		ballULY = ballPosition.y - ballPosition.radius  # ball upper left y
		surface.blit(state.ball.getImage(frame), (ballULX, ballULY))

		Graphics.flip()
