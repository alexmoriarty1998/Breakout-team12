import Graphics
from GameConstants import *
from game.GameController import GameController
from game.GameRenderer import GameRenderer
from game.GameState import GameState
from screens.Screen import Screen


class GameScreen(Screen):
	state: GameState
	controller: GameController
	renderer: GameRenderer
	frame: int = 0  # current game tick, used for animations

	def __init__(self, state: GameState, controller: GameController, renderer: GameRenderer):
		self.state = state
		self.controller = controller
		self.renderer = renderer

	def update(self):
		super().update()


		self.frame += 1

		self.controller.update()

		Graphics.clear()
		self.renderer.render(self.state, self.frame)
		Graphics.flip()

		if pygame.key.get_pressed()[GC_KEY_GAME_PAUSE]:
			pass  # TODO: pause

		# TODO: move to next level if won or lost
		pass
