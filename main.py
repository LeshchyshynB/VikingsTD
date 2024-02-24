import pygame

from Event_handler.handler import Handler
from UI.main_menu import DrawMenu


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
screen.fill("gray")

while running:

	dt = clock.tick(200) / 1000

	all_obj = []
	all_obj.append(DrawMenu().draw(screen))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		Handler(event)

		for obj_buttons in all_obj:
			for obj in obj_buttons:
				Handler().clickable(event, obj)

	pygame.display.flip()

pygame.quit()