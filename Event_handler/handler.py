import pygame
from .Menu.menu import Menu

class Handler():
	def __init__(self, event=None) -> None:
		...
			
	def clickable(self, event, obj):
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			if 1230 <= event.pos[0] <= 1280 and 0 <= event.pos[1] <= 50:
				Menu().exit_button()

			if 1130 <= event.pos[0] <= 1180 and 0 <= event.pos[1] <= 50:
				Menu().print_button()
				