import pygame
from .Menu.menu import Menu

class Handler(Menu):
	def __init__(self, event) -> None:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			button_rect = pygame.Rect(125, 125, 150, 50)
			if button_rect.collidepoint(event.pos):
				print("Button clicked!")
				self.exit_button(event.pos)
			