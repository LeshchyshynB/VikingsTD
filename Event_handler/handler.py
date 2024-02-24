import pygame
from .Menu.menu import Menu

class Handler(Menu):
	def __init__(self, event) -> None:
		if event.type == pygame.MOUSEBUTTONDOWN:	
			self.exit_button()
			
		...