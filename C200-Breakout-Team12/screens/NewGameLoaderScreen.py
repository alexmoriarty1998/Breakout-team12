from screens.Screen import Screen


# creates a new game and starts it
# separated from MainMenuScreen to allow game to be easily restarted from other
# points, e.g. the game over screen
class NewGameLoaderScreen(Screen):
	def update(self):
		super().update()  # TODO: stuff goes here
