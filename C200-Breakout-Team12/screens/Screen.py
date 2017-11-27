# Screen 'abstract' class
import pygame

import Graphics
import ScreenManager


class Screen:
	frame: int = 0

	def update(self):
		# screen is not cleared here to allow for motion blur effects

		# this pump is necessary for quit events to reliably be found below
		# it still allows for events to be gotten via event.get(), so while
		# there is a small performance cost, it allows the rest of the code
		# to be simplified and does not interfere
		pygame.event.pump()
		# this won't reliably work without the pump() above
		if pygame.event.peek(pygame.QUIT):
			ScreenManager.exit()
		# for some reason fullscreen mode disables alt-f4, at least on Linux
		# so simulate alt-f4 working by exiting when both are pressed
		if pygame.key.get_pressed()[pygame.K_F4] and pygame.key.get_mods() & pygame.KMOD_ALT:
			ScreenManager.exit()

		# update window size on resize
		for e in pygame.event.get(pygame.VIDEORESIZE):
			Graphics.resizeWindow(e.size)

		self.frame += 1  # advance frame number, for animations
