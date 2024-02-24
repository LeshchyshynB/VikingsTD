import pygame
import time
import sys

from Event_handler.handler import Handler

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

	dt = clock.tick(200) / 1000
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		Handler(event)

	screen.fill("white")

	pygame.draw.circle(screen, "red", player_pos, 40)


	pygame.display.flip()
	pygame.display.update()

pygame.quit()