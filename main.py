import pygame
import time

pygame.init()

prev_time = time.time()

while True:
	dt = time.time() - prev_time
	prev_time = time.time()

	
