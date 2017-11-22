# Screen 'abstract' class
import pygame

import Graphics
import ScreenManager


class Screen:
	def update(self):
		# handle pygame.QUIT events without messing with the event queue
		# Very, very weird & spooky bug:
		# Pygame will randomly refuse to quit, often requiring many presses of the
		# quit button on the window to actually quit, if the following two print()
		# statements are removed.
		# This behaviour (refusing to quit) has *never* been observed while the
		# two print()s are present below.
		# Interestingly, removing them does not cause the behaviour to come back
		# immediately, even after many attempts to trigger it. Only when you
		# go away from this class and start working on other code does this bug
		# start to occur again. Then, you must re-add the print() statements to
		# stop the bug.
		# It is yet to be determined whether commenting out the print()s without
		# removing them entirely works for stopping the bug.
		print("looking for quit events")
		if pygame.event.peek(pygame.QUIT):
			print("quit event found")
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
