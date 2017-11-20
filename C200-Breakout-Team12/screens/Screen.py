# Screen 'abstract' class
import pygame

import Graphics
import ScreenManager


class Screen:
	def update(self):
		# handle pygame.QUIT events without messing with the event queue
		if pygame.event.peek(pygame.QUIT):
			ScreenManager.exit()
		# for some reason fullscreen mode disables alt-f4, at least on Linux
		# so simulate alt-f4 working by exiting when both are pressed
		if pygame.key.get_pressed()[pygame.K_F4] and pygame.key.get_mods() & pygame.KMOD_ALT:
			ScreenManager.exit()

		# update window size on resize
		for e in pygame.event.get(pygame.VIDEORESIZE):
			Graphics.resizeWindow(e.size)

		# clear the screen [super.update() is the first thing called by subclasses, so clearing can be done here]
		Graphics.surface.fill((0, 0, 0))
