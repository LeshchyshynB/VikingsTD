import pygame

class DrawMenu():
	def draw(self, screen):
		all_buttons = []

		menu_bg = pygame.image.load("./Images/menu.png").convert()
		screen.blit(menu_bg, menu_bg.get_rect())
		# exit button
		all_buttons.append(pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(screen.get_width()-50, 0, 50, 50)))
		# print button
		all_buttons.append(pygame.draw.rect(screen, (200, 22, 100), pygame.Rect(screen.get_width()-150, 0, 50, 50)))

		

		return all_buttons



